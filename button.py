import pygame

class Button():
	def __init__(self,text,pos,width,height,font):
		self.rect=pygame.Rect(pos,(width,height))
		self.color=(80,80,80)
		self.text_surf=font.render(text,True,(30,30,30))
		self.text_rect=self.text_surf.get_rect(center=(self.rect.center))
		self.clicked=False

	def draw(self,surface):
		pygame.draw.rect(surface,self.color,self.rect,border_radius=12)
		surface.blit(self.text_surf,self.text_rect)

	def hover(self,surface):
		pygame.draw.rect(surface,self.color,self.rect,border_radius=12)
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

					
			# if event.type==pygame.KEYDOWN:
			# 	if event.key==K_f:
			# 		reset()
			# 		all_point()
			# 		store_edge()
			# 		find_edge()
			# 	if event.key==K_b:
			# 		draw_graph()
			# 		bfs()
			# 		all_point()
			# 		for e in list_edge.values():
			# 			e[1]=gray
			# 		visited.clear()
			# 	if event.key==K_d:
			# 		draw_graph()
			# 		dfs()
			# 		all_point()
			# 		for e in list_edge.values():
			# 			e[1]=gray
			# 		visited.clear()
			# 	if event.key==K_s:
			# 		mymain()	
			# 	if event.key==K_q:
			# 		pygame.quit()
			# update_menu()