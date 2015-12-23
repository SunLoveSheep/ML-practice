"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    strList = s.split(' ');#to split the string into a list of words
    rList = [];#to store the each word only once
    nList = [];#to store how many times each word has occured
    for i in range(len(strList)):
        if ((strList[i] in rList)==False):
            rList.append(strList[i]);
            nList.append(int(1));
        else:
            for j in range(len(rList)):
                if (strList[i]==rList[j]):
                    nList[j]=nList[j]+1;
    
    tList = list();#a new empty tuple list
    for i in range(len(rList)):
        tList.append((rList[i],nList[i]));#construct the tuple list from rList and nList
    
    tList.sort(key=lambda tList: (-tList[1], tList[0]));#sort the tuple list: first by its 2nd element in reverse order "-", then sort by its 1st element in non-reverse order, no "-"
    
    # for testing
    #for i in tList:
    #    print i;
    
     
    # TODO: Count the number of occurences of each word in s
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    
    return tList[:n] #return the first n pairs of elements as required


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
