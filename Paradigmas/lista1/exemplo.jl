using Pkg
Pkg.add("PyCall")
using PyCall

pushfirst!(PyVector(pyimport("sys")."path"), "")

script = pyimport("bomba")

segundos = 5
resultado = script.bomba(segundos)
