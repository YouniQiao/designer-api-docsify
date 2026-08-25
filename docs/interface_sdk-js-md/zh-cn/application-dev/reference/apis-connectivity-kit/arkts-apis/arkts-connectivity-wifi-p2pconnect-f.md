# p2pConnect

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## p2pConnect

```TypeScript
function p2pConnect(config: WifiP2PConfig): boolean
```

使用指定配置发起与设备的P2P连接。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [p2pConnect](arkts-connectivity-wifimanager-p2pconnect-f.md)

**需要权限：** ohos.permission.GET_WIFI_INFO and ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [WifiP2PConfig](arkts-connectivity-wifi-wifip2pconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
