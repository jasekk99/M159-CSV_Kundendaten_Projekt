




param (
    [Parameter()]
    [array]$uniqueBundeslaender
)


$cred = Get-Credential

$NewOUName = ''
$NewOUPath = ''

function AddOU {
    param (
            [Parameter()]
            [string]$NewOUName,

            [Parameter()]
            [string]$NewOUPath
        )
    
        

        Invoke-Command -ComputerName sr-dc01 -Scriptblock {
            param (
                $NewOUName,
                $NewOUPath
            )

            New-ADOrganizationalUnit -Name $NewOUName -Path $NewOUPath
        } -Credential $cred -ArgumentList $NewOUName, $NewOUPath
    
    
}

function DisableDeletePrevention {
    param (
        [Parameter()]
        [string]$search_DeletePrev
    )
    
    Invoke-Command -ComputerName sr-dc01 -Scriptblock {
        param (
            $search_DeletePrev
        )

        Get-ADObject -Filter * -SearchBase $search_DeletePrev |ForEach-Object -Process {Set-ADObject -ProtectedFromAccidentalDeletion $false -Identity $_}
    } -Credential $cred -ArgumentList $search_DeletePrev

}


#Erstelle OUs
#Mitarbeiter OU
Write-Progress -PercentComplete ((1/23)*100) -Status "OUs werden erstellt..." -Activity "OU 1 von 23"
AddOU -NewOUName "Mitarbeiter" -NewOUPath "DC=intersped,DC=loc"
Write-Progress -PercentComplete ((2/23)*100) -Status "OUs werden erstellt..." -Activity "OU 2 von 23"
    AddOU -NewOUName "Rheinstadt" -NewOUPath "OU=Mitarbeiter,DC=intersped,DC=loc"
    Write-Progress -PercentComplete ((3/23)*100) -Status "OUs werden erstellt..." -Activity "OU 3 von 23"
    AddOU -NewOUName "Berlin" -NewOUPath "OU=Mitarbeiter,DC=intersped,DC=loc"
    Write-Progress -PercentComplete ((4/23)*100) -Status "OUs werden erstellt..." -Activity "OU 4 von 23"
    AddOU -NewOUName "Wien" -NewOUPath "OU=Mitarbeiter,DC=intersped,DC=loc"
    Write-Progress -PercentComplete ((5/23)*100) -Status "OUs werden erstellt..." -Activity "OU 5 von 23"
    AddOU -NewOUName "Vancouver" -NewOUPath "OU=Mitarbeiter,DC=intersped,DC=loc"
    Write-Progress -PercentComplete ((6/23)*100) -Status "OUs werden erstellt..." -Activity "OU 6 von 23"
    AddOU -NewOUName "Washington" -NewOUPath "OU=Mitarbeiter,DC=intersped,DC=loc"
    Write-Progress -PercentComplete ((7/23)*100) -Status "OUs werden erstellt..." -Activity "OU 7 von 23"

