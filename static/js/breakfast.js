function openForm() {
    document.getElementById("myForm").style.display = "block";
  }
  
  function closeForm() {
    document.getElementById("myForm").style.display = "none";
    
  }
  function openWin() {
    //window.open("sign_up");
   Location.href="{% url 'sign_up' %}";
   
  }
  function myFunction() {
    document.getElementById("user_form").reset();
  }

  //back to search results
  function goBack() {
    window.history.back();
  }