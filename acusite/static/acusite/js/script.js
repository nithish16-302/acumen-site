
function onSignIn(googleUser)
{
  var profile = googleUser.getBasicProfile();
  $(".g-signin2").css("display","none");

  $(".data").css("display","block");
  $("#pic").attr('src',profile.getImageUrl());
  $("#email").attr('value',profile.getEmail());
  $("#userName").attr('value',profile.getGivenName());


   //document.getElementById("email").innerHTML =profile.getEmail();
   //document.getElementById("userName").innerHTML=profile.getGivenName();

}

function onSignedIn(googleUser)
{
  var profile = googleUser.getBasicProfile();
  $(".g-signin2").css("display","none");
  $("#email").attr('value',profile.getEmail());
  console.log(profile.getEmail());
  $("#lform").submit();
  //$("#btnClk").click();
  //$("#btnClk").trigger("click")


   //document.getElementById("email").innerHTML =profile.getEmail();
   //document.getElementById("userName").innerHTML=profile.getGivenName();

}


function signOut() {
  var auth2 = gapi.auth2.getAuthInstance();
auth2.signOut().then(function () {
  $(".g-signin2").css("display","block");
  $(".data").css("display","none");
});
    auth2.disconnect();
 }
