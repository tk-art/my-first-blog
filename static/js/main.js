$(document).ready(function() {
  var heartIcon = $("#heart-icon");
  var likeCount = $(".like-count");
  var likeStatus = localStorage.getItem("likeStatus");

  if (likeStatus === "liked") {
    heartIcon.removeClass("far").addClass("fas");
  }
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
          localStorage.setItem("likeStatus", "liked");

        } else {
          heartIcon.removeClass("fas").addClass("far");
          likeCount.text(response.like_count);
          localStorage.removeItem("likeStatus");
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
