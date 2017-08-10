#include <stdlib.h>
#include <stdio.h>
#include <GL/glut.h>

void changeSize(int w, int h) {
  printf("changeSize: %d %d\n",w,h);
  fflush(stdout);
  // Prevent a divide by zero, when window is too short
  // (you cant make a window of zero width).
  if(h == 0)
    h = 1;
  float ratio = 1.0* w / h;
  
  // Use the Projection Matrix
  glMatrixMode(GL_PROJECTION);
  
  // Reset Matrix
  glLoadIdentity();
  
  // Set the viewport to be the entire window
  //  glViewport(0, 0, w, h);
  glViewport(-1000,1000,-1000,1000);
  
  // Set the correct perspective.
  gluPerspective(45,ratio,1,1000);
  
  // Get Back to the Modelview
  glMatrixMode(GL_MODELVIEW);
}

float angle = 0.0f;

void renderScene(void) {
  
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

  /* // Reset transformations */
  glLoadIdentity(); 
  /* // Set the camera */
  /* gluLookAt(	0.0f, 0.0f, 10.0f,  */
  /* 		0.0f, 0.0f,  0.0f,  */
  /* 		0.0f, 1.0f,  0.0f);  */
  
  glRotatef(angle, 1.0, 1.0f, 0.0f);
  
  glBegin(GL_TRIANGLES);
  glColor3f(1,1,1);
  glVertex3f(0.5,0.5,0.0);
  glVertex3f(0.5,0.75,0.0);
  glVertex3f(0.75,0.5,0.0);
  glEnd();
  
  glBegin(GL_LINES);
  glColor3f(1,0,0);
  glVertex3f(0,0,0);
  glVertex3f(1,0,0);
  glColor3f(0,1,0);
  glVertex3f(0,0,0);
  glVertex3f(0,1,0);
  glColor3f(0,0,1);
  glVertex3f(0,0,0);
  glVertex3f(0,0,1);
  glEnd();

#if 0
  glBegin(GL_POINTS);
  for(float x = -1.0 ; x <= 1.0 ; x = x + 0.1)
    for(float y = -1.0 ; y <= 1.0 ; y = y + 0.1)
      for(float z = -1.0 ; z <= 1.0 ; z = z + 0.1)
	glVertex3f(x,y,z);
  glEnd();
#endif
  angle+=0.01f;

#if 0
  glBegin(GL_POINTS);
  for(float x = -1.0 ; x <= 1.0 ; x = x + 0.1)
    for(float y = -1.0 ; y <= 1.0 ; y = y + 0.1)
      glVertex3f(x,y,0.0);
  glEnd();
#endif

  glutSwapBuffers();
}

int main(int argc, char**argv){
  glutInit(&argc,argv);

  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);


  //  glutInitWindowPosition(0,0);
  //  glutInitWindowSize(800,500);
  glutInitWindowPosition(100,100);
  glutInitWindowSize(320,320);
  glutCreateWindow("home");
  glutDisplayFunc(renderScene);
  glutIdleFunc(renderScene);
  //  glutReshapeFunc(changeSize);

  //  glMatrixMode(GL_PROJECTION);
  //  glLoadIdentity();
  //  glViewport(0,0,10,10);
  //  gluPerspective(145,1.0,0.1,1.0);

  glutMainLoop();
}
