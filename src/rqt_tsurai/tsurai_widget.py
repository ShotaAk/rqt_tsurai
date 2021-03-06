# coding: UTF-8

import os

from ament_index_python.resources import get_resource

from python_qt_binding import loadUi
from python_qt_binding.QtWidgets import QWidget
from python_qt_binding.QtGui import QPainter, QFont
from python_qt_binding.QtCore import Qt

# クラス名は参照されるので書き間違えないように
# Tusrai とか書くとつらいです
class TsuraiWidget(QWidget):

    def __init__(self):
        super(TsuraiWidget, self).__init__()

        # パッケージ名も書き間違えないように
        pkg_name = 'rqt_tsurai'
        _, package_path = get_resource('packages', pkg_name)
        # UIをロードするけどファイル名を間違えないように
        ui_file = os.path.join(
            package_path, 'share', pkg_name, 'resource', 'tsurai_widget.ui')
        loadUi(ui_file, self)

        # オブジェクト名は間違えても動く？未調査
        self.setObjectName('TsuraiWidget')


    # この関数が一定周期で呼び出される
    def paintEvent(self, event):
        painter = QPainter(self)

        # Hello world
        # ブラシ（塗りつぶし）の色を黒に
        painter.setBrush(Qt.black)
        # ペン（線描画）の色も黒に
        painter.setPen(Qt.black)
        # 背景を描く
        # self.rect()はwidgetのサイズを返すので、widget全体を埋める四角形を描画する
        # ペンとブラシの色が黒なので背景色は真っ黒
        painter.drawRect(self.rect())

        # ペン（線描画）の色を白にする
        painter.setPen(Qt.white)

        # フォントサイズを変更する
        font = painter.font()
        # つらさはできるだけ大きく表現したほうが良い
        # 周りが気づくように
        font.setPointSize(80)
        painter.setFont(font)
        
        # テキストを描画する
        x = 0 # 左端
        y = self.rect().height()*0.5 # 上下の中心
        painter.drawText(x,y, "TSU☆RA☆I")
