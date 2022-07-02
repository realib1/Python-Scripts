$(document).ready(function(){

    setInterval(function(){
        $.ajax({
            type: 'GET',
            url : "/getMessages/{{room}}/",
            success: function(response){
                console.log(response);
                $("#display").empty();
                for (var key in response.messages)
                {
                    var temp="<div class='container darker'><b>"+response.messages[key].user+"</b><p>"+response.messages[key].value+"</p><span class='time-left'>"+response.messages[key].date+"</span></div>";
                    $("#display").append(temp);
                }
            },
            error: function(response){
                alert('An error occured')
            }
        });
    },1000);
    })
    
    $(document).on('submit','#post-form',function(e){
        e.preventDefault();
    
        $.ajax({
          type:'POST',
          url:'/send',
          data:{
              username:$('#username').val(),
              room_id:$('#room_id').val(),
              message:$('#message').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
          },
          success: function(data){
             //alert(data)
          }
        });
        document.getElementById('message').value = ''
      });