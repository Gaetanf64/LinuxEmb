# PROJET LINUX EMBARQUE

## Objectifs du projet
Le but de ce projet est d'implémenter un système embarqué qui détecte les mouvements de la main, et qui allume un feu tricolore.
Le sytème embarqué doit être construit avec Buildroot

## Principe de fonctionnement 
- Sans détection de présence le feu est vert
- En passant la main devant le détecteur le feu devient orange
- En laissant la main devant le détecteur le feu est rouge

## Résumé Lundi
- On a installé le système avec une image Raspbian 64 bits sur la carte SD avec le logiciel Raspbian Imager sur Windows
- Nous avons insérer la carte SD dans le système, et on l'a relié à un moniteur et un clavier
- On a récupéré l'adresse IP du système avec la commande 
````
hostname -I
````
- On a ainsi pu se connecter en SSH depuis l'ordinateur Windows
- On a programmé en Python le système en respectant le principe de fonctionnement et en copiant le fichier .py dans le système

## Résumé Mardi
- On s'est connecté à buildroot depuis une machine configurée. On a utilisé une clé RSA fournie et un login admin pour se connecter en SSH
````
ssh -i buildroot.pem admin@idBuildroot
````
- Depuis la machine buildroot on configure l'image raspberry :
    ````
    cp -R builroot buildroot_2
    cd buildroot_2
    make raspberrypi3_64_defconfig
    make -j12 (pour prendre en compte 12 processeurs)
    make menuconfig
        - Dans Toolchain :
        - Dans Target Packages -> Interpreter Languages and scripting :
            - Activer python 3
            - dans External Modules : activer Rpi-GPIO et pip
        -> Networking Applications :
            - Activer ssh
        A cause d'une erreur avec Python :
            - Filesystem images -> exact size -> 220 M
    make -j12
    ````
- On copie l'image généré sdcard.img par make qui est dans buildroot_2/output/images avec WinSCP pour transférer sur Windows
- On recommence l'installation depuis le logiciel Raspberry Imager avec l'image personnalisé
- La connexion se fait en root sans mdp

- Se connecter sur la carte Raspberry en Ethernet :
    - Depuis la carte sd raspberry avec la nouvelle image :
        ````
        cd etc/network
        nano interfaces OU vi interfaces
        Ajouter : 
            auto eth0
            iface eth0 inet static
            address 10.0.0.1
            netmask 255.0.0.0
        redémarrer les services :
            ifdown eth0
            ifup eth0
            ifconfig (pour vérifier que tout est bon)
    - Depuis Windows configurer Ethernet avec l'adresse 10.0.0.2 et le mask : 255.0.0.0
- Copier le programme Python sur la carte Raspberry
- Executer avec
````
python3 detection.py
````





