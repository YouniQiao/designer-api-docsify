# onGnssFenceStatusChange

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## onGnssFenceStatusChange

```TypeScript
function onGnssFenceStatusChange(request: GeofenceRequest, want: WantAgent): void
```

Add a geofence and subscribe geofence status changed.

**起始版本：** 26.1.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.1.0。

**需要权限：** ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function onGnssFenceStatusChange(request: GeofenceRequest, want: WantAgent): void--><!--Device-geoLocationManager-function onGnssFenceStatusChange(request: GeofenceRequest, want: WantAgent): void-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [GeofenceRequest](arkts-location-geolocationmanager-geofencerequest-i.md) | 是 | Indicates the Geofence configuration parameters. |
| want | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-t.md) | 是 | Indicates which ability to start when the geofence event is triggered. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.onGnssFenceStatusChange} due to limited device capabilities. |
| 3301600 | Failed to operate the geofence. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

