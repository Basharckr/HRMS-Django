
// -----------------drag and drop---------------------

$( function() {
    $( ".card panel" ).draggable();
    $( ".kanban-wrap" ).droppable(
        {
            drop :function(event, ui)
        {
            var id = $(ui.draggable).attr('id');
            var status = $(this).attr('id');
            $.ajax({
               url: '/emp-change-task-status/'+id+status+'/',
               method: 'get',
               success: function(response){
                   if(response=='true'){

                   }
               }
            })
         



        }
        } );
        } );