#verts in connected_verts contain letter and distance from path

connected_verts = [("b",1), ("c",4)]

def smallest_path(connected_verts,position=("a",0)):
		lowest_path = None
		for verts in connected_verts:
				if verts[0] != position[0]:
						if lowest_path and lowest_path > verts[1]:
									lowest_path = verts[1]
						elif not lowest_path:
								lowest_path = verts[1]						
		print lowest_path

smallest_path(connected_verts)
