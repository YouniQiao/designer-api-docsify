# @ohos.geoLocationManager(位置服务)

位置服务提供GNSS定位、网络定位（蜂窝基站、WLAN、蓝牙定位技术）、地理编码、逆地理编码、国家码和地理围栏等基本功能。使用位置服务时请打开设备“位置”开关。如果“位置”开关关闭并且代码未设置捕获异常，可能导致应用异常。

**起始版本：** 9

**系统能力：** 
- API版本11+：SystemCapability.Location.Location.Core

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [addBeaconFence(位置服务)](arkts-location-geolocationmanager-addbeaconfence-f.md) |
| [addGnssGeofence(位置服务)](arkts-location-geolocationmanager-addgnssgeofence-f.md) |
| [findMatchingWlan(位置服务)](arkts-location-geolocationmanager-findmatchingwlan-f.md) |
| [flushCachedGnssLocations(位置服务)](arkts-location-geolocationmanager-flushcachedgnsslocations-f.md) |
| [flushCachedGnssLocations(位置服务)](arkts-location-geolocationmanager-flushcachedgnsslocations-f.md) |
| [getActiveGeoFences(位置服务)](arkts-location-geolocationmanager-getactivegeofences-f.md) |
| [getAddressesFromLocation(位置服务)](arkts-location-geolocationmanager-getaddressesfromlocation-f.md) |
| [getAddressesFromLocation(位置服务)](arkts-location-geolocationmanager-getaddressesfromlocation-f.md) |
| [getAddressesFromLocationName(位置服务)](arkts-location-geolocationmanager-getaddressesfromlocationname-f.md) |
| [getAddressesFromLocationName(位置服务)](arkts-location-geolocationmanager-getaddressesfromlocationname-f.md) |
| [getCachedGnssLocationsSize(位置服务)](arkts-location-geolocationmanager-getcachedgnsslocationssize-f.md) |
| [getCachedGnssLocationsSize(位置服务)](arkts-location-geolocationmanager-getcachedgnsslocationssize-f.md) |
| [getCountryCode(位置服务)](arkts-location-geolocationmanager-getcountrycode-f.md) |
| [getCountryCode(位置服务)](arkts-location-geolocationmanager-getcountrycode-f.md) |
| [getCurrentDistrict(位置服务)](arkts-location-geolocationmanager-getcurrentdistrict-f.md) |
| [getCurrentLocation(位置服务)](arkts-location-geolocationmanager-getcurrentlocation-f.md) |
| [getCurrentLocation(位置服务)](arkts-location-geolocationmanager-getcurrentlocation-f.md) |
| [getCurrentLocation(位置服务)](arkts-location-geolocationmanager-getcurrentlocation-f.md) |
| [getCurrentWifiBssidForLocating(位置服务)](arkts-location-geolocationmanager-getcurrentwifibssidforlocating-f.md) |
| [getDistanceBetweenLocations(位置服务)](arkts-location-geolocationmanager-getdistancebetweenlocations-f.md) |
| [getGeofenceSupportedCoordTypes(位置服务)](arkts-location-geolocationmanager-getgeofencesupportedcoordtypes-f.md) |
| [getLastLocation(位置服务)](arkts-location-geolocationmanager-getlastlocation-f.md) |
| [getPoiInfo(位置服务)](arkts-location-geolocationmanager-getpoiinfo-f.md) |
| [getPostProcessingTrack(位置服务)](arkts-location-geolocationmanager-getpostprocessingtrack-f.md) |
| [isBeaconFenceSupported(位置服务)](arkts-location-geolocationmanager-isbeaconfencesupported-f.md) |
| [isCachedGnssServiceSupported(位置服务)](arkts-location-geolocationmanager-iscachedgnssservicesupported-f.md) |
| [isGeocoderAvailable(位置服务)](arkts-location-geolocationmanager-isgeocoderavailable-f.md) |
| [isGnssFenceServiceSupported(位置服务)](arkts-location-geolocationmanager-isgnssfenceservicesupported-f.md) |
| [isGnssServiceSupported(位置服务)](arkts-location-geolocationmanager-isgnssservicesupported-f.md) |
| [isLocationEnabled(位置服务)](arkts-location-geolocationmanager-islocationenabled-f.md) |
| [isPoiServiceSupported(位置服务)](arkts-location-geolocationmanager-ispoiservicesupported-f.md) |
| [isWlanBssidMatched(位置服务)](arkts-location-geolocationmanager-iswlanbssidmatched-f.md) |
| [off(位置服务)](arkts-location-geolocationmanager-off-f.md#offlocationchange) |
| [off(位置服务)](arkts-location-geolocationmanager-off-f.md#offlocationerror) |
| [off(位置服务)](arkts-location-geolocationmanager-off-f.md#offlocationenabledchange) |
| [off(位置服务)](arkts-location-geolocationmanager-off-f.md#offcachedgnsslocationschange) |
| [off(位置服务)](arkts-location-geolocationmanager-off-f.md#offsatellitestatuschange) |
| [off(位置服务)](arkts-location-geolocationmanager-off-f.md#offnmeamessage) |
| [off(位置服务)](arkts-location-geolocationmanager-off-f.md#offgnssfencestatuschange) |
| [off(位置服务)](arkts-location-geolocationmanager-off-f.md#offcountrycodechange) |
| [off(位置服务)](arkts-location-geolocationmanager-off-f.md#offbluetoothscanresultchange) |
| [offLocationChange(位置服务)](arkts-location-geolocationmanager-offlocationchange-f.md) |
| [on(位置服务)](arkts-location-geolocationmanager-on-f.md#onlocationchange) |
| [on(位置服务)](arkts-location-geolocationmanager-on-f.md#onlocationerror) |
| [on(位置服务)](arkts-location-geolocationmanager-on-f.md#onlocationenabledchange) |
| [on(位置服务)](arkts-location-geolocationmanager-on-f.md#oncachedgnsslocationschange) |
| [on(位置服务)](arkts-location-geolocationmanager-on-f.md#onsatellitestatuschange) |
| [on(位置服务)](arkts-location-geolocationmanager-on-f.md#onnmeamessage) |
| [on(位置服务)](arkts-location-geolocationmanager-on-f.md#ongnssfencestatuschange) |
| [on(位置服务)](arkts-location-geolocationmanager-on-f.md#oncountrycodechange) |
| [on(位置服务)](arkts-location-geolocationmanager-on-f.md#onbluetoothscanresultchange) |
| [onLocationChange(位置服务)](arkts-location-geolocationmanager-onlocationchange-f.md) |
| [removeBeaconFence(位置服务)](arkts-location-geolocationmanager-removebeaconfence-f.md) |
| [removeGnssGeofence(位置服务)](arkts-location-geolocationmanager-removegnssgeofence-f.md) |
| [sendCommand(位置服务)](arkts-location-geolocationmanager-sendcommand-f.md) |
| [sendCommand(位置服务)](arkts-location-geolocationmanager-sendcommand-f.md) |
| [startBluetoothSearch(位置服务)](arkts-location-geolocationmanager-startbluetoothsearch-f.md) |
| [stopBluetoothSearch(位置服务)](arkts-location-geolocationmanager-stopbluetoothsearch-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addFusionFence(位置服务)](arkts-location-geolocationmanager-addfusionfence-f-sys.md) |
| [disableLocation(位置服务)](arkts-location-geolocationmanager-disablelocation-f-sys.md) |
| [disableLocationByUserId(位置服务)](arkts-location-geolocationmanager-disablelocationbyuserid-f-sys.md) |
| [disableLocationMock(位置服务)](arkts-location-geolocationmanager-disablelocationmock-f-sys.md) |
| [disableReverseGeocodingMock(位置服务)](arkts-location-geolocationmanager-disablereversegeocodingmock-f-sys.md) |
| [enableLocation(位置服务)](arkts-location-geolocationmanager-enablelocation-f-sys.md) |
| [enableLocation(位置服务)](arkts-location-geolocationmanager-enablelocation-f-sys.md) |
| [enableLocationByUserId(位置服务)](arkts-location-geolocationmanager-enablelocationbyuserid-f-sys.md) |
| [enableLocationMock(位置服务)](arkts-location-geolocationmanager-enablelocationmock-f-sys.md) |
| [enableReverseGeocodingMock(位置服务)](arkts-location-geolocationmanager-enablereversegeocodingmock-f-sys.md) |
| [getLocatingRequiredData(位置服务)](arkts-location-geolocationmanager-getlocatingrequireddata-f-sys.md) |
| [getLocationIconStatus(位置服务)](arkts-location-geolocationmanager-getlocationiconstatus-f-sys.md) |
| [isFusionFenceSupported(位置服务)](arkts-location-geolocationmanager-isfusionfencesupported-f-sys.md) |
| [isLocationEnabledByUserId(位置服务)](arkts-location-geolocationmanager-islocationenabledbyuserid-f-sys.md) |
| [isLocationPrivacyConfirmed(位置服务)](arkts-location-geolocationmanager-islocationprivacyconfirmed-f-sys.md) |
| off(位置服务) |
| off(位置服务) |
| on(位置服务) |
| on(位置服务) |
| [removeFusionFence(位置服务)](arkts-location-geolocationmanager-removefusionfence-f-sys.md) |
| [setLocationPrivacyConfirmStatus(位置服务)](arkts-location-geolocationmanager-setlocationprivacyconfirmstatus-f-sys.md) |
| [setLocationSwitchIgnored(位置服务)](arkts-location-geolocationmanager-setlocationswitchignored-f-sys.md) |
| [setMockedLocations(位置服务)](arkts-location-geolocationmanager-setmockedlocations-f-sys.md) |
| [setReverseGeocodingMockInfo(位置服务)](arkts-location-geolocationmanager-setreversegeocodingmockinfo-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [BeaconFence(位置服务)](arkts-location-geolocationmanager-beaconfence-i.md) |
| [BeaconFenceRequest(位置服务)](arkts-location-geolocationmanager-beaconfencerequest-i.md) |
| [BeaconManufactureData(位置服务)](arkts-location-geolocationmanager-beaconmanufacturedata-i.md) |
| [BluetoothScanResult(位置服务)](arkts-location-geolocationmanager-bluetoothscanresult-i.md) |
| [BluetoothSearchRequestParams(位置服务)](arkts-location-geolocationmanager-bluetoothsearchrequestparams-i.md) |
| [CachedGnssLocationsRequest(位置服务)](arkts-location-geolocationmanager-cachedgnsslocationsrequest-i.md) |
| [ContinuousLocationRequest(位置服务)](arkts-location-geolocationmanager-continuouslocationrequest-i.md) |
| [CountryCode(位置服务)](arkts-location-geolocationmanager-countrycode-i.md) |
| [CurrentLocationRequest(位置服务)](arkts-location-geolocationmanager-currentlocationrequest-i.md) |
| [DistrictInfo(位置服务)](arkts-location-geolocationmanager-districtinfo-i.md) |
| [DistrictRequestParams(位置服务)](arkts-location-geolocationmanager-districtrequestparams-i.md) |
| [GeoAddress(位置服务)](arkts-location-geolocationmanager-geoaddress-i.md) |
| [GeoCodeRequest(位置服务)](arkts-location-geolocationmanager-geocoderequest-i.md) |
| [Geofence(位置服务)](arkts-location-geolocationmanager-geofence-i.md) |
| [GeofenceRequest(位置服务)](arkts-location-geolocationmanager-geofencerequest-i.md) |
| [GeofenceTransition(位置服务)](arkts-location-geolocationmanager-geofencetransition-i.md) |
| [GnssGeofenceRequest(位置服务)](arkts-location-geolocationmanager-gnssgeofencerequest-i.md) |
| [Location(位置服务)](arkts-location-geolocationmanager-location-i.md) |
| [LocationCommand(位置服务)](arkts-location-geolocationmanager-locationcommand-i.md) |
| [LocationRequest(位置服务)](arkts-location-geolocationmanager-locationrequest-i.md) |
| [MatchingWlanInfo(位置服务)](arkts-location-geolocationmanager-matchingwlaninfo-i.md) |
| [Poi(位置服务)](arkts-location-geolocationmanager-poi-i.md) |
| [PoiInfo(位置服务)](arkts-location-geolocationmanager-poiinfo-i.md) |
| [Point(位置服务)](arkts-location-geolocationmanager-point-i.md) |
| [ReverseGeoCodeRequest(位置服务)](arkts-location-geolocationmanager-reversegeocoderequest-i.md) |
| [SatelliteStatusInfo(位置服务)](arkts-location-geolocationmanager-satellitestatusinfo-i.md) |
| [SingleLocationRequest(位置服务)](arkts-location-geolocationmanager-singlelocationrequest-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [BluetoothScanInfo(位置服务)](arkts-location-geolocationmanager-bluetoothscaninfo-i-sys.md) |
| [CellFence(位置服务)](arkts-location-geolocationmanager-cellfence-i-sys.md) |
| [CellInfo(位置服务)](arkts-location-geolocationmanager-cellinfo-i-sys.md) |
| [FusionFenceRequestParams(位置服务)](arkts-location-geolocationmanager-fusionfencerequestparams-i-sys.md) |
| [FusionFenceTransition(位置服务)](arkts-location-geolocationmanager-fusionfencetransition-i-sys.md) |
| [GeoAddress(位置服务)](arkts-location-geolocationmanager-geoaddress-i-sys.md) |
| [GnssFence(位置服务)](arkts-location-geolocationmanager-gnssfence-i-sys.md) |
| [LocatingRequiredData(位置服务)](arkts-location-geolocationmanager-locatingrequireddata-i-sys.md) |
| [LocatingRequiredDataConfig(位置服务)](arkts-location-geolocationmanager-locatingrequireddataconfig-i-sys.md) |
| [LocationMockConfig(位置服务)](arkts-location-geolocationmanager-locationmockconfig-i-sys.md) |
| [ReverseGeocodingMockInfo(位置服务)](arkts-location-geolocationmanager-reversegeocodingmockinfo-i-sys.md) |
| [WifiFence(位置服务)](arkts-location-geolocationmanager-wififence-i-sys.md) |
| [WifiScanInfo(位置服务)](arkts-location-geolocationmanager-wifiscaninfo-i-sys.md) |
| [WirelessSignalFeature(位置服务)](arkts-location-geolocationmanager-wirelesssignalfeature-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [BeaconFenceInfoType(位置服务)](arkts-location-geolocationmanager-beaconfenceinfotype-e.md) |
| [CoordinateSystemType(位置服务)](arkts-location-geolocationmanager-coordinatesystemtype-e.md) |
| [CountryCodeType(位置服务)](arkts-location-geolocationmanager-countrycodetype-e.md) |
| [GeofenceTransitionEvent(位置服务)](arkts-location-geolocationmanager-geofencetransitionevent-e.md) |
| [LocatingPriority(位置服务)](arkts-location-geolocationmanager-locatingpriority-e.md) |
| [LocationError(位置服务)](arkts-location-geolocationmanager-locationerror-e.md) |
| [LocationRequestPriority(位置服务)](arkts-location-geolocationmanager-locationrequestpriority-e.md) |
| [LocationRequestScenario(位置服务)](arkts-location-geolocationmanager-locationrequestscenario-e.md) |
| [LocationSourceType(位置服务)](arkts-location-geolocationmanager-locationsourcetype-e.md) |
| [PowerConsumptionScenario(位置服务)](arkts-location-geolocationmanager-powerconsumptionscenario-e.md) |
| [SatelliteAdditionalInfo(位置服务)](arkts-location-geolocationmanager-satelliteadditionalinfo-e.md) |
| [SatelliteConstellationCategory(位置服务)](arkts-location-geolocationmanager-satelliteconstellationcategory-e.md) |
| [SportsType(位置服务)](arkts-location-geolocationmanager-sportstype-e.md) |
| [UserActivityScenario(位置服务)](arkts-location-geolocationmanager-useractivityscenario-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [FusionFenceScene(位置服务)](arkts-location-geolocationmanager-fusionfencescene-e-sys.md) |
| [FusionFenceType(位置服务)](arkts-location-geolocationmanager-fusionfencetype-e-sys.md) |
| [GeofenceTransitionEvent(位置服务)](arkts-location-geolocationmanager-geofencetransitionevent-e-sys.md) |
| [GnssFenceType(位置服务)](arkts-location-geolocationmanager-gnssfencetype-e-sys.md) |
| [LocatingRequiredDataType(位置服务)](arkts-location-geolocationmanager-locatingrequireddatatype-e-sys.md) |
| [LocationIconStatus(位置服务)](arkts-location-geolocationmanager-locationiconstatus-e-sys.md) |
| [LocationPrivacyType(位置服务)](arkts-location-geolocationmanager-locationprivacytype-e-sys.md) |
| [WifiFingerprintType(位置服务)](arkts-location-geolocationmanager-wififingerprinttype-e-sys.md) |
<!--DelEnd-->
