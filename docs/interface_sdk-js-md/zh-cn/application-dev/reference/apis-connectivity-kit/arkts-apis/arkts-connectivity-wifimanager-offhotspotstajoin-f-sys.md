# offHotspotStaJoin（系统接口）

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## offHotspotStaJoin

```TypeScript
function offHotspotStaJoin(callback?: Callback<StationInfo>): void
```

Unsubscribe Wi-Fi hotspot sta join events.All callback functions will be deregistered If there is no specific callback parameter.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.MANAGE_WIFI_HOTSPOT

<!--Device-wifiManager-function offHotspotStaJoin(callback?: Callback<StationInfo>): void--><!--Device-wifiManager-function offHotspotStaJoin(callback?: Callback<StationInfo>): void-End-->

**系统能力：** SystemCapability.Communication.WiFi.AP.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StationInfo&gt; | 否 | the callback of off |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 202 | System API is not allowed called by Non-system application. |
| 2601000 | Operation failed. |

