# MINI COURS

## Make
La commande make lance la génération du système, c'est-à-dire : 

- la génération de la chaîne de cross-compilation pour l'architecture demandée ;
- la compilation, via la chaîne de cross-compilation, des applications/services afin de générer le système ;
- la compilation du noyau ;
- la génération du rootfs en créant une image disque (rootfs.ext4), et en recopiant le système cross-compilé.


## MenuConfig
- Le menu **Toolchain** permet de configurer la chaîne de cross-compilation
- Le menu **System** permet de personnaliser le système obtenu :
    - le nom d'hôte et la bannière de connexion ;
    - le format de stockage des mots de passe, et le mot de passe root ; 
    - le système de démarrage des services (BusyBox, init, systemd) ;
    - la gestion des périphériques dans/dev et les périphériques persistants à créer ;
    - la configuration du réseau (dhcp sur l'interface eth0) ;
    - la localisation par défaut et l'heure locale
- Le menu **Kernel** permet de configurer le noyau
- Le menu **Target packages** contient l'ensemble des applications/librairies que vous pouvez installer sur votre système cible
- Le menu **Filesystem images** vous offre la possibilité de choisir le ou les formats finaux de votre image. Dans notre cas, nous générons une image d'une carte SD contenant un système de fichier racine en EXT4. Mais vous pouvez aussi générer une archive (tar) de ce système
- Le menu **Bootloaders** permet de sélectionner son chargeur de démarrage, l'équivalent de GRUB sur PC. Dans le cas de la Raspberry PI, il s'agit de U-Boot
- Différentes applications sont nécessaires sur la machine hôte pour générer l'image finale. Ces applications sont rassemblées dans le menu **Host Utilities**
- Le dernier menu, **Legacy config**, contient la liste des options qui sont actuellement sélectionnées, mais qui ne sont plus supportées par Buildroot

## Générez l'image
Finalement, générez l'image via un :
````
make
````
Comme vous utilisez la chaîne de cross-compilation déjà installée, vous noterez que cette étape est plus rapide que lors de la génération de l'image aarch64 de la partie précédente.

Vous obtenez finalement une image sdcard.img contenant deux partitions.