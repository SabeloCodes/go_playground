/*==========================CAROUSEL JAVASCRIPT=================================*/

//     $('.carousel').carousel({
//     interval: 2000
//     })
    
//       $(document).ready(function(){
//     $('.carousel').carousel();
//      interval: 2000
//   });
    
    
/*==========================INITIALIZE SELECT ELEMENT=================================*/

   document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, options);
  });
  
   $(document).ready(function(){
    $('.carousel').carousel();
     interval: 2000   
    $('select').formSelect();
    $('input#input_text, textarea#textarea2').characterCounter();
  });
  
 
	