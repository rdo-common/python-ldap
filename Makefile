# Makefile for source rpm: python-ldap
# $Id$
NAME := python-ldap
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
