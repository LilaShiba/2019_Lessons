import pprint

class Board:
    def __init__(self):
        self.board = [[0 for x in range(8)]for y in range(6)] 

    def make_move(self, col, piece, row = 0):
        move = self.board[row][col]
        if move != 0:
            print("Make a move in a free spot")
            return ("Make a move in a free spot")
        elif row == 5 or self.board[row+1][col] != 0:
            self.board[row][col] = piece
            return self.board, (row,col)
        elif move == 0:
            return self.make_move(col, piece, row+1)
    
    def show_board(self):
        pprint.pprint(self.board)
        
    def check_board(self,last_move,piece,direction):
        queue = [last_move]
        visited = []
        count = 0
        
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                count += 1
                if count >= 4:
                    return True, visited
                    
                # set direction to check
                row,col = node
                
                if direction == 'col':
                    direction = [ (row-1, col), (row+1, col) ]
                    
                elif direction == 'row':
                    direction = [ (row, col-1), (row, col+1) ]
                
                for cx,cy in direction:
                    if 0 <= cx < 6 and 0 <= cy < 8:
                        if self.board[cx][cy] == piece:
                            print(cx,cy)    
                            queue.append((cx,cy))
                        
                
        return False, None

    def bfs(self, last_move, piece, direction):
        queue = [last_move]
        visited = []
        ans = []
        count = 0
        
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                x,y = node
                
                if direction == 'col':
                    directions = (x-1,y), (x+1,y)
                elif direction == 'row':
                    directions = (x, y+1), (x, y-1)
                elif direction == 'l_dia':
                    directions = (x-1, y+1), (x+1, y-1)
                elif direction == 'r_dia':
                    directions = (x+1, y+1), (x-1, y-1)
                    
                    
                for cx, cy in directions:
                    if 0 <= cx < 6 and 0 <= cy < 8:
                        if self.board[cx][cy] == piece:
                            queue.append((cx,cy))
                            
                            if (cx,cy) not in ans:
                                ans.append((cx,cy))
                                count += 1
                                if count >= 4:
                                    return True, ans
        return False, None
                                    
                                    
    def check_row(self,last_move,piece):
        # check row
        x,y = last_move
        best = ans = 0
        for col in self.board[x]:
            if col == piece:
                ans += 1
            else:
                best = max(ans, best)
                ans = 0
        return best >= 4, piece
    
    def check_col(self,last_move,piece):
        # check col
        _,col = last_move
        best, current = 0,0
        n = len(self.board[0])-2
        
        for row in range(n):
            val = self.board[row][col]
            if val == piece:
                current += 1
                best = max(current, best)
            else:
                current = 0
        return best >= 4, piece
         
        
        
        
    
        






board = Board()
piece = 1
past_move = (0,0)
won = False


while won == False:
  
  print('it is player ', piece, 'turn to go')
  user_move = int(input("what col?"))
  _, past_move = board.make_move(user_move, piece)
  #won, path = board.check_row(past_move, piece)
  #won, path = board.check_col(past_move, piece)
  won, path = board.bfs(past_move, piece, 'l_dia')
  if piece == 1:
    piece = 2
  elif piece == 2:
    piece = 1

  board.show_board()


print(path)
