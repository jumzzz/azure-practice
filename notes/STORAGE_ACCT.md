### Uploading to Storage account using Python

```Python
block_blob_service = BlockBlobService(
    account_name='account_name',
    account_key='account_key
)
```
`account_name`: Storage account name
`account_key`: Storage account key

### From Stackoverflow 

[Source](https://stackoverflow.com/questions/61487550/get-access-key-from-azure-file-share-terraform)
```
data "azurerm_storage_account" "example" {
  name                = "packerimages"
  resource_group_name = "packer-storage"
}

output "storage_account_primary_access_key" {
  value = data.azurerm_storage_account.example.primary_access_key
}
```
**Note:** Try using data.azurerm_storage_account.example.primary_access_key


### As per docs you can use Custom Script Extension

[Custom Script Extension](https://docs.microsoft.com/en-us/previous-versions/azure/virtual-machines/scripts/virtual-machines-linux-cli-sample-create-vm-nginx?toc=%2Fcli%2Fazure%2Ftoc.json)

### You can also refer here

[Azure Container Group in Terraform](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/container_group)