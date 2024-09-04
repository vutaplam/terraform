# Terraform Fundamentals

## IaC Overview

## Terraform vs other Iac tools

## Terraform workflow

## Core Terraform Commands

* init
* fmt
* validate
* plan
* apply
* destroy
* import
* output
* state
  * list
  * show
  * rm
* login

## Variables

* string
* list(string)
* list(object({key=value}))
* number
* bool
* map
* set
* map(any)

## Blocks

* resource
* data
* output
* module
* terraform
* provider
* variable
* dynamic

## dependencies

* implicit
* explicit

## meta-argument

* count
* lifecycle
* depends_on
* for_each

## functions

* lookup
* templatefile
* file

## expressions

## Provisioners

* file

* local-exec
  * when
  * on_failure
  * command
  * Multiple Provisioners

* remote-exec
  * inline
  * script
  * scripts

* connection type
  * ssh
  * winrm

## null_resource

* triggers
