# startDiscoverDevices

## Modules to Import

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## startDiscoverDevices

```TypeScript
function startDiscoverDevices(): boolean
```

Discover Wi-Fi P2P devices.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.wifiManager/wifiManager.startDiscoverP2pDevices

**Required permissions:** ohos.permission.GET_WIFI_INFO and ohos.permission.LOCATION

<!--Device-wifi-function startDiscoverDevices(): boolean--><!--Device-wifi-function startDiscoverDevices(): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import wifi from '@ohos.wifi';

try {
  wifi.startDiscoverDevices();  
}catch(error){
  console.error("failed:" + JSON.stringify(error));
}
```
