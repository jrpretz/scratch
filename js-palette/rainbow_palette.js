// implements a red-to-blue-through-green
// palette
var rainbow_palette = function(psi){
    rgb = {"red":0,"green":0,"blue":0};
    if(psi < 0)
	rgb.red = 255;
    else if(psi > 0.5)
	rgb.red = 0;
    else if(psi >= 0 && psi <= 0.25)
	rgb.red = 255;
    else
	rgb.red = 255 * ((-psi+0.25) / 0.25)  + 255.;
    
    if(psi < 0)
	rgb.green = 0;
    else if(psi > 1.0)
	rgb.green = 0;
    else if(psi >= 0 && psi <= 0.25)
        rgb.green = (255. * ((psi) / 0.25) );
    else if(psi >= 0.75 && psi <= 1.0)
	rgb.green =
	(255. * ((-psi + 0.75) / 0.25) + 255);
    else
	rgb.green = 255;
    
    if(psi < 0.5)
	rgb.blue = 0;
    else if(psi > 0.75)
	rgb.blue = 255;
    else if(psi >= 0.75 && psi <= 1.0)
	rgb.blue = 255;
    else
	rgb.blue = (255. * ((psi-0.75) / 0.25)  + 255);
       
    rgb.red = parseInt(rgb.red);
    rgb.green = parseInt(rgb.green);
    rgb.blue = parseInt(rgb.blue);
    return rgb;
}