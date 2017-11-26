# -*- coding: utf-8 -*-
"""
Student No:  10362185
""" 

#Imports

# pandas
import pandas as pd

# numpy, matplotlib 
import numpy as np
import matplotlib.pyplot as plt

#create commit class
#information on - revision number, author, date, time, number of lines, changed path and comments
#
class Commit(object):

    def __init__(self, revision, author, date, time, number_of_lines, changed_path=[], comment=[]):
        self.revision = revision
        self.author = author
        self.date = date
        self.time = time
        self.number_of_lines = number_of_lines
        self.changed_path = changed_path
        self.comment = comment

    def __repr__(self):
        return self.revision + ',' + self.author + \
                ',' + self.date + ',' + self.time + ',' + str(self.number_of_lines) + \
				',' + ' '.join(self.comment) + '\n'

#process file to extract revision,author,date,time,number_of_lines,comment information
#remove extra commas from csv file comments - as extra commas in comments are seen as extra fields
#append details to commits list and return
 
def get_commits(data):
    sep = 72*'-'
    commits = []
    index = 0
    while index < len(data):
        try:
            # parse each of the commits and put them into a list of commits
            details = data[index + 1].split('|')
            
            # the author with spaces at end removed.
            commit = Commit(details[0].strip(),
                details[1].strip(),
                details[2].strip().split(' ')[0],
                details[2].strip().split(' ')[1],
                int(details[3].strip().split(' ')[0]))
            change_file_end_index = data.index('', index + 1)
            commit.changed_path = data[index + 3 : change_file_end_index]
            commit.comment = data[change_file_end_index + 1 : 
                    change_file_end_index + 1 + commit.number_of_lines]
            # remove extra commas from csv file comments 
            commit.comment = [line.replace(',',' ') for line in commit.comment]
            commits.append(commit)
            index = data.index(sep, index + 1)
        # error handling    
        except IndexError:
            index = len(data)
    return commits
 
# read input file and return striped data
def read_file(any_file):
    # use strip to strip out spaces and trim the line.
    return [line.strip() for line in open(any_file, 'r')]

# write output file with commit information
def save_commits(commits, any_file):
    my_file = open(any_file, 'w')
    my_file.write("revision,author,date,time,number_of_lines,comment\n")
    for commit in commits:
        my_file.write(str(commit))
    my_file.close()

#create a dataframe to ascertain statistics re: authors entries - mean, std
#min, max, spread of data
#plot author counts on bar chart
def plot_authors(any_file): 
    #use a DataFrame
    changes_df = pd.read_csv(any_file)   
    #count_authors changes
    count_authors = changes_df.author.value_counts()
    print count_authors
    # get statistics on authors
    print count_authors.describe() 
    #create bar plot of author entries
    count_authors.plot.bar(title='Author Entries')
    plt.show()

#create a plot re: entry timings - what time of day entries are submitted.
#first create a frequency bin count(use 2 hourly slots -from 5:00a.m.to 21:00p.m.)
#use a dictionary to match counts with slot times
#use matplotlib to create a plot to show busiest time slots
def plot_work_time(any_file):   
     # read in plot file
     work_time_df = pd.read_csv(any_file)
     # initialise bin counters
     bin1 =0
     bin2 =0
     bin3 =0
     bin4 =0
     bin5 =0
     bin6 =0  
     bin7 =0
     bin8 =0

     # create frequency bins for 2 hour slots 
     for ind in work_time_df.index:
         if work_time_df['time'][ind]  > '05:00:01' and work_time_df['time'][ind] < '07:00:00' :
             bin1 =  bin1 + 1
         elif work_time_df['time'][ind]  > '07:00:01' and work_time_df['time'][ind] < '09:00:00' :
             bin2 =  bin2 + 1
         elif work_time_df['time'][ind]  > '09:00:01' and work_time_df['time'][ind] < '11:00:00' :
             bin3 =  bin3 + 1
         elif work_time_df['time'][ind]  > '11:00:01' and work_time_df['time'][ind] < '13:00:00' :
             bin4 =  bin4 + 1
         elif work_time_df['time'][ind]  > '13:00:01' and work_time_df['time'][ind] < '15:00:00' :
             bin5 =  bin5 + 1
         elif work_time_df['time'][ind]  > '15:00:01' and work_time_df['time'][ind] < '17:00:00' :
             bin6 =  bin6 + 1
         elif work_time_df['time'][ind]  > '17:00:01' and work_time_df['time'][ind] < '19:00:00' :
             bin7 =  bin7 + 1 
         elif work_time_df['time'][ind]  > '19:00:01' and work_time_df['time'][ind] < '21:00:00' :
             bin8 =  bin8 + 1
     #assign frequency to slot times
     range_bin_dict = {'05:00:01 to 07:00:00':bin1,'07:00:01 to 09:00:00':bin2,'09:00:01 to 11:00:00':bin3,'11:00:01 to 13:00:00' :bin4,'13:00:01 to 15:00:00':bin5,'15:00:01 to 17:00:00':bin6,'17:00:01 to 19:00:00':bin7,'19:00:01 to 21:00:00':bin8}
     # number of bins
     bin_range = np.arange(len(range_bin_dict))
      
     # create frequency plot of comments submitted by time
     plt.bar(bin_range, range_bin_dict.values(), align='center', width=0.5,label='Entry Times')
     plt.xticks(bin_range, range_bin_dict.keys(),rotation='vertical')
     ymax = max(range_bin_dict.values()) + 1
     plt.ylim(0, ymax)
     plt.show() 
     print range_bin_dict

# Main    
if __name__ == '__main__': 
    # assign input file 
    changes_file = 'changes_python.log'
    #assign plot file
    plot_file = 'changes.csv'
    # read input file  
    data = read_file(changes_file)
    # process data
    commits = get_commits(data)
    #write processed data to output file
    save_commits(commits, plot_file) 
    #plot authors stats
    plot_authors(plot_file)
    #plot work committed stats
    plot_work_time(plot_file)

  
  

     
     
    


