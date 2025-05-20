#version 330 core

// Variable de sortie (sera utilisé comme couleur)
out vec4 color;

//Un Fragment Shader minimaliste
void main (void)
{
  //Couleur du fragment vect4(R,G,B,opacité)
  color = vec4(0.0,0.0,1.0,1.0);
}
