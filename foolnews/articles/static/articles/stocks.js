function reorderStocks () {
    $('#stock-list-container > div').each(function() {
        $(this).prependTo(this.parentNode);
    })
}