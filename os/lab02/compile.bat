if exist PROG.OBJ del PROG.OBJ
TASM32\TASM.EXE %1 PROG.OBJ
TASM32\TLINK.EXE PROG.OBJ