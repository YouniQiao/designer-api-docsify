# allowAutoConnect（系统接口）

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## allowAutoConnect

```TypeScript
function allowAutoConnect(netId: int, isAllowed: boolean): void
```

Set whther to allow automatic connnect by networkId.The network can be associated with again if isAllowed is true, else not.

**起始版本：** 17

**ArkTS模式：** ArkTS-Dyn起始版本为17；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifiManager-function allowAutoConnect(netId: int, isAllowed: boolean): void--><!--Device-wifiManager-function allowAutoConnect(netId: int, isAllowed: boolean): void-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Identifies the network to be set. The value of networkId cannot be less than 0. |
| isAllowed | boolean | 是 | Identifies whether allow auto connect or not. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 202 | System API is not allowed called by Non-system application. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

