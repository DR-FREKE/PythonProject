class DataStat():

    def __init__(self, myList):
        self.myArray = myList;
    
    def getList(self):
        if type(self.myArray) != list:
            #do something
            return 'error'
        else:
            return self.pSort(self.myArray);
    
    def pSort(self, mList):
        
        for m in range(len(mList)):
            mn_List = m;
            
            for j in range(m+1, len(mList)):
                if mList[mn_List] > mList[j]:
                    mn_List = j;
            
            temp = mList[mn_List];
            mList[mn_List] = mList[m];
            mList[m] = temp;
        return mList

    def Mean(self):
        theList = self.getList();
        total = 0;
        
        for x in range(len(theList)):
            total = total + theList[x];
        after_division = total/len(theList);
        return after_division;

    def Median(self):
        theList = self.getList();
        mid_num = 0;
        divide_num = 0;
        
        if(len(theList) % 2 == 0):
            divide_num = round((len(theList) / 2) - 1);
            first_num = theList[divide_num];
            second_num = theList[divide_num + 1];
            mid_num = (first_num + second_num) / 2;
        else:
            mid_num = theList[round((len(theList) - 1) / 2)];
        return mid_num;

    def Mode(self):
        theList = self.getList();
        maxi = 0;
        mode_num = 0;
        
        for x in range(len(theList)):
            num = theList.count(theList[x])
            if maxi < num:
                maxi = num;
                if(maxi > 1):
                    mode_num = theList[x]
                else:
                    mode_num = 'each number appeared once'
        return mode_num;