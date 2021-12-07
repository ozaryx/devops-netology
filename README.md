# devops-netology
first change

# Исключаются все файлы из подкаталога .terraform любых каталогов
**/.terraform/*

# исключаются все файлы, в имени которых есть .tfstate
*.tfstate
*.tfstate.*

# исключается файл с именем crash.log 
crash.log

# Исключаются все файлы с расширением .tfvars
*.tfvars

# Исключаются файлы override.tf, override.tf.json, и файлы в имени которы есть _override.tf и _override.tf.json
override.tf
override.tf.json
*_override.tf
*_override.tf.json

# Исключаются файлы .terraformrc и terraform.rc
.terraformrc
terraform.rc

# IDE commits
Second line change