$.ajax({
    "url": "fend/nD",
    "type": "GET",
    "dataType": "json",
    "success": loadData,
    "error": function(jqXHR, status, error) {
        console.log("status:", status, "error:", error);
    }
});

function getAudio() {
    return window.location.search.slice(4);
}


//function to read json file
function loadData(data){
    //creating State from folder
    for(var i = 0; i < data.length; i++) {
        $('#id_state').append('<option state_id="'+ data[i].state.id +'" value="'+ data[i].state.name +'" >'+data[i].state.name+'</option>')
    }

    $("#id_state").change(function(){
        var p = $(this).val(),
            t = $(this).attr('state_id') - 1
        console.log(p)
        do{
           for(var j = 0; j < data[t].state.locals.length; j++){
            console.log(data[t].state.locals[j].name)
           }
        }while(data.state.name == p)

    })
}



//function maritalStatus(){
//    $(document).ready(function(){
//        $('#married').hide();
//        $('#single').hide();
//        var stat = $('#id_status').val()
//        $('#id_status').change(function(){
//            if(stat == "S"){
//                $('#married').hide();
//                $('#single').show();
//                console.log(stat)
//             }else{
//                $('#married').show();
//                $('#single').hide();
//                console.log(stat)
//             }
//        })
//    })
//}

//maritalStatus();