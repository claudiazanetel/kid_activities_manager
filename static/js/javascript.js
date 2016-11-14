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

//(function() {
  //('.collapse').on('shown.bs.collapse', function (e) {
       // console.log('Calling #' + e.currentTarget.id);
    //})
//})

//$(function() {
  //$('.collapse').on('shown.bs.collapse', function (e) {
        //$("#log").text(('Calling #' + e.currentTarget.id));
    //})
//})

//var file = document.getElementById("files").value;

function File_save(){
	alert(this.document.getElementById("week").innerHTML)
}


function create_groups() {
	  //var file = document.getElementsByClassName('panel-title')[0].id;
	  var file = document.getElementById("week").innerHTML;
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
      
	  alert(file)
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