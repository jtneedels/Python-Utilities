# Unit Conversion Scripts
# Jacob Needels
# Created: 10.27.21

def SLPM2kg_s(Tgas, Pgas, rhoGas, SLPM):
    """
    Inputs:
    Tgas: K
    Pgas: psi
    rhoGas: g/L

    Returns: flow rate in kg/s

    """
    LPM = SLPM * Tgas / 273.15 * 14.504 / Pgas
    g_m = LPM * rhoGas
    kg_s = g_m / 60 / 1e3
    return kg_s



