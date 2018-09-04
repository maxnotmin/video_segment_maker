import sys, os
from standard_csv_reader2 import TheCSVReader
from video_segment_maker import MakeMovies
from cmd_creator import MakeCommand
import sys, os
from os import listdir
from os.path import isfile, join


VIDEO_PATH = 'FOLDER_NAME'
VIDEO_CLIPS_DIR = 'SUB_FOLDER_NAME'

clip_path = os.path.join(VIDEO_PATH, VIDEO_CLIPS_DIR)


def get_thumbnail(thumb_path=''):
    # GET FULL MOVIE

    # print("def get_movie : GET MOVIE FOLDER: ", self.cur_dir,  the_folder)
    for thumb in os.listdir(VIDEO_PATH):
        if thumb.endswith(".jpg"):
            the_thumbnail = thumb
            thumb_path = VIDEO_PATH + "\\" + the_thumbnail
            return thumb_path

def check_dir_files():
    print("CLIP PATH: ", clip_path)
    movie_clips = [f for f in listdir(clip_path) if isfile(join(clip_path, f))]
    return movie_clips


def write_com_file(self, the_ep='', the_file_name='', the_com=''):
    the_text_file = the_ep + "_cmds.txt"
    with open(the_text_file, 'w') as movie_cmds:
        movie_cmds.write(the_com)
        movie_cmds.write('\n')
        movie_cmds.write('\n')

if __name__ == "__main__":
    pass






