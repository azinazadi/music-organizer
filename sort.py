import os
import sys
file_list = []
rootdir = 'Music'
exportdir  = 'sorted'
for root, subFolders, files in os.walk(rootdir):
	for file in files:
		file_list.append(os.path.join(root,file))

import eyeD3, shutil
for file in file_list:
	tag = eyeD3.Tag()
	tag.link(file)
	title= tag.getTitle()[:min(len(tag.getTitle()), 50)]
	if title == None or title == "": title = file[-8:-5]
	tracknum = str(tag.getTrackNum()[0])
	if tracknum == "None":
		tracknum = ""
	else: 
		tracknum = str(tracknum) + " -"
	dest = exportdir + "/%s/%s/%s %s" % (tag.getArtist(), tag.getAlbum(),tracknum, title)
	print file, dest
	destdir = os.path.dirname(dest) 
	if not os.path.isdir(destdir): os.makedirs( destdir ) 
	shutil.copy( file, dest )
	print
