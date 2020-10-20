#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "omp/EquityCalculator.h"
#include <string.h> 

using namespace omp;
using namespace std;

double equity(std::vector<string> &sranges, std::string board_cards, int maxRuns){    
    EquityCalculator eq;
    
    std::vector<CardRange> ranges(sranges.begin(), sranges.end());
    uint64_t board = CardRange::getCardMask(board_cards);
    uint64_t dead = CardRange::getCardMask("");
    double stdErrMargin = 0.5; // stop when standard error below 0.2%
    eq.start(ranges, board, dead, false, stdErrMargin, maxRuns);
    eq.wait();
    auto r = eq.getResults();
    return r.equity[0];
}

PYBIND11_MODULE(ompeval, m) {
    m.doc() = "OMPEval fast montecarlo texas holdem simulation"; // optional module docstring
    m.def("equity", &equity, "A function for texas holdem monte carlo calculation");
}