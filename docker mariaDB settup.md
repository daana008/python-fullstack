# python-fullstack Docker Mariadb server Tutorial
## prosjekt beskrivelse 
i dette prosjekte lager jeg en server som lagrer filer og en nettside som lar deg sette dem inn. du kan også laste ned filene som er satt inn eller slette dem, men etter 7 dager slettes de automatisk. det er også mulig å sende serveren til noen andre takket være docker

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
7. skriv inn passorded ditt
8.   lag dattabasen din
```
CREATE DATABASER prosjekter
```
9. GÅ INN OG BRUK DATABASEN
```
USE PROSJEKTER
```
10. lag filene hvor informtionen blir lagret
```
CREATE TABLE files (
  id INT AUTO_INCREMENT PRIMARY KEY,
  filename VARCHAR(255),
  filepath VARCHAR(255),
  filesize INT,
  uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
11. sjekk at de fungerer ved å sette in en av filene dine
    * først kopier inn dette. INSERT INTO files (filename, filepath, filesize)
    * så følg opp med å skrive inn informationen til filene dine
    * så tast dette ; og trykk enter






