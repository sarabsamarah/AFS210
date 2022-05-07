class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist
        self.next = None
        self.prev = None

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
class Playlist:
     def __init__(self):
         self.head = None
         self.tail = None
         self.count = 0

#iterate through the playlist
     def iter(self):
        temp = self.head
        while temp:
            val = temp.title, temp.artist
            temp = temp.next
            yield val

     def __str__(self):
       myStr = ""
       for node in self.iter():
             myStr += str(node)+ " "
       return myStr

     def __getitem__(self, index):
        if index > self.count -1:
            return "out of range"
        temp = self.tail
        for n in range(index):
            temp = temp.next
            return temp.title

     def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        temp = self.head
        for n in range(index):
           temp = temp.next
        temp.title = value    

#adds a song to playlist
     def addSong(self, title, artist):
         if self.head is None:
             self.head = Song(title, artist)
         else:
            new_node = Song(title, artist)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

#adds a song to playlist
     def add(self, title, artist):
         newNode = Song(title, artist)
         newNode.next = self.head
         self.head = newNode


#delete song by value
     def deleteSong(self, title, artist):
        temp = self.head
        prev = self.head
        while temp:
            if temp.title == title and temp.artist == artist:
                if temp == self.head:
                   temp.next.prev = None
                   self.head = temp.next
                else:
                    prev.next = temp.next
                    temp.next = prev
                self.count -= 1
                return
            prev = temp
            temp = temp.next

     def pop(self):
         if self.head is None:
             return None
         elif self.head.next is None:
             temp = self.head.title, self.head.artist
             self.head = None
             return temp
         else:
             temp = self.head.title, self.head.artist
             self.head = self.head.next
             self.head.prev = None
             return temp

#size of playlist        
     def size(self):
         temp = self.head
         count = 0

         while temp is not None:
            count = count + 1
            temp = temp.next
         return count 

#play first song 
     def playFirstSong(self):
         return self.head.title, self.head.artist

#print whole playlist
     def printAll(self):
         print("Playlist: ")
         temp = self.head
         while temp is not None: 
             print(temp.title, temp.artist)
             temp = temp.next
#not working
     def getCurrentSong(self):
        temp = self.head
        while temp is not None:
            print(temp.title, temp.artist)
            temp = temp.next 

#get previous song
     def getprevSong(self):
        temp = self.head
        while temp is not None:
            print(temp.title, temp.artist)
            temp = temp.prev 


#skips one song
     def skipSong(self):
         prev = None
         temp = self.head
         while temp is not None:
             next = temp.next
             temp.next = prev 
             temp = next
             return temp 
             
#reverses the playlist
     def shuff(self):
         prev = None
         temp = self.head
         while (temp is not None):
             next = temp.next
             temp.next = prev
             prev = temp
             temp = next
             self.head = prev
            

def shuffle(playlist):
        sizeofList = len(playlist)
        if sizeofList == 1:
         return playlist
        if sizeofList > 1:
          mid = sizeofList // 2

        lefthalf = playlist[:mid]
        righthalf = playlist[mid:]

        shuffle(lefthalf)
        shuffle(righthalf)

        return merge(playlist, lefthalf, righthalf)

         
def merge(nlist,lefthalf,righthalf):
      i=j=k=0       
      while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            nlist[k]=lefthalf[i]
            i=i+1
        else:
            nlist[k]=righthalf[j]
            j=j+1
        k=k+1

      while i < len(lefthalf):
        nlist[k]=lefthalf[i]
        i=i+1
        k=k+1

      while j < len(righthalf):
        nlist[k]=righthalf[j]
        j=j+1
        k=k+1
      return nlist


list = Playlist()

def menu():
  print(20 * "-" , "MENU" , 20 * "-")
  print("1. Add Song to Playlist")
  print("2. Remove song from Playlist")
  print("3. Play")
  print("4. Skip")
  print("5. Go Back")
  print("6. Shuffle")
  print("7. Show Currently Playing Song")
  print("8. Show Current Playlist Order")
  print("0. Exit")
  print(47 * "-")

list.addSong("Money", "Cardi B")
list.addSong("Animal", "Pearl Jam")
list.addSong("Layla", "Eric Clapton")
list.addSong("Moondance", "Van Morrison")
list.addSong("Hey Jude", "The Beatles")
list.addSong("Supersonic", "Oasis")

while True:
    menu()
    choice = int(input())

    if choice == 1:
        title = input("Enter an song title: ")
        artist = input("Enter the artist: ")

        list.addSong(title, artist)
        print("New Song Added to Playlist")

    elif choice == 2:
        title = input("Enter an song title to delete: ")
        artist = input("Enter the artist of song you want to delete: ")
        list.deleteSong(title, artist)
        # Prompt user for Song Title 
        # remove song from playlist
        print("Song Removed to Playlist")

    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        print("Playing....")   
        print(list.playFirstSong())

    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        print("Skipping....")  
        print(list.skipSong())

    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        print("Replaying....")  
        print(list.getprevSong())

    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        print("Shuffling....")  
        print(list.shuff())   

    elif choice == 7:
        print("Currently playing: ", end=" ")  
        list.getCurrentSong()
        # Display the song name and artist of the currently playing song

    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
        list.printAll()

    elif choice == 0:
        print("Goodbye.Rock On!")
        break



