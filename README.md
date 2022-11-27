[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/brucellino/ansible-role-vault-cluster/main.svg)](https://results.pre-commit.ci/latest/github/brucellino/ansible-role-vault-cluster/main)
[![main](https://github.com/brucellino/ansible-role-vault-cluster/actions/workflows/main.yml/badge.svg)](https://github.com/brucellino/ansible-role-vault-cluster/actions/workflows/main.yml)
[![semantic-release: angular](https://img.shields.io/badge/semantic--release-conventional-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)

# Ansible Role for Vault

This is an Ansible role for configuring a Vault cluster from scratch.

## Requirements

None.

## Role Variables

See [`defaults/main.yml`](defaults/main.yml)

## Dependencies

None

## Example Playbook

```yaml
- name: vault-servers
  roles:
    - ansible-role-vault
```

## License

MIT

## Author Information

Bruce Becker @brucellino
