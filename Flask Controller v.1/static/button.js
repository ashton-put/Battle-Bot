var button = $("#led_button");
button.click(function() {
	console.log(button.text());
	if (button.text() === "FORWARD") {
		$.ajax({
			url: "/forward_on",
			type: "post",
			success: function(response) {
				console.log(response);
				button.text("FORWARD");
			}
		});
	} else if (button.text() === "BACKWARD"){
		$.ajax({
			url: "/backward_on",
			type: "post",
			success: function() {
				button.text("BACKWARD");
			}
		})
	}
});