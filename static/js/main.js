
$(document).ready(function() {
  var heartIcon = $("#heart-icon");

  $.ajax({
    type: "GET",
    url: "/get_like_status/" + itemId + "/",
    success: function(response) {
      console.log(response);
      if (response.is_liked) {
        heartIcon.removeClass("far").addClass("fas");
      }
    },
    error: function(xhr, status, error) {
      console.log(error);
    }
  });

});

function likeButtonClicked() {
  var heartIcon = $("#heart-icon");
  var likeCount = $(".like-count");

  $.ajax({
    type: "POST",
    url: "/like_item/" + itemId + "/",
    data: {
      item_id: itemId,
      csrfmiddlewaretoken: csrfToken,
    },

    success: function(response) {
        if (response.is_liked) {
          heartIcon.removeClass("far").addClass("fas");
          likeCount.text(response.like_count);

        } else {
          heartIcon.removeClass("fas").addClass("far");
          likeCount.text(response.like_count);
        }
      },
      error: function(xhr, status, error) {
        console.log(error);
      }
  });
}


$(document).ready(function() {
    $('#comment-form').submit(function(event) {
        event.preventDefault();
        var form = $(this);
        $.ajax({
            type: "POST",
            url: "/comment_item/" + itemId + "/",
            data: form.serialize(),
            dataType: 'json',

            success: function(response) {
                if (response.success) {
                  var commentUser = response.comment.user;
                  var commentText = response.comment.text;
                  var commentUserElement = $('<p>').text(commentUser);
                  var commentTextElement = $('<p>').text(commentText).addClass('comment-text');
                  $('#comment-container').append(commentUserElement);
                  $('#comment-container').append(commentTextElement);
                  form.find('#text').val('');
                } else {
                    alert('コメントの作成に失敗しました。フォームをご確認ください。');
                }
            },
            error: function() {
                alert('コメント作成中にエラーが発生しました');
            }
        });
    });
});

$(document).ready(function() {
  // 通知の新規有無を確認する関数を定義します
  function checkNewNotifications() {
    $.ajax({
      url: '/api/notifications/check',
      method: 'GET',
      success: function(response) {
        console.log(response);
        // バックエンドからのレスポンスを確認し、通知があればshowNewNotification()関数を呼び出す
        if (response.hasNewNotification) {
          showNewNotification();
        }
      },
      error: function(error) {
        console.log('通知の問い合わせに失敗しました。', error);
      }
    });
  }

  checkNewNotifications();

  $('#notification-link').click(function() {
    $('#notification-icon').empty();
  });

  function showNewNotification() {
    $('#notification-icon').html('⭕️');
  }
});


$(document).ready(function() {
  const socket = new WebSocket(
      'ws://' + window.location.host +　'/ws/chat/'
      );

  chatSocket.onmessage = function(e) {
      const data = JSON.parse(e.data);
      const chatBox = $('#chat-box');
      const messageElement = $('<div></div>').text(data.message);
      chatBox.append(messageElement);
  };

  $('#send-button').on('click', function() {
      const messageInput = $('#message-input');
      const message = messageInput.val();
      socket.send(JSON.stringify({ 'message': message }));
      messageInput.val('');
  });
});