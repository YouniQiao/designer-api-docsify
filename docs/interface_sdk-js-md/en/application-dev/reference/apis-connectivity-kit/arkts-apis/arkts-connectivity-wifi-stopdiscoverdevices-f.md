# stopDiscoverDevices

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## stopDiscoverDevices

```TypeScript
function stopDiscoverDevices(): boolean
```

Stops discovering Wi-Fi P2P devices.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** stopDiscoverP2pDevices

**Required permissions:** ohos.permission.GET_WIFI_INFO

**System capability:** SystemCapability.Communication.WiFi.P2P

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Examples**

```TypeScript
import wifi from '@ohos.wifi';

try {
  wifi.stopDiscoverDevices();  
}catch(error){
  console.error("failed:" + JSON.stringify(error));
}
```
