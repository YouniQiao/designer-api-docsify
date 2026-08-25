# connectToDevice（系统接口）

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## connectToDevice

```TypeScript
function connectToDevice(config: WifiDeviceConfig): boolean
```

连接到指定网络。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [connectToDevice](arkts-connectivity-wifimanager-connecttodevice-f-sys.md)

**需要权限：** ohos.permission.SET_WIFI_INFO and ohos.permission.SET_WIFI_CONFIG and ohos.permission.MANAGE_WIFI_CONNECTION

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [WifiDeviceConfig](arkts-connectivity-wifi-wifideviceconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
