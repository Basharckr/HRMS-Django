function assignEmployee(pk, id){
    var emp_id = pk
    var pjt_id = id
    console.log('hiiii')

    $.ajax({
        url: '/hr/'+emp_id+ '/' +pjt_id+ '/assign/',
        method: "GET",
        success:function(response){
            if(response=='selected'){
                document.getElementById('list-'+emp_id).style.background ="#4ed04e";
                
                
            }
            if(response=='not selected'){
                document.getElementById('list-'+emp_id).style.background ="";
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


function taskDelete(pk){
    var tsk_id = pk
    console.log('hiiii')

    $.ajax({
        url: '/tasks-delete/'+tsk_id+'/',
        method: "GET",
        success:function(response){
            if(response=='true'){
                console.log('hiiii2222222') 
                window.location.reload()
            // $("#taskcontent").load(location.href + " #taskcontent");
        }
        }
    })

}