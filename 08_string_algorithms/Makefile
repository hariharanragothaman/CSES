# +--------------------+
# |                    |
# |   GENERAL CONFIG   |
# |                    |
# +--------------------+

PROBLEM_NAME := concert_tickets
DEBUG := true
LANG := cpp

CXX := g++-11
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
	@ mkdir -p "output"
	${CXX} ${CXXFLAGS}  ${PROBLEM_NAME}.cpp -o output/${PROBLEM_NAME}

.PHONY: run
run: build
	./output/${PROBLEM_NAME}

.PHONY: clean
clean:
	rm -rf output/