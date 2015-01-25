#!/usr/bin/bash

import random

class graph_generator:
		def letter_list_generator(self,amount):
				letter_list=list(map(chr,range(97,123)))
				random_letter_list=random.sample(letter_list,amount)
				return random_letter_list

		# Takes a list of letters and the letter you want to add connections to.
		# Randomly picks how many connections to make. Then chooses random letters in letter list,
		# while verifying that the chosen letter is not the letter given.
		# Randomly generates distances between 1 and 20, and returns a list containing a list of connected letters, 
		# and a dict of the distances to those letters.

		def connection_generator(self,letter,letter_list,max_dist=20, min_dist=1):

				number_of_connections=random.randint(1,len(letter_list))
				rand_letters=random.sample(letter_list,number_of_connections)
				connections=[]
				con_dict={}

				for other_letter in rand_letters:
						if letter != other_letter:
								dist=random.randint(min_dist,max_dist)
								connections.append(other_letter)
								con_dict[other_letter]=dist
				return [connections,con_dict]

		def __init__(self,list_amount=8):
				self.graph={}
				letter_list=self.letter_list_generator(list_amount)
				for letter in letter_list:
						self.graph[letter]=self.connection_generator(letter,letter_list)

class dijkstras_shortest_path:
		def __init__(self,graph):
				self.graph=graph
				self.value_checker(graph)

		def keep_track_lowest_distance(self):
				pass
		def value_checker(self,graph):
				for letter,value_list in graph.iteritems():
						letter_list=value_list[0]
						connections=value_list[1]
						for other_letter,distance in connections.iteritems():
								print letter+" to "+other_letter+" is "+str(distance)+" miles away"

dijkstras_shortest_path(graph_generator().graph)
