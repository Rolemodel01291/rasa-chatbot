$(document).ready(function() {

	var mybot = '<div class="chatCont" id="chatCont">'+
								'<div class="bot_profile">'+
									'<img src="/static/img/bot2.png" class="bot_p_img">'+
									'<div class="close">'+
										'<i class="fa fa-times" aria-hidden="true"></i>'+
									'</div>'+
								'</div><!--bot_profile end-->'+
								'<div id="result_div" class="resultDiv"></div>'+
								'<div class="chatForm" id="chat-div">'+
									'<div class="spinner">'+
										'<div class="bounce1"></div>'+
										'<div class="bounce2"></div>'+
										'<div class="bounce3"></div>'+
									'</div>'+
									'<div style = "display:flex;"><input type="text" id="chat-input" class="form-control" autocomplete="off" placeholder="Try typing here"'+ 'class="form-control bot-txt"/>'+
									'<button type=\'button\' id=\'send\' class=\'btn btn-square btn-success row\'>Send</button></div>' + 
								'</div>'+
							'</div><!--chatCont end-->'+
							'<div class="profile_div">'+
								'<div class="row">'+
									
									'<div class="col-hgt">'+
										'<div class="chat-txt">'+
											'Chat with us now!'+
										'</div>'+
									'</div><!--col-hgt end-->'+
								'</div><!--row end-->'+
							'</div><!--profile_div end-->';
	$("mybot").html(mybot);

	// ------------------------------------------ Toggle chatbot -----------------------------------------------
	$('.profile_div').click(function() {
		$('.profile_div').toggle();
		$('.chatCont').toggle();
		$('.bot_profile').toggle();
		$('.chatForm').toggle();
		document.getElementById('chat-input').focus();
	});

	$('.close').click(function() {
		$('.profile_div').toggle();
		$('.chatCont').toggle();
		$('.bot_profile').toggle();
		$('.chatForm').toggle();
	});
	var input = document.getElementById("chat-input");
      input.addEventListener("keyup", function(event) {
        if (event.keyCode === 13) {
         event.preventDefault();
         document.getElementById("send").click();
        }
      });

});
