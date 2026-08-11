# @ohos.geoLocationManager

Provides interfaces for acquiring location information, managing location switches,geocoding, reverse geocoding, country code, fencing and other functions.

**Since:** 9

<!--Device-unnamed-declare namespace geoLocationManager--><!--Device-unnamed-declare namespace geoLocationManager-End-->

**System capability:** 
- API version 11 and later: SystemCapability.Location.Location.Core

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addBeaconFence](arkts-location-geolocationmanager-addbeaconfence-f.md#addbeaconfence) |
| [addGnssGeofence](arkts-location-geolocationmanager-addgnssgeofence-f.md#addgnssgeofence) |
| [findMatchingWlan](arkts-location-geolocationmanager-findmatchingwlan-f.md#findmatchingwlan) |
| [flushCachedGnssLocations](arkts-location-geolocationmanager-flushcachedgnsslocations-f.md#flushcachedgnsslocations) |
| [flushCachedGnssLocations](arkts-location-geolocationmanager-flushcachedgnsslocations-f.md#flushcachedgnsslocations-1) |
| [getActiveGeoFences](arkts-location-geolocationmanager-getactivegeofences-f.md#getactivegeofences) |
| [getAddressesFromLocation](arkts-location-geolocationmanager-getaddressesfromlocation-f.md#getaddressesfromlocation) |
| [getAddressesFromLocation](arkts-location-geolocationmanager-getaddressesfromlocation-f.md#getaddressesfromlocation-1) |
| [getAddressesFromLocationName](arkts-location-geolocationmanager-getaddressesfromlocationname-f.md#getaddressesfromlocationname) |
| [getAddressesFromLocationName](arkts-location-geolocationmanager-getaddressesfromlocationname-f.md#getaddressesfromlocationname-1) |
| [getCachedGnssLocationsSize](arkts-location-geolocationmanager-getcachedgnsslocationssize-f.md#getcachedgnsslocationssize) |
| [getCachedGnssLocationsSize](arkts-location-geolocationmanager-getcachedgnsslocationssize-f.md#getcachedgnsslocationssize-1) |
| [getCountryCode](arkts-location-geolocationmanager-getcountrycode-f.md#getcountrycode) |
| [getCountryCode](arkts-location-geolocationmanager-getcountrycode-f.md#getcountrycode-1) |
| [getCurrentDistrict](arkts-location-geolocationmanager-getcurrentdistrict-f.md#getcurrentdistrict) |
| [getCurrentLocation](arkts-location-geolocationmanager-getcurrentlocation-f.md#getcurrentlocation) |
| [getCurrentLocation](arkts-location-geolocationmanager-getcurrentlocation-f.md#getcurrentlocation-1) |
| [getCurrentLocation](arkts-location-geolocationmanager-getcurrentlocation-f.md#getcurrentlocation-2) |
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
| [off](arkts-location-geolocationmanager-off-f.md#off) |
| [off](arkts-location-geolocationmanager-off-f.md#off-1) |
| [off](arkts-location-geolocationmanager-off-f.md#off-2) |
| [off](arkts-location-geolocationmanager-off-f.md#off-3) |
| [off](arkts-location-geolocationmanager-off-f.md#off-4) |
| [off](arkts-location-geolocationmanager-off-f.md#off-5) |
| [off](arkts-location-geolocationmanager-off-f.md#off-6) |
| [off](arkts-location-geolocationmanager-off-f.md#off-7) |
| [off](arkts-location-geolocationmanager-off-f.md#off-10) |
| [offLocationChange](arkts-location-geolocationmanager-offlocationchange-f.md#offlocationchange) |
| [on](arkts-location-geolocationmanager-on-f.md#on) |
| [on](arkts-location-geolocationmanager-on-f.md#on-1) |
| [on](arkts-location-geolocationmanager-on-f.md#on-2) |
| [on](arkts-location-geolocationmanager-on-f.md#on-3) |
| [on](arkts-location-geolocationmanager-on-f.md#on-4) |
| [on](arkts-location-geolocationmanager-on-f.md#on-5) |
| [on](arkts-location-geolocationmanager-on-f.md#on-6) |
| [on](arkts-location-geolocationmanager-on-f.md#on-7) |
| [on](arkts-location-geolocationmanager-on-f.md#on-10) |
| [onLocationChange](arkts-location-geolocationmanager-onlocationchange-f.md#onlocationchange) |
| [removeBeaconFence](arkts-location-geolocationmanager-removebeaconfence-f.md#removebeaconfence) |
| [removeGnssGeofence](arkts-location-geolocationmanager-removegnssgeofence-f.md#removegnssgeofence) |
| [sendCommand](arkts-location-geolocationmanager-sendcommand-f.md#sendcommand) |
| [sendCommand](arkts-location-geolocationmanager-sendcommand-f.md#sendcommand-1) |
| [startBluetoothSearch](arkts-location-geolocationmanager-startbluetoothsearch-f.md#startbluetoothsearch) |
| [stopBluetoothSearch](arkts-location-geolocationmanager-stopbluetoothsearch-f.md#stopbluetoothsearch) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addFusionFence](arkts-location-geolocationmanager-addfusionfence-f-sys.md#addfusionfence) |
| [disableLocation](arkts-location-geolocationmanager-disablelocation-f-sys.md#disablelocation) |
| [disableLocationByUserId](arkts-location-geolocationmanager-disablelocationbyuserid-f-sys.md#disablelocationbyuserid) |
| [disableLocationMock](arkts-location-geolocationmanager-disablelocationmock-f-sys.md#disablelocationmock) |
| [disableReverseGeocodingMock](arkts-location-geolocationmanager-disablereversegeocodingmock-f-sys.md#disablereversegeocodingmock) |
| [enableLocation](arkts-location-geolocationmanager-enablelocation-f-sys.md#enablelocation) |
| [enableLocation](arkts-location-geolocationmanager-enablelocation-f-sys.md#enablelocation-1) |
| [enableLocationByUserId](arkts-location-geolocationmanager-enablelocationbyuserid-f-sys.md#enablelocationbyuserid) |
| [enableLocationMock](arkts-location-geolocationmanager-enablelocationmock-f-sys.md#enablelocationmock) |
| [enableReverseGeocodingMock](arkts-location-geolocationmanager-enablereversegeocodingmock-f-sys.md#enablereversegeocodingmock) |
| [getLocatingRequiredData](arkts-location-geolocationmanager-getlocatingrequireddata-f-sys.md#getlocatingrequireddata) |
| [getLocationIconStatus](arkts-location-geolocationmanager-getlocationiconstatus-f-sys.md#getlocationiconstatus) |
| [isFusionFenceSupported](arkts-location-geolocationmanager-isfusionfencesupported-f-sys.md#isfusionfencesupported) |
| [isLocationEnabledByUserId](arkts-location-geolocationmanager-islocationenabledbyuserid-f-sys.md#islocationenabledbyuserid) |
| [isLocationPrivacyConfirmed](arkts-location-geolocationmanager-islocationprivacyconfirmed-f-sys.md#islocationprivacyconfirmed) |
| [off](arkts-location-geolocationmanager-off-f-sys.md#off-8) |
| [off](arkts-location-geolocationmanager-off-f-sys.md#off-9) |
| [on](arkts-location-geolocationmanager-on-f-sys.md#on-8) |
| [on](arkts-location-geolocationmanager-on-f-sys.md#on-9) |
| [removeFusionFence](arkts-location-geolocationmanager-removefusionfence-f-sys.md#removefusionfence) |
| [setLocationPrivacyConfirmStatus](arkts-location-geolocationmanager-setlocationprivacyconfirmstatus-f-sys.md#setlocationprivacyconfirmstatus) |
| [setLocationSwitchIgnored](arkts-location-geolocationmanager-setlocationswitchignored-f-sys.md#setlocationswitchignored) |
| [setMockedLocations](arkts-location-geolocationmanager-setmockedlocations-f-sys.md#setmockedlocations) |
| [setReverseGeocodingMockInfo](arkts-location-geolocationmanager-setreversegeocodingmockinfo-f-sys.md#setreversegeocodingmockinfo) |
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
