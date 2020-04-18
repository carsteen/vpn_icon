#!/bin/bash

function func_build() {
    debuild
}

function func_test_install() {
    docker run -v $PWD/../:/shared tests/Dockerfile
}

usageRun() {
  cat <<-EOF
      Usage: ./tools.sh <CIBLE> [-h]

      PARAMETRES:
      ===========
          build
          test-install
          test

      OPTIONS:
      ========
          -h    Affiche ce message

      EXAMPLES:
      =========

EOF
} 


while getopts "h" arg
do
  case $arg in
    h)
    usageRun
    exit 0
    ;;
    ?)
    echo -e "\\033[31m Unknow argument \\033[0m"
    exit 1
    ;;
  esac
done

shift $((OPTIND-1))

case $1 in
  build)
  shift 1
  func_build "$@"
  ;;
  test-install)
  shift 1
  func_test_install "$@"
  ;;
  "")
  exit 0
  ;;
  *)
  echo -e "\\033[31m Error \\033[0m No Such Option" 1>&2
  exit 1
  ;;
esac
