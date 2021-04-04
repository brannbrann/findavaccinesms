$latfromzip = '37.7' # [math]::round(($zipcodelist | where-object { $_.zip -eq $lookupzip }).lat,3)
$lngfromzip = '-122' # [math]::round(($zipcodelist | where-object { $_.zip -eq $lookupzip }).lng,3)

# $stfromzip = 'CA' #( $zipcodelist | where-object { $_.zip -eq $lookupzip } ).state_id
$radiusdist = 50

$header = @{
    "Referer" = "https://www.freemaptools.com/find-cities-and-towns-inside-radius.htm"
    "path" = "/ajax/get-all-cities-inside.php?lat=$($latfromzip)&lng=$($lngfromzip)&sortaplha=0&radius=$radiusdist"
    }

$allLocalities = Invoke-RestMethod -uri "https://www.freemaptools.com/ajax/get-all-cities-inside.php?lat=$($latfromzip)&lng=$($lngfromzip)&sortaplha=0&radius=$radiusdistkm" -method get -headers $header

