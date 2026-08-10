# ReverseGeocodingMockInfo（系统接口）

Configuration parameters for simulating reverse geocoding.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-export interface ReverseGeocodingMockInfo--><!--Device-geoLocationManager-export interface ReverseGeocodingMockInfo-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## geoAddress

```TypeScript
geoAddress: GeoAddress
```

Actual address information corresponding to the location.

**类型：** [GeoAddress](arkts-location-geolocationmanager-geoaddress-i-sys.md)

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-ReverseGeocodingMockInfo-geoAddress: GeoAddress--><!--Device-ReverseGeocodingMockInfo-geoAddress: GeoAddress-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## location

```TypeScript
location: ReverseGeoCodeRequest
```

Location for which reverse geocoding query is required.

**类型：** [ReverseGeoCodeRequest](arkts-location-geolocation-reversegeocoderequest-i.md)

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-ReverseGeocodingMockInfo-location: ReverseGeoCodeRequest--><!--Device-ReverseGeocodingMockInfo-location: ReverseGeoCodeRequest-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

