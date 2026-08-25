# getActiveGeoFences

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## getActiveGeoFences

```TypeScript
function getActiveGeoFences(): Promise<Map<number, Geofence>>
```

查询当前有效的围栏信息。使用Promise异步回调。调用该接口前建议先通过 [geoLocationManager.isGnssFenceServiceSupported](arkts-location-geolocationmanager-isgnssfenceservicesupported-f.md)接口判断对应能力是否支持。

**起始版本：** 23

**需要权限：** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

**系统能力：** SystemCapability.Location.Location.Geofence

**返回值：**

| 类型 |
| --- |
| Promise & lt;Map & lt;number, Geofence & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
