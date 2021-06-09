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

function submitLdr(){    
    $("#ldr-card").load(" #ldr-card");
}

function submitEmp(){    
    $("#emp-card").load(" #emp-card");
}


// function taskDelete(pk){
//     var tsk_id = pk
//     console.log('hiiii')

//     $.ajax({
//         url: '/tasks-delete/'+tsk_id+'/',
//         method: "GET",
//         success:function(response){
//             if(response=='true'){
//                 console.log('hiiii2222222') 
//                 window.location.reload()
//             // $("#taskcontent").load(location.href + " #taskcontent");
//         }
//         }
//     })

// }

// function addTask(pk){
//     var obj_id = pk
//     $.ajax({
//         url: '/hr/addtask/'+obj_id+'/',
//         method: 'post',
//         data: $('#addnewtask').serialize(),
//         success:function(response){
//             if(response=='true'){
//                 console.log('hiiii2222222') 
//                 window.location.reload()
                
//         }
//     }
//     })
// }

function assignTask(pk, id, pr){
    var emp_id = pk
    var tsk_id = id
    var pr_id = pr

    $.ajax({
        url: '/projectlead/'+emp_id+ '/' +tsk_id+ '/assign-task/'+pr_id+'/',
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

// ------------------drag and drop ------------------------------------------------
// const card_item = document.querySelectorAll('.kanban-box');
// const cards = document.querySelectorAll('.kanban-wrap');
// let draggedItem = null;

// for (let i = 0; i < card_item.length; i++){
//     const item = card_item[i];
    
//     item.addEventListener('dragstart', function (){
//         draggedItem = item;
//         setTimeout(function (){
//             item.style.display = 'none';
//         }, 0)

//     });

//     item.addEventListener('dragend', function (){
//         setTimeout(function (){
//             draggedItem.style.display = 'block';
//             draggedItem = null;
//         }, 0);

//     })

//     for (let j = 0; j < cards.length; j++){
//         const card = cards[j];
//         card.addEventListener('dragover', function (e){
//             e.preventDefault();
//         });

//         card.addEventListener('dragenter', function (e){
//             e.preventDefault();
//         });
//         card.addEventListener('dragleave', function (e){
//         });

//         card.addEventListener('drop', function (e){
//             console.log('drop')
//             console.log('droppppp')
//             this.append(draggedItem);
//         });
//     }
// }

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