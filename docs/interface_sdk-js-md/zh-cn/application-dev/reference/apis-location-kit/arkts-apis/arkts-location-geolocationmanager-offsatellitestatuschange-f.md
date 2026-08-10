# offSatelliteStatusChange

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## offSatelliteStatusChange

```TypeScript
function offSatelliteStatusChange(callback?: Callback<SatelliteStatusInfo>): void
```

Unsubscribe satellite status changed.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function offSatelliteStatusChange(callback?: Callback<SatelliteStatusInfo>): void--><!--Device-geoLocationManager-function offSatelliteStatusChange(callback?: Callback<SatelliteStatusInfo>): void-End-->

**系统能力：** SystemCapability.Location.Location.Gnss

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SatelliteStatusInfo&gt; | 否 | Indicates the callback for reporting the satellite status. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.offSatelliteStatusChange} due to limited device capabilities. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

