#include "pybode.h"
#include "ui_pybode.h"

pyBode::pyBode(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::pyBode)
{
    ui->setupUi(this);
}

pyBode::~pyBode()
{
    delete ui;
}
