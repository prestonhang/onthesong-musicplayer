import random
import sys
import time

def read_file(file_path):
	with open(file_path, 'r') as file:
		file_contents = file.readline()
	return file_contents

def wait_update(file_path):
	change = False
	initial = read_file(file_path)
	while not change:
		current = read_file(file_path)
		if initial != current:
			change = True
		time.sleep(1)


def write_file(file_path, content):
	with open(file_path, 'w') as file:
		file.write(str(content))

def get_songs(song_list_path):
	songs = []
	with open(song_list_path, 'r') as file:
		for song in file:
			songs.append(song.strip())
	return songs

def get_suggestion(song_list):
	rand = random.randint(0, len(song_list) - 1)
	return song_list[rand]

def main():
	if len(sys.argv) != 3:
		print("Usage: " + sys.argv[0] + " song_list_path pipe_file_path")
		quit()
	
	song_list_path = str(sys.argv[1])
	pipe_file_path = str(sys.argv[2])

	songs = get_songs(song_list_path)

	while True:
		wait_update(pipe_file_path)
		time.sleep(1)
		suggestion = get_suggestion(songs)
		write_file(pipe_file_path, suggestion)
main()
