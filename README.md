<h1 align='center'>Reconnaissance et classification des déchets</h1>
<p align='center'>
<i>
M. Seris & M. Allain
</i>
</p>

### _Abstract_
<p align='justify'>
L'objectif de ce projet est de s'intéresser à la problématique de la reconnaissance des déchets. Ce problème est un enjeu majeur dans la gestion des déchets.
Pour cela, nous allons présenter nos deux étapes de notre démarche. Premièment, nous nous sommes penchés sur la reconnaissance d'objets sur une image en utilisant des techniques de vision par ordinateur. Cette étape permet de détecter puis d'isoler des objets sur une photo grâce à l'algorithme de segmentation MeanShift de Comaniciu et Meer \cite{c3}.
Deuxièmement, nous avons utilisé des techniques de réseaux profonds afin de classifier ces images d'objets isolés selon plusieurs catégories concernant six types de déchets : plastique, métal, cartons, verre, papier et autres.
</p>

## Architecture du Projet

Le projet est composé de deux parties :

### Vision par Ordinateur

- Le notebook *MeanShiftSegmentation_OpenCV* décrit un MeanShift écrit à la main pour la segmentation
- Le notebook *MeanShiftSegmentation_ScikitLearn* décrit un MeanShift en utilisant SciKitLearn
- Les images en racine servent d'exemples pour nos notebooks
- Les objets identifiés dans les images sont dans le dossier Objets

### Deep Learning

- _lenet.py_ : définit l'architecture du réseau de neurones.
- *train_network* : script entraînant le modèle.
- *test_model* : script permettant de tester le modèle sur notre set de données test.
- *test_network* : script testant le modèle sur des images.

## Stack Technique
Nous avons utilisé Python, avec les frameworks cv2 (vision), scikit-learn, numpy, pandas (traitement des données)
ou encore Keras, avec Tensoflow en back-end (Deep Learning).

## Utilisation

- Cloner le repository : `git clone https://github.com/maximallain/VISORD`
- Installer les librairies : `pip install -r requirements`

Pour utiliser la Vision par Ordinateur, accéder aux NoteBooks.


Pour entraîner le modèle de Deep Learning :
- Accéder au dossier *DL_model* : `cd DL_model`
- Entraîner le modèle : `python train_network.py -d './data/dataset-resized' -m ./lenet.model -p ./plot.png`
- Tester le modèle sur le dataset-test : `python test_model.py -m ./lenet.model -d data/dataset-test`
- Tester le modèle sur une image : `python test_network.py -m ./lenet.model -i data/test/verre.jpg` (ou remplacer _verre.jpg_ par _cardboard.jpg_)

