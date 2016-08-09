#!/usr/bin/python
# By: Alexander Diana
# A 670B webcrawler
from sys import argv as A,stderr as R
from bs4 import BeautifulSoup as B
from urllib.request import urlopen as U
from urllib.error import HTTPError as E,URLError as L
from urllib.parse import urljoin as J
p=print
z={'file':R}
def D(G):
	try:p("\tParsing:",G,**z);\
	r=[J(G,a.get('href')) for a in B(U(G)).findAll('a')]
	except E as e:p(e.code,**z)
	except L as e:p(e.args,**z)
	except Exception as e:p(e,**z)
	return r
S=K={A[1]}
V=int(A[2])
C="http"
if len(A)>3:C=A[3]
for W in range(V):
	p("Entering level:",W,**z)
	S={N for G in S if G.startswith(C) for N in D(G)}-K
	K.update(S)
	p('',**z)
p("\n".join(K))
