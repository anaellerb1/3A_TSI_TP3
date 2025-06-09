Projet réalisé dans le cadre du cours de Traitement du Signal et de l'Image en 3e année ETI à CPE Lyon.
Réalisé par Anaëlle ROBIN et chat gpt ;)

# TP OpenGL – Affichage d'objets 3D texturés avec Phong Shading

##  Objectifs du TP

Ce mini-projet a pour but d'explorer les bases de l'affichage 3D avec OpenGL moderne (version 3.3), en Python via `PyOpenGL` et `glfw`. Les principaux objectifs sont :

- Créer une fenêtre graphique avec `glfw`.
- Afficher des objets 3D à l’aide de Vertex Buffer Objects (VBO) et Vertex Array Objects (VAO).
- Gérer les transformations 3D (translation, rotation, perspective).
- Appliquer des textures via des coordonnées UV.
- Mettre en œuvre l’éclairage avec un modèle de Phong shading.

---

##  Contenu du projet

- `main.py` : Fichier principal contenant la classe `Game`, qui gère la fenêtre, le rendu, les entrées clavier et le chargement des données.
- `tools.py` : Fonctions utilitaires pour la compilation et la liaison des shaders OpenGL.
- `texture/texture1.jpg` : Image utilisée comme texture.
- `code/phong.vert` : Shader de vertex (transformation des sommets).
- `code/phong.frag` : Shader de fragment (calcul de l’éclairage).

---

## Fonctionnalités

- **Affichage d’un objet 3D** composé de deux triangles formant une sorte de pyramide.
- **Ajout d’un sol texturé**, positionné en dessous des objets mobiles.
- **Contrôle clavier** :
  - Flèches ← ↑ ↓ → : translation des objets.
  - `I`, `J`, `K`, `L` : rotation de la scène.
  - `Y` / `H` : zoom avant / arrière.
  - `R`, `G`, `B` : changer la couleur (rouge, vert, bleu).
  - `ESPACE` : réinitialisation de la position et des rotations.
  - `ECHAP` : quitter l'application.

```bash
pip install PyOpenGL glfw numpy Pillow pyrr
