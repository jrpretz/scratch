// implements a "viridis" palette
// Ones I've seen are implemented through tabulated data.
// I did a high-order polynomial fit just for brevity.
// red and green were fine with 4-th order polynomials.
// blue had a little curvature at the end that wanted a 6th order
// polynomial.
var viridis = function(psi){
    rgb = {"red":0,"green":0,"blue":0};

    A = 0.235957;
    B = 1.22391;
    C = -7.46021;
    D = 11.1815;
    E = -4.15319;

    rgb.red = 256 * (A 
	+ psi*B 
	+ psi*psi * C 
	+ psi * psi *psi * D 
	+ psi*psi*psi*psi *E);
    
    A = 0.00170237;
    B = 1.58277;
    C = -1.73326;
    D = 2.2675;
    E = -1.2192;

    rgb.green = 256 * (A 
	+ psi*B 
	+ psi*psi * C 
	+ psi * psi *psi * D 
	+ psi*psi*psi*psi *E);

    A = 0.332664;
    B = 1.38677;
    C = 0.0919604;
    D = -19.2918;
    E = 56.6562;
    F = -65.3209;
    G = 26.2721;


    rgb.blue = 256 * (A 
        + psi*B 
        + psi*psi * C 
	+ psi * psi *psi * D 
	+ psi*psi*psi*psi *E
        + psi*psi*psi*psi*psi *F
        + psi*psi*psi*psi*psi*psi *G);
    rgb.red = parseInt(rgb.red);
    rgb.green = parseInt(rgb.green);
    rgb.blue = parseInt(rgb.blue);
    return rgb;
}