// implements a "inferno" palette
// Ones I've seen are implemented through tabulated data.
// I did a high-order polynomial fit just for brevity.
// red and green were fine with 4-th order polynomials.
// blue had a little curvature at the end that wanted a 6th order
// polynomial.
var inferno = function(psi){
    rgb = {"red":0,"green":0,"blue":0};

    A = 0.00021337;
    B = 0.106293;
    C = 11.7084;
    D = -42.2018;
    E = 78.3748;
    F = -72.6964;
    G = 25.6888;

    rgb.red = 256 * (A 
	+ psi*B 
	+ psi*psi * C 
	+ psi * psi *psi * D 
	+ psi*psi*psi*psi *E
	+ psi*psi*psi*psi *psi*F
	+ psi*psi*psi*psi *psi*psi*G);
    
    A = 0.00163489;
    B = 0.568582;
    C = -3.97872;
    D = 17.6639;
    E = -33.9429;
    F = 33.1972;
    G = -12.5126;

    rgb.green = 256 * (A 
	+ psi*B 
	+ psi*psi * C 
	+ psi * psi *psi * D 
	+ psi*psi*psi*psi *E
	+ psi*psi*psi*psi *psi*F
	+ psi*psi*psi*psi *psi*psi*G);


    A = -0.0371299;
    B = 4.13407;
    C = -16.3851;
    D = 45.1723;
    E = -83.5516;
    F = 75.0423;
    G = -23.6649;


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
