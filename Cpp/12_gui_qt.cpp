#include <QApplication> 
#include <QWidget>
#include <QLabel>

int main(int argc, char* argv[]){
    // Init the app class
    QApplication app(argc, argv);
    QWidget win;

    // Set window geometry
    win.setGeometry(0, 0, 800, 600);
    win.setWindowTitle("Title");

    // Set a label
    QLabel* label = new QLabel("This is a label", &win);
    label->setText("This is a updated label juhuu!");
    label->move(50, 50);

    // Show the window
    win.show();
    return app.exec();
}
// $ qmake-qt4 && make && ./12_gui_qt