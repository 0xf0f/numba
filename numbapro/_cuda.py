from numbapro import cuda
import numbapro.cudapy  # import time sideeffect
from numba.cuda.cudadrv.driver import FuncAttr


def calc_occupancy(cc, reg, smem=0, smem_config=None):
    """Occupancy calculator

    Args
    ----
    - cc
        compute capability as a tuple-2 of ints.
    - reg
        register used per thread.
    - smem
        shared memory used per block.
    - smem_config
        (optional) smem configuration

    Returns
    -------
    returns an AutoTuner object

    """
    from .cudadrv import autotune

    usage = FuncAttr(regs=reg, shared=smem, local=0, const=0,
                     maxthreads=cuda.get_current_device().MAX_THREADS_PER_BLOCK)
    at = autotune.AutoTuner(cc=cc, info=usage, smem_config=smem_config)
    return at

# Install extensions
cuda.calc_occupancy = calc_occupancy
