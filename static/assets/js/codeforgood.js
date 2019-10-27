// AJAX for incrementing the view of an article
function increment_article_view(article_pk) {
    // Send a post request to the url below
    // and pass the primary key (pk) of the article.
    var url = '/increment_news_view_count/';

    $.ajax({
        url: url,
        type: "POST",
        data: {"pk": article_pk}, // sending the video primary key to backend

        // handle a successful response
        success: function (json) {
            console.log("Inremented view count by 1");
        },
    });
}