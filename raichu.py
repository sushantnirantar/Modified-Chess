#
# raichu.py : Play the game of Raichu
#
# Sushant Nirantar sniranta
#
# Based on skeleton code by D. Crandall, Oct 2021
#
import sys
import time

def board_to_string(board, N):
    return "\n".join(board[i:i+N] for i in range(0, len(board), N))

def board_to_list(board,n):
	lst=[[0 for i in range(n)] for i in range(n)]
	k=0
	for i in range(n):
		for j in range(n):
			lst[i][j]=board[k]
			k=k+1
	return lst


def list_to_board(lst):
	str1=""
	for i in range(len(lst)):
		for j in range(len(lst[0])):
			str1+=lst[i][j]
	return str1

def find_white_pichus(lst):
	lst1=[]
	for i in range(len(lst)):
		for j in range(len(lst[0])):
			if(lst[i][j]=="w"):
				lst1.append((i,j))
	return lst1

def find_black_pichus(lst):
	lst1=[]
	for i in range(len(lst)):
		for j in range(len(lst[0])):
			if(lst[i][j]=="b"):
				lst1.append((i,j))
	return lst1

def find_white_pikachus(lst):
	lst1=[]
	for i in range(len(lst)):
		for j in range(len(lst[0])):
			if(lst[i][j]=="W"):
				lst1.append((i,j))
	return lst1

def find_black_pikachus(lst):
	lst1=[]
	for i in range(len(lst)):
		for j in range(len(lst[0])):
			if(lst[i][j]=="B"):
				lst1.append((i,j))
	return lst1

def find_white_raichus(lst):
	lst1=[]
	for i in range(len(lst)):
		for j in range(len(lst[0])):
			if(lst[i][j]=="@"):
				lst1.append((i,j))
	return lst1

def find_black_raichus(lst):
	lst1=[]
	for i in range(len(lst)):
		for j in range(len(lst[0])):
			if(lst[i][j]=="$"):
				lst1.append((i,j))
	return lst1

def empty_space(lst):
	lst1=[]
	for i in range(len(lst)):
		for j in range(len(lst[0])):
			if(lst[i][j]=="."):
				lst1.append((i,j))
	return lst1

def utility_score(w,b,W,B,Rw,Rb):
	
	score=(w+(W*2)+(Rw*3))-(b+(B*2)+(Rb*3))
	return score

def lst_copy(lst):
	lst1=[]
	for i in lst:
		lst1.append(i)
	return lst1

def create_board(w,W,b,B,Rw,Rb,n):
	lst=[[0 for i in range(n)] for i in range(n)]
	for i in range(n):
		for j in range(n):
			if((i,j) in w):
				lst[i][j]="w"
			elif((i,j) in W):
				lst[i][j]="W"
			elif((i,j) in b):
				lst[i][j]="b"
			elif((i,j) in B):
				lst[i][j]="B"
			elif((i,j) in Rw):
				lst[i][j]="@"
			elif((i,j) in Rb):
				lst[i][j]="$"
			else:
				lst[i][j]="."
	return lst

def valid_w_pichu(x,y):
	lst=[]
	x1=x+1
	y1=y+1
	y2=y-1
	if(x1>=0 and x1<8 and y1>=0 and y1<8):
		lst.append((x1,y1))
	if(x1>=0 and x1<8 and y2>=0 and y2<8):
		lst.append((x1,y2))
	return lst

def valid_w_pichu_ld(x,y,n):
	lst=[]
	x1=x+1
	y1=y-1
	if(x1>=0 and x1<n and y1>=0 and y1<n):
		lst.append((x1,y1))
	return lst

def valid_w_pichu_rd(x,y,n):
	lst=[]
	x1=x+1
	y1=y+1
	if(x1>=0 and x1<n and y1>=0 and y1<n):
		lst.append((x1,y1))
	return lst

def valid_b_pichu_ld(x,y,n):
	lst=[]
	x1=x-1
	y1=y-1
	if(x1>=0 and x1<n and y1>=0 and y1<n):
		lst.append((x1,y1))
	return lst

def valid_b_pichu_rd(x,y,n):
	lst=[]
	x1=x-1
	y1=y+1
	if(x1>=0 and x1<n and y1>=0 and y1<n):
		lst.append((x1,y1))
	return lst

def valid_w_pikachu_up1(x,y,n):
	lst=[]
	x1=x+1
	y1=y
	if(x1>=0 and x1<n and y1>=0 and y1<n):
		lst.append((x1,y1))
	return lst

def valid_w_pikachu_up2(x,y,n):
	lst=[]
	x1=x+2
	y1=y
	if(x1>=0 and x1<n and y1>=0 and y1<n):
		lst.append((x1,y1))
	return lst

def valid_b_pikachu_up1(x,y,n):
	lst=[]
	x1=x-1
	y1=y
	if(x1>=0 and x1<n and y1>=0 and y1<n):
		lst.append((x1,y1))
	return lst

def valid_b_pikachu_up2(x,y,n):
	lst=[]
	x1=x-2
	y1=y
	if(x1>=0 and x1<n and y1>=0 and y1<n):
		lst.append((x1,y1))
	return lst

def valid_w_pikachu_r1(x,y,n):
	lst=[]
	x1=x
	y1=y+1
	if(x1>=0 and x1<n and y1>=0 and y1<n):
		lst.append((x1,y1))
	return lst

def valid_w_pikachu_r2(x,y,n):
	lst=[]
	x1=x
	y1=y+2
	if(x1>=0 and x1<n and y1>=0 and y1<n):
		lst.append((x1,y1))
	return lst

def valid_w_pikachu_l1(x,y,n):
	lst=[]
	x1=x
	y1=y-1
	if(x1>=0 and x1<n and y1>=0 and y1<n):
		lst.append((x1,y1))
	return lst

def valid_w_pikachu_l2(x,y,n):
	lst=[]
	x1=x
	y1=y-2
	if(x1>=0 and x1<n and y1>=0 and y1<n):
		lst.append((x1,y1))
	return lst

def raichu_beam_up(x,y,n):
	lst=[]
	while(x>=0):
		
		lst.append((x,y))
		x=x-1
	lst.pop(0)
	return lst

def raichu_beam_down(x,y,n):
	lst=[]
	while(x<n):
		
		lst.append((x,y))
		x=x+1
	lst.pop(0)
	return lst

def raichu_beam_right(x,y,n):
	lst=[]
	while(y<n):
		
		lst.append((x,y))
		y=y+1
	lst.pop(0)
	return lst

def raichu_beam_left(x,y,n):
	lst=[]
	while(y>=0):
		
		lst.append((x,y))
		y=y-1
	lst.pop(0)
	return lst

def raichu_beam_leftd_up(x,y,n):
	lst=[]
	while(x>=0 and y>=0):
		
		lst.append((x,y))
		x=x-1
		y=y-1
	lst.pop(0)
	return lst

