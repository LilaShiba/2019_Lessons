UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def spiral(matrix):
    spaces_left = len(matrix) * len(matrix[0])
    current_direction = RIGHT
    current_position = (0,0)
    ans = []

    while spaces_left > 0:
        r,c = current_position
        spaces_left -= 1
        #print(matrix[r][c])
        print(r,c)
        ans.append(matrix[r][c])
        matrix[r][c] = None

        # generate next possiable position
        possiable_position = next_position(current_position, current_direction)
        if should_change(possiable_position[0], possiable_position[1], matrix):

            next_move = next_direction(current_direction)
            #print(next_move)
            possiable_position = next_position(current_position, next_move)
            current_direction = next_move

        current_position = possiable_position


        # check if should change direction
            # if should
    return ans


def next_direction(current_direction):
    if current_direction == RIGHT:
        return DOWN
    elif current_direction == DOWN:
        return LEFT
    elif current_direction == LEFT:
        return UP
    elif current_direction == UP:
        return RIGHT

def next_position(position, direction):
    if direction == RIGHT:
        return(position[0], position[1]+1)
    elif direction == LEFT:
        return(position[0], position[1]-1)
    elif direction == UP:
        return(position[0]-1, position[1])
    elif direction == DOWN:
        return(position[0]+1, position[1])

def should_change(r,c,matrix):
    if ( 0 <= r < len(matrix) ) and  ( 0<= c < len(matrix[0]) ):
        if matrix[r][c] != None:
            return False
    return True


if __name__ == '__main__':
    matrix = [[x + 1 for x in range(10)]for y in range(10)]
    print(spiral(matrix))
