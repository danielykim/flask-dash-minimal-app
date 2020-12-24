index_string = '''
<!DOCTYPE html>
<html>
<head>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-167989003-2"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-167989003-2');
</script>
  {%metas%}
  <title>{%title%}</title>
  {%favicon%}
  {%css%}
<style>
/* Center the loader */
#loader {
position: absolute;
left: 50%;
top: 50%;
z-index: 1;
width: 150px;
height: 150px;
margin: -75px 0 0 -75px;
border: 16px solid #f3f3f3;
border-radius: 50%;
border-top: 16px solid #3498db;
width: 120px;
height: 120px;
-webkit-animation: spin 2s linear infinite;
animation: spin 2s linear infinite;
}

@-webkit-keyframes spin {
0% { -webkit-transform: rotate(0deg); }
100% { -webkit-transform: rotate(360deg); }
}

@keyframes spin {
0% { transform: rotate(0deg); }
100% { transform: rotate(360deg); }
}

#myContent {
display: block;
}
</style>
</head>
<body onload="myFunction()">
  <div id="loader"></div>
  {%app_entry%}
  <footer>
  {%config%}
  {%scripts%}
  {%renderer%}
  </footer>
<script>
var myVar;

function myFunction() {
  myVar = setTimeout(showPage, 2000);
}

function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("myContent").style.display = "block";
}
</script>
</body>
</html>
'''
