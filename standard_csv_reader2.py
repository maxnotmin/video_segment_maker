import os, sys
import csv
import re
import glob

class TheCSVReader(object):

    ab_path = os.path.abspath(__file__)
    cur_dir = os.getcwd()

    def __init__(self, path='', movie_dir=''):
        self.path = path
        self.file_name = ''
        self.full_path = ''
        self.cvs_dict = []
        self.raw_data = []
        self.time_start = 0
        self.time_end = 0
        self.clean_data = []
        self.source_link = ''
        self.movie_dir = movie_dir
        self.ab_path = os.path.abspath(__file__)
        self.cur_dir = os.getcwd()
        self.full_clip_path = ''

    def get_csv_file(self):

        the_folder = self.cur_dir + "\\" + self.path

        #print("THE FOLDER: ", self.cur_dir,  the_folder)
        for file in os.listdir(the_folder):
            if file.endswith(".csv"):
                the_file = file
                #print("GET FILE :", the_file)
                self.file_name = the_file
                self.full_path = the_folder + "\\" + the_file
                #print("FULL PATH: ", self.full_path)

                return self

    def store_raw_data(self):
        full_path = self.path + "/" + self.file_name

        with open(full_path, 'r') as csvfile:

            the_read = csv.reader(csvfile)
            for i in the_read:
                self.raw_data.append(i)

            return self

    def create_movie_dir(self):
        full_clip_path = self.cur_dir + "\\" + self.movie_dir + "\\" + self.movie_dir + "_clips"
        print("FULL CLIP PATH: ", full_clip_path)
        if not os.path.exists(full_clip_path):
            os.makedirs(full_clip_path)
        return self

    def create_full_clip_path(self, file_name):
        strip_name = self.replace_space(sent=file_name)
        full_clip_path = self.cur_dir + "\\" + self.movie_dir + "\\" + self.movie_dir + "_clips"
        supreme_path = full_clip_path + "\\" + strip_name + ".mp4"
        return supreme_path

    def get_time_start_index(self):
        for master_index, row in enumerate(self.raw_data):
            #SAVE PREVIOUS ITEM
            previous_item = self.raw_data[master_index -1]

            shaved_time = [i for i in row]
            for key, value in enumerate(shaved_time):

                time_marker = 0
                #print(value)
                if value.lower() == 'time':
                    #print("IN IF")
                    #print("Master Index: ", master_index)
                    #print("Row: ", row)
                    #print("key: ", key)
                    #print("value: ", value)
                    self.time_start = master_index
                    return self
                break


    def get_time_end_index(self):
        for master_index, row in enumerate(self.raw_data):
            #print("IN END: ", self.time_start)
            shaved_time = [i for i in row]
            for key, value in enumerate(shaved_time):
                #print("BLANK VALUE: ", value)
                if value == '' and master_index > self.time_start:
                    self.time_end = master_index
                    return self
                break

    def get_sourcelink(self):
        for master_index, row in enumerate(self.raw_data):
            # SAVE PREVIOUS ITEM
            #print("PRINT SOURCE LINK", row)

            if row[0].lower() == 'youtube:':
                #print('SOURCE: ', row[1])
                self.source_link = row[1]
                return self


    def parse_data(self):
        print("PARSE")
        parse_holder = []
        start_loop = self.time_start + 1
        end_loop = self.time_end
        main_data = self.raw_data
        standard_info = ['obdmpod.com', 'twitter.com/obdmpod', '']



        for key, value in enumerate(main_data[start_loop: end_loop]):
            time_dict = {'segment_name': '',
                         'segment_info': '',
                         'time_begin': '',
                         'time_end': '',
                         'source_link': '',
                         'tags': '',
                         'standard_info': '',
                         'file_name': '',
                         'full_path': ''}
            #print("Parse : ", key, value)
            segment_name = self.string_cleaner(the_string=value[1])

            time_dict['segment_name'] = segment_name
            time_dict['time_begin'] = self.string_cleaner(the_string=value[0])
            time_dict['source_link'] = self.source_link
            tmp_place = start_loop + key + 1
            tmp_end_hold = main_data[tmp_place][0]
            #print("TMP END: ",self.string_cleaner(tmp_end_hold))
            time_dict['time_end'] = self.string_cleaner(the_string=tmp_end_hold)
            get_all_tags = self.tag_maker(sentence=segment_name)
            #print("GET ALL TAGS: ", get_all_tags)
            cleaned_tags = self.tag_cleaner(the_dirty_tags=get_all_tags)
            string_tags = ','.join(map(str, cleaned_tags))
            time_dict['tags'] = string_tags
            time_dict['file_name'] = self.replace_space(sent=segment_name) + ".mp4"

            fin_clip_path = self.create_full_clip_path(file_name=segment_name)
            time_dict['full_path'] = fin_clip_path


            #time_dict['time_end'] = self.string_cleaner(the_string=tmp_end_hold)

            parse_holder.append(time_dict)
            #print("CLEAN IN PARSE: ", time_dict)


        print("PARSE HOLDER: ", parse_holder)
        self.clean_data = parse_holder
        return self

    def tag_maker(self, sentence=''):
        base_tags = ['obdm', 'paranormal', 'conspiracy', 'comedy']
        if len(sentence) > 1:
            seg_tags = sentence.split()
            #print("SEG : ", seg_tags)
            all_tags = base_tags + seg_tags
            #print("ALL TAGS: ", all_tags)
            return all_tags

    def tag_cleaner(self, the_dirty_tags=list):
        bad_tags = ['!', '-', 'and', '|', 'with', 'the', 'due', 'to', 'too', 'for', 'up', 'a', 'or', 'as', 'if', 'in']
        clean_tags = []
        for tag in the_dirty_tags:
            for i in bad_tags:
                if i in the_dirty_tags:
                    the_dirty_tags.remove(i)
        #print("CLEAN TAGS: ", the_dirty_tags)
        return set([i.lower() for i in the_dirty_tags])

    def store_data(self, the_data):
        self.cvs_dict = the_data
        return self

    def time_determine(self, the_time):
        for letter in the_time:
            if int(letter):
                return the_time
            else:
                return ''

    def string_cleaner(self, the_string):
        if len(the_string) > 1:
            clean_string = the_string.lstrip().rstrip()
            return clean_string
        else:
            return ''

    def has_int(self, the_string):
        pass

    def replace_space(self, sent=''):
        the_sentence = sent.replace(" ", "_")
        return the_sentence








