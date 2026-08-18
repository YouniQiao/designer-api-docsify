# @ohos.geolocation

Provides interfaces for initiating location requests, ending the location service, and obtaining the location result cached by the system.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [geoLocationManager](arkts-geolocationmanager.md#ohosgeolocationmanager)

**Required permissions:** ohos.permission.LOCATION

<!--Device-unnamed-declare namespace geolocation--><!--Device-unnamed-declare namespace geolocation-End-->

**System capability:** SystemCapability.Location.Location.Core

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [flushCachedGnssLocations](arkts-location-geolocation-flushcachedgnsslocations-f.md#flushcachedgnsslocations) |
| [flushCachedGnssLocations](arkts-location-geolocation-flushcachedgnsslocations-f.md#flushcachedgnsslocations) |
| [getAddressesFromLocation](arkts-location-geolocation-getaddressesfromlocation-f.md#getaddressesfromlocation) |
| [getAddressesFromLocation](arkts-location-geolocation-getaddressesfromlocation-f.md#getaddressesfromlocation) |
| [getAddressesFromLocationName](arkts-location-geolocation-getaddressesfromlocationname-f.md#getaddressesfromlocationname) |
| [getAddressesFromLocationName](arkts-location-geolocation-getaddressesfromlocationname-f.md#getaddressesfromlocationname) |
| [getCachedGnssLocationsSize](arkts-location-geolocation-getcachedgnsslocationssize-f.md#getcachedgnsslocationssize) |
| [getCachedGnssLocationsSize](arkts-location-geolocation-getcachedgnsslocationssize-f.md#getcachedgnsslocationssize) |
| [getCurrentLocation](arkts-location-geolocation-getcurrentlocation-f.md#getcurrentlocation) |
| [getCurrentLocation](arkts-location-geolocation-getcurrentlocation-f.md#getcurrentlocation) |
| [getCurrentLocation](arkts-location-geolocation-getcurrentlocation-f.md#getcurrentlocation) |
| [getLastLocation](arkts-location-geolocation-getlastlocation-f.md#getlastlocation) |
| [getLastLocation](arkts-location-geolocation-getlastlocation-f.md#getlastlocation) |
| [isGeoServiceAvailable](arkts-location-geolocation-isgeoserviceavailable-f.md#isgeoserviceavailable) |
| [isGeoServiceAvailable](arkts-location-geolocation-isgeoserviceavailable-f.md#isgeoserviceavailable) |
| [isLocationEnabled](arkts-location-geolocation-islocationenabled-f.md#islocationenabled) |
| [isLocationEnabled](arkts-location-geolocation-islocationenabled-f.md#islocationenabled) |
| [off_cachedGnssLocationsReporting](arkts-location-geolocation-offcachedgnsslocationsreporting-f.md#offcachedgnsslocationsreporting) |
| [off_fenceStatusChange](arkts-location-geolocation-offfencestatuschange-f.md#offfencestatuschange) |
| [off_gnssStatusChange](arkts-location-geolocation-offgnssstatuschange-f.md#offgnssstatuschange) |
| [off_locationChange](arkts-location-geolocation-offlocationchange-f.md#offlocationchange) |
| [off_locationServiceState](arkts-location-geolocation-offlocationservicestate-f.md#offlocationservicestate) |
| [off_nmeaMessageChange](arkts-location-geolocation-offnmeamessagechange-f.md#offnmeamessagechange) |
| [on_cachedGnssLocationsReporting](arkts-location-geolocation-oncachedgnsslocationsreporting-f.md#oncachedgnsslocationsreporting) |
| [on_fenceStatusChange](arkts-location-geolocation-onfencestatuschange-f.md#onfencestatuschange) |
| [on_gnssStatusChange](arkts-location-geolocation-ongnssstatuschange-f.md#ongnssstatuschange) |
| [on_locationChange](arkts-location-geolocation-onlocationchange-f.md#onlocationchange) |
| [on_locationServiceState](arkts-location-geolocation-onlocationservicestate-f.md#onlocationservicestate) |
| [on_nmeaMessageChange](arkts-location-geolocation-onnmeamessagechange-f.md#onnmeamessagechange) |
| [requestEnableLocation](arkts-location-geolocation-requestenablelocation-f.md#requestenablelocation) |
| [requestEnableLocation](arkts-location-geolocation-requestenablelocation-f.md#requestenablelocation) |
| [sendCommand](arkts-location-geolocation-sendcommand-f.md#sendcommand) |
| [sendCommand](arkts-location-geolocation-sendcommand-f.md#sendcommand) |

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
