# GeoCodeRequest

Configuring parameters in geocode requests.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-export interface GeoCodeRequest--><!--Device-geoLocationManager-export interface GeoCodeRequest-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## country

```TypeScript
country?: string
```

Indicates the country information.

**类型：** string

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-GeoCodeRequest-country?: string--><!--Device-GeoCodeRequest-country?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## description

```TypeScript
description: string
```

Address information.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoCodeRequest-description: string--><!--Device-GeoCodeRequest-description: string-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## locale

```TypeScript
locale?: string
```

Indicates the language area information.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoCodeRequest-locale?: string--><!--Device-GeoCodeRequest-locale?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## maxItems

```TypeScript
maxItems?: int
```

Indicates the maximum number of geocode query results.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoCodeRequest-maxItems?: int--><!--Device-GeoCodeRequest-maxItems?: int-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## maxLatitude

```TypeScript
maxLatitude?: double
```

Indicates the maximum latitude for geocoding query results.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoCodeRequest-maxLatitude?: double--><!--Device-GeoCodeRequest-maxLatitude?: double-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## maxLongitude

```TypeScript
maxLongitude?: double
```

Indicates the maximum longitude for geocoding query results.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoCodeRequest-maxLongitude?: double--><!--Device-GeoCodeRequest-maxLongitude?: double-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## minLatitude

```TypeScript
minLatitude?: double
```

Indicates the minimum latitude for geocoding query results.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoCodeRequest-minLatitude?: double--><!--Device-GeoCodeRequest-minLatitude?: double-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## minLongitude

```TypeScript
minLongitude?: double
```

Indicates the minimum longitude for geocoding query results.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-GeoCodeRequest-minLongitude?: double--><!--Device-GeoCodeRequest-minLongitude?: double-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

