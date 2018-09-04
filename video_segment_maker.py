import os, sys
import moviepy
from moviepy import editor as THE_EDITOR
from pathlib import Path
import humanfriendly


class MakeMovies():

    ab_path = os.path.abspath(__file__)
    cur_dir = os.getcwd()

    def __init__(self, movie_dir=''):
        self.movie_dir = movie_dir
        self.clip_folder = ''
        self.file_name = ''
        self.full_path = ''
        self.clip_path = ''
        self.ab_path = os.path.abspath(__file__)
        self.cur_dir = os.getcwd()



    def get_movie(self):
        # GET FULL MOVIE
        the_folder = self.cur_dir + "\\" + self.movie_dir
        #print("def get_movie : GET MOVIE FOLDER: ", self.cur_dir,  the_folder)
        for file in os.listdir(the_folder):
            if file.endswith(".mp4"):
                the_movie = file
                #print("def get_movie : GET FILE :", the_movie)
                self.file_name = the_movie
                self.full_path = the_folder + "\\" + the_movie
                #print(": def get_movie : FULL PATH: ", self.full_path)
                return self

    def create_movie_dir(self):
        full_clip_path = self.cur_dir + "\\" + self.movie_dir + "\\" + self.movie_dir + "_clips"
        print("FULL CLIP PATH: ", full_clip_path)
        if not os.path.exists(full_clip_path):
            os.makedirs(full_clip_path)
        self.clip_path = full_clip_path
        return self

    def create_clip(self, begin_clip, end_clip, clip_name):
        try:
            print("Create Clip")
            title_clip = clip_name
            clean_begin = self.convert_string_time(time_str=begin_clip)
            clean_end = self.convert_string_time(time_str=end_clip)
            clip_vid_path = self.cur_dir + "\\" + self.movie_dir + "\\" + self.movie_dir + "_clips" + "\\" + clip_name
            vid_clip = THE_EDITOR.VideoFileClip(self.full_path).subclip(clean_begin, clean_end)
            fin_clip = THE_EDITOR.CompositeVideoClip([vid_clip])
            cur_vid = Path(clip_vid_path)
            if cur_vid.is_file():
                pass
            else:
                fin_clip.write_videofile(clip_vid_path)
                fin_clip.close()
                fin_clip.audio.reader.close_proc()
        except Exception as clip_create_error:
            print("Clip Create Error: ", clip_create_error, clip_name)


    def convert_string_time(self, time_str):
        count_colon = time_str.count(":")
        #if count_colon
        #h, m, s = time_str.split(':')
        try:
            if len(time_str) < 1:
                return None
            elif count_colon is 0 and len(time_str) > 1:
                s = time_str
                return int(s)
            elif count_colon is 1:
                m, s = time_str.split(':')
                return int(m) * 60 + int(s)
            else:
                h, m, s = time_str.split(':')
                return int(h) * 3600 + int(m) * 60 + int(s)
        except Exception as conerror:
            print("CONVERT TIME EXCEPTION: ", conerror)







