main = function(){
  console.log("hello");
  loadXMLDoc();

}

function loadXMLDoc() {
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      myFunction(this);
    }
  };
  xmlhttp.open("GET", "data.php", true);
  xmlhttp.send();
}

function myFunction(xml) {
  var x, i, xmlDoc, txt;
  xmlDoc = xml.responseXML;
  console.log(xml.responseText);
  //parser = new DOMParser();
  //xmlDoc = parser.parseFromString(xml.responseText,"text/xml");
  //console.log(xmlDoc);
  txt = "";
  x = xmlDoc.getElementsByTagName("x");
  y = xmlDoc.getElementsByTagName("y");
  for (i = 0; i< x.length; i++) {
    txt += x[i].childNodes[0].nodeValue + "," + y[i].childNodes[0].nodeValue + "<br>";
  }
  document.getElementById("demo").innerHTML = txt;
}
