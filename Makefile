#--------------------------------------------Variables--------------------------------------------

MAKEFLAGS	+=	--silent

NAME		=	computor
SRC_DIR 	=	src/
PYTHON		=	python3
PIP			=	pip3
RM			=	rm -rf
ECHO		=	echo

#--------------------------------------------Colors--------------------------------------------

DEF_COLOR	=	\033[0;39m
ORANGE		=	\033[0;33m
GRAY		=	\033[0;90m
RED			=	\033[0;91m
GREEN		=	\033[1;92m
YELLOW		=	\033[1;93m
BLUE		=	\033[0;94m
MAGENTA		=	\033[0;95m
CYAN		=	\033[0;96m
WHITE		=	\033[0;97m
CLEARLINE	=	\033[1A\033[K

#--------------------------------------------Files--------------------------------------------

MAIN_DIR	=	$(SRC_DIR)
MAIN_FILES	=	computor.py
CORE_FILES	=	core.py init.py
MATH_DIR	=	$(SRC_DIR)math/
PARSER_DIR	=	$(SRC_DIR)parser/

SRC_MAIN_FILE=	$(addprefix $(MAIN_DIR), $(MAIN_FILES))

OBJF		=	.cache_exists

#--------------------------------------------Rules--------------------------------------------

all:       message $(NAME)

message: ## Display the building of files.
            @echo "\n$(YELLOW)[Starting to build...]$(DEF_COLOR)\n\n$(MAGENTA)"

$(NAME): 
			check_requirements
            @$(ECHO) "$(GREEN)[COMPUTORV1]:\tall files built successfully!$(DEF_COLOR)\n"

check_requirements: ## Verify dependencies are installed.
            @$(PYTHON) -m pip install -q -r requirements.txt
            @$(ECHO) "$(GREEN)[COMPUTORV1]:\tdependencies installed$(DEF_COLOR)\n"

help: ## Print help on Makefile.
                    @grep '^[^.#]\+:\s\+.*#' Makefile | \
                    sed "s/\(.\+\):\s*\(.*\) #\s*\(.*\)/`printf "$(GRAY)"`\1`printf "$(DEF_COLOR)"`	\3 /" | \
                    expand -t8

clean: ## Clean generated files and cache.
                    @$(RM) __pycache__ .pytest_cache .mypy_cache
                    @find $(SRC_DIR) -type d -name __pycache__ -exec $(RM) {} + 2>/dev/null || true
                    @$(ECHO) "$(BLUE)[COMPUTORV1]:\tobject files$(DEF_COLOR)\t$(GREEN) => Cleaned!$(DEF_COLOR)\n"

fclean: ## Clean all generated file, including binaries.
                    @make clean
                    @$(RM) $(NAME) libft.a woody .cache_exists
                    @$(ECHO) "$(CYAN)[COMPUTORV1]:\texec. files$(DEF_COLOR)\t$(GREEN) => Cleaned!$(DEF_COLOR)\n"

re: ## Clean and rebuild binary file.
                    @make fclean all
                    @$(ECHO) "\n$(GREEN)###\tCleaned and rebuilt everything for [COMPUTORV1]!\t###$(DEF_COLOR)\n"

.PHONY:			all clean fclean re message help check_requirements