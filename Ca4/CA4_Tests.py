import unittest
#from process_changes_with_object import get_commits, read_file
from CA4 import get_commits, read_file 
 
class TestCommits(unittest.TestCase):
    # test read input file 
  
    def setUp(self): 
        self.data = read_file('changes_python.log')
   
    # test number of lines read 
    
    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data)) 
  
    # test commits processed 
    def test_number_of_commits(self): 
        commits = get_commits(self.data) 
        #test number of commits found
        self.assertEqual(422, len(commits))
        #test commits - revision number
        self.assertEqual('r1551332', commits[10].revision)
        self.assertEqual('r1538454', commits[101].revision)
        #test commits - author
        self.assertEqual('Thomas', commits[12].author)
        self.assertEqual('Vincent', commits[119].author)
        #test commits - no of lines
        self.assertEqual(1, commits[12].number_of_lines)
        self.assertEqual(2, commits[91].number_of_lines)
        #test commits - date
        self.assertEqual('12:33:51', commits[42].time)
        self.assertEqual('15:00:06', commits[91].time)
        #test commits - time
        self.assertEqual('2015-11-26', commits[10].date)
        self.assertEqual('2015-10-22', commits[141].date)
        #test commits- path
        self.assertEqual(['M /cloud/personal/client-international/android/branches/android-15.2-solutions/libs/model/src/com/biscay/client/android/model/util/sync/dv/SyncAdapter.java'],
                commits[20].changed_path)
        self.assertEqual( ['M /cloud/personal/client-international/android/branches/android-15.2-solutions/settings.gradle'],
                commits[120].changed_path)
        #test commits - comments
        self.assertEqual(['FTRPC-500: Frontier Android || Inconsistencey in My Activity screen',
                'Client used systemAttribute name="Creation-Date" instead of versionCreated as version created.'],
                commits[24].comment)
        self.assertEqual(['FTRPC-160: Frontier Android || Favorite icon is not shown for some of the PDF files'],
                commits[102].comment)
  
#main 
if __name__ == '__main__':
    unittest.main()
