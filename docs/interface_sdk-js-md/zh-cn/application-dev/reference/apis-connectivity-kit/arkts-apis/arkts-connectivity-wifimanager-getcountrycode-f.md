# getCountryCode

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## getCountryCode

```TypeScript
function getCountryCode(): string
```

获取设备的国家码。

**起始版本：** 9

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [2401000](../errorcode-wifi.md#2401000-sta内部异常) |
