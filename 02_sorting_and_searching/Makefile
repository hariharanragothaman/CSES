# +--------------------+
# |                    |
# |   GENERAL CONFIG   |
# |                    |
# +--------------------+

FNAME := contest
DEBUG := true
LANG := cpp

CXX := g++
CXXFLAGS := -std=c++17 -O2 -Wall -Wextra -pedantic -Wshadow -Wformat=2 -Wfloat-equal -Wconversion -Wlogical-op -Wshift-overflow=2 -Wduplicated-cond -Wcast-qual -Wcast-align -Wno-unused-result -Wno-sign-conversion
DEBUG_CXXFLAGS := -fsanitize=address -fsanitize=undefined -fsanitize=float-divide-by-zero -fsanitize=float-cast-overflow -fno-sanitize-recover=all -fstack-protector-all -D_FORTIFY_SOURCE=2
DEBUG_CXXFLAGS += -D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC
PRECOMPILE_HEADERS := bits/stdc++.h


# +-------------------+
# |                   |
# |   GENERAL RULES   |
# |                   |
# +-------------------+


.PHONY: default
default: build

.PHONY: build
build:
	g++ ${CXXFLAGS} ${FNAME}.cpp -o ${FNAME}

.PHONY: run
run:
	g++ ${CXXFLAGS} -o ${FNAME} && ./${FNAME}