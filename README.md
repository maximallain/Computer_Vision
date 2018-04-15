_M. Seris & M. Allain_

## Idée du projet :
- Tester plusieurs techniques de segmentations
- Tester les segmentations avec plusieurs images :
    - fond blanc ou non
    - un seul ou plusieurs objet(s)
    - différents types d'objets (couleur, texture, intensité...)


## Approche :
- Segmenter une image en testant la méthode MeanShift
- Faire tourner un classifier utilisant des réseaux de neurones artificielles pour classer les régions (ou segments d'image)

## Fichiers/Dossiers importants
- Le notebook MeanShiftSegmentation_OpenCV décrit un MeanShift écrit à la main pour la segmentation
- Le notebook MeanShiftSegmentation_ScikitLearn décrit un MeanShift en utilisant SciKitLearn 
- Les images en racine servent d'exemples pour nos notebooks
- Les objets identifiés dans les images sont dans le dossier Objets
