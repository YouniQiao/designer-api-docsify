# @ohos.geoLocationManager

Provides interfaces for acquiring location information, managing location switches, geocoding, reverse geocoding, country code, fencing and other functions.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

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
| [addBeaconFence](arkts-location-geolocationmanager-addbeaconfence-f.md) |
| [addGnssGeofence](arkts-location-geolocationmanager-addgnssgeofence-f.md) |
| [findMatchingWlan](arkts-location-geolocationmanager-findmatchingwlan-f.md) |
| [flushCachedGnssLocations](arkts-location-geolocationmanager-flushcachedgnsslocations-f.md) |
| [flushCachedGnssLocations](arkts-location-geolocationmanager-flushcachedgnsslocations-f.md) |
| [getActiveGeoFences](arkts-location-geolocationmanager-getactivegeofences-f.md) |
| [getAddressesFromLocation](arkts-location-geolocationmanager-getaddressesfromlocation-f.md) |
| [getAddressesFromLocation](arkts-location-geolocationmanager-getaddressesfromlocation-f.md) |
| [getAddressesFromLocationName](arkts-location-geolocationmanager-getaddressesfromlocationname-f.md) |
| [getAddressesFromLocationName](arkts-location-geolocationmanager-getaddressesfromlocationname-f.md) |
| [getCachedGnssLocationsSize](arkts-location-geolocationmanager-getcachedgnsslocationssize-f.md) |
| [getCachedGnssLocationsSize](arkts-location-geolocationmanager-getcachedgnsslocationssize-f.md) |
| [getCountryCode](arkts-location-geolocationmanager-getcountrycode-f.md) |
| [getCountryCode](arkts-location-geolocationmanager-getcountrycode-f.md) |
| [getCurrentDistrict](arkts-location-geolocationmanager-getcurrentdistrict-f.md) |
| [getCurrentLocation](arkts-location-geolocationmanager-getcurrentlocation-f.md) |
| [getCurrentLocation](arkts-location-geolocationmanager-getcurrentlocation-f.md) |
| [getCurrentLocation](arkts-location-geolocationmanager-getcurrentlocation-f.md) |
| [getCurrentWifiBssidForLocating](arkts-location-geolocationmanager-getcurrentwifibssidforlocating-f.md) |
| [getDistanceBetweenLocations](arkts-location-geolocationmanager-getdistancebetweenlocations-f.md) |
| [getGeofenceSupportedCoordTypes](arkts-location-geolocationmanager-getgeofencesupportedcoordtypes-f.md) |
| [getLastLocation](arkts-location-geolocationmanager-getlastlocation-f.md) |
| [getPoiInfo](arkts-location-geolocationmanager-getpoiinfo-f.md) |
| [getPostProcessingTrack](arkts-location-geolocationmanager-getpostprocessingtrack-f.md) |
| [isBeaconFenceSupported](arkts-location-geolocationmanager-isbeaconfencesupported-f.md) |
| [isCachedGnssServiceSupported](arkts-location-geolocationmanager-iscachedgnssservicesupported-f.md) |
| [isGeocoderAvailable](arkts-location-geolocationmanager-isgeocoderavailable-f.md) |
| [isGnssFenceServiceSupported](arkts-location-geolocationmanager-isgnssfenceservicesupported-f.md) |
| [isGnssServiceSupported](arkts-location-geolocationmanager-isgnssservicesupported-f.md) |
| [isLocationEnabled](arkts-location-geolocationmanager-islocationenabled-f.md) |
| [isPoiServiceSupported](arkts-location-geolocationmanager-ispoiservicesupported-f.md) |
| [isWlanBssidMatched](arkts-location-geolocationmanager-iswlanbssidmatched-f.md) |
| [off](arkts-location-geolocationmanager-off-f.md#offlocationchange) |
| [off](arkts-location-geolocationmanager-off-f.md#offlocationerror) |
| [off](arkts-location-geolocationmanager-off-f.md#offlocationenabledchange) |
| [off](arkts-location-geolocationmanager-off-f.md#offcachedgnsslocationschange) |
| [off](arkts-location-geolocationmanager-off-f.md#offsatellitestatuschange) |
| [off](arkts-location-geolocationmanager-off-f.md#offnmeamessage) |
| [off](arkts-location-geolocationmanager-off-f.md#offgnssfencestatuschange) |
| [off](arkts-location-geolocationmanager-off-f.md#offcountrycodechange) |
| [off](arkts-location-geolocationmanager-off-f.md#offbluetoothscanresultchange) |
| [offBluetoothScanResultChange](arkts-location-geolocationmanager-offbluetoothscanresultchange-f.md) |
| [offCachedGnssLocationsChange](arkts-location-geolocationmanager-offcachedgnsslocationschange-f.md) |
| [offCountryCodeChange](arkts-location-geolocationmanager-offcountrycodechange-f.md) |
| [offGnssFenceStatusChange](arkts-location-geolocationmanager-offgnssfencestatuschange-f.md) |
| [offLocationChange](arkts-location-geolocationmanager-offlocationchange-f.md) |
| [offLocationEnabledChange](arkts-location-geolocationmanager-offlocationenabledchange-f.md) |
| [offLocationError](arkts-location-geolocationmanager-offlocationerror-f.md) |
| [offNmeaMessage](arkts-location-geolocationmanager-offnmeamessage-f.md) |
| [offSatelliteStatusChange](arkts-location-geolocationmanager-offsatellitestatuschange-f.md) |
| [on](arkts-location-geolocationmanager-on-f.md#onlocationchange) |
| [on](arkts-location-geolocationmanager-on-f.md#onlocationerror) |
| [on](arkts-location-geolocationmanager-on-f.md#onlocationenabledchange) |
| [on](arkts-location-geolocationmanager-on-f.md#oncachedgnsslocationschange) |
| [on](arkts-location-geolocationmanager-on-f.md#onsatellitestatuschange) |
| [on](arkts-location-geolocationmanager-on-f.md#onnmeamessage) |
| [on](arkts-location-geolocationmanager-on-f.md#ongnssfencestatuschange) |
| [on](arkts-location-geolocationmanager-on-f.md#oncountrycodechange) |
| [on](arkts-location-geolocationmanager-on-f.md#onbluetoothscanresultchange) |
| [onBluetoothScanResultChange](arkts-location-geolocationmanager-onbluetoothscanresultchange-f.md) |
| [onCachedGnssLocationsChange](arkts-location-geolocationmanager-oncachedgnsslocationschange-f.md) |
| [onCountryCodeChange](arkts-location-geolocationmanager-oncountrycodechange-f.md) |
| [onGnssFenceStatusChange](arkts-location-geolocationmanager-ongnssfencestatuschange-f.md) |
| [onLocationChange](arkts-location-geolocationmanager-onlocationchange-f.md) |
| [onLocationEnabledChange](arkts-location-geolocationmanager-onlocationenabledchange-f.md) |
| [onLocationError](arkts-location-geolocationmanager-onlocationerror-f.md) |
| [onNmeaMessage](arkts-location-geolocationmanager-onnmeamessage-f.md) |
| [onSatelliteStatusChange](arkts-location-geolocationmanager-onsatellitestatuschange-f.md) |
| [removeBeaconFence](arkts-location-geolocationmanager-removebeaconfence-f.md) |
| [removeGnssGeofence](arkts-location-geolocationmanager-removegnssgeofence-f.md) |
| [sendCommand](arkts-location-geolocationmanager-sendcommand-f.md) |
| [sendCommand](arkts-location-geolocationmanager-sendcommand-f.md) |
| [startBluetoothSearch](arkts-location-geolocationmanager-startbluetoothsearch-f.md) |
| [stopBluetoothSearch](arkts-location-geolocationmanager-stopbluetoothsearch-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addFusionFence](arkts-location-geolocationmanager-addfusionfence-f-sys.md) |
| [disableLocation](arkts-location-geolocationmanager-disablelocation-f-sys.md) |
| [disableLocationByUserId](arkts-location-geolocationmanager-disablelocationbyuserid-f-sys.md) |
| [disableLocationMock](arkts-location-geolocationmanager-disablelocationmock-f-sys.md) |
| [disableReverseGeocodingMock](arkts-location-geolocationmanager-disablereversegeocodingmock-f-sys.md) |
| [enableLocation](arkts-location-geolocationmanager-enablelocation-f-sys.md) |
| [enableLocation](arkts-location-geolocationmanager-enablelocation-f-sys.md) |
| [enableLocationByUserId](arkts-location-geolocationmanager-enablelocationbyuserid-f-sys.md) |
| [enableLocationMock](arkts-location-geolocationmanager-enablelocationmock-f-sys.md) |
| [enableReverseGeocodingMock](arkts-location-geolocationmanager-enablereversegeocodingmock-f-sys.md) |
| [getLocatingRequiredData](arkts-location-geolocationmanager-getlocatingrequireddata-f-sys.md) |
| [getLocationIconStatus](arkts-location-geolocationmanager-getlocationiconstatus-f-sys.md) |
| [isFusionFenceSupported](arkts-location-geolocationmanager-isfusionfencesupported-f-sys.md) |
| [isLocationEnabledByUserId](arkts-location-geolocationmanager-islocationenabledbyuserid-f-sys.md) |
| [isLocationPrivacyConfirmed](arkts-location-geolocationmanager-islocationprivacyconfirmed-f-sys.md) |
| [off](arkts-location-geolocationmanager-off-f-sys.md#offlocatingrequireddatachange) |
| [off](arkts-location-geolocationmanager-off-f-sys.md#offlocationiconstatuschange) |
| [offLocatingRequiredDataChange](arkts-location-geolocationmanager-offlocatingrequireddatachange-f-sys.md) |
| [offLocationIconStatusChange](arkts-location-geolocationmanager-offlocationiconstatuschange-f-sys.md) |
| [on](arkts-location-geolocationmanager-on-f-sys.md#onlocatingrequireddatachange) |
| [on](arkts-location-geolocationmanager-on-f-sys.md#onlocationiconstatuschange) |
| [onLocatingRequiredDataChange](arkts-location-geolocationmanager-onlocatingrequireddatachange-f-sys.md) |
| [onLocationIconStatusChange](arkts-location-geolocationmanager-onlocationiconstatuschange-f-sys.md) |
| [removeFusionFence](arkts-location-geolocationmanager-removefusionfence-f-sys.md) |
| [setLocationPrivacyConfirmStatus](arkts-location-geolocationmanager-setlocationprivacyconfirmstatus-f-sys.md) |
| [setLocationSwitchIgnored](arkts-location-geolocationmanager-setlocationswitchignored-f-sys.md) |
| [setMockedLocations](arkts-location-geolocationmanager-setmockedlocations-f-sys.md) |
| [setReverseGeocodingMockInfo](arkts-location-geolocationmanager-setreversegeocodingmockinfo-f-sys.md) |
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
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BluetoothScanInfo](arkts-location-geolocationmanager-bluetoothscaninfo-i-sys.md) |
| [CellFence](arkts-location-geolocationmanager-cellfence-i-sys.md) |
| [CellInfo](arkts-location-geolocationmanager-cellinfo-i-sys.md) |
| [FusionFenceRequestParams](arkts-location-geolocationmanager-fusionfencerequestparams-i-sys.md) |
| [FusionFenceTransition](arkts-location-geolocationmanager-fusionfencetransition-i-sys.md) |
| [GeoAddress](arkts-location-geolocationmanager-geoaddress-i-sys.md) |
| [GnssFence](arkts-location-geolocationmanager-gnssfence-i-sys.md) |
| [LocatingRequiredData](arkts-location-geolocationmanager-locatingrequireddata-i-sys.md) |
| [LocatingRequiredDataConfig](arkts-location-geolocationmanager-locatingrequireddataconfig-i-sys.md) |
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
### Enums(System API)

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
