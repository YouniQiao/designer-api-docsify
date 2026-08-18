# setDeviceName（系统接口）

## 导入模块

```TypeScript
```

## setDeviceName

```TypeScript
function setDeviceName(devName: string): void
```

设置WLAN P2P设备的名称。

**起始版本：** 23

**需要权限：** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifiManager-function setDeviceName(devName: string): void--><!--Device-wifiManager-function setDeviceName(devName: string): void-End-->

**系统能力：** SystemCapability.Communication.WiFi.P2P

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| devName | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [2801000](../errorcode-wifi.md#2801000-p2p模块异常) |
| [2801001](../errorcode-wifi.md#2801001-p2p模块异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

try {
  let name = "****";
  wifiManager.setDeviceName(name);  
} catch (error) {
  console.error("failed:" + JSON.stringify(error));
}
```
