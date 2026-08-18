# getIpv6Info

## 导入模块

```TypeScript
```

## getIpv6Info

```TypeScript
function getIpv6Info(): Ipv6Info
```

获取WLAN连接的IPv6信息。 IPv6信息包括主机IP地址、网关地址和DNS信息。

**起始版本：** 23

**需要权限：** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function getIpv6Info(): Ipv6Info--><!--Device-wifiManager-function getIpv6Info(): Ipv6Info-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 |
| --- |
| [Ipv6Info](arkts-connectivity-wifimanager-ipv6info-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2501000](../errorcode-wifi.md#2501000-sta内部异常) |

**示例**

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let info = wifiManager.getIpv6Info();
    console.info("info:" + JSON.stringify(info));
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```
