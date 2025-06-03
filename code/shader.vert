#version 330 core

// Variable d'entrée, ici la position
layout (location = 0) in vec3 position;
out vec3 coordonnee_3d;

//Un Vertex Shader minimaliste
uniform vec4 translation;
uniform mat4 rotation;
uniform mat4 projection;

void main (void)
{
  coordonnee_3d = position;

  //Coordonnees du sommet
  gl_Position = projection * (rotation * vec4(position, 1.0) + translation);

}
