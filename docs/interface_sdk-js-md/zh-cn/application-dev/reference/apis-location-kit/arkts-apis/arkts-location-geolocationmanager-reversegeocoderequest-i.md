# ReverseGeoCodeRequest

Configuring parameters in reverse geocode requests.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-export interface ReverseGeoCodeRequest--><!--Device-geoLocationManager-export interface ReverseGeoCodeRequest-End-->

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

<!--Device-ReverseGeoCodeRequest-country?: string--><!--Device-ReverseGeoCodeRequest-country?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## latitude

```TypeScript
latitude: double
```

Latitude for reverse geocoding query.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-ReverseGeoCodeRequest-latitude: double--><!--Device-ReverseGeoCodeRequest-latitude: double-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## locale

```TypeScript
locale?: string
```

Indicates the language area information.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-ReverseGeoCodeRequest-locale?: string--><!--Device-ReverseGeoCodeRequest-locale?: string-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## longitude

```TypeScript
longitude: double
```

Longitude for reverse geocoding query.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-ReverseGeoCodeRequest-longitude: double--><!--Device-ReverseGeoCodeRequest-longitude: double-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

## maxItems

```TypeScript
maxItems?: int
```

Indicates the maximum number of addresses returned by reverse geocoding query.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-ReverseGeoCodeRequest-maxItems?: int--><!--Device-ReverseGeoCodeRequest-maxItems?: int-End-->

**系统能力：** SystemCapability.Location.Location.Geocoder

