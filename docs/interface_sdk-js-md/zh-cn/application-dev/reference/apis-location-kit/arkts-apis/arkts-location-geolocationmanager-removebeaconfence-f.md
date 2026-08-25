# removeBeaconFence

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## removeBeaconFence

```TypeScript
function removeBeaconFence(beaconFence?: BeaconFence): Promise<void>
```

删除beacon围栏，并取消订阅地理围栏事件。使用Promise异步回调。

**起始版本：** 20

**需要权限：** 
- API版本20 - 24：ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Location.Location.Geofence

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [beaconFence](arkts-location-geolocationmanager-geofencetransition-i.md) | [BeaconFence](arkts-location-geolocationmanager-beaconfence-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3501602](../errorcode-geoLocationManager.md#3501602-由于beacon围栏信息不正确导致删除围栏失败) |
