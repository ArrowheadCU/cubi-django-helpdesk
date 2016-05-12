// For JQuery UI Calendar

$(function() {
    $( "#id_due_date" ).datepicker();
});


// Calendar not working
//$("input[type=date]").each(function() {
//    if  (this.type != 'date' ) $(this).datepicker();
//});




//Sortable Tables
$(document).ready(function() {
    var table = $('table.sort-table').DataTable( {
		searching: false,
		paging: false,
		info: false,
		bAutoWidth: false,	

	});
     
    $('table.sort-table tbody')
        .on( 'mouseenter', 'td, th', function () {
            var colIdx = table.cell(this).index().column;
 
            $( table.cells().nodes() ).removeClass( 'highlight' );
            $( table.column( colIdx ).nodes() ).addClass( 'highlight' );
        } );
} );