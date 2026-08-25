# Geofence

GNSS围栏的配置参数。目前只支持圆形围栏。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Location.Location.Geofence

## 导入模块

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## coordinateSystemType

```TypeScript
coordinateSystemType?: CoordinateSystemType
```

表示地理围栏圆心坐标的坐标系。APP应先使用[getGeofenceSupportedCoordTypes](arkts-location-geolocationmanager-getgeofencesupportedcoordtypes-f.md)查询支持的坐标系，然后传入正确的圆 心坐标。

**类型：** CoordinateSystemType

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Location.Location.Geofence

## expiration

```TypeScript
expiration: double
```

围栏存活的时间，单位是毫秒。取值范围为大于0。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Location.Location.Geofence

## latitude

```TypeScript
latitude: double
```

表示纬度。取值范围为-90到90。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Location.Location.Geofence

## longitude

```TypeScript
longitude: double
```

表示经度。取值范围为-180到180。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Location.Location.Geofence

## radius

```TypeScript
radius: double
```

表示圆形围栏的半径。单位是米，取值范围为大于0。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Location.Location.Geofence
