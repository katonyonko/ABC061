from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="061"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/abc{0}_{1}".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  N,M=map(int,input().split())
  G=[[] for _ in range(N)]
  for i in range(M):
    a,b,c=map(int,input().split())
    a-=1; b-=1
    G[a].append((-c,b))
  def BellmanFord(G,s=0):
    inf=10**20
    D=[inf]*len(G)
    D[0]=0
    for i in range(len(G)-1):
      for j in range(len(G)):
        for c,v in G[j]:
          if D[j]+c<D[v]:
            D[v]=D[j]+c
    cycle=[0]*len(G)
    for j in range(len(G)):
      for c,v in G[j]:
        if D[j]+c<D[v]: cycle[v]=1
    for i in range(len(G)-1):
      for j in range(len(G)):
        if cycle[j]==1:
          for c,v in G[j]:
            cycle[v]=1
    for i in range(len(G)):
      if cycle[i]==1: D[i]='-inf'
    return D
  D=BellmanFord(G,0)
  if D[N-1]=='-inf': print('inf')
  else: print(-D[N-1])
  """ここから上にコードを記述"""

  print(test_case[__+1])