# disconnect

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## disconnect

```TypeScript
function disconnect(): void
```

断开STA与WLAN热点之间的连接。

**起始版本：** 15

**需要权限：** ohos.permission.SET_WIFI_INFO and (ohos.permission.MANAGE_WIFI_CONNECTION or ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION)

**系统能力：** SystemCapability.Communication.WiFi.STA

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [2501000](../errorcode-wifi.md#2501000-sta内部异常) |
| [2501001](../errorcode-wifi.md#2501001-sta功能未打开) |
