# addHotspotBlockList（系统接口）

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## addHotspotBlockList

```TypeScript
function addHotspotBlockList(stationInfo: StationInfo): void
```

将站点添加到黑名单，该站点无法访问热点。

**起始版本：** 11

**需要权限：** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_HOTSPOT

**系统能力：** SystemCapability.Communication.WiFi.AP.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| stationInfo | [StationInfo](arkts-connectivity-wifimanager-stationinfo-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [2601000](../errorcode-wifi.md#2601000-hotspot模块异常) |
