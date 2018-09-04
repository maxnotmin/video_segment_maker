import os, sys
import youtube_upload
import json
import subprocess



class MakeCommand(object):


    def __init__(self, title='', tags='', full_file_path='', clip_dir='', data_file_name=''):
        self.data_file_name = data_file_name
        self.title = title
        self.tags = tags
        self.full_file_path = full_file_path
        self.clip_dir = clip_dir
        self.ab_path = os.path.abspath(__file__)
        self.cur_dir = os.getcwd()

    def load_json(self):
        the_json = open('client_secret.json')
        data = json.load(the_json)
        return data

    def write_com_string(self, the_ep='', the_file_name='',  ob_link=''):
        the_title = '--title="{clip_title}"'.format(clip_title=self.title)
        the_tags = '--tags="{clip_tags}"'.format(clip_tags=self.tags)
        the_playlist = '--playlist="OBDM Segments"'
        the_desc = '--description="{epnumb} : {eplink}"'.format(epnumb=the_ep, eplink=ob_link)
        full_command_string = 'youtube-upload {xtitle} {xtags} {xdesc} {xplay}'.format(
            xtitle=the_title, xtags=the_tags, xdesc=the_desc, xplay=the_playlist)
        fin_line = full_command_string + " " + the_file_name
        the_text_file = the_ep + "_coms.txt"
        return fin_line