#Kunden OU
AddOU -NewOUName "Kunden" -NewOUPath "DC=intersped,DC=loc"
Write-Progress -PercentComplete ((8/23)*100) -Status "OUs werden erstellt..." -Activity "OU 8 von 23"
    AddOU -NewOUName "Baden-Wuerttemberg" -NewOUPath "OU=Kunden,DC=intersped,DC=loc"
    Write-Progress -PercentComplete ((9/23)*100) -Status "OUs werden erstellt..." -Activity "OU 9 von 23"
    AddOU -NewOUName "Hessen" -NewOUPath "OU=Kunden,DC=intersped,DC=loc"
    Write-Progress -PercentComplete ((10/23)*100) -Status "OUs werden erstellt..." -Activity "OU 10 von 23"
    AddOU -NewOUName "Bayern" -NewOUPath "OU=Kunden,DC=intersped,DC=loc"
    Write-Progress -PercentComplete ((11/23)*100) -Status "OUs werden erstellt..." -Activity "OU 11 von 23"
    AddOU -NewOUName "Rheinland-Pfalz" -NewOUPath "OU=Kunden,DC=intersped,DC=loc"
    Write-Progress -PercentComplete ((12/23)*100) -Status "OUs werden erstellt..." -Activity "OU 12 von 23"
    AddOU -NewOUName "Nordrhein-Westfalen" -NewOUPath "OU=Kunden,DC=intersped,DC=loc"
    Write-Progress -PercentComplete ((13/23)*100) -Status "OUs werden erstellt..." -Activity "OU 13 von 23"
    AddOU -NewOUName "Mecklenburg-Vorpommern" -NewOUPath "OU=Kunden,DC=intersped,DC=loc"
    Write-Progress -PercentComplete ((14/23)*100) -Status "OUs werden erstellt..." -Activity "OU 14 von 23"
    AddOU -NewOUName "Schleswig-Holstein" -NewOUPath "OU=Kunden,DC=intersped,DC=loc"
    Write-Progress -PercentComplete ((15/23)*100) -Status "OUs werden erstellt..." -Activity "OU 15 von 23"
    AddOU -NewOUName "Niedersachsen" -NewOUPath "OU=Kunden,DC=intersped,DC=loc"
    Write-Progress -PercentComplete ((16/23)*100) -Status "OUs werden erstellt..." -Activity "OU 16 von 23"
    AddOU -NewOUName "Bremen" -NewOUPath "OU=Kunden,DC=intersped,DC=loc"
    Write-Progress -PercentComplete ((17/23)*100) -Status "OUs werden erstellt..." -Activity "OU 17 von 23"
    AddOU -NewOUName "Saarland" -NewOUPath "OU=Kunden,DC=intersped,DC=loc"
    Write-Progress -PercentComplete ((18/23)*100) -Status "OUs werden erstellt..." -Activity "OU 18 von 23"
    AddOU -NewOUName "Sachsen-Anhalt" -NewOUPath "OU=Kunden,DC=intersped,DC=loc"
    Write-Progress -PercentComplete ((19/23)*100) -Status "OUs werden erstellt..." -Activity "OU 19 von 23"
    AddOU -NewOUName "Sachsen" -NewOUPath "OU=Kunden,DC=intersped,DC=loc"
    Write-Progress -PercentComplete ((20/23)*100) -Status "OUs werden erstellt..." -Activity "OU 20 von 23"
    AddOU -NewOUName "Hamburg" -NewOUPath "OU=Kunden,DC=intersped,DC=loc"
    Write-Progress -PercentComplete ((21/23)*100) -Status "OUs werden erstellt..." -Activity "OU 21 von 23"
    AddOU -NewOUName "Brandenburg" -NewOUPath "OU=Kunden,DC=intersped,DC=loc"
    Write-Progress -PercentComplete ((22/23)*100) -Status "OUs werden erstellt..." -Activity "OU 22 von 23"
    AddOU -NewOUName "Berlin" -NewOUPath "OU=Kunden,DC=intersped,DC=loc"
    Write-Progress -PercentComplete ((23/23)*100) -Status "OUs werden erstellt..." -Activity "OU 23 von 23"
    AddOU -NewOUName "Thueringen" -NewOUPath "OU=Kunden,DC=intersped,DC=loc"








#$search_DeletePrev = "OU=Mitarbeiter,DC=intersped,DC=loc"
#Get-ADObject -Filter * -SearchBase $search_DeletePrev |ForEach-Object -Process {Set-ADObject -ProtectedFromAccidentalDeletion $false -Identity $_}
DisableDeletePrevention -search_DeletePrev "OU=Mitarbeiter,DC=intersped,DC=loc"

#$search_DeletePrev = "OU=Kunden,DC=intersped,DC=loc"
#Get-ADObject -Filter * -SearchBase $search_DeletePrev |ForEach-Object -Process {Set-ADObject -ProtectedFromAccidentalDeletion $false -Identity $_}
DisableDeletePrevention -search_DeletePrev "OU=Kunden,DC=intersped,DC=loc"

# Clear the credentials from memory (Security Risk)
#$cred = ''


#Call the import script
& "$PSScriptRoot/ADImport.ps1"