#!/usr/bin/env python3

import OpenGL.GL as GL
import glfw
import numpy as np
import tools 
import pyrr

class Game(object):
    """ fenêtre GLFW avec openGL """

    def __init__(self):
        self.window = self.init_window()

        self.color = [1.0, 0.0, 0.0]  # rouge par défaut
        self.translation = [0.0, 0.0]
        
        self.x = 0
        self.y = 0
        self.z = 0
        self.i = 0
        self.j = 0
        self.k = 0

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
        self.program = tools.create_program_from_file("code/shader.vert", "code/shader.frag")
        if self.program:
            GL.glUseProgram(self.program)

        pass
        
    def init_data(self):
        #Création de 3 sommets
        sommets = np.array(((0, 0, 0), (1, 0, 0), (0, 1, 0)), np.float32)

        # attribution d'une liste d'etat (1 indique la création d'une seule liste) ´
        vao = GL.glGenVertexArrays(1)
        # affectation de la liste d'etat courante
        GL.glBindVertexArray(vao)
        # attribution d’un buffer de donnees (1 indique la création d’un seul buffer) ´
        vbo = GL.glGenBuffers(1)
        # affectation du buffer courant
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, vbo)
        # copie des donnees des sommets sur la carte graphique
        GL.glBufferData(GL.GL_ARRAY_BUFFER, sommets, GL.GL_STATIC_DRAW)

        # Les deux commandes suivantes sont stockees dans l' ´ etat du vao courant ´
        # Active l'utilisation des donnees de positions ´
        # (le 0 correspond a la location dans le vertex shader) `
        GL.glEnableVertexAttribArray(0)
        # Indique comment le buffer courant (dernier vbo "binde") ´
        # est utilise pour les positions des sommets ´
        GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 0, None)

        pass

    def run(self):
        """
        boucle principale du programme : affichage et gestion des évènements
        :return: None
        """
        # boucle d'affichage
        while not glfw.window_should_close(self.window):
            speed = 0.01

            # changer la couleur de fond en fonction du temps qui passe
            time = glfw.get_time()
            color = np.sin(time)
            GL.glClearColor(color, 0.5, 0.5, 0.5)
            # nettoyage de la fenêtre : fond et profondeur
            GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

            color_location = GL.glGetUniformLocation(self.program, "uColor")

            # touches directionnelles
            if glfw.get_key(self.window, glfw.KEY_LEFT) == glfw.PRESS:
                self.translation[0] -= speed
            if glfw.get_key(self.window, glfw.KEY_RIGHT) == glfw.PRESS:
                self.translation[0] += speed
            if glfw.get_key(self.window, glfw.KEY_UP) == glfw.PRESS:
                self.translation[1] += speed
            if glfw.get_key(self.window, glfw.KEY_DOWN) == glfw.PRESS:
                self.translation[1] -= speed


            # touches de rotation
            if glfw.get_key(self.window, glfw.KEY_I) == glfw.PRESS:
                self.i += 0.1
            if glfw.get_key(self.window, glfw.KEY_J) == glfw.PRESS:
                self.i -= 0.1
            if glfw.get_key(self.window, glfw.KEY_K) == glfw.PRESS:
                self.j += 0.1
            if glfw.get_key(self.window, glfw.KEY_L) == glfw.PRESS:
                self.j -= 0.1

            xrotation = pyrr.matrix44.create_from_x_rotation(self.i)
            yrotation = pyrr.matrix44.create_from_y_rotation(self.j)
            rotation = xrotation @ yrotation

            GL.glUniform3fv(color_location, 1, self.color)

            ## dessin des sommets
            #GL.glDrawArrays(GL.GL_LINE_LOOP, 0, 3) #GL_LINE_LOOP : ne rempli pas le triangle
            GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3) #GL_TRIANGLES : rempli le triangle

            glfw.swap_buffers(self.window)
            glfw.poll_events()

            # Recupère l'identifiant du programme courant
            prog = GL.glGetIntegerv(GL.GL_CURRENT_PROGRAM)

            loc = GL.glGetUniformLocation(prog, "rotation")
            if loc == -1 :
                print("Pas de variable uniforme : rotation")
                # Modifie la variable pour le programme courant
            GL.glUniformMatrix4fv(loc, 1, GL.GL_FALSE, rotation)

            loc = GL.glGetUniformLocation(prog, "translation")
            if loc == -1 :
                print("Pas de variable uniforme : translation")            
            GL.glUniform4f(loc, self.translation[0], self.translation[1], 0.0, 1.0)

            loc = GL.glGetUniformLocation(prog, "projection")
            if loc == -1 :
                print("Pas de variable uniforme : projection")


    
    def key_callback(self, win, key, scancode, action, mods):
        # sortie du programme si appui sur la touche 'echap'
        if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
            glfw.set_window_should_close(win, glfw.TRUE)

        if action == glfw.PRESS:
            if key == glfw.KEY_R:
                self.color = [1.0, 0.0, 0.0]
            elif key == glfw.KEY_G:
                self.color = [0.0, 1.0, 0.0]
            elif key == glfw.KEY_B:
                self.color = [0.0, 0.0, 1.0]


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

Q_25 : 
    L’opération mathématique principale est la division par w (division perspective) suivie d’un changement d’échelle pour passer de [-1, 1] à [0, width/height].

"""