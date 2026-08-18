# @ohos.geoLocationManager

Provides interfaces for acquiring location information, managing location switches, geocoding, reverse geocoding, country code, fencing and other functions.

**Since:** 23

<!--Device-unnamed-declare namespace geoLocationManager--><!--Device-unnamed-declare namespace geoLocationManager-End-->

**System capability:** 
- API version 11 and later: SystemCapability.Location.Location.Core

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addBeaconFence](arkts-location-geolocationmanager-addbeaconfence-f.md#addbeaconfence) |
| [addGnssGeofence](arkts-location-geolocationmanager-addgnssgeofence-f.md#addgnssgeofence) |
| [findMatchingWlan](arkts-location-geolocationmanager-findmatchingwlan-f.md#findmatchingwlan) |
| [flushCachedGnssLocations](arkts-location-geolocationmanager-flushcachedgnsslocations-f.md#flushcachedgnsslocations) |
| [flushCachedGnssLocations](arkts-location-geolocationmanager-flushcachedgnsslocations-f.md#flushcachedgnsslocations) |
| [getActiveGeoFences](arkts-location-geolocationmanager-getactivegeofences-f.md#getactivegeofences) |
| [getAddressesFromLocation](arkts-location-geolocationmanager-getaddressesfromlocation-f.md#getaddressesfromlocation) |
| [getAddressesFromLocation](arkts-location-geolocationmanager-getaddressesfromlocation-f.md#getaddressesfromlocation) |
| [getAddressesFromLocationName](arkts-location-geolocationmanager-getaddressesfromlocationname-f.md#getaddressesfromlocationname) |
| [getAddressesFromLocationName](arkts-location-geolocationmanager-getaddressesfromlocationname-f.md#getaddressesfromlocationname) |
| [getCachedGnssLocationsSize](arkts-location-geolocationmanager-getcachedgnsslocationssize-f.md#getcachedgnsslocationssize) |
| [getCachedGnssLocationsSize](arkts-location-geolocationmanager-getcachedgnsslocationssize-f.md#getcachedgnsslocationssize) |
| [getCountryCode](arkts-location-geolocationmanager-getcountrycode-f.md#getcountrycode) |
| [getCountryCode](arkts-location-geolocationmanager-getcountrycode-f.md#getcountrycode) |
| [getCurrentDistrict](arkts-location-geolocationmanager-getcurrentdistrict-f.md#getcurrentdistrict) |
| [getCurrentLocation](arkts-location-geolocationmanager-getcurrentlocation-f.md#getcurrentlocation) |
| [getCurrentLocation](arkts-location-geolocationmanager-getcurrentlocation-f.md#getcurrentlocation) |
| [getCurrentLocation](arkts-location-geolocationmanager-getcurrentlocation-f.md#getcurrentlocation) |
| [getCurrentWifiBssidForLocating](arkts-location-geolocationmanager-getcurrentwifibssidforlocating-f.md#getcurrentwifibssidforlocating) |
| [getDistanceBetweenLocations](arkts-location-geolocationmanager-getdistancebetweenlocations-f.md#getdistancebetweenlocations) |
| [getGeofenceSupportedCoordTypes](arkts-location-geolocationmanager-getgeofencesupportedcoordtypes-f.md#getgeofencesupportedcoordtypes) |
| [getLastLocation](arkts-location-geolocationmanager-getlastlocation-f.md#getlastlocation) |
| [getPoiInfo](arkts-location-geolocationmanager-getpoiinfo-f.md#getpoiinfo) |
| [getPostProcessingTrack](arkts-location-geolocationmanager-getpostprocessingtrack-f.md#getpostprocessingtrack) |
| [isBeaconFenceSupported](arkts-location-geolocationmanager-isbeaconfencesupported-f.md#isbeaconfencesupported) |
| [isCachedGnssServiceSupported](arkts-location-geolocationmanager-iscachedgnssservicesupported-f.md#iscachedgnssservicesupported) |
| [isGeocoderAvailable](arkts-location-geolocationmanager-isgeocoderavailable-f.md#isgeocoderavailable) |
| [isGnssFenceServiceSupported](arkts-location-geolocationmanager-isgnssfenceservicesupported-f.md#isgnssfenceservicesupported) |
| [isGnssServiceSupported](arkts-location-geolocationmanager-isgnssservicesupported-f.md#isgnssservicesupported) |
| [isLocationEnabled](arkts-location-geolocationmanager-islocationenabled-f.md#islocationenabled) |
| [isPoiServiceSupported](arkts-location-geolocationmanager-ispoiservicesupported-f.md#ispoiservicesupported) |
| [isWlanBssidMatched](arkts-location-geolocationmanager-iswlanbssidmatched-f.md#iswlanbssidmatched) |
| [offBluetoothScanResultChange](arkts-location-geolocationmanager-offbluetoothscanresultchange-f.md#offbluetoothscanresultchange) |
| [offCachedGnssLocationsChange](arkts-location-geolocationmanager-offcachedgnsslocationschange-f.md#offcachedgnsslocationschange) |
| [offCountryCodeChange](arkts-location-geolocationmanager-offcountrycodechange-f.md#offcountrycodechange) |
| [offGnssFenceStatusChange](arkts-location-geolocationmanager-offgnssfencestatuschange-f.md#offgnssfencestatuschange) |
| [offLocationChange](arkts-location-geolocationmanager-offlocationchange-f.md#offlocationchange) |
| [offLocationEnabledChange](arkts-location-geolocationmanager-offlocationenabledchange-f.md#offlocationenabledchange) |
| [offLocationError](arkts-location-geolocationmanager-offlocationerror-f.md#offlocationerror) |
| [offNmeaMessage](arkts-location-geolocationmanager-offnmeamessage-f.md#offnmeamessage) |
| [offSatelliteStatusChange](arkts-location-geolocationmanager-offsatellitestatuschange-f.md#offsatellitestatuschange) |
| [off_bluetoothScanResultChange](arkts-location-geolocationmanager-offbluetoothscanresultchange-f.md#offbluetoothscanresultchange) |
| [off_cachedGnssLocationsChange](arkts-location-geolocationmanager-offcachedgnsslocationschange-f.md#offcachedgnsslocationschange) |
| [off_countryCodeChange](arkts-location-geolocationmanager-offcountrycodechange-f.md#offcountrycodechange) |
| [off_gnssFenceStatusChange](arkts-location-geolocationmanager-offgnssfencestatuschange-f.md#offgnssfencestatuschange) |
| [off_locationChange](arkts-location-geolocationmanager-offlocationchange-f.md#offlocationchange) |
| [off_locationEnabledChange](arkts-location-geolocationmanager-offlocationenabledchange-f.md#offlocationenabledchange) |
| [off_locationError](arkts-location-geolocationmanager-offlocationerror-f.md#offlocationerror) |
| [off_nmeaMessage](arkts-location-geolocationmanager-offnmeamessage-f.md#offnmeamessage) |
| [off_satelliteStatusChange](arkts-location-geolocationmanager-offsatellitestatuschange-f.md#offsatellitestatuschange) |
| [onBluetoothScanResultChange](arkts-location-geolocationmanager-onbluetoothscanresultchange-f.md#onbluetoothscanresultchange) |
| [onCachedGnssLocationsChange](arkts-location-geolocationmanager-oncachedgnsslocationschange-f.md#oncachedgnsslocationschange) |
| [onCountryCodeChange](arkts-location-geolocationmanager-oncountrycodechange-f.md#oncountrycodechange) |
| [onGnssFenceStatusChange](arkts-location-geolocationmanager-ongnssfencestatuschange-f.md#ongnssfencestatuschange) |
| [onLocationChange](arkts-location-geolocationmanager-onlocationchange-f.md#onlocationchange) |
| [onLocationEnabledChange](arkts-location-geolocationmanager-onlocationenabledchange-f.md#onlocationenabledchange) |
| [onLocationError](arkts-location-geolocationmanager-onlocationerror-f.md#onlocationerror) |
| [onNmeaMessage](arkts-location-geolocationmanager-onnmeamessage-f.md#onnmeamessage) |
| [onSatelliteStatusChange](arkts-location-geolocationmanager-onsatellitestatuschange-f.md#onsatellitestatuschange) |
| [on_bluetoothScanResultChange](arkts-location-geolocationmanager-onbluetoothscanresultchange-f.md#onbluetoothscanresultchange) |
| [on_cachedGnssLocationsChange](arkts-location-geolocationmanager-oncachedgnsslocationschange-f.md#oncachedgnsslocationschange) |
| [on_countryCodeChange](arkts-location-geolocationmanager-oncountrycodechange-f.md#oncountrycodechange) |
| [on_gnssFenceStatusChange](arkts-location-geolocationmanager-ongnssfencestatuschange-f.md#ongnssfencestatuschange) |
| [on_locationChange](arkts-location-geolocationmanager-onlocationchange-f.md#onlocationchange) |
| [on_locationEnabledChange](arkts-location-geolocationmanager-onlocationenabledchange-f.md#onlocationenabledchange) |
| [on_locationError](arkts-location-geolocationmanager-onlocationerror-f.md#onlocationerror) |
| [on_nmeaMessage](arkts-location-geolocationmanager-onnmeamessage-f.md#onnmeamessage) |
| [on_satelliteStatusChange](arkts-location-geolocationmanager-onsatellitestatuschange-f.md#onsatellitestatuschange) |
| [removeBeaconFence](arkts-location-geolocationmanager-removebeaconfence-f.md#removebeaconfence) |
| [removeGnssGeofence](arkts-location-geolocationmanager-removegnssgeofence-f.md#removegnssgeofence) |
| [sendCommand](arkts-location-geolocationmanager-sendcommand-f.md#sendcommand) |
| [sendCommand](arkts-location-geolocationmanager-sendcommand-f.md#sendcommand) |
| [startBluetoothSearch](arkts-location-geolocationmanager-startbluetoothsearch-f.md#startbluetoothsearch) |
| [stopBluetoothSearch](arkts-location-geolocationmanager-stopbluetoothsearch-f.md#stopbluetoothsearch) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addFusionFence](arkts-location-geolocationmanager-addfusionfence-f-sys.md#addfusionfence-system-api) |
| [disableLocation](arkts-location-geolocationmanager-disablelocation-f-sys.md#disablelocation-system-api) |
| [disableLocationByUserId](arkts-location-geolocationmanager-disablelocationbyuserid-f-sys.md#disablelocationbyuserid-system-api) |
| [disableLocationMock](arkts-location-geolocationmanager-disablelocationmock-f-sys.md#disablelocationmock-system-api) |
| [disableReverseGeocodingMock](arkts-location-geolocationmanager-disablereversegeocodingmock-f-sys.md#disablereversegeocodingmock-system-api) |
| [enableLocation](arkts-location-geolocationmanager-enablelocation-f-sys.md#enablelocation-system-api) |
| [enableLocation](arkts-location-geolocationmanager-enablelocation-f-sys.md#enablelocation-system-api) |
| [enableLocationByUserId](arkts-location-geolocationmanager-enablelocationbyuserid-f-sys.md#enablelocationbyuserid-system-api) |
| [enableLocationMock](arkts-location-geolocationmanager-enablelocationmock-f-sys.md#enablelocationmock-system-api) |
| [enableReverseGeocodingMock](arkts-location-geolocationmanager-enablereversegeocodingmock-f-sys.md#enablereversegeocodingmock-system-api) |
| [getLocatingRequiredData](arkts-location-geolocationmanager-getlocatingrequireddata-f-sys.md#getlocatingrequireddata-system-api) |
| [getLocationIconStatus](arkts-location-geolocationmanager-getlocationiconstatus-f-sys.md#getlocationiconstatus-system-api) |
| [isFusionFenceSupported](arkts-location-geolocationmanager-isfusionfencesupported-f-sys.md#isfusionfencesupported-system-api) |
| [isLocationEnabledByUserId](arkts-location-geolocationmanager-islocationenabledbyuserid-f-sys.md#islocationenabledbyuserid-system-api) |
| [isLocationPrivacyConfirmed](arkts-location-geolocationmanager-islocationprivacyconfirmed-f-sys.md#islocationprivacyconfirmed-system-api) |
| [offLocatingRequiredDataChange](arkts-location-geolocationmanager-offlocatingrequireddatachange-f-sys.md#offlocatingrequireddatachange) |
| [offLocationIconStatusChange](arkts-location-geolocationmanager-offlocationiconstatuschange-f-sys.md#offlocationiconstatuschange) |
| [off_locatingRequiredDataChange](arkts-location-geolocationmanager-offlocatingrequireddatachange-f-sys.md#offlocatingrequireddatachange) |
| [off_locationIconStatusChange](arkts-location-geolocationmanager-offlocationiconstatuschange-f-sys.md#offlocationiconstatuschange) |
| [onLocatingRequiredDataChange](arkts-location-geolocationmanager-onlocatingrequireddatachange-f-sys.md#onlocatingrequireddatachange) |
| [onLocationIconStatusChange](arkts-location-geolocationmanager-onlocationiconstatuschange-f-sys.md#onlocationiconstatuschange) |
| [on_locatingRequiredDataChange](arkts-location-geolocationmanager-onlocatingrequireddatachange-f-sys.md#onlocatingrequireddatachange) |
| [on_locationIconStatusChange](arkts-location-geolocationmanager-onlocationiconstatuschange-f-sys.md#onlocationiconstatuschange) |
| [removeFusionFence](arkts-location-geolocationmanager-removefusionfence-f-sys.md#removefusionfence-system-api) |
| [setLocationPrivacyConfirmStatus](arkts-location-geolocationmanager-setlocationprivacyconfirmstatus-f-sys.md#setlocationprivacyconfirmstatus-system-api) |
| [setLocationSwitchIgnored](arkts-location-geolocationmanager-setlocationswitchignored-f-sys.md#setlocationswitchignored-system-api) |
| [setMockedLocations](arkts-location-geolocationmanager-setmockedlocations-f-sys.md#setmockedlocations-system-api) |
| [setReverseGeocodingMockInfo](arkts-location-geolocationmanager-setreversegeocodingmockinfo-f-sys.md#setreversegeocodingmockinfo-system-api) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BeaconFence](arkts-location-geolocationmanager-beaconfence-i.md) |
| [BeaconFenceRequest](arkts-location-geolocationmanager-beaconfencerequest-i.md) |
| [BeaconManufactureData](arkts-location-geolocationmanager-beaconmanufacturedata-i.md) |
| [BluetoothScanResult](arkts-location-geolocationmanager-bluetoothscanresult-i.md) |
| [BluetoothSearchRequestParams](arkts-location-geolocationmanager-bluetoothsearchrequestparams-i.md) |
| [CachedGnssLocationsRequest](arkts-location-geolocationmanager-cachedgnsslocationsrequest-i.md) |
| [ContinuousLocationRequest](arkts-location-geolocationmanager-continuouslocationrequest-i.md) |
| [CountryCode](arkts-location-geolocationmanager-countrycode-i.md) |
| [CurrentLocationRequest](arkts-location-geolocationmanager-currentlocationrequest-i.md) |
| [DistrictInfo](arkts-location-geolocationmanager-districtinfo-i.md) |
| [DistrictRequestParams](arkts-location-geolocationmanager-districtrequestparams-i.md) |
| [GeoAddress](arkts-location-geolocationmanager-geoaddress-i.md) |
| [GeoCodeRequest](arkts-location-geolocationmanager-geocoderequest-i.md) |
| [Geofence](arkts-location-geolocationmanager-geofence-i.md) |
| [GeofenceRequest](arkts-location-geolocationmanager-geofencerequest-i.md) |
| [GeofenceTransition](arkts-location-geolocationmanager-geofencetransition-i.md) |
| [GnssGeofenceRequest](arkts-location-geolocationmanager-gnssgeofencerequest-i.md) |
| [Location](arkts-location-geolocationmanager-location-i.md) |
| [LocationCommand](arkts-location-geolocationmanager-locationcommand-i.md) |
| [LocationRequest](arkts-location-geolocationmanager-locationrequest-i.md) |
| [MatchingWlanInfo](arkts-location-geolocationmanager-matchingwlaninfo-i.md) |
| [Poi](arkts-location-geolocationmanager-poi-i.md) |
| [PoiInfo](arkts-location-geolocationmanager-poiinfo-i.md) |
| [Point](arkts-location-geolocationmanager-point-i.md) |
| [ReverseGeoCodeRequest](arkts-location-geolocationmanager-reversegeocoderequest-i.md) |
| [SatelliteStatusInfo](arkts-location-geolocationmanager-satellitestatusinfo-i.md) |
| [SingleLocationRequest](arkts-location-geolocationmanager-singlelocationrequest-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BluetoothScanInfo](arkts-location-geolocationmanager-bluetoothscaninfo-i-sys.md) |
| [CellFence](arkts-location-geolocationmanager-cellfence-i-sys.md) |
| [CellInfo](arkts-location-geolocationmanager-cellinfo-i-sys.md) |
| [ContinuousLocationRequest](arkts-location-geolocationmanager-continuouslocationrequest-i-sys.md) |
| [FusionFenceRequestParams](arkts-location-geolocationmanager-fusionfencerequestparams-i-sys.md) |
| [FusionFenceTransition](arkts-location-geolocationmanager-fusionfencetransition-i-sys.md) |
| [GeoAddress](arkts-location-geolocationmanager-geoaddress-i-sys.md) |
| [GnssFence](arkts-location-geolocationmanager-gnssfence-i-sys.md) |
| [LocatingRequiredData](arkts-location-geolocationmanager-locatingrequireddata-i-sys.md) |
| [LocatingRequiredDataConfig](arkts-location-geolocationmanager-locatingrequireddataconfig-i-sys.md) |
| [Location](arkts-location-geolocationmanager-location-i-sys.md) |
| [LocationMockConfig](arkts-location-geolocationmanager-locationmockconfig-i-sys.md) |
| [ReverseGeocodingMockInfo](arkts-location-geolocationmanager-reversegeocodingmockinfo-i-sys.md) |
| [WifiFence](arkts-location-geolocationmanager-wififence-i-sys.md) |
| [WifiScanInfo](arkts-location-geolocationmanager-wifiscaninfo-i-sys.md) |
| [WirelessSignalFeature](arkts-location-geolocationmanager-wirelesssignalfeature-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BeaconFenceInfoType](arkts-location-geolocationmanager-beaconfenceinfotype-e.md) |
| [CoordinateSystemType](arkts-location-geolocationmanager-coordinatesystemtype-e.md) |
| [CountryCodeType](arkts-location-geolocationmanager-countrycodetype-e.md) |
| [GeofenceTransitionEvent](arkts-location-geolocationmanager-geofencetransitionevent-e.md) |
| [LocatingPriority](arkts-location-geolocationmanager-locatingpriority-e.md) |
| [LocationError](arkts-location-geolocationmanager-locationerror-e.md) |
| [LocationRequestPriority](arkts-location-geolocationmanager-locationrequestpriority-e.md) |
| [LocationRequestScenario](arkts-location-geolocationmanager-locationrequestscenario-e.md) |
| [LocationSourceType](arkts-location-geolocationmanager-locationsourcetype-e.md) |
| [PowerConsumptionScenario](arkts-location-geolocationmanager-powerconsumptionscenario-e.md) |
| [SatelliteAdditionalInfo](arkts-location-geolocationmanager-satelliteadditionalinfo-e.md) |
| [SatelliteConstellationCategory](arkts-location-geolocationmanager-satelliteconstellationcategory-e.md) |
| [SportsType](arkts-location-geolocationmanager-sportstype-e.md) |
| [UserActivityScenario](arkts-location-geolocationmanager-useractivityscenario-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FusionFenceScene](arkts-location-geolocationmanager-fusionfencescene-e-sys.md) |
| [FusionFenceType](arkts-location-geolocationmanager-fusionfencetype-e-sys.md) |
| [GeofenceTransitionEvent](arkts-location-geolocationmanager-geofencetransitionevent-e-sys.md) |
| [GnssFenceType](arkts-location-geolocationmanager-gnssfencetype-e-sys.md) |
| [LocatingRequiredDataType](arkts-location-geolocationmanager-locatingrequireddatatype-e-sys.md) |
| [LocationIconStatus](arkts-location-geolocationmanager-locationiconstatus-e-sys.md) |
| [LocationPrivacyType](arkts-location-geolocationmanager-locationprivacytype-e-sys.md) |
| [WifiFingerprintType](arkts-location-geolocationmanager-wififingerprinttype-e-sys.md) |
<!--DelEnd-->
