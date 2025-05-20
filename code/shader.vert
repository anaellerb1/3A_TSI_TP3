#version 130

in vec3 position;

uniform mat4 rotation;
uniform vec4 translation;
uniform mat4 projection;

void main() {
    gl_Position = projection * (rotation * vec4(position, 1.0) + translation);
}
