class Name:
    per_name = ['']
    
    def __init__(self, name=''):
        
        per_name = [str(nme) for nme in name.split()] #split name into array
        #print(per_name)
        count = 0 #instantiate count for use later
        #**** START get the total value needed for count ********
        for nme in per_name: 
            count += 1
        #**** END get the total value needed for count ********
        self.count = count #set total count
        #print(f'self.count = {self.count}')
        #**** START setting the variables from the 
        # per_name array to the individual variables *****
        
        #print(self.first)
        if count == 1:
            self.first = per_name[0]
            self.middle = ''
            self.last = ''
            self.suffix = ''
        elif count == 2:
            self.first = per_name[0]
            self.middle = ''
            self.last = per_name[1]
            self.suffix = ''
        elif count == 3:
            self.first = per_name[0]
            self.middle = per_name[1]
            self.last = per_name[2]
            self.suffix = ''
        elif count == 4:
            self.first = per_name[0]
            self.middle = per_name[1]
            self.last = per_name[2]
            self.suffix = per_name[3]
        else:
            self.first = ''
            self.middle = ''
            self.last = ''
            self.suffix = ''
        #print(self.last)
        #**** END setting the variables from the 
        # per_name array to the individual variables *****

    def set_first(self, value):
        prior_name = self.first

        if(prior_name != '' and value != ''):
            pass
        elif(prior_name != '' and value == ''):
            self.count -= 1
        elif(prior_name == '' and value != ''):
            self.count += 1
        
        self.first = value

    def get_first(self):
        return self.first

    def set_middle(self, value=''):
        prior_name = self.middle

        if(prior_name != '' and value != ''):
            pass
        elif(prior_name != '' and value == ''):
            self.count -= 1
        elif(prior_name == '' and value != ''):
            self.count += 1
        
        self.middle = value

    def get_middle(self):
        return self.middle

    def set_last(self, value=''):
        prior_name = self.last

        if(prior_name != '' and value != ''):
            pass
        elif(prior_name != '' and value == ''):
            self.count -= 1
        elif(prior_name == '' and value != ''):
            self.count += 1
        
        self.last = value
        

    def get_last(self):
        return self.last

    def set_suffix(self, value=''):
        prior_name = self.suffix

        if(prior_name != '' and value != ''):
            pass
        elif(prior_name != '' and value == ''):
            self.count -= 1
        elif(prior_name == '' and value != ''):
            self.count += 1

        self.suffix = value

    def get_suffix(self):
        return self.suffix

    def get_count(self):
        return self.count

    def get_name(self):
        if self.count == 4:
            nme = self.first + " " + self.middle + " " + self.last + " " + self.suffix
        elif self.count == 3:
            nme = self.first + " " + self.middle + " " + self.last
        elif self.count == 2:
            nme = self.first + " " + self.last
        elif self.count == 1:
            nme = self.first
        else:
            print('No Name Found')
        return nme
    
    def get_initials(self):
        all_init = ''
        initial = ['','','']
        initial[0] = self.first[0]

        if self.count == 3:
            initial[1] = self.middle[0]
            initial[2] = self.last[0]
        else:
            initial[1] = self.last[0]
        
        for word in initial:
            all_init = all_init + "" + word
        return all_init