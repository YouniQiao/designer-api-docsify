# offSatelliteStatusChange

## 导入模块

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## offSatelliteStatusChange

```TypeScript
function offSatelliteStatusChange(callback?: Callback<SatelliteStatusInfo>): void
```

取消订阅GNSS卫星状态信息上报事件。调用该接口前建议先通过 [geoLocationManager.isGnssServiceSupported](arkts-location-geolocationmanager-isgnssservicesupported-f.md)接口判断对应能力是否支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.APPROXIMATELY_LOCATION

**系统能力：** SystemCapability.Location.Location.Gnss

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SatelliteStatusInfo&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-位置服务不可用) |
| [3301100](../errorcode-geoLocationManager.md#3301100-位置功能的开关未开启导致功能失败) |
