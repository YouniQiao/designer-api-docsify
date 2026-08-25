# addBeaconFence

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## addBeaconFence

```TypeScript
function addBeaconFence(fenceRequest: BeaconFenceRequest): Promise<number>
```

添加一个beacon围栏，并订阅地理围栏事件。使用Promise异步回调。 beacon围栏是指通过蓝牙beacon设备和手机应用配合，实现“虚拟围栏”的功能。当用户靠近或离开某个特定的beacon设备时，手机应用会收到通知。 应用可以在入参[BeaconFenceRequest](arkts-location-geolocationmanager-beaconfencerequest-i.md)中传入回调函数用于接收围栏事件；也可以传入 [FenceExtensionAbility](arkts-location-app-ability-fenceextensionability-fenceextensionability-c.md)名称，在系统识别到围栏事件发生时通知应用。 单应用添加beacon围栏上限为10，超过上限会导致添加beacon围栏失败，并抛出3501601错误码。

**起始版本：** 20

**需要权限：** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Location.Location.Geofence

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fenceRequest | [BeaconFenceRequest](arkts-location-geolocationmanager-beaconfencerequest-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3501100](../errorcode-geoLocationManager.md#3501100-由于位置功能开关未打开导致添加beacon围栏失败) |
| [3501101](../errorcode-geoLocationManager.md#3501101-由于蓝牙功能开关未打开导致添加beacon围栏失败) |
| [3501601](../errorcode-geoLocationManager.md#3501601-由于beacon围栏个数超过最大值限制导致添加围栏失败) |
| [3501603](../errorcode-geoLocationManager.md#3501603-由于存在重复的beacon围栏导致添加围栏失败) |
