# Generate random text for a unique storage account name
resource "random_id" "randomId" {
    keepers = {
        # Generate a new ID only when a new resource group is defined
        resource_group = "${var.resource_group_name}"
    }

    byte_length = 8
}

# Create storage account for boot diagnostics
resource "azurerm_storage_account" "storageaccount" {
    name                = "diag${random_id.randomId.hex}"
    location            = "${var.resource_group_location}" 
    resource_group_name = "${var.resource_group_name}"
    account_tier             = "Standard"
    account_replication_type = "LRS"
}

resource "azurerm_container_group" "data_gen_container" {
    name                = "data-gen"
    location            = "${var.resource_group_location}" 
    resource_group_name = "${var.resource_group_name}"
    
    ip_address_type     = "Public"
    dns_name_label      = "aci-label"
    os_type             = "Linux"
    
    container {
        name   = "data-gen-worker"
        image  = "jumzzz/data-gen-az:latest"
        cpu    = "0.5"
        memory = "1.5"

        environment_variables {
            AZURE_STORAGE_CONNECTION_STRING = data.azurerm_storage_account.storageaccount.primary_access_key
        }
    }
    
    tags = {
        environment = "testing"
    }
}