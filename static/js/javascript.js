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

<<<<<<< HEAD
function get_value(name_file){
    var x=document.getElementById('modal_file');
    x.setAttribute('value', name_file);
	
}
function create_groups(button) {
	  var file = document.getElementById('modal_file').value;
=======

function create_groups(button, file) {
>>>>>>> 73842e1700717f7b30ad4184b0e00286507c0465
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
<<<<<<< HEAD
		  //location.href = "/weeks";
=======
		  location.href = "/weeks";
>>>>>>> 73842e1700717f7b30ad4184b0e00286507c0465
	  }
	  
	  else if (n_group == 'undefined'){
		  alert('Attenzione! Ti sei dimenticato di selezionare il tipo di gruppo o il numero di gruppi');
<<<<<<< HEAD
		  //location.href = "/weeks";
=======
		  location.href = "/weeks";
>>>>>>> 73842e1700717f7b30ad4184b0e00286507c0465
	  }

	  else{
		  location.href = "/groups/" +file+ "/" +type+"/"+n_group;
		  }
	  
      
}