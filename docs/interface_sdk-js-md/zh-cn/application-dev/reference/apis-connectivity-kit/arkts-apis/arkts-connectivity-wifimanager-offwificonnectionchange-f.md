# offWifiConnectionChange

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## offWifiConnectionChange

```TypeScript
function offWifiConnectionChange(callback?: Callback<int>): void
```

Unsubscribe Wi-Fi connection change events.All callback functions will be deregistered If there is no specific callback parameter.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function offWifiConnectionChange(callback?: Callback<int>): void--><!--Device-wifiManager-function offWifiConnectionChange(callback?: Callback<int>): void-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 否 | the callback of off |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 2501000 | Operation failed. |

