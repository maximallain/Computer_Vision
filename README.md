_Team de l'enfer : Mr Seris & Mr Allain_

## Idée du projet :
### VISORD
- Tester plusieurs de segmentations
- Tester les segmentations avec plusieurs images :
    - fond blanc ou non
    - un seul ou plusieurs objet(s)
    - différents types d'objets (couleur, texture, intensité...)

### DEEP LEARNING
- Entraîner un modèle sur un data-set de 2500 images de déchets (6 classes différentes)
    - Évaluation du modèle, puis modification des hyperparamètres

Si mauvaise performance du modèle :
- Entraînement du modèle avec ImageNet puis entrainement sur le dataset de base (technique de fine-tuning ou transfer learning)


## Première approche :
- Segmenter une image en testant la méthode Mean-Shift


## Lancement de commande
Entraînement du modèle :
`python3 train_network.py -d './data/dataset-resized' -m resuls/lenet.model`


# Rapport
### Introduction
But du projet.
Ce qui se passe actuellement. L'enjeu du recyclage et de la qualité d'outils de machine learning.

### État de l'art
Projet Stanford : https://github.com/garythung/trashnet
=> parler de son approche

### Approche
Forme du modèle (CNN), batch resize, etc.

### Expérience

### Conclusion

### Références
Adrian Rosebrock pour Keras: https://www.pyimagesearch.com/2017/12/11/image-classification-with-keras-and-deep-learning/