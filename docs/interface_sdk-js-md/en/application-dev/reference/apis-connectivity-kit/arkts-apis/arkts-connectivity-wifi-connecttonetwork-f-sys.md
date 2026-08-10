# connectToNetwork (System API)

## Modules to Import

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## connectToNetwork

```TypeScript
function connectToNetwork(networkId: number): boolean
```

Connects to Wi-Fi network.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** ohos.wifiManager/wifiManager.connectToNetwork

**Required permissions:** ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifi-function connectToNetwork(networkId: number): boolean--><!--Device-wifi-function connectToNetwork(networkId: number): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| networkId | number | Yes | ID of the connected network. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

## Examples

```TypeScript
import wifi from '@ohos.wifi';

try {
    let networkId = 0;
    wifi.connectToNetwork(networkId);
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

