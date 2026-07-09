# import random
# Pieces=["bP","bR","bN","bB","bQ","bK","wP","wR","wN","wB","wQ","wK"]

# Piece_values={'P':100,'N':300,'B':320,'R':500,'Q':900,'K':20000}


# class Gamestate:

#     def __init__(self):
#         self.board=[
#             ["bR","bN","bB","bQ","bK","bB","bN","bR"],
#             ["bP","bP","bP","bP","bP","bP","bP","bP"],
#             ["--","--","--","--","--","--","--","--"],
#             ["--","--","--","--","--","--","--","--"],
#             ["--","--","--","--","--","--","--","--"],
#             ["--","--","--","--","--","--","--","--"],
#             ["wP","wP","wP","wP","wP","wP","wP","wP"],
#             ["wR","wN","wB","wQ","wK","wB","wN","wR"]
#         ]

#         self.white_to_move=True
#         self.move_log=[]

#     def print_board(self):
#         print("\n  a     b    c    d    e    f    g    h  ")
#         for r in range(8):
#             print(f"{8-r}", end="")
#             for c in range(8):
#                 piece=self.board[r][c]
#                 print(f"[{piece if piece != '--' else ' '}]", end=" ")
#             print(f"{8-r}")
#         print("  a     b    c    d    e    f    g    h  \n")


# state= Gamestate()
# state.print_board()



# class move:
#     ranks_to_rows={"1":7,"2":6,"3":5,"4":4,"5":3,"6":2,"7":1,"8":0}
#     rows_to_rank={v: k for k, v in ranks_to_rows.items()}

#     files_to_columns={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
#     cols_to_files={v: k for k, v in files_to_columns.items()}

#     def __init__(self,start_sq,end_sq,board):
#         self.start_row,self.start_col=self.start_sq
#         self.end_row,self.end_col=end_sq
#         self.piece_moved=board[self.start_row][self.start_col]
#         self.pieces_captured=board[self.end_row][self.end_col]
#         self.move_id=self.start_row*1000+self.start_col+self.end_row*10+self.end_col


#     def __eq__(self,other):
#         if instance(other,move):
#             return self.move_id == other.move_id
#         return False
    
#     def get_algebraic_notation(self):
#         return self.get_rank_files(self.start_row,self.start_col)+(self.get_row,self.end_col)
    
#     def get_rank_files(self,row,col):
#         return self.cols_to_find(col)+self.rows_to_rank(row)
    

# class zobrist:
#     def __init__(self):
#         self.table=[[{random}]]
        

import random

Pieces=["bP","bR","bN","bB","bQ","bK","wP","wR","wN","wB","wQ","wK"]

Piece_values={'P':100,'N':300,'B':320,'R':500,'Q':900,'K':20000}

class Gamestate:
    def __init__(self):
        self.board=[
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","bP","bP","bP","bP"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]

        self.white_to_move=True
        self.move_log=[]

        self.zobrist_hash=zobrist.get_initial_hash(self.board,self.white_to_move)

    def print_board(board):
        print("\n a b c d e f g h")
        for r in range(8):
            print(f"{8-r}",end="")
            for c in range(8):
                piece=board[r][c]
                print(f"[{piece if piece != '--' else ' '}]")
            print(f"{8-r}")
        print(" a b c d e f g h \n")
    

    


class Move:
    ranks_to_rows={"1":7,"2":6,"3":5,"4":4,"5":3,"6":2,"7":1,"8":0}
    rows_to_rank={v:k for k, v in ranks_to_rows.items()}

    files_to_cols={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
    cols_to_files={v:k for k,v in files_to_cols.items()}

    def __init__(self,start_sq,end_sq,board):
        self.start_row,self.start_col=start_sq
        self.end_row,self.end_col=end_sq
        self.piece_moved=board[self.start_row][self.start_col]
        self.pieces_captured=board[self.end_row][self.end_col]
        self.move_id=self.start_row*1000+self.start_col*100+self.end_row*10+self.end_col
        

    def __eq__(self,other):
        if instance(other,move):
            return self.move_id == other.move_id
        return False

    def get_algebraic_notation(self):
        return self.get_rank_files(self.start_row,self.start_col)+(self.get_row,self.end_col)

    def get_rank_file(self,row,col):
        return self.cols_to_find[col]+self.rows_to_rank[row]

    
class zobrist:
    def __init__(self):
        self.table=[[[random.getrandbits(64)] for _ in range(12)] for _ in range(8)]
        self.white_to_move_key=random.getrandbits(64)

    def get_initial_hash(self,board,white_to_move):
        h=0
        for r in range(8):
            for c in range[8]:
                piece=board[r][c]
                if piece!='--':
                    piece_idx=piece_to_idx[piece]
                    h^=self.table[r][c][piece_idx]
        if white_to_move:       
            h^=self.white_to_move_key
        return h

class Gamestate:
    def get_all_pseudo_legal_moves(self):
    elif piece=='0':
    