# updateNetwork（系统接口）

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## updateNetwork

```TypeScript
function updateNetwork(config: WifiDeviceConfig): number
```

更新网络配置。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** updateDeviceConfig

**需要权限：** ohos.permission.SET_WIFI_INFO and ohos.permission.SET_WIFI_CONFIG

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [WifiDeviceConfig](arkts-connectivity-wifi-wifideviceconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |
