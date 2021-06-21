// function projectTask(id){
//     var pk = id
//     console.log('hhhhhhhhhhhh', pk)
//     $.ajax({
//         url: 'project-tasks/'+pk+'/',
//         method: 'get',
//         success: function(response){
//             if(response=='true'){
//                 console.log('kkkk')
//                 $("#myy").load(location.href + " #myy");
//             }
            // var data = JSON.parse(response)
            // for (i=0; i<data.length; i++){
                // if (data[i].fields.task_complete == True){
                //     $('ul li a').click(function() {
                //         $('ul li.current').removeClass('current');
                //         $(this).closest('li').addClass('current');
                //     });
                // }
              
            
            // }
//         }
//     })
// } 


//---------------------assign task for employee

function assignTask(pk, id, uk){
    var emp_id = pk
    var tsk_id = id
    var pj_id = uk
    $.ajax({
        url: '/projectlead/'+emp_id+ '/' +tsk_id+ '/assign-task/'+pj_id+'/',
        method: "GET",
        success:function(response){
            if(response=='selected'){
                document.getElementById('assigntask-'+tsk_id+emp_id).style.background ="#4ed04e";                
            }
            if(response=='not selected'){
                document.getElementById('assigntask-'+tsk_id+emp_id).style.background ="#ff3333";
            }
        }
    })

}
function submitAssign(){    
    window.location.reload()
}


function taskDelete(pk){
    var tsk_id = pk

    $.ajax({
        url: '/tasks-delete/'+tsk_id+'/',
        method: "GET",
        success:function(response){
            if(response=='true'){
                window.location.reload()
            // $("#taskcontent").load(location.href + " #taskcontent");
        }
        }
    })

}


function assignEmployee(pk, id){
    var emp_id = pk
    var pjt_id = id
    $.ajax({
        url: '/hr/'+emp_id+ '/' +pjt_id+ '/assign/',
        method: "GET",
        success:function(response){
            if(response=='selected'){
                document.getElementById('list-'+emp_id).style.background ="#4ed04e";
                
                
            }
            if(response=='not selected'){
                document.getElementById('list-'+emp_id).style.background ="#ff3333";
                $("#emp-card").load(" #emp-card");
            }
        }
    })

}


function submitEmp(){    
    $("#emp-card").load(" #emp-card");
}
$( function() {
    $( ".card panel" ).draggable();
    $( ".kanban-wrap" ).droppable(
        {
            drop :function(event, ui)
        {
            var id = $(ui.draggable).attr('id');
            var status = $(this).attr('id');
            $.ajax({
               url: '/hr/change-task-status/'+id+status+'/',
               method: 'get',
               success: function(response){
                   if(response=='true'){
                   }
               }
            })

        }
        } );
        } );