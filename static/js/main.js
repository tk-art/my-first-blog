
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
                  var commentTextElement = $('<p>').text(commentText);
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
  function checkNewNotifications() {
    $.ajax({
      url: '/api/notifications/check',
      method: 'GET',
      success: function(response) {
        console.log(response);
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
  $("#message-form").submit(function(event) {
      event.preventDefault();

      var form = $(this);

      $.ajax({
          type: "POST",
          url: "/message/" + itemid + "/",
          data: form.serialize(),
          dataType: "json",
          success: function(response) {
            var imageElement = $('<img>').attr({
              src: response.message.image,
              alt: response.message.user,
              class: "messa-image-size"
            });
            var messageUser = response.message.user;
            var messageText = response.message.message;
            var messageTimestamp = response.message.timestamp;
            var messageUserElement = $('<p>').text(messageUser);
            var messageTextElement = $('<p>').text(messageText);
            var messageTimestampElement = $('<p>').text(messageTimestamp).addClass('message-timestamp');
            var divElement = $('<div>').addClass('kugiri');

            var messageLinkElement = $('<a>').attr({
              href: "/profile/" + response.message.sender,
              class: "message-link"
            }).append(imageElement);

            var messageInfoElement = $('<div>').addClass("message-info")
                .append(messageUserElement)
                .append(messageTimestampElement)
                .append(messageTextElement);

            var profileDetailElement = $('<div>').addClass("profile-detail")
                .append(messageLinkElement)
                .append(messageInfoElement);

            $('#message-container').append(profileDetailElement);
            $('#message-container').append(divElement);
            form.find('#content').val('');
          },
          error: function(error) {
            console.log(error);
          }
      });
   });
});

$('.reply-btn').click(function() {
  var reply_to_id = $(this).data('reply-to');
  var reply_to_name = $(this).data('reply-to-name');
  $('#reply_to').val(reply_to_id);
  $('#content').val(reply_to_name + "に対しての返信 :");
  $('#content').focus();
});

$('#confirmButton').click(function() {
  $.ajax({
    url: '/button_click',
    method: 'POST',
    data: {
      'itemId' : itemid,
      'csrfmiddlewaretoken' : csrfToken,
    },
    success: function(data) {
      window.location.href = '/';
    },
    error: function(error) {
        console.error('Error:', error);
    }
  })
});
