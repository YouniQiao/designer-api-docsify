# updateNetwork (System API)

## updateNetwork

```TypeScript
function updateNetwork(config: WifiDeviceConfig): number
```

Updates the specified Wi-Fi configuration.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.wifiManager/wifiManager.updateDeviceConfig

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.SET_WIFI_CONFIG

<!--Device-wifi-function updateNetwork(config: WifiDeviceConfig): number--><!--Device-wifi-function updateNetwork(config: WifiDeviceConfig): number-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the Wi-Fi configuration to update. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Returns the network ID in the updated Wi-Fi configuration if the update is successful; returns { |

**Example**

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

