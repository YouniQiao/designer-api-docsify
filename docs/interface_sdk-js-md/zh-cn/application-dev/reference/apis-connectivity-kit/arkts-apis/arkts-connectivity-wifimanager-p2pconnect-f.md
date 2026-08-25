# p2pConnect

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## p2pConnect

```TypeScript
function p2pConnect(config: WifiP2PConfig): void
```

使用指定配置发起与设备的P2P连接。

**起始版本：** 10

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [WifiP2PConfig](arkts-connectivity-wifi-wifip2pconfig-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [2801000](../errorcode-wifi.md#2801000-p2p模块异常) |
| [2801001](../errorcode-wifi.md#2801001-p2p功能未打开) |
