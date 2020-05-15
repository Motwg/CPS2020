from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout


def layouting(main_layout, matrix):
    for y in matrix:
        if isinstance(y, QVBoxLayout):
            main_layout.addLayout(y)
        else:
            h_box = QHBoxLayout()
            for x in y:
                h_box.addWidget(x)
            h_box.addStretch(1)
            main_layout.addLayout(h_box)
    return main_layout
