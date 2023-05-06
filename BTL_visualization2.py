import pygame
from pygame import *
import math
from math import dist
import random
from random import randint
import keyboard

pygame.init()

display_width=920
display_height=800
extraH=60
center_width=display_width/2
center_height=display_height/2
k=40
radius=int(k*0.2)
ratio=40

white=(255,255,255)
black=(0,0,0)
spacegray=(30,30,30)
red=(205,38,38)
green=(34,139,34)
gray=(81,81,81)
grayy=(80,80,80)
gridcolor=(45,45,45)
font=pygame.font.SysFont(None,int(k*0.35))
font2=pygame.font.SysFont(None,int(extraH*0.8))
font3=pygame.font.SysFont(None,int(k*0.7))
n=3456
d=0

dai=k*2.5
rong=extraH*0.75

class Point:
	border=gray
	fill=gray
	def __init__(self,x,y):
		self.x=x
		self.y=y

def check(i,j,d):
	a=(i.x,i.y)
	b=(j.x,j.y)
	return dist(a,b)<=d

def cal(i,j):
	a=(i.x,i.y)
	b=(j.x,j.y)
	return round(dist(a,b),2)

class Button():
	def __init__(self,text,pos,width,height,font):
		self.rect=pygame.Rect(pos,(width,height))
		self.color=(80,80,80)
		self.text_surf=font.render(text,True,(30,30,30))
		self.text_rect=self.text_surf.get_rect(center=(self.rect.center))
		self.clicked=False

	def draw(self,surface):
		pygame.draw.rect(surface,self.color,self.rect,border_radius=10)
		surface.blit(self.text_surf,self.text_rect)

	def hover(self,surface):
		pygame.draw.rect(surface,self.color,self.rect,border_radius=10)
		surface.blit(self.text_surf,self.text_rect)
		action=False
		pos=pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			self.color=(255,255,255)
			action=True
		else:
			self.color=(80,80,80)
			action=False
		return action

	def click(self,surface):
		pygame.draw.rect(surface,self.color,self.rect,border_radius=12)
		surface.blit(self.text_surf,self.text_rect)
		action=False
		pos=pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
				self.clicked=True
				action=True
			if pygame.mouse.get_pressed()[0]==0 and self.clicked==True:
				# self.color=(80,80,80)
				self.clicked=False
		return action

P=[]

pygame.display.set_caption('Tìm thành phần liên thông')
screen=pygame.display.set_mode((display_width,display_height+extraH))
clock=pygame.time.Clock()

main_screen=pygame.Rect(0,0,display_width,display_height+1)
menu_screen=pygame.Rect(0,display_height+1,display_width,extraH)

button_start=Button('START',(center_width-k*5.5,display_height+extraH/8),dai,rong,font3)
button_return=Button('RETURN',(center_width-k*2.5,display_height+extraH/8),dai,rong,font3)
button_bfs=Button('BFS',(center_width+k*0.5,display_height+extraH/8),dai,rong,font3)
button_dfs=Button('DFS',(center_width+k*3.5,display_height+extraH/8),dai,rong,font3)
button_exit=Button('EXIT',(center_width+k*6.5,display_height+extraH/8),dai,rong,font3)

input_box=pygame.Rect(center_width-k*9,display_height+extraH/8,k*3,rong)

visited=[False]*n
edges=[False]*n
edges2=[False]*n
list_edge={}
text=''

def graphpaper():
	screen.fill(spacegray,main_screen)
	for i in range (int(display_width/k)):
		gridX=k*i
		pygame.draw.line(screen,gridcolor,(gridX,0),(gridX,display_height),1)
	for i in range (int(display_height/k)):
		gridY=k*i
		pygame.draw.line(screen,gridcolor,(0,gridY),(display_width,gridY),1)
	pygame.draw.line(screen,gridcolor,(display_width,0),(display_width,display_height),1)
	pygame.draw.line(screen,gridcolor,(0,display_height),(display_width,display_height),1)
	midX,midY=k,display_height-k
	pygame.draw.line(screen,gridcolor,(midX,0),(midX,display_height),4)
	pygame.draw.line(screen,gridcolor,(0,midY),(display_width,midY),4)
	x=font3.render('x',0,gray)
	screen.blit(x,x.get_rect(center=(display_width-k/2,display_height-k/2)))
	y=font3.render('y',0,gray)
	screen.blit(y,y.get_rect(center=(k+k/2,k/2)))
	o=font3.render('O',0,gray)
	screen.blit(o,o.get_rect(center=(k/2,display_height-k/2)))

