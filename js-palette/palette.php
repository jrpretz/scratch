<html>
<head>
<title>JS Palettes</title>
<style>
#container{
width: 420px;
height: 512px;
background:white;
padding: 0px 0px 0px 0px;
margin: 0px 0px 0px 0px;
}
.pixel{
 width:100;
 height:2px;
 display: inline-block;
 }
.gap{
 width:20;
 height:2px;
 display: inline-block;
 }
.row{
 width:420px;
 height: 2px;
 display: inline-block;
}
.marker{
 width:420px;
 height: 2px;
 position: absolute;
 left: 8px;
 top: 256px;
   background-color: rgb(200,200,200);
}
</style>
<script src="rainbow_palette.js"></script>
<script src="viridis.js"></script>
<script>


var main = function(){
   for(i = 0 ; i < 256 ; i++){
     color = parseInt(i * 255./100.);
     //     color = rainbow_palette(i /255.);
     color = viridis(i /255.);
     //     document.getElementById("bar" + i).style.backgroundColor="rgb(" + color.red + "," + color.green + "," + color.blue + ")";
     //document.getElementById("bar" + i).style.backgroundColor="rgb(" + color.red + "," + color.green + "," + color.blue + ")";
     document.getElementById("red_" + i).style.backgroundColor="rgb(" + color.red + ",0,0)";
     document.getElementById("green_" + i).style.backgroundColor="rgb(0," + color.green + ",0)";
     document.getElementById("blue_" + i).style.backgroundColor="rgb(0,0," + color.blue + ")";
     document.getElementById("palette_" + i).style.backgroundColor="rgb(" + color.red + "," + color.green + "," + color.blue + ")";
   }
 }
</script>

</head>
<body onload="main()">

<div id="container">
<?php 
   for($i = 0 ; $i < 256 ; $i++){
     //echo("<div id=\"bar$i\" class=\"bar\"></div>");
     echo("<div class=\"row\"><div id=\"palette_$i\" class=\"pixel\"></div><div class=\"gap\"></div><div id=\"red_$i\" class=\"pixel\"></div><div id=\"green_$i\" class=\"pixel\"></div><div id=\"blue_$i\" class=\"pixel\"></div></div>");
    }
//echo("<div class=\"marker\"></div>");
?>

</div>

</body>
</html>