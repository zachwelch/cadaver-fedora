# Makefile for source rpm: cadaver
# $Id$
NAME := cadaver
SPECFILE = $(firstword $(wildcard *.spec))
UPSTREAM_CHECKS := asc

include ../common/Makefile.common
