# connectToNetwork（系统接口）

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## connectToNetwork

```TypeScript
function connectToNetwork(networkId: number): boolean
```

应用使用该接口连接到热点。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [connectToNetwork](arkts-connectivity-wifimanager-connecttonetwork-f.md)

**需要权限：** ohos.permission.MANAGE_WIFI_CONNECTION

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| networkId | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
