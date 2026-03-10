# python-fullstack Docker Mariadb server Tutorial
i denne tutorialen skal jeg gå frem de nødvendige stegene du må gjøre til å aktivere og sette opp mariadbe servern din. (nb du må ha kopiert docker koden over) 
1. åpne terminalen
2. naviger til filen du har satt docker koden i
3. skjekk at koden fungerte 
```
ls -al 
```
4. kjør kontainerne som er i definert i filen
```
docker compose up
```
5. åpne en ny terminal
6. execute mariadb serveren
```
docker exec -it mariadb_container mariadb -u root -p
```