def menu():
	global grayy
	screen.fill(spacegray,menu_screen)
	button_start.draw(screen)
	button_exit.draw(screen)
	button_bfs.draw(screen)
	button_dfs.draw(screen)
	button_return.draw(screen)
	pygame.draw.rect(screen,grayy,input_box,3)
	d_box=font2.render('d=',1,grayy)
	screen.blit(d_box,(center_width-k*8.5,display_height+extraH/4))
	txt_surface = font2.render(text, True, grayy)
	screen.blit(txt_surface,(center_width-k*7.5,display_height+extraH/4))

def all_point():
	graphpaper()
	for i in range(n):
		P[i].border=gray
		P[i].fill=gray
		color_fill(i)

def edge_id(n1,n2): return tuple(sorted((n1,n2))) 

def store_edge():
	for i in range (n):
		if not edges[i]:
			edges[i]=True
			for j in range(n):
				if not edges[i] and check(P[i],P[j],d):
					list_edge[edge_id(i,j)]=[(i,j),gray,1]

def find_edge():
	for i in range (n):
		if keyboard.is_pressed("ESCAPE"): 
			print('PAUSE')
			break
		if not edges2[i]:
			if keyboard.is_pressed("ESCAPE"): break
			edges2[i]=True
			P[i].border=white
			P[i].fill=red
			color_fill(i)
			update_edge()
			for j in range (n):
				if keyboard.is_pressed("ESCAPE"): break
				if not edges2[j]:
					P[j].border=white
					P[j].fill=green
					color_fill(j)
					update_edge()
					if edge_id(i,j) in list_edge:
						draw_line(i,j,list_edge[edge_id(i,j)][1],list_edge[edge_id(i,j)][2])
						print('Khoảng cách đỉnh '+str(i)+' và '+str(j)+': '+str(cal(P[i],P[j])))
						color_fill(i)
						color_fill(j)
						update_edge()
					P[j].border=gray
					P[j].fill=gray
					color_fill(j)
					update_edge()
			P[i].border=gray
			P[i].fill=gray
			color_fill(i)
			update_edge()

def bfs():
	draw_graph()
	dem=0
	for k in range (n):
		if keyboard.is_pressed("ESCAPE"): 
			print('PAUSE')
			break
		if not visited[k]:
			dem+=1
			print('TP '+str(dem)+':',end=' ')
			cl=random_color()
			queue=[]
			visited[k]=True
			queue.append(k)
			while queue:
				if keyboard.is_pressed("ESCAPE"): break
				u=queue.pop(0)
				print(u+1,end=' ')
				P[u].border=white
				P[u].fill=red
				update_graph()
				for i in range (n):
					if keyboard.is_pressed("ESCAPE"): break
					if check(P[u],P[i],d) and not visited[i]:
						queue.append(i)
						visited[i]=True
						P[i].border=white
						P[i].fill=green
						# list_edge[edge_id(u,i)][1]=white
						# list_edge[edge_id(u,i)][2]=2
						update_graph()
				P[u].fill=cl
				update_graph()
			print()
	# update_graph()

def dfs():
	draw_graph()
	dem=0
	for k in range (n):
		if keyboard.is_pressed("ESCAPE"): 
			print('PAUSE')
			break
		if not visited[k]:		
			dem+=1
			print('TP '+str(dem)+':',end=' ')
			cl=random_color()
			store=[]
			stack=[]
			visited[k]=True
			stack.append(k)
			while stack:
				if keyboard.is_pressed("ESCAPE"): break			
				u=stack.pop()
				if u not in store:
					print(u+1,end=' ')
					store.append(u)
				P[u].border=white
				P[u].fill=red
				update_graph()
				for i in range (n):
					if keyboard.is_pressed("ESCAPE"): break	
					if check(P[u],P[i],d) and not visited[i]:
						stack.append(u)
						stack.append(i)
						visited[i]=True
						P[i].border=white
						P[i].fill=green
						# list_edge[edge_id(u,i)][1]=white
						# list_edge[edge_id(u,i)][2]=2
						update_graph()
						break
				P[u].fill=cl
				update_graph()
			print()
	# update_graph()

