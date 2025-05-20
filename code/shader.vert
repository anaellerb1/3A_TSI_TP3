#version 330 core

// Variable d'entrée, ici la position
layout (location = 0) in vec3 position;

//Un Vertex Shader minimaliste
uniform vec4 translation;
void main (void)
{
  //Coordonnees du sommet
  gl_Position = vec4(position,1.0);

  //prendre en compte la translation issue de la variable uniforme dans l’affichage
  gl_Position.x += translation.x;
  gl_Position.y += translation.y;
  gl_Position.z += translation.z;
  gl_Position.w += translation.w;
}
