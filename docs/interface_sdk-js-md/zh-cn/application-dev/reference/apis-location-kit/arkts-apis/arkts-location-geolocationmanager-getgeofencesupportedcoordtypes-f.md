# getGeofenceSupportedCoordTypes

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## getGeofenceSupportedCoordTypes

```TypeScript
function getGeofenceSupportedCoordTypes(): Array<CoordinateSystemType>
```

获取地理围栏功能支持的坐标系列表。调用该接口前建议先通过 [geoLocationManager.isGnssFenceServiceSupported](arkts-location-geolocationmanager-isgnssfenceservicesupported-f.md)接口判断对应能力是否支持。

**起始版本：** 12

**系统能力：** SystemCapability.Location.Location.Geofence

**返回值：**

| 类型 |
| --- |
| Array & lt;CoordinateSystemType & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-位置服务不可用) |
