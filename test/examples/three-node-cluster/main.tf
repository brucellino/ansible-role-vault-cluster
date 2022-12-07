terraform {
  required_providers {
    vault = {
      source = "hashicorp/vault"
    }
    digitalocean = {
      source = "digitalocean/digitalocean"
      # version = "~>2.0.0"
    }
  }

}

provider "digitalocean" {}


module "vpc" {
  source  = "brucellino/vpc/digitalocean"
  version = "1.0.3"
  project = {
    description = "Vault test"
    environment = "development"
    name        = "VaultTest"
    purpose     = "Personal"
  }
  vpc_description = "Vault Test VPC"
  vpc_name        = "vault-test"
  vpc_region      = "ams3"
}


module "consul" {
  depends_on = [module.vpc]
  source     = "brucellino/consul/digitalocean"
  version    = "1.0.6"
  agents     = 3
  datacenter = "test"
}
