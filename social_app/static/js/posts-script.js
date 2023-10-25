$(document).ready(function() {
    $(".like-form").on("submit", function(event) {
        event.preventDefault();
        var form = $(this);
        var postId = form.data("post-id");
        var url = form.attr("action");
        var data = form.serialize();

        $.ajax({
            type: "POST",
            url: url,
            data: data,
            dataType: "json",
            success: function(response) {
                // Update the like count
                var likeCountElement = $("#like-count-" + postId);
                likeCountElement.text("Total Likes: " + response.like_count);

                // Update the like/unlike button text and icon
                var likeButton = $(".like-form[data-post-id='" + postId + "'] button");
                var icon = likeButton.find('i');  // Get the icon element

                // Check the current class of the icon and change it
                if (icon.hasClass('fas fa-heart')) {
                    icon.removeClass('fas fa-heart');
                    icon.addClass('far fa-heart');
                    likeButton.text(' Like');
                } else {
                    icon.removeClass('far fa-heart');
                    icon.addClass('fas fa-heart');
                    likeButton.text(' Unlike');
                }

                likeButton.prepend(icon);
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    });
    // Show/hide comment panel
    $('.comment-button').click(function() {
        var postId = $(this).data('post-id');
        var commentPanel = $('#comment-panel-' + postId);
        var commentOverlay = $('#comment-overlay');

        // Make AJAX request to retrieve comments
        $.ajax({
            url: getCommentsUrl,
            type: 'GET',
            data: { 'post_id': postId },
            success: function(response) {
                // Update comments section
                commentPanel.find('.comments').html(response.comments_html);

                // Show comment panel and overlay
                commentOverlay.show();
                commentPanel.show();
                // Add CSS class to body element to prevent scrolling of background content
                $('body').addClass('no-scroll');
            },
            error: function(xhr) {
                // Handle error
                console.log(xhr.responseText);
            }
        });
    });

    // Close comment panel when clicking outside of it
    $('#comment-overlay').click(function(event) {
        if (event.target === this) {
            closeCommentPanel();
        }
    });

    // Submit comment form
    $('.comment-form').submit(function(event) {
        event.preventDefault(); // Prevent form submission

        var postId = $(this).data('post-id');
        var commentContent = $(this).find('textarea[name="comment-content"]').val();

        // AJAX request to post comment
        $.ajax({
            url: "{% url 'posts:post_comment' %}",
            type: 'POST',
            data: {
                'post_id': postId,
                'content': commentContent,
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
            success: function(response) {
                // Append new comment to comments section
                var commentHtml = '<div class="comment">' +
                    '<p>' + response.comment.content + '</p>' +
                    '<p class="comment-info">' + response.comment.created_at + ' by ' + response.comment.user.username + '</p>' +
                    '</div>';
                $('#comment-panel-' + postId + ' .comments').append(commentHtml);

                // Clear comment textarea
                $('#comment-panel-' + postId + ' textarea[name="comment-content"]').val('');
            },
            error: function(xhr) {
                // Handle error
                console.log(xhr.responseText);
            }
        });
    });

    // Close comment panel function
    function closeCommentPanel() {
        $('.comment-panel').hide();
        $('#comment-overlay').hide();
        // Remove CSS class from body element to restore scrolling of background content
        $('body').removeClass('no-scroll');
    }
});