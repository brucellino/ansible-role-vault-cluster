def test_vault_user(host):
    assert host.group("vault").exists
    assert host.user("vault").exists
    assert "vault" in host.user("vault").groups


def test_vault_raft_dir(host):
    """
    Ensure that the vault configuration directory is present and properly configured
    """
    vault_config_dir = host.file("/etc/vault.d")
    assert vault_config_dir.exists
    assert vault_config_dir.is_directory
    assert vault_config_dir.user == "vault"
    assert vault_config_dir.group == "vault"
    assert vault_config_dir.mode == 0o770

def test_vault_raft_dir(host):
    """_Vault raft dir_

    Args:
        host (_string_): _Test whether the vault raft dir is properly configured_
    """
    vault_raft_dir = host.file("/vault")
    assert vault_raft_dir.exists
    assert vault_raft_dir.is_directory
    assert vault_raft_dir.user == "vault"
    assert vault_raft_dir.group == "vault"
    assert vault_raft_dir.mode == 0o770

def test_vault_config_file(host):
    """_Vault Configuration File_

    Args:
        host (_string_): _Check that configuration file is present_
    """

    vault_config_file = host.file("/etc/vault.d/vault.hcl")
    assert vault_config_file.exists
    assert vault_config_file.is_file
    assert vault_config_file.user == "vault"
    assert vault_config_file.group == "vault"
