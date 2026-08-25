# getScanInfoList

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## getScanInfoList

```TypeScript
function getScanInfoList(): Array<WifiScanInfo>
```

获取扫描结果。如果未获取ohos.permission.GET_WIFI_PEERS_MAC权限，返回随机bssid。

**起始版本：** 12

**需要权限：** ohos.permission.GET_WIFI_INFO

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 |
| --- |
| Array & lt;WifiScanInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [2501000](../errorcode-wifi.md#2501000-sta内部异常) |
