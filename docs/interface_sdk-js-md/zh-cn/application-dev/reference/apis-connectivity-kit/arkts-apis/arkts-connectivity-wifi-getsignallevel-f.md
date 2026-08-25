# getSignalLevel

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## getSignalLevel

```TypeScript
function getSignalLevel(rssi: number, band: number): number
```

查询WLAN信号强度。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [getSignalLevel](arkts-connectivity-wifimanager-getsignallevel-f.md)

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rssi | number | 是 |
| band | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |
