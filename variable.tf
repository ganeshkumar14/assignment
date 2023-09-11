variable "region" {
  description = "Infrastructure region"
  type        = string
  default     = "ap-south-1"
}
variable "access_key" {
  description = "The access_key that belongs to the IAM user"
  type        = string
  sensitive   = true
  default     = "AKIASQMLDE4RWIN7KVTV"
}
variable "secret_key" {
  description = "The secret_key that belongs to the IAM user"
  type        = string
  sensitive   = true
  default     = "KYm+chpLIR4N+ir7f2ZLiVQQtqfAXa34ZUJXckvs"
}
variable "subnet_cidr_public" {
  description = "cidr blocks for the public subnets"
  default     = ["10.0.1.0/24", "10.0.2.0/24"]
  type        = list(any)
}
variable "availability_zone" {
  description = "availability zones for the public subnets"
  default     = ["ap-south-1a", "ap-south-1b"]
  type        = list(any)
}
