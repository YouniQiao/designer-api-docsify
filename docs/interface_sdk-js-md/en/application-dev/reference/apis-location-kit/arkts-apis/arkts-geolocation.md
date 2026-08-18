# @ohos.geolocation

Provides interfaces for initiating location requests, ending the location service, and obtaining the location result cached by the system.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [geoLocationManager](arkts-geolocationmanager.md)

**Required permissions:** ohos.permission.LOCATION

<!--Device-unnamed-declare namespace geolocation--><!--Device-unnamed-declare namespace geolocation-End-->

**System capability:** SystemCapability.Location.Location.Core

## Modules to Import

```TypeScript
import { geolocation } from '@kit.LocationKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [flushCachedGnssLocations](arkts-location-geolocation-flushcachedgnsslocations-f.md) | All prepared GNSS locations are returned to the application through the callback function, and the bottom-layer buffer is cleared. |
| [flushCachedGnssLocations](arkts-location-geolocation-flushcachedgnsslocations-f.md) | All prepared GNSS locations are returned to the application through the callback function, and the bottom-layer buffer is cleared. |
| [getAddressesFromLocation](arkts-location-geolocation-getaddressesfromlocation-f.md) | Obtain address info from location |
| [getAddressesFromLocation](arkts-location-geolocation-getaddressesfromlocation-f.md) | Obtain address info from location |
| [getAddressesFromLocationName](arkts-location-geolocation-getaddressesfromlocationname-f.md) | Obtain latitude and longitude info from location address |
| [getAddressesFromLocationName](arkts-location-geolocation-getaddressesfromlocationname-f.md) | Obtain latitude and longitude info from location address |
| [getCachedGnssLocationsSize](arkts-location-geolocation-getcachedgnsslocationssize-f.md) | Obtain the number of cached GNSS locations reported at a time |
| [getCachedGnssLocationsSize](arkts-location-geolocation-getcachedgnsslocationssize-f.md) | Obtain the number of cached GNSS locations reported at a time |
| [getCurrentLocation](arkts-location-geolocation-getcurrentlocation-f.md) | Obtain current location |
| [getCurrentLocation](arkts-location-geolocation-getcurrentlocation-f.md) | Obtain current location |
| [getCurrentLocation](arkts-location-geolocation-getcurrentlocation-f.md) | Obtain current location |
| [getLastLocation](arkts-location-geolocation-getlastlocation-f.md) | Obtain last known location |
| [getLastLocation](arkts-location-geolocation-getlastlocation-f.md) | Obtain last known location |
| [isGeoServiceAvailable](arkts-location-geolocation-isgeoserviceavailable-f.md) | Obtain geocode service status |
| [isGeoServiceAvailable](arkts-location-geolocation-isgeoserviceavailable-f.md) | Obtain geocode service status |
| [isLocationEnabled](arkts-location-geolocation-islocationenabled-f.md) | Obtain current location switch status |
| [isLocationEnabled](arkts-location-geolocation-islocationenabled-f.md) | Obtain current location switch status |
| [off_cachedGnssLocationsReporting](arkts-location-geolocation-offcachedgnsslocationsreporting-f.md#off_cachedgnsslocationsreportingcachedgnsslocationsreporting) | Unsubscribe to cache GNSS locations update messages |
| [off_fenceStatusChange](arkts-location-geolocation-offfencestatuschange-f.md#off_fencestatuschangefencestatuschange) | Remove a geofence and unsubscribe geo fence status changed |
| [off_gnssStatusChange](arkts-location-geolocation-offgnssstatuschange-f.md#off_gnssstatuschangegnssstatuschange) | Unsubscribe gnss status changed |
| [off_locationChange](arkts-location-geolocation-offlocationchange-f.md#off_locationchangelocationchange) | Unsubscribe location changed |
| [off_locationServiceState](arkts-location-geolocation-offlocationservicestate-f.md#off_locationservicestatelocationservicestate) | Unsubscribe location switch changed |
| [off_nmeaMessageChange](arkts-location-geolocation-offnmeamessagechange-f.md#off_nmeamessagechangenmeamessagechange) | Unsubscribe nmea message changed |
| [on_cachedGnssLocationsReporting](arkts-location-geolocation-oncachedgnsslocationsreporting-f.md#on_cachedgnsslocationsreportingcachedgnsslocationsreporting) | Subscribe to cache GNSS locations update messages |
| [on_fenceStatusChange](arkts-location-geolocation-onfencestatuschange-f.md#on_fencestatuschangefencestatuschange) | Add a geofence and subscribe geo fence status changed |
| [on_gnssStatusChange](arkts-location-geolocation-ongnssstatuschange-f.md#on_gnssstatuschangegnssstatuschange) | Subscribe gnss status changed |
| [on_locationChange](arkts-location-geolocation-onlocationchange-f.md#on_locationchangelocationchange) | Subscribe location changed |
| [on_locationServiceState](arkts-location-geolocation-onlocationservicestate-f.md#on_locationservicestatelocationservicestate) | Subscribe location switch changed |
| [on_nmeaMessageChange](arkts-location-geolocation-onnmeamessagechange-f.md#on_nmeamessagechangenmeamessagechange) | Subscribe nmea message changed |
| [requestEnableLocation](arkts-location-geolocation-requestenablelocation-f.md) | Request enable location |
| [requestEnableLocation](arkts-location-geolocation-requestenablelocation-f.md) | Request enable location |
| [sendCommand](arkts-location-geolocation-sendcommand-f.md) | Send extended commands to location subsystem. |
| [sendCommand](arkts-location-geolocation-sendcommand-f.md) | Send extended commands to location subsystem. |

### Interfaces

| Name | Description |
| --- | --- |
| [CachedGnssLocationsRequest](arkts-location-geolocation-cachedgnsslocationsrequest-i.md) | Parameters for requesting to report cache location information |
| [CurrentLocationRequest](arkts-location-geolocation-currentlocationrequest-i.md) | Configuring parameters in current location requests |
| [GeoAddress](arkts-location-geolocation-geoaddress-i.md) | Data struct describes geographic locations. |
| [GeoCodeRequest](arkts-location-geolocation-geocoderequest-i.md) | Configuring parameters in geocode requests |
| [Geofence](arkts-location-geolocation-geofence-i.md) | Circular fence information. |
| [GeofenceRequest](arkts-location-geolocation-geofencerequest-i.md) | Configuring parameters in geo fence requests |
| [Location](arkts-location-geolocation-location-i.md) | Provides information about geographic locations |
| [LocationCommand](arkts-location-geolocation-locationcommand-i.md) | Location subsystem command structure |
| [LocationRequest](arkts-location-geolocation-locationrequest-i.md) | Configuring parameters in location requests |
| [ReverseGeoCodeRequest](arkts-location-geolocation-reversegeocoderequest-i.md) | Configuring parameters in reverse geocode requests |
| [SatelliteStatusInfo](arkts-location-geolocation-satellitestatusinfo-i.md) | Satellite status information |

### Enums

| Name | Description |
| --- | --- |
| [GeoLocationErrorCode](arkts-location-geolocation-geolocationerrorcode-e.md) | Enum for error code |
| [LocationPrivacyType](arkts-location-geolocation-locationprivacytype-e.md) | Enum for location privacy type |
| [LocationRequestPriority](arkts-location-geolocation-locationrequestpriority-e.md) | Enum for location priority |
| [LocationRequestScenario](arkts-location-geolocation-locationrequestscenario-e.md) | Enum for location scenario |

