/*function Button_fuction(){

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].onclick = function(){
        this.classList.toggle("active");
        this.nextElementSibling.classList.toggle("show");
    }
}
}*/


function create_groups(button, file) {
	  var form = button.parentNode.parentNode;
	  var n_group = form.getElementsByClassName("num_groups")[0].value;
	  var t_group = form.getElementsByClassName("group_type")[0].value;
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
	  if (type == undefined){
		  alert('Attenzione! Ti sei dimenticato di selezionare il tipo di gruppo o il numero di gruppi');
		  location.href = "/weeks";
	  }
	  
	  else if (n_group == 'undefined'){
		  alert('Attenzione! Ti sei dimenticato di selezionare il tipo di gruppo o il numero di gruppi');
		  location.href = "/weeks";
	  }

	  else{
		  location.href = "/groups/" +file+ "/" +type+"/"+n_group;
		  }
	  
      
}