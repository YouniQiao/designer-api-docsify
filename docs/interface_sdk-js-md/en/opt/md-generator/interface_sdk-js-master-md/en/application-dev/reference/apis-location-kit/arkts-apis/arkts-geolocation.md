# @ohos.geolocation

Provides interfaces for initiating location requests, ending the location service, and obtaining the location result cached by the system.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [geoLocationManager](arkts-geolocationmanager.md#@ohos.geoLocationManager)

**Required permissions:** ohos.permission.LOCATION

<!--Device-unnamed-declare namespace geolocation--><!--Device-unnamed-declare namespace geolocation-End-->

**System capability:** SystemCapability.Location.Location.Core

## Modules to Import

```TypeScript
import { geolocation } from '@kit.LocationKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [flushCachedGnssLocations](arkts-location-geolocation-flushcachedgnsslocations-f.md#flushCachedGnssLocations) |
| [flushCachedGnssLocations](arkts-location-geolocation-flushcachedgnsslocations-f.md#flushCachedGnssLocations) |
| [getAddressesFromLocation](arkts-location-geolocation-getaddressesfromlocation-f.md#getAddressesFromLocation) |
| [getAddressesFromLocation](arkts-location-geolocation-getaddressesfromlocation-f.md#getAddressesFromLocation) |
| [getAddressesFromLocationName](arkts-location-geolocation-getaddressesfromlocationname-f.md#getAddressesFromLocationName) |
| [getAddressesFromLocationName](arkts-location-geolocation-getaddressesfromlocationname-f.md#getAddressesFromLocationName) |
| [getCachedGnssLocationsSize](arkts-location-geolocation-getcachedgnsslocationssize-f.md#getCachedGnssLocationsSize) |
| [getCachedGnssLocationsSize](arkts-location-geolocation-getcachedgnsslocationssize-f.md#getCachedGnssLocationsSize) |
| [getCurrentLocation](arkts-location-geolocation-getcurrentlocation-f.md#getCurrentLocation) |
| [getCurrentLocation](arkts-location-geolocation-getcurrentlocation-f.md#getCurrentLocation) |
| [getCurrentLocation](arkts-location-geolocation-getcurrentlocation-f.md#getCurrentLocation) |
| [getLastLocation](arkts-location-geolocation-getlastlocation-f.md#getLastLocation) |
| [getLastLocation](arkts-location-geolocation-getlastlocation-f.md#getLastLocation) |
| [isGeoServiceAvailable](arkts-location-geolocation-isgeoserviceavailable-f.md#isGeoServiceAvailable) |
| [isGeoServiceAvailable](arkts-location-geolocation-isgeoserviceavailable-f.md#isGeoServiceAvailable) |
| [isLocationEnabled](arkts-location-geolocation-islocationenabled-f.md#isLocationEnabled) |
| [isLocationEnabled](arkts-location-geolocation-islocationenabled-f.md#isLocationEnabled) |
| [off_cachedGnssLocationsReporting](arkts-location-geolocation-offcachedgnsslocationsreporting-f.md#off_cachedGnssLocationsReporting) |
| [off_fenceStatusChange](arkts-location-geolocation-offfencestatuschange-f.md#off_fenceStatusChange) |
| [off_gnssStatusChange](arkts-location-geolocation-offgnssstatuschange-f.md#off_gnssStatusChange) |
| [off_locationChange](arkts-location-geolocation-offlocationchange-f.md#off_locationChange) |
| [off_locationServiceState](arkts-location-geolocation-offlocationservicestate-f.md#off_locationServiceState) |
| [off_nmeaMessageChange](arkts-location-geolocation-offnmeamessagechange-f.md#off_nmeaMessageChange) |
| [on_cachedGnssLocationsReporting](arkts-location-geolocation-oncachedgnsslocationsreporting-f.md#on_cachedGnssLocationsReporting) |
| [on_fenceStatusChange](arkts-location-geolocation-onfencestatuschange-f.md#on_fenceStatusChange) |
| [on_gnssStatusChange](arkts-location-geolocation-ongnssstatuschange-f.md#on_gnssStatusChange) |
| [on_locationChange](arkts-location-geolocation-onlocationchange-f.md#on_locationChange) |
| [on_locationServiceState](arkts-location-geolocation-onlocationservicestate-f.md#on_locationServiceState) |
| [on_nmeaMessageChange](arkts-location-geolocation-onnmeamessagechange-f.md#on_nmeaMessageChange) |
| [requestEnableLocation](arkts-location-geolocation-requestenablelocation-f.md#requestEnableLocation) |
| [requestEnableLocation](arkts-location-geolocation-requestenablelocation-f.md#requestEnableLocation) |
| [sendCommand](arkts-location-geolocation-sendcommand-f.md#sendCommand) |
| [sendCommand](arkts-location-geolocation-sendcommand-f.md#sendCommand) |

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
