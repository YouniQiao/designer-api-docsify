# disableNetwork (System API)

## disableNetwork

```TypeScript
function disableNetwork(netId: number): boolean
```

Disables a specified network. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_The disabled network will not be associated with again.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.wifiManager/wifiManager.disableDeviceConfig

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifi-function disableNetwork(netId: number): boolean--><!--Device-wifi-function disableNetwork(netId: number): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| netId | number | Yes | Identifies the network to disable. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Example**

```TypeScript
import wifi from '@ohos.wifi';

try {
    let netId = 0;
    wifi.disableNetwork(netId);        
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

