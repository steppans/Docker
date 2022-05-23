hello:
	docker run --rm --name PythonHello hello
SimpleSolver:
	docker run --rm --name SimpleSolver -it solver:v1.1
ImprovedSolver:
	docker run --rm --name ImprovedSolver -it solver:v2.6
