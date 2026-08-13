# @ohos.geoLocationManager

Provides interfaces for acquiring location information, managing location switches, geocoding, reverse geocoding, country code, fencing and other functions.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace geoLocationManager--><!--Device-unnamed-declare namespace geoLocationManager-End-->

**System capability:** 
- API version 11 and later: SystemCapability.Location.Location.Core

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addBeaconFence](arkts-location-geolocationmanager-addbeaconfence-f.md#addBeaconFence) |
| [addGnssGeofence](arkts-location-geolocationmanager-addgnssgeofence-f.md#addGnssGeofence) |
| [findMatchingWlan](arkts-location-geolocationmanager-findmatchingwlan-f.md#findMatchingWlan) |
| [flushCachedGnssLocations](arkts-location-geolocationmanager-flushcachedgnsslocations-f.md#flushCachedGnssLocations) |
| [flushCachedGnssLocations](arkts-location-geolocationmanager-flushcachedgnsslocations-f.md#flushCachedGnssLocations) |
| [getActiveGeoFences](arkts-location-geolocationmanager-getactivegeofences-f.md#getActiveGeoFences) |
| [getAddressesFromLocation](arkts-location-geolocationmanager-getaddressesfromlocation-f.md#getAddressesFromLocation) |
| [getAddressesFromLocation](arkts-location-geolocationmanager-getaddressesfromlocation-f.md#getAddressesFromLocation) |
| [getAddressesFromLocationName](arkts-location-geolocationmanager-getaddressesfromlocationname-f.md#getAddressesFromLocationName) |
| [getAddressesFromLocationName](arkts-location-geolocationmanager-getaddressesfromlocationname-f.md#getAddressesFromLocationName) |
| [getCachedGnssLocationsSize](arkts-location-geolocationmanager-getcachedgnsslocationssize-f.md#getCachedGnssLocationsSize) |
| [getCachedGnssLocationsSize](arkts-location-geolocationmanager-getcachedgnsslocationssize-f.md#getCachedGnssLocationsSize) |
| [getCountryCode](arkts-location-geolocationmanager-getcountrycode-f.md#getCountryCode) |
| [getCountryCode](arkts-location-geolocationmanager-getcountrycode-f.md#getCountryCode) |
| [getCurrentDistrict](arkts-location-geolocationmanager-getcurrentdistrict-f.md#getCurrentDistrict) |
| [getCurrentLocation](arkts-location-geolocationmanager-getcurrentlocation-f.md#getCurrentLocation) |
| [getCurrentLocation](arkts-location-geolocationmanager-getcurrentlocation-f.md#getCurrentLocation) |
| [getCurrentLocation](arkts-location-geolocationmanager-getcurrentlocation-f.md#getCurrentLocation) |
| [getCurrentWifiBssidForLocating](arkts-location-geolocationmanager-getcurrentwifibssidforlocating-f.md#getCurrentWifiBssidForLocating) |
| [getDistanceBetweenLocations](arkts-location-geolocationmanager-getdistancebetweenlocations-f.md#getDistanceBetweenLocations) |
| [getGeofenceSupportedCoordTypes](arkts-location-geolocationmanager-getgeofencesupportedcoordtypes-f.md#getGeofenceSupportedCoordTypes) |
| [getLastLocation](arkts-location-geolocationmanager-getlastlocation-f.md#getLastLocation) |
| [getPoiInfo](arkts-location-geolocationmanager-getpoiinfo-f.md#getPoiInfo) |
| [getPostProcessingTrack](arkts-location-geolocationmanager-getpostprocessingtrack-f.md#getPostProcessingTrack) |
| [isBeaconFenceSupported](arkts-location-geolocationmanager-isbeaconfencesupported-f.md#isBeaconFenceSupported) |
| [isCachedGnssServiceSupported](arkts-location-geolocationmanager-iscachedgnssservicesupported-f.md#isCachedGnssServiceSupported) |
| [isGeocoderAvailable](arkts-location-geolocationmanager-isgeocoderavailable-f.md#isGeocoderAvailable) |
| [isGnssFenceServiceSupported](arkts-location-geolocationmanager-isgnssfenceservicesupported-f.md#isGnssFenceServiceSupported) |
| [isGnssServiceSupported](arkts-location-geolocationmanager-isgnssservicesupported-f.md#isGnssServiceSupported) |
| [isLocationEnabled](arkts-location-geolocationmanager-islocationenabled-f.md#isLocationEnabled) |
| [isPoiServiceSupported](arkts-location-geolocationmanager-ispoiservicesupported-f.md#isPoiServiceSupported) |
| [isWlanBssidMatched](arkts-location-geolocationmanager-iswlanbssidmatched-f.md#isWlanBssidMatched) |
| [offBluetoothScanResultChange](arkts-location-geolocationmanager-offbluetoothscanresultchange-f.md#offBluetoothScanResultChange) |
| [offCachedGnssLocationsChange](arkts-location-geolocationmanager-offcachedgnsslocationschange-f.md#offCachedGnssLocationsChange) |
| [offCountryCodeChange](arkts-location-geolocationmanager-offcountrycodechange-f.md#offCountryCodeChange) |
| [offGnssFenceStatusChange](arkts-location-geolocationmanager-offgnssfencestatuschange-f.md#offGnssFenceStatusChange) |
| [offLocationChange](arkts-location-geolocationmanager-offlocationchange-f.md#offLocationChange) |
| [offLocationEnabledChange](arkts-location-geolocationmanager-offlocationenabledchange-f.md#offLocationEnabledChange) |
| [offLocationError](arkts-location-geolocationmanager-offlocationerror-f.md#offLocationError) |
| [offNmeaMessage](arkts-location-geolocationmanager-offnmeamessage-f.md#offNmeaMessage) |
| [offSatelliteStatusChange](arkts-location-geolocationmanager-offsatellitestatuschange-f.md#offSatelliteStatusChange) |
| [off_bluetoothScanResultChange](arkts-location-geolocationmanager-offbluetoothscanresultchange-f.md) |
| [off_cachedGnssLocationsChange](arkts-location-geolocationmanager-offcachedgnsslocationschange-f.md) |
| [off_countryCodeChange](arkts-location-geolocationmanager-offcountrycodechange-f.md) |
| [off_gnssFenceStatusChange](arkts-location-geolocationmanager-offgnssfencestatuschange-f.md) |
| off_locationChange |
| [off_locationEnabledChange](arkts-location-geolocationmanager-offlocationenabledchange-f.md) |
| [off_locationError](arkts-location-geolocationmanager-offlocationerror-f.md) |
| [off_nmeaMessage](arkts-location-geolocationmanager-offnmeamessage-f.md) |
| [off_satelliteStatusChange](arkts-location-geolocationmanager-offsatellitestatuschange-f.md) |
| [onBluetoothScanResultChange](arkts-location-geolocationmanager-onbluetoothscanresultchange-f.md#onBluetoothScanResultChange) |
| [onCachedGnssLocationsChange](arkts-location-geolocationmanager-oncachedgnsslocationschange-f.md#onCachedGnssLocationsChange) |
| [onCountryCodeChange](arkts-location-geolocationmanager-oncountrycodechange-f.md#onCountryCodeChange) |
| [onGnssFenceStatusChange](arkts-location-geolocationmanager-ongnssfencestatuschange-f.md#onGnssFenceStatusChange) |
| [onLocationChange](arkts-location-geolocationmanager-onlocationchange-f.md#onLocationChange) |
| [onLocationEnabledChange](arkts-location-geolocationmanager-onlocationenabledchange-f.md#onLocationEnabledChange) |
| [onLocationError](arkts-location-geolocationmanager-onlocationerror-f.md#onLocationError) |
| [onNmeaMessage](arkts-location-geolocationmanager-onnmeamessage-f.md#onNmeaMessage) |
| [onSatelliteStatusChange](arkts-location-geolocationmanager-onsatellitestatuschange-f.md#onSatelliteStatusChange) |
| [on_bluetoothScanResultChange](arkts-location-geolocationmanager-onbluetoothscanresultchange-f.md) |
| [on_cachedGnssLocationsChange](arkts-location-geolocationmanager-oncachedgnsslocationschange-f.md) |
| [on_countryCodeChange](arkts-location-geolocationmanager-oncountrycodechange-f.md) |
| [on_gnssFenceStatusChange](arkts-location-geolocationmanager-ongnssfencestatuschange-f.md) |
| on_locationChange |
| [on_locationEnabledChange](arkts-location-geolocationmanager-onlocationenabledchange-f.md) |
| [on_locationError](arkts-location-geolocationmanager-onlocationerror-f.md) |
| [on_nmeaMessage](arkts-location-geolocationmanager-onnmeamessage-f.md) |
| [on_satelliteStatusChange](arkts-location-geolocationmanager-onsatellitestatuschange-f.md) |
| [removeBeaconFence](arkts-location-geolocationmanager-removebeaconfence-f.md#removeBeaconFence) |
| [removeGnssGeofence](arkts-location-geolocationmanager-removegnssgeofence-f.md#removeGnssGeofence) |
| [sendCommand](arkts-location-geolocationmanager-sendcommand-f.md#sendCommand) |
| [sendCommand](arkts-location-geolocationmanager-sendcommand-f.md#sendCommand) |
| [startBluetoothSearch](arkts-location-geolocationmanager-startbluetoothsearch-f.md#startBluetoothSearch) |
| [stopBluetoothSearch](arkts-location-geolocationmanager-stopbluetoothsearch-f.md#stopBluetoothSearch) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addFusionFence](arkts-location-geolocationmanager-addfusionfence-f-sys.md#addFusionFence-(System-API)) |
| [disableLocation](arkts-location-geolocationmanager-disablelocation-f-sys.md#disableLocation-(System-API)) |
| [disableLocationByUserId](arkts-location-geolocationmanager-disablelocationbyuserid-f-sys.md#disableLocationByUserId-(System-API)) |
| [disableLocationMock](arkts-location-geolocationmanager-disablelocationmock-f-sys.md#disableLocationMock-(System-API)) |
| [disableReverseGeocodingMock](arkts-location-geolocationmanager-disablereversegeocodingmock-f-sys.md#disableReverseGeocodingMock-(System-API)) |
| [enableLocation](arkts-location-geolocationmanager-enablelocation-f-sys.md#enableLocation-(System-API)) |
| [enableLocation](arkts-location-geolocationmanager-enablelocation-f-sys.md#enableLocation-(System-API)) |
| [enableLocationByUserId](arkts-location-geolocationmanager-enablelocationbyuserid-f-sys.md#enableLocationByUserId-(System-API)) |
| [enableLocationMock](arkts-location-geolocationmanager-enablelocationmock-f-sys.md#enableLocationMock-(System-API)) |
| [enableReverseGeocodingMock](arkts-location-geolocationmanager-enablereversegeocodingmock-f-sys.md#enableReverseGeocodingMock-(System-API)) |
| [getLocatingRequiredData](arkts-location-geolocationmanager-getlocatingrequireddata-f-sys.md#getLocatingRequiredData-(System-API)) |
| [getLocationIconStatus](arkts-location-geolocationmanager-getlocationiconstatus-f-sys.md#getLocationIconStatus-(System-API)) |
| [isFusionFenceSupported](arkts-location-geolocationmanager-isfusionfencesupported-f-sys.md#isFusionFenceSupported-(System-API)) |
| [isLocationEnabledByUserId](arkts-location-geolocationmanager-islocationenabledbyuserid-f-sys.md#isLocationEnabledByUserId-(System-API)) |
| [isLocationPrivacyConfirmed](arkts-location-geolocationmanager-islocationprivacyconfirmed-f-sys.md#isLocationPrivacyConfirmed-(System-API)) |
| [offLocatingRequiredDataChange](arkts-location-geolocationmanager-offlocatingrequireddatachange-f-sys.md#offLocatingRequiredDataChange-(System-API)) |
| [offLocationIconStatusChange](arkts-location-geolocationmanager-offlocationiconstatuschange-f-sys.md#offLocationIconStatusChange-(System-API)) |
| [off_locatingRequiredDataChange](arkts-location-geolocationmanager-offlocatingrequireddatachange-f-sys.md) |
| [off_locationIconStatusChange](arkts-location-geolocationmanager-offlocationiconstatuschange-f-sys.md) |
| [onLocatingRequiredDataChange](arkts-location-geolocationmanager-onlocatingrequireddatachange-f-sys.md#onLocatingRequiredDataChange-(System-API)) |
| [onLocationIconStatusChange](arkts-location-geolocationmanager-onlocationiconstatuschange-f-sys.md#onLocationIconStatusChange-(System-API)) |
| [on_locatingRequiredDataChange](arkts-location-geolocationmanager-onlocatingrequireddatachange-f-sys.md) |
| [on_locationIconStatusChange](arkts-location-geolocationmanager-onlocationiconstatuschange-f-sys.md) |
| [removeFusionFence](arkts-location-geolocationmanager-removefusionfence-f-sys.md#removeFusionFence-(System-API)) |
| [setLocationPrivacyConfirmStatus](arkts-location-geolocationmanager-setlocationprivacyconfirmstatus-f-sys.md#setLocationPrivacyConfirmStatus-(System-API)) |
| [setLocationSwitchIgnored](arkts-location-geolocationmanager-setlocationswitchignored-f-sys.md#setLocationSwitchIgnored-(System-API)) |
| [setMockedLocations](arkts-location-geolocationmanager-setmockedlocations-f-sys.md#setMockedLocations-(System-API)) |
| [setReverseGeocodingMockInfo](arkts-location-geolocationmanager-setreversegeocodingmockinfo-f-sys.md#setReverseGeocodingMockInfo-(System-API)) |
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
