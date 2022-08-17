# GUI File
window_style = '''
* {
    font-family: Segoe UI;
    font-size: 14px;
}
QLabel[cssClass="bigFont"] {
    font-family: Segoe UI;
    font-size: 22px;
    color: rgb(29, 32, 37);
}
QPushButton[cssClass="navButton"] {
	background-color:rgb(141, 150, 169);
	border: none;
color: white;
}
QPushButton[cssClass="normalBtn"] {
	color: rgb(255, 255, 255);
    border: 1px solid white;
	background-color: rgb(141, 150, 169);;
    border-radius: 10px;
    font-family: Segoe UI;
    font-size: 14px;
    font-weight: bold;
}
QPushButton[cssClass="normalBtn"]:hover {
background-color: rgb(129, 138, 158);
}
QPushButton[cssClass="normalBtn"]:pressed {
	background-color: rgb(145, 152, 170);
}
QPushButton[cssClass="navButton"]:hover {
	background-color:rgb(183, 188, 200);
color: white;
}
QFrame[cssClass="navBar"] {
	background-color:rgb(141, 150, 169);
}
QLineEdit {
border: 1px solid rgb(141, 150, 169);
border-radius: 5px;
}
QTextEdit {
border: 1px solid rgb(129, 138, 158);
border-radius: 5px;
}
QFrame[cssClass="listItem"] {
    background-color: rgb(196, 201, 210);
    border: 1px solid rgb(196, 201, 210);
}
QFrame[cssClass="listItem"]:hover {
    background-color: rgb(206, 209, 217);
    border: 1px solid rgb(227, 230, 234);
}
QScrollArea {
    border: none;
}
QPushButton[cssClass="deleteItemBtn"] {
    border: transparent;
    font-size: 10px;
    border-radius: 15px;
}
QPushButton[cssClass="deleteItemBtn"]:hover {
    background-color: rgb(196, 201, 210);
}
QPushButton[cssClass="deleteItemBtn"]:pressed {
    background-color: rgb(180, 185, 197);
}
QScrollBar {
    width: 5px;
}
QPushButton[cssClass="special_btn"] {
border: 2px solid  rgb(167, 178, 200);
border-radius: 5px;
color:white;
font-weight: bold;
background-color: rgb(141, 150, 169);
}
QPushButton[cssClass="special_btn"]:hover {
border: 2px solid  rgb(167, 178, 200);
border-radius: 5px;
color:white;
font-weight: bold;
background-color: rgb(158, 168, 189);
}
'''