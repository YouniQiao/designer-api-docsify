# setDeviceName (System API)

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## setDeviceName

```TypeScript
function setDeviceName(devName: string): boolean
```

Sets the name of the Wi-Fi P2P device.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [setP2pDeviceName](ohos.wifiManager/wifiManager.setP2pDeviceName)

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifi-function setDeviceName(devName: string): boolean--><!--Device-wifi-function setDeviceName(devName: string): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| devName | string | Yes | Indicates the name to be set. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

## Examples

```TypeScript
import wifi from '@ohos.wifi';

try {
    let name = "****";
    wifi.setDeviceName(name);    
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

