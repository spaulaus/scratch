//
// Created by stanp on 12/19/2020.
//
#include <random>

#if defined(_WIN64) || defined(_WIN32)
#include <w32pragma.h>
#include <Windows.h>
#endif

#include <TCanvas.h>
#include <TH1D.h>

using namespace std;

int main(int argc, char** argv) {
    default_random_engine generator;
    normal_distribution<double> distribution(5.0, 1.5);

    auto* h1 = new TH1D("h1", "h1 title", 10, 0, 10);

    for (auto i = 0; i < 10000; i++)
        h1->Fill(distribution(generator));

    auto* c1 = new TCanvas("c1", "Histogram Drawing Options", 200, 10, 700, 900);
    h1->Draw();
    c1->SaveAs("test_root_cern.pdf", "PDF");
}