def draw_graph():
	graphpaper()
	# for e in list_edge.values():
	# 	(n1,n2),color,size=e
	# 	draw_line(n1,n2,color,size)
	for i in range (n):
		color_fill(i)
	pygame.display.update(main_screen)

def color_fill(i):
	pos=(P[i].x*ratio+k,display_height-P[i].y*ratio-k)
	# pygame.draw.circle(screen,P[i].border,pos,radius)
	pygame.draw.circle(screen,P[i].fill,pos,radius)
	num=font.render(str(i+1),True,white)
	num_rect=num.get_rect(center=(pos))
	# screen.blit(num,num_rect)

def draw_line(i,j,color,size):
	pygame.draw.line(screen,color,(P[i].x*ratio+k,display_height-P[i].y*ratio-k),(P[j].x*ratio+k,display_height-P[j].y*ratio-k),size)

def reset_graph():
	reset()
	all_point()
	pygame.display.update(main_screen)

def update_edge():
	pygame.display.update(main_screen)
	# clock.tick(150)

def update_graph():
	draw_graph()
	# clock.tick(10)

def update_menu():
	menu()
	pygame.display.update(input_box)

def random_color():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    return (r,g,b)

def reset():
	global visited
	global edges
	global edges2
	visited=[False]*n
	edges=[False]*n
	edges2=[False]*n
	list_edge.clear()

def main():
	global visited
	global visited
	global text
	global grayy
	global d
	menu()
	all_point()
	pygame.display.flip()
	selectbox=False
	active=True
	while active:	
		# clock.tick(60)
		if button_start.hover(screen): pass
		if button_return.hover(screen): pass
		if button_exit.hover(screen): pass
		if button_bfs.hover(screen): pass
		if button_dfs.hover(screen): pass
		if button_start.click(screen) and text!='':
			reset()
			print('Khoảng cách d='+str(text))
			d=float(text)
			all_point()
			# store_edge()
			# find_edge()
		if button_return.click(screen):
			text=''
			d=0
			main()
		if button_bfs.click(screen):
			draw_graph()
			bfs()
			print()
			all_point()
			for e in list_edge.values():
				e[1]=gray
				e[2]=2
			visited=[False]*n
		if button_dfs.click(screen):
			draw_graph()
			dfs()
			print()
			all_point()
			for e in list_edge.values():
				e[1]=gray
				e[2]=2
			visited=[False]*n
		if button_exit.click(screen):
			active=False
		if input_box.collidepoint(pygame.mouse.get_pos()):
			grayy=white
			update_menu()
		if input_box.collidepoint(pygame.mouse.get_pos())==False and selectbox==False:
			grayy=(80,80,80)
			update_menu()

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				active=False
			if event.type==pygame.MOUSEBUTTONDOWN:
				if input_box.collidepoint(event.pos):
					selectbox=True
					reset_graph()
				else:
					selectbox=False
				grayy=white if selectbox else gray
				update_menu()
			if event.type==pygame.KEYDOWN:
				if selectbox:
					if event.key==pygame.K_RETURN:
						reset()
						print('Khoảng cách d='+str(text))
						d=float(text)
						all_point()
						# store_edge()
						# find_edge()
					if event.key==pygame.K_BACKSPACE:
						text=text[:-1]
						update_menu()
					if event.key==pygame.K_1:
						text+='1'
						update_menu()
					if event.key==pygame.K_2:
						text+='2'
						update_menu()
					if event.key==pygame.K_3:
						text+='3'
						update_menu()
					if event.key==pygame.K_4:
						text+='4'
						update_menu()
					if event.key==pygame.K_5:
						text+='5'
						update_menu()
					if event.key==pygame.K_6:
						text+='6'
						update_menu()
					if event.key==pygame.K_7:
						text+='7'
						update_menu()
					if event.key==pygame.K_8:
						text+='8'
						update_menu()
					if event.key==pygame.K_9:
						text+='9'
						update_menu()
					if event.key==pygame.K_0:
						text+='0'
						update_menu()
					if event.key==pygame.K_PERIOD:
						text+='.'
						update_menu()
					if event.key==pygame.K_COMMA:
						text+='.'
						update_menu()

		pygame.display.update(menu_screen)
		
if __name__=='__main__':
	f=open('3456.csv','r')
	for line in f:
		x,y=[float(x) for x in line.split(',')]
		P.append(Point(x,y))
	main()
	pygame.quit()