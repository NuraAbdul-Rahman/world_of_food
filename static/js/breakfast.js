var base64Img = null;
margins = {
  top: 70,
  bottom: 40,
  left: 30,
  width: 550
};

function openForm() {
    document.getElementById("myForm").style.display = "block";
  }
  
  function closeForm() {
    document.getElementById("myForm").style.display = "none";
    
  }
  function openWin() {
   Location.href="{% url 'sign_up' %}";
   
  }
  function myFunction() {
    document.getElementById("user_form").reset();
  }

  //back to search results
  function goBack() {
    window.history.back();
  }
  $(document).ready(function() {
    $(".dropdown-toggle").dropdown();
});

generate = function()
{
  window.print();
};