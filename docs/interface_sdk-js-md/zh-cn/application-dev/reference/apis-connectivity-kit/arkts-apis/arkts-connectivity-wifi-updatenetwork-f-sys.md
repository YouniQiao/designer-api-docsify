# updateNetwork（系统接口）

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## updateNetwork

```TypeScript
function updateNetwork(config: WifiDeviceConfig): number
```

Updates the specified Wi-Fi configuration.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.updateDeviceConfig

**需要权限：** ohos.permission.SET_WIFI_INFO and ohos.permission.SET_WIFI_CONFIG

<!--Device-wifi-function updateNetwork(config: WifiDeviceConfig): number--><!--Device-wifi-function updateNetwork(config: WifiDeviceConfig): number-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [WifiDeviceConfig](arkts-connectivity-wifi-wifideviceconfig-i-sys.md) | 是 | Indicates the Wi-Fi configuration to update. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | Returns the network ID in the updated Wi-Fi configuration if the update is successful; returns { |

## 示例

```TypeScript
import wifi from '@ohos.wifi';

try {
    let config:wifi.WifiDeviceConfig = {
        ssid : "****",
        bssid:  "****",
        preSharedKey: "****",
        isHiddenSsid: false,
        securityType: 3,
        creatorUid: 0,
        disableReason: 0,
        netId: 0,
        randomMacType: 0,
        randomMacAddr:  "****",
        ipType: 0,
        staticIp: {
            ipAddress: "",
            gateway: "",
            dnsServers: [],
            domains: []
        }
    }
    let ret = wifi.updateNetwork(config);
    console.error("ret:" + ret);        
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

