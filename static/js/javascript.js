function Button_fuction(){

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].onclick = function(){
        this.classList.toggle("active");
        this.nextElementSibling.classList.toggle("show");
    }
}
}

function create_groups() {
	    
	  var file = document.getElementById("files").value;
	  var n_group = document.getElementById("num_groups").value;
	  var t_group = document.getElementById("type_group").value;
	  if (t_group =='aged'){
		  var type = 1
	  }
	  else if (t_group =='mix'){
		  var type = 2 
	  }
	  //if(document.getElementById('type_aged').checked) {
		  //var type = 1
	  //}
	  //else if(document.getElementById('type_mix').checked) {
			//var type = 2
	  //}
      
	  
	  //document.write(type + "  " + n_group );
      location.href = "/groups/" + file+ "/" +type+"/"+n_group;
}