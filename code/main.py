#!/usr/bin/env python3

import OpenGL.GL as GL
import glfw
import numpy as np

class Game(object):
    """ fenêtre GLFW avec openGL """

    def __init__(self):
        self.window = self.init_window()
        self.init_context()
        self.init_programs()
        self.init_data()


    def init_window(self):
        """ 
        création de la fenêtre et initialisation de la librairie glfw et du contexte opengl associé

        :return: la fenêtre créée
        """
        # initialisation de la librairie glfw et du context opengl associé
        glfw.init()
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL.GL_TRUE)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        # création et parametrage de la fenêtre
        glfw.window_hint(glfw.RESIZABLE, False)
        window = glfw.create_window(800, 800, 'OpenGL', None, None)
        # parametrage de la fonction de gestion des évènements
        glfw.set_key_callback(window, self.key_callback)
        return window

    def init_context(self):
        """
        initialisation du contexte opengl associé à la fenêtre
        :return: None
        """
        # activation du context OpenGL pour la fenêtre
        glfw.make_context_current(self.window)
        glfw.swap_interval(1)
        # activation de la gestion de la profondeur
        GL.glEnable(GL.GL_DEPTH_TEST)

    def init_programs(self):
        pass
        
    def init_data(self):
        pass

    def run(self):
        """
        boucle principale du programme : affichage et gestion des évènements
        :return: None
        """
        # boucle d'affichage
        while not glfw.window_should_close(self.window):
            # changer la couleur de fond en fonction du temps qui passe
            time = glfw.get_time()
            color = np.sin(time)
            GL.glClearColor(color, 0.5, 0.5, 0.5)
            # nettoyage de la fenêtre : fond et profondeur
            GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
            # changement de buffer d'affichage pour éviter un effet de scintillement
            glfw.swap_buffers(self.window)
            # gestion des évènements
            glfw.poll_events()
            #print("Couleur de fond : ", color)
            #print("Temps écoulé : ", time)
    
    def key_callback(self, win, key, scancode, action, mods):
        # sortie du programme si appui sur la touche 'echap'
        if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
            glfw.set_window_should_close(win, glfw.TRUE)

    def compile_shader(shader_content, shader_type):
        # compilation d'un shader donné selon son type
        shader_id = GL.glCreateShader(shader_type)
        GL.glShaderSource(shader_id, shader_content)
        GL.glCompileShader(shader_id)

        success = GL.glGetShaderiv(shader_id, GL.GL_COMPILE_STATUS)
        if not success:
            log = GL.glGetShaderInfoLog(shader_id).decode('ascii')
            print(f'{25*"-"}\nError compiling shader: \n{shader_content}\n{5*"-"}\n{log}\n{25*"-"}')
        return shader_id

    def create_program(vertex_source, fragment_source):
        # création d'un programme GPU
        vs_id = compile_shader(vertex_source, GL.GL_VERTEX_SHADER)
        fs_id = compile_shader(fragment_source, GL.GL_FRAGMENT_SHADER)

        if vs_id and fs_id:
            program_id = GL.glCreateProgram()
            GL.glAttachShader(program_id, vs_id)
            GL.glAttachShader(program_id, fs_id)
            GL.glLinkProgram(program_id)

            success = GL.glGetProgramiv(program_id, GL.GL_LINK_STATUS)
            if not success:
                log = GL.glGetProgramInfoLog(program_id).decode('ascii')
                print(f'{25*"-"}\nError linking program:\n{log}\n{25*"-"}')

            GL.glDeleteShader(vs_id)
            GL.glDeleteShader(fs_id)

            return program_id

    def create_program_from_file(vs_file, fs_file):
        # création d'un programme GPU à partir de fichiers
        vs_content = open(vs_file, 'r').read() if os.path.exists(vs_file) \
            else print(f'{25*"-"}\nError reading file:\n{vs_file}\n{25*"-"}')

        fs_content = open(fs_file, 'r').read() if os.path.exists(fs_file) \
            else print(f'{25*"-"}\nError reading file:\n{fs_file}\n{25*"-"}')

        return create_program(vs_content, fs_content)

def main():
    g = Game()
    g.run()
    glfw.terminate()

if __name__ == '__main__':
    main()


"""
### Réponses aux questions
Q_5 : 
    En comptant le nombre de ligne pour une seconde, on a 60 images par seconde.
    Cela correspond à un temps d'affichage de 16.67 ms par image.

"""