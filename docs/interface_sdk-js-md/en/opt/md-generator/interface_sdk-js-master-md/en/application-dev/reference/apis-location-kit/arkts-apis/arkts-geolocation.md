# @ohos.geolocation

Provides interfaces for initiating location requests, ending the location service,and obtaining the location result cached by the system.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.geoLocationManager

**Required permissions:** ohos.permission.LOCATION

<!--Device-unnamed-declare namespace geolocation--><!--Device-unnamed-declare namespace geolocation-End-->

**System capability:** SystemCapability.Location.Location.Core

## Modules to Import

```TypeScript
import { geolocation } from 'kits/@kit.LocationKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [flushCachedGnssLocations](arkts-location-geolocation-flushcachedgnsslocations-f.md#flushcachedgnsslocations) |
| [flushCachedGnssLocations](arkts-location-geolocation-flushcachedgnsslocations-f.md#flushcachedgnsslocations-1) |
| [getAddressesFromLocation](arkts-location-geolocation-getaddressesfromlocation-f.md#getaddressesfromlocation) |
| [getAddressesFromLocation](arkts-location-geolocation-getaddressesfromlocation-f.md#getaddressesfromlocation-1) |
| [getAddressesFromLocationName](arkts-location-geolocation-getaddressesfromlocationname-f.md#getaddressesfromlocationname) |
| [getAddressesFromLocationName](arkts-location-geolocation-getaddressesfromlocationname-f.md#getaddressesfromlocationname-1) |
| [getCachedGnssLocationsSize](arkts-location-geolocation-getcachedgnsslocationssize-f.md#getcachedgnsslocationssize) |
| [getCachedGnssLocationsSize](arkts-location-geolocation-getcachedgnsslocationssize-f.md#getcachedgnsslocationssize-1) |
| [getCurrentLocation](arkts-location-geolocation-getcurrentlocation-f.md#getcurrentlocation) |
| [getCurrentLocation](arkts-location-geolocation-getcurrentlocation-f.md#getcurrentlocation-1) |
| [getCurrentLocation](arkts-location-geolocation-getcurrentlocation-f.md#getcurrentlocation-2) |
| [getLastLocation](arkts-location-geolocation-getlastlocation-f.md#getlastlocation) |
| [getLastLocation](arkts-location-geolocation-getlastlocation-f.md#getlastlocation-1) |
| [isGeoServiceAvailable](arkts-location-geolocation-isgeoserviceavailable-f.md#isgeoserviceavailable) |
| [isGeoServiceAvailable](arkts-location-geolocation-isgeoserviceavailable-f.md#isgeoserviceavailable-1) |
| [isLocationEnabled](arkts-location-geolocation-islocationenabled-f.md#islocationenabled) |
| [isLocationEnabled](arkts-location-geolocation-islocationenabled-f.md#islocationenabled-1) |
| [off](arkts-location-geolocation-off-f.md#off) |
| [off](arkts-location-geolocation-off-f.md#off-1) |
| [off](arkts-location-geolocation-off-f.md#off-2) |
| [off](arkts-location-geolocation-off-f.md#off-3) |
| [off](arkts-location-geolocation-off-f.md#off-4) |
| [off](arkts-location-geolocation-off-f.md#off-5) |
| [on](arkts-location-geolocation-on-f.md#on) |
| [on](arkts-location-geolocation-on-f.md#on-1) |
| [on](arkts-location-geolocation-on-f.md#on-2) |
| [on](arkts-location-geolocation-on-f.md#on-3) |
| [on](arkts-location-geolocation-on-f.md#on-4) |
| [on](arkts-location-geolocation-on-f.md#on-5) |
| [requestEnableLocation](arkts-location-geolocation-requestenablelocation-f.md#requestenablelocation) |
| [requestEnableLocation](arkts-location-geolocation-requestenablelocation-f.md#requestenablelocation-1) |
| [sendCommand](arkts-location-geolocation-sendcommand-f.md#sendcommand) |
| [sendCommand](arkts-location-geolocation-sendcommand-f.md#sendcommand-1) |

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
