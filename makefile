primera : ecu.pdf
ecu.pdf : datos.txt grafica.py
	python grafica.py

datos.txt : sol.cpp
	c++ sol.cpp -o sol
	./sol > datos.txt

segunda : ecu2.pdf
ecu2.pdf : datos2.txt grafica2.py
	python grafica2.py

datos2.txt : sol2.cpp
	c++ sol2.cpp -o sol2
	./sol2 > datos2.txt
