$(document).ready(function() {
// everything starts

function b_search(e) {
    e.preventDefault();
    var query = $('#t_query').val();
    $.ajax({
        type: "GET",
        url: "get_result",
        data: {"query": query},
        success: function(res) {
            $('#result').text(res); 
        }
    });
}

$('#b_search').on('click', b_search);
$('#search').on('submit', b_search);

// everything ends
});

