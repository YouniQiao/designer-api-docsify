# getIpInfo

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## getIpInfo

```TypeScript
function getIpInfo(): IpInfo
```

Obtains the IP information of a Wi-Fi connection.

&lt;p&gt;The IP information includes the host IP address, gateway address, and DNS information.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.getIpInfo

**需要权限：** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function getIpInfo(): IpInfo--><!--Device-wifi-function getIpInfo(): IpInfo-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IpInfo](arkts-connectivity-wifi-ipinfo-i.md) | Returns the IP information of the Wi-Fi connection. |

## 示例

```TypeScript
import wifi from '@ohos.wifi';

try {
  let info = wifi.getIpInfo();
  console.info("info:" + JSON.stringify(info));
}catch(error){
  console.error("failed:" + JSON.stringify(error));
}
```

