# Makefile for source rpm: cadaver
# $Id$
NAME := cadaver
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
