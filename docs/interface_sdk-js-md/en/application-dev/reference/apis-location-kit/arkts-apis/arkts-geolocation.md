# @ohos.geolocation

Provides interfaces for initiating location requests, ending the location service, and obtaining the location result cached by the system.@namespace geolocation

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** [geoLocationManager](arkts-geolocationmanager.md)

**Required permissions:** ohos.permission.LOCATION

**System capability:** SystemCapability.Location.Location.Core

## Modules to Import

```TypeScript
import { geolocation } from '@kit.LocationKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [GeoLocationErrorCode](arkts-location-geolocation-geolocationerrorcode-e.md) |
| [LocationPrivacyType](arkts-location-geolocation-locationprivacytype-e.md) |
| [LocationRequestPriority](arkts-location-geolocation-locationrequestpriority-e.md) |
| [LocationRequestScenario](arkts-location-geolocation-locationrequestscenario-e.md) |
