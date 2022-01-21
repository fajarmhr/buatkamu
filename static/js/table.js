$(document).ready(function() {
    $('#example').DataTable( {
        select: {
            style: 'single'
        },
        buttons: [
            'colvis'
        ]
    } );
} );