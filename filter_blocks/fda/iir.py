"""
"""

import myhdl as hdl
from myhdl import Signal, ResetSignal, intbv, always

from filter_blocks import Clock, Reset, Samples
from filter_blocks import filter_iir, filter_iir_sos

from .filter_hw import FilterHardware


class FilterIIR(FilterHardware):
    def __init__(self, b, a, sos=None):
        """Configuration and analysis of a hardware digital filter.
        """
        super(FilterIIR, self).__init__(b, a)
        self.n_sections = 1
        self.convert_coefficients(b, a, sos)
        self .iir_sections = [None for _ in range(self.n_sections)]
        self.first_pass = True

    def convert_coefficients(self, b, a, sos):
        """Extract the coefficients and convert to fixed-point.
        """
        pass

    def process(self, x):
        for ii in range(self.n_sections):
            x = self.iir_sections[ii].process(x)
        y = x
        return y

    def get_filter_instance(self, glbl, sigin, sigout):
        """Get the filter hardware instance.

        Args:
            glbl: global signals like clock, reset, enable
            sigin: input signal bus
            sigout: output signal bus

        Returns:
            inst (myhdl.Block): an object that represents the
               filter block.

        """
        inst = None
        if self.is_sos:
            pass
        else:
            pass

        return inst

    @hdl.block
    def filter_iir_top(self, clock, reset, x, xdv, y, ydv):
        """Small top-level wrapper"""
        w = (len(x), 0, len(x)-1)
        sigin = Samples(word_format=w)
        sigin.data, sigin.valid = x, xdv
        sigout = Samples(word_format=w)
        sigout.data, sigout.valid = y, ydv

        return filter_inst

    def convert(self, hdl='verilog'):
        """Convert to verilog or vhdl"""
        w = self.word_format
        imax = 2**(w[0]-1)
        clock = Clock(0, frequency=50e6)
        reset = Reset(0, active=0, async=True)
        x = Signal(intbv(0, min=-imax, max=imax))
        y = Signal(intbv(0, min=-imax, max=imax))
        xdv, ydv = Signal(bool(0)), Signal(bool(0))

        inst = self.filter_iir_top(clock, reset, x, xdv, y, ydv)
        inst.name = self.hdl_name
        inst.directory = self.hdl_directory
        inst.convert(hdl=hdl)
