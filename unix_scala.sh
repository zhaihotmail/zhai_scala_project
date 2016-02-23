#!bin/sh
exec scala $0 $@
!#
println("Hello world"+args(0)+"|"+args(1))
