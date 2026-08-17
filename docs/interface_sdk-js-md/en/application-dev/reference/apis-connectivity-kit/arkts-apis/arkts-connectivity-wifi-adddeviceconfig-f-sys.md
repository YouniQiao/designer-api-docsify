# addDeviceConfig (System API)

## Modules to Import

```TypeScript
import { wifi } from 'wifi';
```

## addDeviceConfig

```TypeScript
function addDeviceConfig(config: WifiDeviceConfig): Promise<number>
```

Adds Wi-Fi connection configuration to the device. &lt;p&gt;The configuration will be updated when the configuration is added.&lt;/p&gt;

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [addDeviceConfig](arkts-connectivity-wifimanager-adddeviceconfig-f.md#adddeviceconfig)

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.SET_WIFI_CONFIG

<!--Device-wifi-function addDeviceConfig(config: WifiDeviceConfig): Promise<number>--><!--Device-wifi-function addDeviceConfig(config: WifiDeviceConfig): Promise<number>-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | WifiDeviceConfig | Yes | Indicates the device configuration for connection to the Wi-Fi network. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Returns { |

**Examples**

```TypeScript
import wifi from '@ohos.wifi';

try {
    let config:wifi.WifiDeviceConfig = {
        ssid : "****",
        bssid:  "****",
        preSharedKey: "****",
        isHiddenSsid: false,
        securityType: 0,
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
    wifi.addDeviceConfig(config).then(result => {
        console.info("result:" + JSON.stringify(result));
    });    
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```


## addDeviceConfig

```TypeScript
function addDeviceConfig(config: WifiDeviceConfig, callback: AsyncCallback<number>): void
```

Adds Wi-Fi connection configuration to the device. &lt;p&gt;The configuration will be updated when the configuration is added.&lt;/p&gt;

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [addDeviceConfig](arkts-connectivity-wifimanager-adddeviceconfig-f.md#adddeviceconfig)

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.SET_WIFI_CONFIG

<!--Device-wifi-function addDeviceConfig(config: WifiDeviceConfig, callback: AsyncCallback<number>): void--><!--Device-wifi-function addDeviceConfig(config: WifiDeviceConfig, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | WifiDeviceConfig | Yes | Indicates the device configuration for connection to the Wi-Fi network. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |  |

**Examples**

```TypeScript
import wifi from '@ohos.wifi';

try {
    let config:wifi.WifiDeviceConfig = {
        ssid : "****",
        bssid:  "****",
        preSharedKey: "****",
        isHiddenSsid: false,
        securityType: 0,
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
    wifi.addDeviceConfig(config,(error,result) => {
        console.info("result:" + JSON.stringify(result));
    });    
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