def raichu_beam_leftd_down(x,y,n):
	lst=[]
	while(x<n and y>=0):
		
		lst.append((x,y))
		x=x+1
		y=y-1
	lst.pop(0)
	return lst

def raichu_beam_rightd_up(x,y,n):
	lst=[]
	while(x>=0 and y<n):
		
		lst.append((x,y))
		x=x-1
		y=y+1
	lst.pop(0)
	return lst

def raichu_beam_rightd_down(x,y,n):
	lst=[]
	while(x<n and y<n):
		
		lst.append((x,y))
		x=x+1
		y=y+1
	lst.pop(0)
	return lst


def wraichu_move(w,W,b,B,Rw,Rb,e,n1):#Add size of board
	lst=[]
	
	for i in range(len(Rw)):
		n=n1
		lst1=raichu_beam_up(*Rw[i],n)
		lst2=raichu_beam_down(*Rw[i],n)
		lst3=raichu_beam_right(*Rw[i],n)
		lst4=raichu_beam_left(*Rw[i],n)
		lst5=raichu_beam_rightd_down(*Rw[i],n)
		lst6=raichu_beam_rightd_up(*Rw[i],n)
		lst7=raichu_beam_leftd_down(*Rw[i],n)
		lst8=raichu_beam_leftd_up(*Rw[i],n)
		#print(lst2)

		for j in range(len(lst1)):
			w1=lst_copy(w)
			b1=lst_copy(b)
			W1=lst_copy(W)
			B1=lst_copy(B)
			Rw1=lst_copy(Rw)
			Rb1=lst_copy(Rb)
			e1=lst_copy(e)
			initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			if(lst1[j] in b1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst1[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst1)):
						b2=lst_copy(b)
						if(lst1[m] in e1):
							b2.remove(lst1[j])
							Rw1[i]=lst1[m]
							res=list_to_board(create_board(w1,W1,b2,B1,Rw1,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst1[j] in B1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst1[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst1)):
						B2=lst_copy(B)
						if(lst1[m] in e1):
							B2.remove(lst1[j])
							Rw1[i]=lst1[m]
							res=list_to_board(create_board(w1,W1,b1,B2,Rw1,Rb1,n))
							if(initial_board==res):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst1[j] in Rb1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst1[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst1)):
						Rb2=lst_copy(Rb)
						if(lst1[m] in e1):
							Rb2.remove(lst1[j])
							Rw1[i]=lst1[m]
							res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb2,n))
							if(initial_board==res):
								pass
							else:
								lst.append(res)
						else:
							break

			elif(lst1[j] in e1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst1[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					Rw1[i]=lst1[j]
					res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
					if(initial_board==res):
						pass
					else:
						lst.append(res)
			else:
				pass



		for j in range(len(lst2)):
			w1=lst_copy(w)
			b1=lst_copy(b)
			W1=lst_copy(W)
			B1=lst_copy(B)
			Rw1=lst_copy(Rw)
			Rb1=lst_copy(Rb)
			e1=lst_copy(e)
			initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			if(lst2[j] in b1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst2[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst2)):
						b2=lst_copy(b)
						if(lst2[m] in e1):
							b2.remove(lst2[j])
							Rw1[i]=lst2[m]
							res=list_to_board(create_board(w1,W1,b2,B1,Rw1,Rb1,n))
							if(initial_board==res):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst2[j] in B1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst2[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst2)):
						B2=lst_copy(B)
						if(lst2[m] in e1):
							B2.remove(lst2[j])
							Rw1[i]=lst2[m]
							res=list_to_board(create_board(w1,W1,b1,B2,Rw1,Rb1,n))
							if(initial_board==res):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst2[j] in Rb1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst2[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst2)):
						Rb2=lst_copy(Rb)
						if(lst2[m] in e1):
							Rb2.remove(lst2[j])
							Rw1[i]=lst2[m]
							res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb2,n))
							if(initial_board==res):
								pass
							else:
								lst.append(res)
						else:
							break

			elif(lst2[j] in e1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst2[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					Rw1[i]=lst2[j]
					res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
					if(res==initial_board):
						pass
					else:
						lst.append(res)
			else:
				pass

		for j in range(len(lst3)):
			w1=lst_copy(w)
			b1=lst_copy(b)
			W1=lst_copy(W)
			B1=lst_copy(B)
			Rw1=lst_copy(Rw)
			Rb1=lst_copy(Rb)
			e1=lst_copy(e)
			initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			if(lst3[j] in b1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst3[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst3)):
						b2=lst_copy(b)
						if(lst3[m] in e1):
							b2.remove(lst3[j])
							Rw1[i]=lst3[m]
							res=list_to_board(create_board(w1,W1,b2,B1,Rw1,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst3[j] in B1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst3[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst3)):
						B2=lst_copy(B)
						if(lst3[m] in e1):
							B2.remove(lst3[j])
							Rw1[i]=lst3[m]
							res=list_to_board(create_board(w1,W1,b1,B2,Rw1,Rb1,n))
							if(initial_board==res):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst3[j] in Rb1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst3[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst3)):
						Rb2=lst_copy(Rb)
						if(lst3[m] in e1):
							Rb2.remove(lst3[j])
							Rw1[i]=lst3[m]
							res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb2,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break

			elif(lst3[j] in e1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst3[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					Rw1[i]=lst3[j]
					res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
					if(res==initial_board):
						pass
					else:
						lst.append(res)
			else:
				pass

		for j in range(len(lst4)):
			w1=lst_copy(w)
			b1=lst_copy(b)
			W1=lst_copy(W)
			B1=lst_copy(B)
			Rw1=lst_copy(Rw)
			Rb1=lst_copy(Rb)
			e1=lst_copy(e)
			initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			if(lst4[j] in b1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst4[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst4)):
						b2=lst_copy(b)
						if(lst4[m] in e1):
							b2.remove(lst4[j])
							Rw1[i]=lst4[m]
							res=list_to_board(create_board(w1,W1,b2,B1,Rw1,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst4[j] in B1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst4[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst4)):
						B2=lst_copy(B)
						if(lst4[m] in e1):
							B2.remove(lst4[j])
							Rw1[i]=lst4[m]
							res=list_to_board(create_board(w1,W1,b1,B2,Rw1,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst4[j] in Rb1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst4[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst4)):
						Rb2=lst_copy(Rb)
						if(lst4[m] in e1):
							Rb2.remove(lst4[j])
							Rw1[i]=lst4[m]
							res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb2,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break

			elif(lst4[j] in e1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst4[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					Rw1[i]=lst4[j]
					res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
					if(res==initial_board):
						pass
					else:
						lst.append(res)
			else:
				pass
		for j in range(len(lst5)):
			w1=lst_copy(w)
			b1=lst_copy(b)
			W1=lst_copy(W)
			B1=lst_copy(B)
			Rw1=lst_copy(Rw)
			Rb1=lst_copy(Rb)
			e1=lst_copy(e)
			initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			if(lst5[j] in b1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst5[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst5)):
						b2=lst_copy(b)
						if(lst5[m] in e1):
							b2.remove(lst5[j])
							Rw1[i]=lst5[m]
							res=list_to_board(create_board(w1,W1,b2,B1,Rw1,Rb1,n))
							if(initial_board==res):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst5[j] in B1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst5[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst5)):
						B2=lst_copy(B)
						if(lst5[m] in e1):
							B2.remove(lst5[j])
							Rw1[i]=lst5[m]
							res=list_to_board(create_board(w1,W1,b1,B2,Rw1,Rb1,n))
							if(initial_board==res):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst5[j] in Rb1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst5[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst5)):
						Rb2=lst_copy(Rb)
						if(lst5[m] in e1):
							Rb2.remove(lst5[j])
							Rw1[i]=lst5[m]
							res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb2,n))
							if(initial_board==res):
								pass
							else:
								lst.append(res)
						else:
							break

			elif(lst5[j] in e1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst5[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					Rw1[i]=lst5[j]
					res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
					if(initial_board==res):
						pass
					else:
						lst.append(res)
			else:
				pass
		for j in range(len(lst6)):
			w1=lst_copy(w)
			b1=lst_copy(b)
			W1=lst_copy(W)
			B1=lst_copy(B)
			Rw1=lst_copy(Rw)
			Rb1=lst_copy(Rb)
			e1=lst_copy(e)
			initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			if(lst6[j] in b1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst6[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst6)):
						b2=lst_copy(b)
						if(lst6[m] in e1):
							b2.remove(lst6[j])
							Rw1[i]=lst6[m]
							res=list_to_board(create_board(w1,W1,b2,B1,Rw1,Rb1,n))
							if(initial_board==res):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst6[j] in B1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst6[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst6)):
						B2=lst_copy(B)
						if(lst6[m] in e1):
							B2.remove(lst6[j])
							Rw1[i]=lst6[m]
							res=list_to_board(create_board(w1,W1,b1,B2,Rw1,Rb1,n))
							if(initial_board==res):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst6[j] in Rb1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst6[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst6)):
						Rb2=lst_copy(Rb)
						if(lst6[m] in e1):
							Rb2.remove(lst6[j])
							Rw1[i]=lst6[m]
							res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb2,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break

			elif(lst6[j] in e1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst6[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					Rw1[i]=lst6[j]
					res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
					if(initial_board==res):
						pass
					else:
						lst.append(res)
			else:
				pass
		for j in range(len(lst7)):
			w1=lst_copy(w)
			b1=lst_copy(b)
			W1=lst_copy(W)
			B1=lst_copy(B)
			Rw1=lst_copy(Rw)
			Rb1=lst_copy(Rb)
			e1=lst_copy(e)
			initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			if(lst7[j] in b1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst7[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst7)):
						b2=lst_copy(b)
						if(lst7[m] in e1):
							b2.remove(lst7[j])
							Rw1[i]=lst7[m]
							res=list_to_board(create_board(w1,W1,b2,B1,Rw1,Rb1,n))
							if(initial_board==res):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst7[j] in B1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst7[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst7)):
						B2=lst_copy(B)
						if(lst7[m] in e1):
							B2.remove(lst7[j])
							Rw1[i]=lst7[m]
							res=list_to_board(create_board(w1,W1,b1,B2,Rw1,Rb1,n))
							if(initial_board==res):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst7[j] in Rb1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst7[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst7)):
						Rb2=lst_copy(Rb)
						if(lst7[m] in e1):
							Rb2.remove(lst7[j])
							Rw1[i]=lst7[m]
							res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb2,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break

			elif(lst7[j] in e1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst7[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					Rw1[i]=lst7[j]
					res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
					if(initial_board==res):
						pass
					else:
						lst.append(res)
			else:
				pass

		for j in range(len(lst8)):
			w1=lst_copy(w)
			b1=lst_copy(b)
			W1=lst_copy(W)
			B1=lst_copy(B)
			Rw1=lst_copy(Rw)
			Rb1=lst_copy(Rb)
			e1=lst_copy(e)
			initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			if(lst8[j] in b1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst8[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst8)):
						b2=lst_copy(b)
						if(lst8[m] in e1):
							b2.remove(lst8[j])
							Rw1[i]=lst8[m]
							res=list_to_board(create_board(w1,W1,b2,B1,Rw1,Rb1,n))
							if(initial_board==res):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst8[j] in B1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst8[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst8)):
						B2=lst_copy(B)
						if(lst8[m] in e1):
							B2.remove(lst8[j])
							Rw1[i]=lst8[m]
							res=list_to_board(create_board(w1,W1,b1,B2,Rw1,Rb1,n))
							if(initial_board==res):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst8[j] in Rb1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst8[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst8)):
						Rb2=lst_copy(Rb)
						if(lst8[m] in e1):
							Rb2.remove(lst8[j])
							Rw1[i]=lst8[m]
							res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb2,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break

			elif(lst8[j] in e1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst8[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					Rw1[i]=lst8[j]
					res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
					if(initial_board==res):
						pass
					else:
						lst.append(res)
			else:
				pass

	lst.reverse()			
	return lst

		
def braichu_move(w,W,b,B,Rw,Rb,e,n1):
	lst=[]
	
	for i in range(len(Rb)):
		n=n1
		lst1=raichu_beam_up(*Rb[i],n)
		lst2=raichu_beam_down(*Rb[i],n)
		lst3=raichu_beam_right(*Rb[i],n)
		lst4=raichu_beam_left(*Rb[i],n)
		lst5=raichu_beam_rightd_down(*Rb[i],n)
		lst6=raichu_beam_rightd_up(*Rb[i],n)
		lst7=raichu_beam_leftd_down(*Rb[i],n)
		lst8=raichu_beam_leftd_up(*Rb[i],n)
		#print(lst2)

		for j in range(len(lst1)):
			w1=lst_copy(w)
			b1=lst_copy(b)
			W1=lst_copy(W)
			B1=lst_copy(B)
			Rw1=lst_copy(Rw)
			Rb1=lst_copy(Rb)
			e1=lst_copy(e)
			initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			if(lst1[j] in w1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst1[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst1)):
						w2=lst_copy(w)
						if(lst1[m] in e1):
							w2.remove(lst1[j])
							Rb1[i]=lst1[m]
							res=list_to_board(create_board(w2,W1,b1,B1,Rw1,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst1[j] in W1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst1[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst1)):
						W2=lst_copy(W)
						if(lst1[m] in e1):
							W2.remove(lst1[j])
							Rb1[i]=lst1[m]
							res=list_to_board(create_board(w1,W2,b1,B1,Rw1,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst1[j] in Rw1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst1[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst1)):
						Rw2=lst_copy(Rw)
						if(lst1[m] in e1):
							Rw2.remove(lst1[j])
							Rb1[i]=lst1[m]
							res=list_to_board(create_board(w1,W1,b1,B1,Rw2,Rb1,n))
							if(initial_board==res):
								pass
							else:
								lst.append(res)
						else:
							break

			elif(lst1[j] in e1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst1[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					Rb1[i]=lst1[j]
					res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
					if(initial_board==res):
						pass
					else:
						lst.append(res)
			else:
				pass



		for j in range(len(lst2)):
			w1=lst_copy(w)
			b1=lst_copy(b)
			W1=lst_copy(W)
			B1=lst_copy(B)
			Rw1=lst_copy(Rw)
			Rb1=lst_copy(Rb)
			e1=lst_copy(e)
			initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			if(lst2[j] in w1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst2[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst2)):
						w2=lst_copy(w)
						if(lst2[m] in e1):
							w2.remove(lst2[j])
							Rb1[i]=lst2[m]
							res=list_to_board(create_board(w2,W1,b1,B1,Rw1,Rb1,n))
							if(initial_board==res):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst2[j] in W1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst2[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst2)):
						W2=lst_copy(W)
						if(lst2[m] in e1):
							W2.remove(lst2[j])
							Rb1[i]=lst2[m]
							res=list_to_board(create_board(w1,W2,b1,B1,Rw1,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst2[j] in Rw1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst2[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst2)):
						Rw2=lst_copy(Rw)
						if(lst2[m] in e1):
							Rw2.remove(lst2[j])
							Rb1[i]=lst2[m]
							res=list_to_board(create_board(w1,W1,b1,B1,Rw2,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break

			elif(lst2[j] in e1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst2[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					Rb1[i]=lst2[j]
					res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
					if(res==initial_board):
						pass
					else:
						lst.append(res)
			else:
				pass

		for j in range(len(lst3)):
			w1=lst_copy(w)
			b1=lst_copy(b)
			W1=lst_copy(W)
			B1=lst_copy(B)
			Rw1=lst_copy(Rw)
			Rb1=lst_copy(Rb)
			e1=lst_copy(e)
			initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			if(lst3[j] in w1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst3[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst3)):
						w2=lst_copy(w)
						if(lst3[m] in e1):
							w2.remove(lst3[j])
							Rb1[i]=lst3[m]
							res=list_to_board(create_board(w2,W1,b1,B1,Rw1,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst3[j] in W1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst3[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst3)):
						W2=lst_copy(W)
						if(lst3[m] in e1):
							W2.remove(lst3[j])
							Rb1[i]=lst3[m]
							res=list_to_board(create_board(w1,W2,b1,B1,Rw1,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst3[j] in Rw1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst3[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst3)):
						Rw2=lst_copy(Rw)
						if(lst3[m] in e1):
							Rw2.remove(lst3[j])
							Rb1[i]=lst3[m]
							res=list_to_board(create_board(w1,W1,b1,B1,Rw2,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break

			elif(lst3[j] in e1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst3[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					Rb1[i]=lst3[j]
					res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
					if(res==initial_board):
						pass
					else:
						lst.append(res)
			else:
				pass

		for j in range(len(lst4)):
			w1=lst_copy(w)
			b1=lst_copy(b)
			W1=lst_copy(W)
			B1=lst_copy(B)
			Rw1=lst_copy(Rw)
			Rb1=lst_copy(Rb)
			e1=lst_copy(e)
			initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			if(lst4[j] in w1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst4[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst4)):
						w2=lst_copy(w)
						if(lst4[m] in e1):
							w2.remove(lst4[j])
							Rb1[i]=lst4[m]
							res=list_to_board(create_board(w2,W1,b1,B1,Rw1,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst4[j] in W1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst4[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst4)):
						W2=lst_copy(W)
						if(lst4[m] in e1):
							W2.remove(lst4[j])
							Rb1[i]=lst4[m]
							res=list_to_board(create_board(w1,W2,b1,B1,Rw1,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst4[j] in Rw1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst4[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst4)):
						Rw2=lst_copy(Rw)
						if(lst4[m] in e1):
							Rw2.remove(lst4[j])
							Rb1[i]=lst4[m]
							res=list_to_board(create_board(w1,W1,b1,B1,Rw2,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break

			elif(lst4[j] in e1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst4[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					Rb1[i]=lst4[j]
					res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
					if(res==initial_board):
						pass
					else:
						lst.append(res)
			else:
				pass
		for j in range(len(lst5)):
			w1=lst_copy(w)
			b1=lst_copy(b)
			W1=lst_copy(W)
			B1=lst_copy(B)
			Rw1=lst_copy(Rw)
			Rb1=lst_copy(Rb)
			e1=lst_copy(e)
			initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			if(lst5[j] in w1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst5[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst5)):
						w2=lst_copy(w)
						if(lst5[m] in e1):
							w2.remove(lst5[j])
							Rb1[i]=lst5[m]
							res=list_to_board(create_board(w2,W1,b1,B1,Rw1,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst5[j] in W1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst5[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst5)):
						W2=lst_copy(W)
						if(lst5[m] in e1):
							W2.remove(lst5[j])
							Rb1[i]=lst5[m]
							res=list_to_board(create_board(w1,W2,b1,B1,Rw1,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst5[j] in Rw1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst5[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst5)):
						Rw2=lst_copy(Rw)
						if(lst5[m] in e1):
							Rw2.remove(lst5[j])
							Rb1[i]=lst5[m]
							res=list_to_board(create_board(w1,W1,b1,B1,Rw2,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break

			elif(lst5[j] in e1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst5[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					Rb1[i]=lst5[j]
					res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
					if(res==initial_board):
						pass
					else:
						lst.append(res)
			else:
				pass
		for j in range(len(lst6)):
			w1=lst_copy(w)
			b1=lst_copy(b)
			W1=lst_copy(W)
			B1=lst_copy(B)
			Rw1=lst_copy(Rw)
			Rb1=lst_copy(Rb)
			e1=lst_copy(e)
			initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			if(lst6[j] in w1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst6[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst6)):
						w2=lst_copy(w)
						if(lst6[m] in e1):
							w2.remove(lst6[j])
							Rb1[i]=lst6[m]
							res=list_to_board(create_board(w2,W1,b1,B1,Rw1,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst6[j] in W1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst6[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst6)):
						W2=lst_copy(W)
						if(lst6[m] in e1):
							W2.remove(lst6[j])
							Rb1[i]=lst6[m]
							res=list_to_board(create_board(w1,W2,b1,B1,Rw1,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst6[j] in Rw1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst6[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst6)):
						Rw2=lst_copy(Rw)
						if(lst6[m] in e1):
							Rw2.remove(lst6[j])
							Rb1[i]=lst6[m]
							res=list_to_board(create_board(w1,W1,b1,B1,Rw2,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break

			elif(lst6[j] in e1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst6[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					Rb1[i]=lst6[j]
					res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
					if(res==initial_board):
						pass
					else:
						lst.append(res)
			else:
				pass
		for j in range(len(lst7)):
			w1=lst_copy(w)
			b1=lst_copy(b)
			W1=lst_copy(W)
			B1=lst_copy(B)
			Rw1=lst_copy(Rw)
			Rb1=lst_copy(Rb)
			e1=lst_copy(e)
			initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			if(lst7[j] in w1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst7[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst7)):
						w2=lst_copy(w)
						if(lst7[m] in e1):
							w2.remove(lst7[j])
							Rb1[i]=lst7[m]
							res=list_to_board(create_board(w2,W1,b1,B1,Rw1,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst7[j] in W1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst7[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst7)):
						W2=lst_copy(W)
						if(lst7[m] in e1):
							W2.remove(lst7[j])
							Rb1[i]=lst7[m]
							res=list_to_board(create_board(w1,W2,b1,B1,Rw1,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst7[j] in Rw1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst7[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst7)):
						Rw2=lst_copy(Rw)
						if(lst7[m] in e1):
							Rw2.remove(lst7[j])
							Rb1[i]=lst7[m]
							res=list_to_board(create_board(w1,W1,b1,B1,Rw2,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break

			elif(lst7[j] in e1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst7[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					Rb1[i]=lst7[j]
					res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
					if(res==initial_board):
						pass
					else:
						lst.append(res)
			else:
				pass

		for j in range(len(lst8)):
			w1=lst_copy(w)
			b1=lst_copy(b)
			W1=lst_copy(W)
			B1=lst_copy(B)
			Rw1=lst_copy(Rw)
			Rb1=lst_copy(Rb)
			e1=lst_copy(e)
			initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			if(lst8[j] in w1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst8[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst8)):
						w2=lst_copy(w)
						if(lst8[m] in e1):
							w2.remove(lst8[j])
							Rb1[i]=lst8[m]
							res=list_to_board(create_board(w2,W1,b1,B1,Rw1,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst8[j] in W1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst8[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst8)):
						W2=lst_copy(W)
						if(lst8[m] in e1):
							W2.remove(lst8[j])
							Rb1[i]=lst8[m]
							res=list_to_board(create_board(w1,W2,b1,B1,Rw1,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break
			
			elif(lst8[j] in Rw1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst8[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					for m in range(j+1,len(lst8)):
						Rw2=lst_copy(Rw)
						if(lst8[m] in e1):
							Rw2.remove(lst8[j])
							Rb1[i]=lst8[m]
							res=list_to_board(create_board(w1,W1,b1,B1,Rw2,Rb1,n))
							if(res==initial_board):
								pass
							else:
								lst.append(res)
						else:
							break

			elif(lst8[j] in e1):

				flag=0
				if(j==0):
					pass
				else:
					for k in range(j-1,-1,-1):
						if(lst8[k] in e1):
							pass
						else:
							flag=flag+1

				if(flag==0):
					Rb1[i]=lst8[j]
					res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
					if(res==initial_board):
						pass
					else:
						lst.append(res)
			else:
				pass


	return lst

		
	

				

			




def wpichu_move(w,W,b,B,Rw,Rb,e,n1): # add size to the parameters
	lst=[]
	for i in range(len(w)):
		n=n1
		lst1=valid_w_pichu_ld(*w[i],n)
		lst2=valid_w_pichu_rd(*w[i],n)
		for j in lst1:
			w1=lst_copy(w)
			b1=lst_copy(b)
			W1=lst_copy(W)
			B1=lst_copy(B)
			Rw1=lst_copy(Rw)
			Rb1=lst_copy(Rb)
			e1=lst_copy(e)
			rw_row=[]
			initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			for k in range(n):
				rw_row.append((n-1,k))
			#rw_row=[(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7)]
			if(j in b1):
				temp=valid_w_pichu_ld(*j,n)
				if(len(temp)>0):
					if(temp[0] in e1):
						b1.remove(j)
						if(temp[0] in rw_row):
							w1.remove(w1[i])
							Rw1.append(temp[0])
						else:
							w1[i]=temp[0]
					else:
						pass
			elif(j in rw_row):
				w1.remove(w1[i])
				Rw1.append(j)
			elif(j in e1):
				w1[i]=j
			else:
				pass
			#print(j)
			res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			#print(res)
			if(res==initial_board):
				pass
			else:
				lst.append(res)
		for j in lst2:
			w1=lst_copy(w)
			b1=lst_copy(b)
			W1=lst_copy(W)
			B1=lst_copy(B)
			Rw1=lst_copy(Rw)
			Rb1=lst_copy(Rb)
			e1=lst_copy(e)
			initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			#rw_row=[(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7)]
			rw_row=[]
			for k in range(n):
				rw_row.append((n-1,k))
			if(j in b1):
				temp=valid_w_pichu_rd(*j,n)
				if(len(temp)>0):
					if(temp[0] in e1):
						b1.remove(j)
						if(temp[0] in rw_row):
							w1.remove(w1[i])
							Rw1.append(temp[0])
						else:
							w1[i]=temp[0]
					else:
						pass
			elif(j in rw_row):
				w1.remove(w1[i])
				Rw1.append(j)
			elif(j in e1):
				w1[i]=j
			else:
				pass
			
			res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			if(res==initial_board):
				pass
			else:
				lst.append(res)
	return lst		

def bpichu_move(w,W,b,B,Rw,Rb,e,n1): # add size to the parameters
	lst=[]
	for i in range(len(b)):
		n=n1
		lst1=valid_b_pichu_ld(*b[i],n)
		lst2=valid_b_pichu_rd(*b[i],n)
		for j in lst1:
			w1=lst_copy(w)
			b1=lst_copy(b)
			W1=lst_copy(W)
			B1=lst_copy(B)
			Rw1=lst_copy(Rw)
			Rb1=lst_copy(Rb)
			e1=lst_copy(e)
			rw_row=[]
			initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			for k in range(n):
				rw_row.append((0,k))
			#rw_row=[(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7)]
			if(j in w1):
				temp=valid_b_pichu_ld(*j,n)
				if(len(temp)>0):
					if(temp[0] in e1):
						w1.remove(j)
						if(temp[0] in rw_row):
							b1.remove(b1[i])
							Rb1.append(temp[0])
						else:
							b1[i]=temp[0]
					else:
						pass
			elif(j in rw_row):
				b1.remove(b1[i])
				Rb1.append(j)
			elif(j in e1):
				b1[i]=j
			else:
				pass
			#print(j)
			res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			if(res==initial_board):
				pass
			else:
			#print(res)
				lst.append(res)
		for j in lst2:
			w1=lst_copy(w)
			b1=lst_copy(b)
			W1=lst_copy(W)
			B1=lst_copy(B)
			Rw1=lst_copy(Rw)
			Rb1=lst_copy(Rb)
			e1=lst_copy(e)
			initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			rw_row=[]
			for k in range(n):
				rw_row.append((0,k))
			#rw_row=[(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7)]
			if(j in w1):
				temp=valid_b_pichu_rd(*j,n)
				if(len(temp)>0):
					if(temp[0] in e1):
						w1.remove(j)
						if(temp[0] in rw_row):
							b1.remove(b1[i])
							Rb1.append(temp[0])
						else:
							b1[i]=temp[0]
					else:
						pass
			elif(j in rw_row):
				b1.remove(w1[i])
				Rb1.append(j)
			elif(j in e1):
				b1[i]=j
			else:
				pass
			
			res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
			if(res==initial_board):
				pass
			else:
				lst.append(res)
	return lst	
	
def wpikachu_move(w,W,b,B,Rw,Rb,e,n1): #add size to parameters 
	lst=[]
	for i in range(len(W)):
		n=n1
		lst1=valid_w_pikachu_up1(*W[i],n)
		lst2=valid_w_pikachu_up2(*W[i],n)
		lst3=valid_w_pikachu_r1(*W[i],n)
		lst4=valid_w_pikachu_r2(*W[i],n)
		lst5=valid_w_pikachu_l1(*W[i],n)
		lst6=valid_w_pikachu_l2(*W[i],n)
		
		if(len(lst1)>0):
			for j in lst1:
				w1=lst_copy(w)
				b1=lst_copy(b)
				W1=lst_copy(W)
				B1=lst_copy(B)
				Rw1=lst_copy(Rw)
				Rb1=lst_copy(Rb)
				e1=lst_copy(e)
				initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				rw_row=[]
				for k in range(n):
					rw_row.append((n-1,k))
				#rw_row=[(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7)]
				if(j in b1):
					temp=valid_w_pikachu_up1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							b1.remove(j)
							if(temp[0] in rw_row):
								W1.remove(W1[i])
								Rw1.append(temp[0])
							else:
								W1[i]=temp[0]
						else:
							pass
				elif(j in B1):
					temp=valid_w_pikachu_up1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							B1.remove(j)
							if(temp[0] in rw_row):
								W1.remove(W1[i])
								Rw1.append(temp[0])
							else:
								W1[i]=temp[0]
						else:
							pass
				elif(j in rw_row):
					W1.remove(W1[i])
					Rw1.append(j)
				elif(j in e1):
					#pass
					W1[i]=j
				else:
					pass
			#print(j)
				res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				if(res==initial_board):
					pass
				else:
			#print(res)
					lst.append(res)
		if(len(lst1)>0 and lst1[0] in e):
			for j in lst2:
				w1=lst_copy(w)
				b1=lst_copy(b)
				W1=lst_copy(W)
				B1=lst_copy(B)
				Rw1=lst_copy(Rw)
				Rb1=lst_copy(Rb)
				e1=lst_copy(e)
				initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				rw_row=[]
				for k in range(n):
					rw_row.append((n-1,i))
				#rw_row=[(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7)]
				if(j in b1):
					temp=valid_w_pikachu_up1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							b1.remove(j)
							if(temp[0] in rw_row):
								W1.remove(W1[i])
								Rw1.append(temp[0])
							else:
								W1[i]=temp[0]
						else:
							pass
				elif(j in B1):
					temp=valid_w_pikachu_up1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							B1.remove(j)
							if(temp[0] in rw_row):
								W1.remove(W1[i])
								Rw1.append(temp[0])
							else:
								W1[i]=temp[0]
						else:
							pass
				elif(j in rw_row):
					W1.remove(W1[i])
					Rw1.append(j)
				elif(j in e1):
					W1[i]=j
				
				else:
					pass
			
				res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				if(initial_board==res):
					pass
				else:
					lst.append(res)
		if(len(lst3)>0):
			for j in lst3:
				w1=lst_copy(w)
				b1=lst_copy(b)
				W1=lst_copy(W)
				B1=lst_copy(B)
				Rw1=lst_copy(Rw)
				Rb1=lst_copy(Rb)
				e1=lst_copy(e)
				initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				#rw_row=[(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7)]
				if(j in b1):
					temp=valid_w_pikachu_r1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							b1.remove(j)
							W1[i]=temp[0]
						else:
							pass
				elif(j in B1):
					temp=valid_w_pikachu_r1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							B1.remove(j)
							W1[i]=temp[0]
						else:
							pass
				#elif(j in rw_row):
				#	W1.remove(W1[i])
				#	Rw1.append(j)
				elif(j in e1):
					W1[i]=j
				else:
					pass
			#print(j)
			#####add if condition for checking board with parent in successor
				res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				if(res==initial_board):
					pass
				else:
			#print(res)
					lst.append(res)
		if(len(lst3)>0 and lst3[0] in e):
			for j in lst4:
				w1=lst_copy(w)
				b1=lst_copy(b)
				W1=lst_copy(W)
				B1=lst_copy(B)
				Rw1=lst_copy(Rw)
				Rb1=lst_copy(Rb)
				e1=lst_copy(e)
				initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				if(j in b1):
					temp=valid_w_pikachu_r1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							b1.remove(j)
							W1[i]=temp[0]
						else:
							pass
				elif(j in B1):
					temp=valid_w_pikachu_r1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							B1.remove(j)
							W1[i]=temp[0]
						else:
							pass
				#elif(j in rw_row):
				#	W1.remove(W1[i])
				#	Rw1.append(j)
				elif(j in e1):
					W1[i]=j
				
				else:
					pass
			
				res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				if(res==initial_board):
					pass
				else:
					lst.append(res)
		if(len(lst5)>0):
			for j in lst5:
				w1=lst_copy(w)
				b1=lst_copy(b)
				W1=lst_copy(W)
				B1=lst_copy(B)
				Rw1=lst_copy(Rw)
				Rb1=lst_copy(Rb)
				e1=lst_copy(e)
				initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				#rw_row=[(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7)]
				if(j in b1):
					temp=valid_w_pikachu_l1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							b1.remove(j)
							W1[i]=temp
						else:
							pass
				elif(j in B1):
					temp=valid_w_pikachu_l1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							B1.remove(j)
							W1[i]=temp[0]
						else:
							pass
				#elif(j in rw_row):
				#	W1.remove(W1[i])
				#	Rw1.append(j)
				elif(j in e1):
					W1[i]=j
				else:
					pass
			#print(j)
				res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				if(res==initial_board):
					pass
				else:
			#print(res)
					lst.append(res)
		if(len(lst5)>0 and lst5[0] in e):
			for j in lst6:
				w1=lst_copy(w)
				b1=lst_copy(b)
				W1=lst_copy(W)
				B1=lst_copy(B)
				Rw1=lst_copy(Rw)
				Rb1=lst_copy(Rb)
				e1=lst_copy(e)
				initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				if(j in b1):
					temp=valid_w_pikachu_l1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							b1.remove(j)
							W1[i]=temp[0]
						else:
							pass
				elif(j in B1):
					temp=valid_w_pikachu_l1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							B1.remove(j)
							W1[i]=temp[0]
						else:
							pass
				#elif(j in rw_row):
				#	W1.remove(W1[i])
				#	Rw1.append(j)
				elif(j in e1):
					W1[i]=j
				
				else:
					pass
			
				res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				if(res==initial_board):
					pass
				else:
					lst.append(res)
	return lst

def bpikachu_move(w,W,b,B,Rw,Rb,e,n1): #add size to parameters 
	lst=[]
	for i in range(len(B)):
		n=n1
		lst1=valid_b_pikachu_up1(*B[i],n)
		lst2=valid_b_pikachu_up2(*B[i],n)
		lst3=valid_w_pikachu_r1(*B[i],n)
		lst4=valid_w_pikachu_r2(*B[i],n)
		lst5=valid_w_pikachu_l1(*B[i],n)
		lst6=valid_w_pikachu_l2(*B[i],n)

		if(len(lst1)>0):
			for j in lst1:
				w1=lst_copy(w)
				b1=lst_copy(b)
				W1=lst_copy(W)
				B1=lst_copy(B)
				Rw1=lst_copy(Rw)
				Rb1=lst_copy(Rb)
				e1=lst_copy(e)
				initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				rw_row=[]
				for k in range(n):
					rw_row.append((0,k))
				#rw_row=[(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7)]
				if(j in w1):
					temp=valid_b_pikachu_up1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							w1.remove(j)
							if(temp[0] in rw_row):
								B1.remove(B1[i])
								Rb1.append(temp[0])
							else:
								B1[i]=temp[0]
						else:
							pass
				elif(j in W1):
					temp=valid_b_pikachu_up1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							W1.remove(j)
							if(temp[0] in rw_row):
								B1.remove(B1[i])
								Rb1.append(temp[0])
							else:
								B1[i]=temp[0]
						else:
							pass
				elif(j in rw_row):
					B1.remove(B1[i])
					Rb1.append(j)
				elif(j in e1):
					B1[i]=j
				else:
					pass
			#print(j)
				res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				if(res==initial_board):
					pass
				else:
			#print(res)
					lst.append(res)
		if(len(lst1)>0 and lst1[0] in e):
			for j in lst2:
				w1=lst_copy(w)
				b1=lst_copy(b)
				W1=lst_copy(W)
				B1=lst_copy(B)
				Rw1=lst_copy(Rw)
				Rb1=lst_copy(Rb)
				e1=lst_copy(e)
				initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				rw_row=[]
				for k in range(n):
					rw_row.append((0,k))
				#rw_row=[(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7)]
				if(j in w1):
					temp=valid_b_pikachu_up1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							w1.remove(j)
							if(temp[0] in rw_row):
								B1.remove(B1[i])
								Rb1.append(temp[0])
							else:
								B1[i]=temp[0]
						else:
							pass
				elif(j in W1):
					temp=valid_b_pikachu_up1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							W1.remove(j)
							if(temp[0] in rw_row):
								B1.remove(B1[i])
								Rb1.append(temp[0])
							else:
								B1[i]=temp[0]
						else:
							pass
				elif(j in rw_row):
					B1.remove(B1[i])
					Rb1.append(j)
				elif(j in e1):
					B1[i]=j
				
				else:
					pass
			
				res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				if(res==initial_board):
					pass
				else:
					lst.append(res)
		if(len(lst3)>0):
			for j in lst3:
				w1=lst_copy(w)
				b1=lst_copy(b)
				W1=lst_copy(W)
				B1=lst_copy(B)
				Rw1=lst_copy(Rw)
				Rb1=lst_copy(Rb)
				e1=lst_copy(e)
				initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				#rw_row=[(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7)]
				if(j in w1):
					temp=valid_w_pikachu_r1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							w1.remove(j)
							B1[i]=temp[0]
						else:
							pass
				elif(j in W1):
					temp=valid_w_pikachu_r1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							W1.remove(j)
							B1[i]=temp[0]
						else:
							pass
				#elif(j in rw_row):
				#	W1.remove(W1[i])
				#	Rw1.append(j)
				elif(j in e1):
					B1[i]=j
				else:
					pass
			#print(j)
			#####add if condition for checking board with parent in successor
				res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				if(res==initial_board):
					pass
				else:
			#print(res)
					lst.append(res)
		if(len(lst3)>0 and lst3[0] in e):
			for j in lst4:
				w1=lst_copy(w)
				b1=lst_copy(b)
				W1=lst_copy(W)
				B1=lst_copy(B)
				Rw1=lst_copy(Rw)
				Rb1=lst_copy(Rb)
				e1=lst_copy(e)
				initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				if(j in w1):
					temp=valid_w_pikachu_r1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							w1.remove(j)
							B1[i]=temp[0]
						else:
							pass
				elif(j in W1):
					temp=valid_w_pikachu_r1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							W1.remove(j)
							B1[i]=temp[0]
						else:
							pass
				#elif(j in rw_row):
				#	W1.remove(W1[i])
				#	Rw1.append(j)
				elif(j in e1):
					B1[i]=j
				
				else:
					pass
			
				res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				if(res==initial_board):
					pass
				else:
					lst.append(res)
		if(len(lst5)>0):
			for j in lst5:
				w1=lst_copy(w)
				b1=lst_copy(b)
				W1=lst_copy(W)
				B1=lst_copy(B)
				Rw1=lst_copy(Rw)
				Rb1=lst_copy(Rb)
				e1=lst_copy(e)
				initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				#rw_row=[(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7)]
				if(j in w1):
					temp=valid_w_pikachu_l1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							w1.remove(j)
							B1[i]=temp
						else:
							pass
				elif(j in W1):
					temp=valid_w_pikachu_l1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							W1.remove(j)
							B1[i]=temp[0]
						else:
							pass
				#elif(j in rw_row):
				#	W1.remove(W1[i])
				#	Rw1.append(j)
				elif(j in e1):
					B1[i]=j
				else:
					pass
			#print(j)
				res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				if(res==initial_board):
					pass
				else:
			#print(res)
					lst.append(res)
		if(len(lst5)>0 and lst5[0] in e):
			for j in lst6:
				w1=lst_copy(w)
				b1=lst_copy(b)
				W1=lst_copy(W)
				B1=lst_copy(B)
				Rw1=lst_copy(Rw)
				Rb1=lst_copy(Rb)
				e1=lst_copy(e)
				initial_board=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				if(j in w1):
					temp=valid_w_pikachu_l1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							w1.remove(j)
							B1[i]=temp[0]
						else:
							pass
				elif(j in W1):
					temp=valid_w_pikachu_l1(*j,n)
					if(len(temp)>0):
						if(temp[0] in e1):
							W1.remove(j)
							B1[i]=temp[0]
						else:
							pass
				#elif(j in rw_row):
				#	W1.remove(W1[i])
				#	Rw1.append(j)
				elif(j in e1):
					B1[i]=j
				
				else:
					pass
			
				res=list_to_board(create_board(w1,W1,b1,B1,Rw1,Rb1,n))
				if(res==initial_board):
					pass
				else:
					lst.append(res)
	return lst


class Board:
	def __init__(self,board,N,p,parent,ismaximizing,player,level):
		self.board=board_to_list(board,N)
		
		self.parent=parent
		self.N=N
		
		self.player=player
		self.p=p
		self.white_pichus=find_white_pichus(board_to_list(board,N))
		self.black_pichus=find_black_pichus(board_to_list(board,N))
		self.white_pikachus=find_white_pikachus(board_to_list(board,N))
		self.black_pikachus=find_black_pikachus(board_to_list(board,N))
		self.white_raichus=find_white_raichus(board_to_list(board,N))
		self.black_raichus=find_black_raichus(board_to_list(board,N))
		self.empty_space=empty_space((board_to_list(board,N)))
		
		self.utility_score=utility_score(len(self.white_pichus),len(self.black_pichus),len(self.white_pikachus),len(self.black_pikachus),len(self.white_raichus),len(self.black_raichus),)
		
		self.move=None
		self.best_score=0
		
		self.min_score=float('inf')
		self.max_score=float('-inf')
		
		self.ismaximizing=ismaximizing
		self.player1=""
		self.level=level

	def successor(self):
		lst=[]
		if(self.player=="w"):
			lst1=wpikachu_move(self.white_pichus,self.white_pikachus,self.black_pichus,self.black_pikachus,self.white_raichus,self.black_raichus,self.empty_space,self.N)
			lst2=wpichu_move(self.white_pichus,self.white_pikachus,self.black_pichus,self.black_pikachus,self.white_raichus,self.black_raichus,self.empty_space,self.N)
			lst3=wraichu_move(self.white_pichus,self.white_pikachus,self.black_pichus,self.black_pikachus,self.white_raichus,self.black_raichus,self.empty_space,self.N)
			for i in lst1:
				lst.append(Board(i,N,self.p,self,not(self.ismaximizing),"b",self.level-1))
			for i in lst2:
				lst.append(Board(i,N,self.p,self,not(self.ismaximizing),"b",self.level-1))
			for i in lst3:
				lst.append(Board(i,N,self.p,self,not(self.ismaximizing),"b",self.level-1))
		else:
			lst1=bpikachu_move(self.white_pichus,self.white_pikachus,self.black_pichus,self.black_pikachus,self.white_raichus,self.black_raichus,self.empty_space,self.N)
			lst2=bpichu_move(self.white_pichus,self.white_pikachus,self.black_pichus,self.black_pikachus,self.white_raichus,self.black_raichus,self.empty_space,self.N)
			lst3=braichu_move(self.white_pichus,self.white_pikachus,self.black_pichus,self.black_pikachus,self.white_raichus,self.black_raichus,self.empty_space,self.N)
			for i in lst1:
				lst.append(Board(i,N,self.p,self,not(self.ismaximizing),"w",self.level-1))
			for i in lst2:
				lst.append(Board(i,N,self.p,self,not(self.ismaximizing),"w",self.level-1))
			for i in lst3:
				lst.append(Board(i,N,self.p,self,not(self.ismaximizing),"w",self.level-1))
		return lst

	def set_player1(self,pla):
		self.player1=pla
	def ret_level(self):
		return self.level
	def return_is_maximizing(self):
		return self.ismaximizing
	def return_board(self):
		#return raichu_beam_rightd_down(4,6,8)
		#return self.max_score
		return self.board
		#return wraichu_move(self.white_pichus,self.white_pikachus,self.black_pichus,self.black_pikachus,self.white_raichus,self.black_raichus,self.empty_space)
	def ret_parent(self):
		return self.parent
	def set_best_move(self,mov):
		self.move=mov
	def ret_lst(self):
		return self.board
	def change_score(self):
		if(self.level==0):
			if(self.parent.return_is_maximizing()):
				self.parent.max_best_score(self.utility_score,self.board)
			else:
				self.parent.min_best_score(self.utility_score,self.board)
		else:
			if(self.parent.return_is_maximizing()):
				self.parent.max_best_score(self.best_score,self.board)
			else:
				self.parent.min_best_score(self.best_score,self.board)


	def min_best_score(self,score,mov):
		if(self.min_score>=score):
			self.min_score=score
			self.best_score=score
			self.move=mov
			
	def max_best_score(self,score,mov):
		if(self.max_score<=score):
			self.max_score=score
			self.best_score=score
			self.move=mov
	def print_max_score(self):
		return self.max_score

	def ret_best_move(self):
		return self.move

	def ret_level(self):
		return self.level

def find_best_move(board, N, player, timelimit):
    # This sample code just returns the same board over and over again (which
    # isn't a valid move anyway.) Replace this with your code!
    #
    #time_duration=10
    #time_start=time.time()
    #while(time.time()<time_start+time_duration):
    #    b1=Board(board,N,player,None,True,player,1)
   	#	lst=b1.successor()
   	#	for i in lst:
   	#		i.change_score()
   	#	yield list_to_board(b1.ret_best_move())
        
   	fringe=[]
   	time_start=time.time()
   	level=2
   	#print(time_start)
   	while(time.time()<time_start+timelimit):
   		
   		b1=Board(board,N,player,None,True,player,level)
   		fringe.append([b1])
   		compute_list=[]
   		while fringe:
   			k=fringe.pop(0)
   			for i in k:
   				if(i.ret_level()==0):
   					compute_list.append(i)
   				else:
   					fringe.append(i.successor())
   					compute_list.append(i)
   		#for i in compute_list:
   		#	print(i.return_board())
   		for i in range(len(compute_list)-1,0,-1):
   			compute_list[i].change_score()
   			#print(compute_list[i].ret_level())
   		yield list_to_board(compute_list[0].ret_best_move())
   		#level=level+1
   			#print(k)
   		#lst=b1.successor()
   		#for i in lst:
   		#	print(i.return_board())
   		#print(b1.ret_level())
   		#for i in lst:
   			#i.change_score()
   		#	print(i.ret_level())
   		#yield list_to_board(b1.ret_best_move())

   	#b2=Board(board,N,player,b1,False,"w",1)
   	#print(b1.print_max_score())
   	#b2.change_score()
   	#print(b1.print_max_score())
   	#lst=b1.successor()
   	#for i in lst:
   #		print(i.ret_level())
   	#b1.set_best_move(b2)
   	#l2=b1.ret_lst()
   	#l2[0]=(3,4)
   	#print(b1.ret_lst())
   	#print(b1.ret_best_move().return_board())
   	#print(b2.ret_parent().return_board())
   	#lst1=[(1,2),(2,3)]
   	#lst2=lst_copy(lst1)
   	#print(lst1)
   	#print(lst2)
   	#print(lst1)
   	#print(lst2)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise Exception("Usage: Raichu.py N player board timelimit")
        
    (_, N, player, board, timelimit) = sys.argv
    N=int(N)
    timelimit=int(timelimit)
    if player not in "wb":
        raise Exception("Invalid player.")

    if len(board) != N*N or 0 in [c in "wb.WB@$" for c in board]:
        raise Exception("Bad board string.")

    print("Searching for best move for " + player + " from board state: \n" + board_to_string(board, N))
    print("Here's what I decided:")
    for new_board in find_best_move(board, N, player, timelimit):
        print(new_board)
    #find_best_move(board, N, player, timelimit)
