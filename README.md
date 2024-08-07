# Terraform content

| Topic | Sub-Topic | Description | Reference |
| ------ | -----------|  ---------- | ----------|
| Overview of IaC | | | |
| Advantages of Terraform | | ||
| Core Terraform Commands |init| downloads required plugins used in provider block|[terraform-commands-cheat-sheet](https://spacelift.io/blog/terraform-commands-cheat-sheet)|
| |fmt| auto indentation||
|| validate| check for syntax||
|| plan| overview of what resources will be created (dry run)| |
|| apply| creates the infrastructure  ||
|| destroy |destroy the infra ||
|| state |show and manage resource metadata | |
|| output |displays the values from output block | |
|Integrate terraform with CICD| | We use github actions for our CICD | |
|Variables|| input can be set from the command line, environment variables, or a variables file.||
|output|| used to share information between modules or to access values from the outside||
| local| |not accessible outside the module.||
|Blocks| resource  | | |
||data  | | |
||terraform  | | |
||provider  | | |
||variable  | | |
||output  | | |
||module  | | |
|Modules| local | | [modules tutorial](https://developer.hashicorp.com/terraform/tutorials/modules/module) |
||remote | | |
||custom | | |
|State management| remote state| | |  
||local state | | |
