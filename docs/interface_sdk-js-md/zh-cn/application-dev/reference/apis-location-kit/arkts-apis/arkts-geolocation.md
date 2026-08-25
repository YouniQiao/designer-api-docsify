# @ohos.geolocation

位置服务提供GNSS定位、网络定位、地理编码、逆地理编码、国家码和地理围栏等基本功能。@namespace geolocation

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [geoLocationManager](arkts-geolocationmanager.md)

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Core

## 导入模块

```TypeScript
import { geolocation } from 'kits/@kit.LocationKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [flushCachedGnssLocations](arkts-location-geolocation-flushcachedgnsslocations-f.md) |
| [flushCachedGnssLocations](arkts-location-geolocation-flushcachedgnsslocations-f.md) |
| [getAddressesFromLocation](arkts-location-geolocation-getaddressesfromlocation-f.md) |
| [getAddressesFromLocation](arkts-location-geolocation-getaddressesfromlocation-f.md) |
| [getAddressesFromLocationName](arkts-location-geolocation-getaddressesfromlocationname-f.md) |
| [getAddressesFromLocationName](arkts-location-geolocation-getaddressesfromlocationname-f.md) |
| [getCachedGnssLocationsSize](arkts-location-geolocation-getcachedgnsslocationssize-f.md) |
| [getCachedGnssLocationsSize](arkts-location-geolocation-getcachedgnsslocationssize-f.md) |
| [getCurrentLocation](arkts-location-geolocation-getcurrentlocation-f.md) |
| [getCurrentLocation](arkts-location-geolocation-getcurrentlocation-f.md) |
| [getCurrentLocation](arkts-location-geolocation-getcurrentlocation-f.md) |
| [getLastLocation](arkts-location-geolocation-getlastlocation-f.md) |
| [getLastLocation](arkts-location-geolocation-getlastlocation-f.md) |
| [isGeoServiceAvailable](arkts-location-geolocation-isgeoserviceavailable-f.md) |
| [isGeoServiceAvailable](arkts-location-geolocation-isgeoserviceavailable-f.md) |
| [isLocationEnabled](arkts-location-geolocation-islocationenabled-f.md) |
| [isLocationEnabled](arkts-location-geolocation-islocationenabled-f.md) |
| [off](arkts-location-geolocation-off-f.md#offlocationchange) |
| [off](arkts-location-geolocation-off-f.md#offlocationservicestate) |
| [off](arkts-location-geolocation-off-f.md#offcachedgnsslocationsreporting) |
| [off](arkts-location-geolocation-off-f.md#offgnssstatuschange) |
| [off](arkts-location-geolocation-off-f.md#offnmeamessagechange) |
| [off](arkts-location-geolocation-off-f.md#offfencestatuschange) |
| [on](arkts-location-geolocation-on-f.md#onlocationchange) |
| [on](arkts-location-geolocation-on-f.md#onlocationservicestate) |
| [on](arkts-location-geolocation-on-f.md#oncachedgnsslocationsreporting) |
| [on](arkts-location-geolocation-on-f.md#ongnssstatuschange) |
| [on](arkts-location-geolocation-on-f.md#onnmeamessagechange) |
| [on](arkts-location-geolocation-on-f.md#onfencestatuschange) |
| [requestEnableLocation](arkts-location-geolocation-requestenablelocation-f.md) |
| [requestEnableLocation](arkts-location-geolocation-requestenablelocation-f.md) |
| [sendCommand](arkts-location-geolocation-sendcommand-f.md) |
| [sendCommand](arkts-location-geolocation-sendcommand-f.md) |

### 接口

| 名称 |
| --- |
| [CachedGnssLocationsRequest](arkts-location-geolocation-cachedgnsslocationsrequest-i.md) |
| [CurrentLocationRequest](arkts-location-geolocation-currentlocationrequest-i.md) |
| [GeoAddress](arkts-location-geolocation-geoaddress-i.md) |
| [GeoCodeRequest](arkts-location-geolocation-geocoderequest-i.md) |
| [Geofence](arkts-location-geolocation-geofence-i.md) |
| [GeofenceRequest](arkts-location-geolocation-geofencerequest-i.md) |
| [Location](arkts-location-geolocation-location-i.md) |
| [LocationCommand](arkts-location-geolocation-locationcommand-i.md) |
| [LocationRequest](arkts-location-geolocation-locationrequest-i.md) |
| [ReverseGeoCodeRequest](arkts-location-geolocation-reversegeocoderequest-i.md) |
| [SatelliteStatusInfo](arkts-location-geolocation-satellitestatusinfo-i.md) |

### 枚举

| 名称 |
| --- |
| [GeoLocationErrorCode](arkts-location-geolocation-geolocationerrorcode-e.md) |
| [LocationPrivacyType](arkts-location-geolocation-locationprivacytype-e.md) |
| [LocationRequestPriority](arkts-location-geolocation-locationrequestpriority-e.md) |
| [LocationRequestScenario](arkts-location-geolocation-locationrequestscenario-e.md) |
