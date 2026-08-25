# getPostProcessingTrack

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## getPostProcessingTrack

```TypeScript
function getPostProcessingTrack(sportsType: SportsType): Promise<Array<Location>>
```

根据传入的[sportsType](arkts-location-geolocationmanager-sportstype-e.md)获取特定运动模式下的后处理轨迹。在调用此接口之前，需要先调用 geoLocationManager.on('locationChange') ，并在[ContinuousLocationRequest](arkts-location-geolocationmanager-continuouslocationrequest-i.md)入参中的 [SportsType](arkts-location-geolocationmanager-sportstype-e.md)配置正确的运动模式。当前仅支持滑雪模式。记录的运动轨迹会在24小时之后清除。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.LOCATION

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Location.Location.Gnss

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [sportsType](arkts-location-geolocationmanager-continuouslocationrequest-i.md) | [SportsType](arkts-location-geolocationmanager-sportstype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;Location & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-位置服务不可用) |
| [3301100](../errorcode-geoLocationManager.md#3301100-位置功能的开关未开启导致功能失败) |
| [3301200](../errorcode-geoLocationManager.md#3301200-定位失败未获取到定位结果) |
