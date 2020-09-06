# ftp://boavista:dados_abertos@ftp2.ciasc.gov.br/boavista_covid_dados_abertos.csv

from ftplib import FTP

ftp = FTP('ftp2.ciasc.gov.br')

ftp.mkd('newdir')

files = []

ftp.retrlines('LIST', files.append)

for fl in files:
    print(fl)
