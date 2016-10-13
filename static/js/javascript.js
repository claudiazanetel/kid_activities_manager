function create_groups() {
	  
	  var file = document.getElementById("file").value;
	  var n_group = document.getElementById("num_groups").value;
	  if(document.getElementById('type_aged').checked) {
		  var type = 1
	  }
	  else if(document.getElementById('type_mix').checked) {
			var type = 2
	  }
      //document.write(type + "  " + n_group );
      location.href = "/groups/" + file+ "/" +type+"/"+n_group;
}