from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# from PyQt5.QtCore import *


import sys
import random

"""
    0 表示无子。
    1 表示黑子。
    2 表示白子。

"""

class Main(QWidget):

    def __init__(self):
        super(Main, self).__init__()
        self.resize(465, 465)

        # 生成15 x 15的棋盘。
        self.chess = [[0 for j in range(15)] for i in range(15)]

        self.table = QTableWidget(self)

        # 基本样式。
        with open('five.qss', 'r') as f:
            self.table.setStyleSheet(f.read())

        self.set_table()


    def set_chess(self, row, column):
        # 根据row, column来进行下棋。

        set_where = []
        # 判断是否存在棋子。
        def judge(row, column, left=0, right=0, up=0, down=0, left_up=0, left_down=0, right_up=0, right_down=0,
                  count=0, is_stop=0):
            if is_stop >=4:
                return [[14, 14, 7], [14, 14, 7]]
            if 0 > row or row > 14 or 0 > column or column > 14:
                return [[14, 14, 7], [14, 14, 7]]

            # 如果计数为3.
            if count == 2:
                # 在其进展的方向下一个棋。
                if up:
                    return [[row, column, 0], [row+2*count, column, 0]]
                if down:
                    return [[row, column, 0], [row-2*count, column, 0]]
                if left:
                    return [[row, column, 0], [row, column+2*count, 0]]
                if right:
                    return [[row, column, 0], [row, column-2*count, 0]]
                if left_up:
                    return [[row, column, 0], [row+2*count, column+2*count, 0]]
                if left_down:
                    return [[row, column, 0], [row-2*count, column+2*count, 0]]
                if right_up:
                    return [[row, column, 0], [row+2*count, column-2*count, 0]]
                if right_down:
                    return [[row, column, 0], [row-2*count, column-2*count, 0]]

            # 此点为空。
            if not self.chess[row][column]:
                return [[row, column, 1], [row, column, 1]]
            # 如果为自己的子(白)，则返回。
            elif self.chess[row][column] == 2:
                return [[0, 0, 3], [0, 0, 3]]
            # 如果是黑子。
            else:
                # 继续判断。
                if up:
                    # 如果上有一个标记，那么给上方向增加一个计数并继续行走。
                    return judge(row-1, column, up=1, count=count+1, is_stop=is_stop+1)
                if down:
                    return judge(row+1, column, down=1, count=count+1, is_stop=is_stop+1)
                if left:
                    return judge(row, column-1, left=1, count=count+1, is_stop=is_stop+1)
                if right:
                    return judge(row, column+1, right=1, count=count-1, is_stop=is_stop+1)
                if left_up:
                    return judge(row-1, column-1, left_up=1, count=count+1, is_stop=is_stop+1)
                if left_down:
                    return judge(row+1, column-1, left_down=1, count=count+1, is_stop=is_stop+1)
                if right_up:
                    return judge(row-1, column+1, right_up=1, count=count+1, is_stop=is_stop+1)
                if right_down:
                    return judge(row+1, column+1, right_down=1, count=count+1, is_stop=is_stop+1)




        # 判断上。
        is_up = judge(row-1, column, up=1)
        # 判断下。
        is_down = judge(row+1, column, down=1)
        # 判断左。
        is_left = judge(row, column-1, left=1)
        # 判断右。
        is_right = judge(row, column+1, right=1)
        # 判断左上。
        is_left_up = judge(row-1, column-1, left_up=1)
        # 判断左下。
        is_left_down = judge(row+1, column-1, left_down=1)
        # 判断右上。
        is_right_up = judge(row-1, column+1, right_up=1)
        # 判断右下。
        is_right_down = judge(row+1, column+1, right_down=1)


        to_where = sorted([is_up, is_down, is_left, is_right, is_left_up, is_left_down, is_right_up, is_right_down],
                          key=lambda x: x[0][2])

        for i in to_where:
            if not i[0][2]:
                if not self.chess[i[0][0]][i[0][1]]:
                    # 没有棋就可以下棋了。
                    self.table.setItem(i[0][0], i[0][1], QTableWidgetItem(QIcon('pic/white.png'), '2'))
                    self.chess[i[0][0]][i[0][1]] = 2
                    break
                else:
                    self.table.setItem(i[1][0], i[1][1], QTableWidgetItem(QIcon('pic/white.png'), '2'))
                    self.chess[i[1][0]][i[1][1]] = 2
                    break
            else:
                number = random.randint(0, 4)
                # 增加随机性。
                if number >= 2:
                    continue

                if not self.chess[i[0][0]][i[0][1]]:
                    # 没有棋就可以下棋了。
                    self.table.setItem(i[0][0], i[0][1], QTableWidgetItem(QIcon('pic/white.png'), '2'))
                    self.chess[i[0][0]][i[0][1]] = 2
                    break
                else:
                    self.table.setItem(i[1][0], i[1][1], QTableWidgetItem(QIcon('pic/white.png'), '2'))
                    self.chess[i[1][0]][i[1][1]] = 2
                    break



    def set_table(self):
        """
            设置棋盘。
            用Table承载。
        """
        self.table.resize(465, 465)
        self.table.setColumnCount(15)
        self.table.setRowCount(15)

        # 设置每个行列的宽，高。
        for i in range(15):
            self.table.setColumnWidth(i,30)
            self.table.setRowHeight(i,30)

        # 设置表格行号不显示。
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)

        # 设置内容不可编辑。
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 设置选择行为。
        #  一次只能选则一个项。
        self.table.setSelectionBehavior(QAbstractItemView.SelectItems)

        # 设置选择模式。
        #  一次只能选则单个。
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)


        # 设置点击的后果。

        self.table.cellClicked.connect(self.item_click)


    def item_click(self):
        # 点击下子。
        column = self.table.currentColumn()
        row = self.table.currentRow()
        # 若有子则
        if self.table.item(row, column):
            return 0
        self.table.setItem(row, column, QTableWidgetItem(QIcon('pic/black.png'), '1'))
        self.chess[row][column] = 1

        self.set_chess(row, column)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Main()
    window.show()

    sys.exit(app.exec_())