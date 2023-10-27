$Csvfile = "..\CSV\output.csv"
$Users = Import-Csv $Csvfile -UseCulture


$cred = Get-Credential
# Import the Active Directory module
Import-Module ActiveDirectory

# Loop through each user
foreach ($User in $Users) {
    $GivenName = $User.'Vorname'
    $Surname = $User.'Nachname'
    #$DisplayName = $User.'Display name'
    $SamAccountName = $User.'Username'
    $UserPrincipalName = $User.'User principal name'
    $StreetAddress = $User.'Strasse'+$User.'Hausnummer'
    $City = $User.'Stadt'
    $State = $User.'Bundesland'
    $PostalCode = $User.'Postleitzahl'
    #$Country = $User.'Country/region'
    #$JobTitle = $User.'Job Title'
    #$Department = $User.'Department'
    $Company = $User.'Firma'
    #$ManagerDisplayName = $User.'Manager'
    <#$Manager = if ($ManagerDisplayName) {
        Get-ADUser -Filter "DisplayName -eq '$ManagerDisplayName'" -Properties DisplayName |
        Select-Object -ExpandProperty DistinguishedName
    }#>
    $OU = $User.'OU'
    #$Description = $User.'Description'
    #$Office = $User.'Office'
    $TelephoneNumber = $User.'Telefon'
    $Email = $User.'EMail'
    $Mobile = $User.'Mobil'
    #$Notes = $User.'Notes'
    $AccountStatus = $User.'Aktiv'
    $Password = $User.'Password'

    # Check if the user already exists in AD
    <#
    Invoke-Command -ComputerName sr-dc01 -Scriptblock {
        $UserExists = Get-ADUser -Filter { SamAccountName -eq $SamAccountName } -ErrorAction SilentlyContinue

        if ($UserExists) {
            Write-Warning "User '$SamAccountName' already exists in Active Directory."
            continue
        }
    } -Credential $cred#>

# Create new user parameters
Write-Host $GivenName " " $Surname "Wurde erstellt"

# Define the parameters as a hashtable
$NewUserParams = @{
    Name                  = "$GivenName $Surname"
    GivenName             = $GivenName
    Surname               = $Surname
    SamAccountName        = $SamAccountName
    UserPrincipalName     = $UserPrincipalName
    StreetAddress         = $StreetAddress
    City                  = $City
    State                 = $State
    PostalCode            = $PostalCode
    Company               = $Company
    Path                  = $OU
    OfficePhone           = $TelephoneNumber
    EmailAddress          = $Email
    MobilePhone           = $Mobile
    AccountPassword       = (ConvertTo-SecureString $Password -AsPlainText -Force)
    Enabled               = if ($AccountStatus -eq "Enabled") { $true } else { $false }
    ChangePasswordAtLogon = $true # Set the "User must change password at next logon" flag
}

# Add the info attribute to OtherAttributes only if Notes field contains a value
if (![string]::IsNullOrEmpty($Notes)) {
    $NewUserParams.OtherAttributes = @{info = $Notes }
}





    # Create a script block that accepts the parameters
    $scriptBlock = {
        param (
            $NewUserParams
        )

        try {
            # Create the new AD user
            New-ADUser @NewUserParams
            Write-Host "User $($NewUserParams.SamAccountName) created successfully." -ForegroundColor Cyan
        }
        catch {
            # Failed to create the new AD user
            $ErrorMessage = $_.Exception.Message
            if ($ErrorMessage -match "The password does not meet the length, complexity, or history requirement") {
                Write-Warning "User $($NewUserParams.SamAccountName) created but account is disabled. $_"
            }
            else {
                Write-Warning "Failed to create user $($NewUserParams.SamAccountName). $_"
            }
        }
    }

    # Pass the $NewUserParams to the remote script using -ArgumentList
    Invoke-Command -ComputerName sr-dc01 -Scriptblock $scriptBlock -Credential $cred -ArgumentList $NewUserParams, $NewOUPath
    
}


    #To do: use the for loop the code is in, to just use one line of code instead of many
    #Write-Progress -PercentComplete ((1/2206)*100) -Status "Import wird durchgeführt..." -Activity "User 1 von 2206"