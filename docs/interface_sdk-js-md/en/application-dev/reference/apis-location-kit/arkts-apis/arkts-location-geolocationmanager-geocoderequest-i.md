# GeoCodeRequest

Configuring parameters in geocode requests.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-geoLocationManager-export interface GeoCodeRequest--><!--Device-geoLocationManager-export interface GeoCodeRequest-End-->

**System capability:** SystemCapability.Location.Location.Geocoder

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## country

```TypeScript
country?: string
```

Indicates the country information.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-GeoCodeRequest-country?: string--><!--Device-GeoCodeRequest-country?: string-End-->

**System capability:** SystemCapability.Location.Location.Geocoder

## description

```TypeScript
description: string
```

Address information.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-GeoCodeRequest-description: string--><!--Device-GeoCodeRequest-description: string-End-->

**System capability:** SystemCapability.Location.Location.Geocoder

## locale

```TypeScript
locale?: string
```

Indicates the language area information.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-GeoCodeRequest-locale?: string--><!--Device-GeoCodeRequest-locale?: string-End-->

**System capability:** SystemCapability.Location.Location.Geocoder

## maxItems

```TypeScript
maxItems?: int
```

Indicates the maximum number of geocode query results.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-GeoCodeRequest-maxItems?: int--><!--Device-GeoCodeRequest-maxItems?: int-End-->

**System capability:** SystemCapability.Location.Location.Geocoder

## maxLatitude

```TypeScript
maxLatitude?: double
```

Indicates the maximum latitude for geocoding query results.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-GeoCodeRequest-maxLatitude?: double--><!--Device-GeoCodeRequest-maxLatitude?: double-End-->

**System capability:** SystemCapability.Location.Location.Geocoder

## maxLongitude

```TypeScript
maxLongitude?: double
```

Indicates the maximum longitude for geocoding query results.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-GeoCodeRequest-maxLongitude?: double--><!--Device-GeoCodeRequest-maxLongitude?: double-End-->

**System capability:** SystemCapability.Location.Location.Geocoder

## minLatitude

```TypeScript
minLatitude?: double
```

Indicates the minimum latitude for geocoding query results.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-GeoCodeRequest-minLatitude?: double--><!--Device-GeoCodeRequest-minLatitude?: double-End-->

**System capability:** SystemCapability.Location.Location.Geocoder

## minLongitude

```TypeScript
minLongitude?: double
```

Indicates the minimum longitude for geocoding query results.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-GeoCodeRequest-minLongitude?: double--><!--Device-GeoCodeRequest-minLongitude?: double-End-->

**System capability:** SystemCapability.Location.Location.Geocoder

