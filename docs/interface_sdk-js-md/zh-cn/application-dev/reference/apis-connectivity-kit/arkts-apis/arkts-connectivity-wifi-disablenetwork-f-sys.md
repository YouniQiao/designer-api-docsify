# disableNetwork（系统接口）

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## disableNetwork

```TypeScript
function disableNetwork(netId: number): boolean
```

去使能网络配置。<p>去使能的网络将不再被关联。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** disableDeviceConfig

**需要权限：** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| netId | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
