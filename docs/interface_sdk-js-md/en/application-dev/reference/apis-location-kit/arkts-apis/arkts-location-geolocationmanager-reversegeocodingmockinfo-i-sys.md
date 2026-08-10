# ReverseGeocodingMockInfo (System API)

Configuration parameters for simulating reverse geocoding.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-geoLocationManager-export interface ReverseGeocodingMockInfo--><!--Device-geoLocationManager-export interface ReverseGeocodingMockInfo-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## geoAddress

```TypeScript
geoAddress: GeoAddress
```

Actual address information corresponding to the location.

**Type:** [GeoAddress](arkts-location-geolocationmanager-geoaddress-i-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ReverseGeocodingMockInfo-geoAddress: GeoAddress--><!--Device-ReverseGeocodingMockInfo-geoAddress: GeoAddress-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

## location

```TypeScript
location: ReverseGeoCodeRequest
```

Location for which reverse geocoding query is required.

**Type:** [ReverseGeoCodeRequest](arkts-location-geolocation-reversegeocoderequest-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ReverseGeocodingMockInfo-location: ReverseGeoCodeRequest--><!--Device-ReverseGeocodingMockInfo-location: ReverseGeoCodeRequest-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

