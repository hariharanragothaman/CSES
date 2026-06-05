# ---- Config ----
pname    ?= contest
CXX      ?= g++
TIMEOUT  ?= timeout 1.0s        # macOS: use gtimeout
DEBUG    ?= 0                   # DEBUG=1 enables sanitizers + debug
COMPILER := $(shell $(CXX) --version | head -n 1)

# ---- Warnings (portable base) ----
BASE_WARNINGS := -Wall -Wextra -Wpedantic -Wshadow -Wformat=2 -Wfloat-equal -Wconversion \
                 -Wcast-qual -Wcast-align -Wno-unused-result -Wno-sign-conversion \
                 -Wvla -Wnull-dereference

# ---- Compiler-specific extras ----
ifeq ($(findstring clang,$(COMPILER)),clang)
  # Clang-specific goodies
  COMP_WARNINGS := -Wrange-loop-analysis -Wpessimizing-move -Wredundant-move \
                   -Wimplicit-fallthrough -Woverloaded-virtual -Wnon-virtual-dtor \
                   -Wextra-semi
  DIAG_COLOR := -fcolor-diagnostics
else
  # GCC-only extras
  COMP_WARNINGS := -Wlogical-op -Wshift-overflow=2 -Wduplicated-cond -Wuseless-cast \
                   -Wimplicit-fallthrough=5 -Woverloaded-virtual -Wnon-virtual-dtor
  DIAG_COLOR := -fdiagnostics-color=always
endif

BASEFLAGS := -std=c++20 $(BASE_WARNINGS) $(COMP_WARNINGS) $(DIAG_COLOR)

# ---- Build flags (debug vs release) ----
ifeq ($(DEBUG),1)
  ifeq ($(findstring clang,$(COMPILER)),clang)
    CXXFLAGS := $(BASEFLAGS) -O0 -g3 -fno-omit-frame-pointer \
                -fsanitize=address,undefined,float-divide-by-zero,float-cast-overflow
    # If using libc++ and you want extra iterator/assert checks, uncomment:
    # CXXFLAGS += -D_LIBCPP_ENABLE_ASSERTIONS=1 -D_LIBCPP_ENABLE_DEBUG_MODE=1
  else
    CXXFLAGS := $(BASEFLAGS) -O0 -g3 -fno-omit-frame-pointer \
                -fsanitize=address,undefined,float-divide-by-zero,float-cast-overflow \
                -fno-sanitize-recover=all -fstack-protector-all -D_FORTIFY_SOURCE=2 \
                -D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC
  endif
else
  CXXFLAGS := $(BASEFLAGS) -O2
endif

# ---- Default: build + run ----
.PHONY: all
all: $(pname)
	$(TIMEOUT) ./$(pname)

# ---- Build (single source: pname.cpp) ----
$(pname): $(pname).cpp
	$(CXX) $(CXXFLAGS) $< -o $@

# ---- Test: feed input file and (optionally) diff expected ----
# Usage:
#   make test                       # uses data.in -> data.out
#   make test FILE=case1.in OUT=case1.out
#   make test FILE=case1.in OUT=case1.out EXPECT=case1.exp
FILE   ?= data.in
OUT    ?= data.out
EXPECT ?=

.PHONY: test
test: $(pname)
	@if [ -f "$(FILE)" ]; then \
	  echo ">> Running: ./$(pname) < $(FILE) > $(OUT)"; \
	  $(TIMEOUT) ./$(pname) < "$(FILE)" > "$(OUT)"; \
	  if [ -n "$(EXPECT)" ] && [ -f "$(EXPECT)" ]; then \
	    echo ">> Diffing: $(OUT) vs $(EXPECT)"; \
	    diff -u "$(EXPECT)" "$(OUT)" || true; \
	  else \
	    echo ">> Output:"; \
	    cat "$(OUT)"; \
	  fi; \
	else \
	  echo "No such input file: $(FILE)"; \
	fi

# ---- Clean ----
.PHONY: clean
clean:
	rm -f $(pname) $(OUT)
