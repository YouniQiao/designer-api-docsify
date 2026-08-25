# addFusionFence（系统接口）

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## addFusionFence

```TypeScript
function addFusionFence(fenceRequestParams: FusionFenceRequestParams): Promise<void>
```

添加一个融合围栏，并订阅围栏事件。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.LOCATION

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fenceRequestParams | [FusionFenceRequestParams](arkts-location-geolocationmanager-fusionfencerequestparams-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-位置服务不可用) |
| [3301100](../errorcode-geoLocationManager.md#3301100-位置功能的开关未开启导致功能失败) |
| [3501603](../errorcode-geoLocationManager.md#3501603-由于存在重复的beacon围栏导致添加围栏失败) |
| [3301601](../errorcode-geoLocationManager.md#3301601-地理围栏个数超过最大值限制导致添加围栏失败) |
