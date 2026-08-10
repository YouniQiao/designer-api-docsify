# scan

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## scan

```TypeScript
function scan(): boolean
```

Scans Wi-Fi hotspot.

&lt;p&gt;This API works in asynchronous mode.&lt;/p&gt;

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.scan

**需要权限：** ohos.permission.SET_WIFI_INFO and ohos.permission.LOCATION

<!--Device-wifi-function scan(): boolean--><!--Device-wifi-function scan(): boolean-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns { |

## 示例

```TypeScript
import wifi from '@ohos.wifi';

try {
  wifi.scan();
}catch(error){
  console.error("failed:" + JSON.stringify(error));
}
```

