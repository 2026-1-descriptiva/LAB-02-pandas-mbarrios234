"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

tbl1 = pd.read_csv("tbl1.tsv", sep="\t")

def pregunta_11():
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c4` del archivo `tbl1.tsv`.

    Rta/
         c0       c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    R11 = tbl1.copy()
    R11 = R11.groupby('_c0').agg({'_c4': lambda var: sorted(list(var))})
    for ind, fil in R11.iterrows():
        fil['_c4'] = ",".join([str(num) for num in fil['_c4']])
    R11.insert(0, '_c0', range(0, 40))
    return R11