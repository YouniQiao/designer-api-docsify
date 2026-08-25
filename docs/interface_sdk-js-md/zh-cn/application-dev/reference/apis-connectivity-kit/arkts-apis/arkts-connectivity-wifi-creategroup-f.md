# createGroup

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## createGroup

```TypeScript
function createGroup(config: WifiP2PConfig): boolean
```

创建P2P群组。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** createP2pGroup

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [WifiP2PConfig](arkts-connectivity-wifi-wifip2pconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
