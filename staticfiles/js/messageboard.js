$(document).ready(function () {
    
    toolsbar={}
    
    toolsbar.reset = function(){
        $("#create_message_box").css("display","none");
        $("#exitButton").css("display","none");
        $("#submitButton").css("display","none");
        $("#plusButton").css("display","block");
    }
    toolsbar.reset();

    toolsbar.activate = function(){
        $("#create_message_box").css("display","block");
        $("#exitButton").css("display","block");
        $("#submitButton").css("display","block");
        $("#plusButton").css("display","none");
    }

    $("#plusButton").click(toolsbar.activate);
    $("#exitButton").click(toolsbar.reset);



});