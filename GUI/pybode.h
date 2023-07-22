#ifndef PYBODE_H
#define PYBODE_H

#include <QMainWindow>

namespace Ui {
class pyBode;
}

class pyBode : public QMainWindow
{
    Q_OBJECT

public:
    explicit pyBode(QWidget *parent = nullptr);
    ~pyBode();

private:
    Ui::pyBode *ui;
};

#endif // PYBODE_H
