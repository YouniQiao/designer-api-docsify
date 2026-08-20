# enableHotspot (System API)

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
import { wifiext } from '@kit.ConnectivityKit';
import { wifiManager } from '@kit.ConnectivityKit';
import { wifiManagerExt } from '@kit.ConnectivityKit';
```

## enableHotspot

```TypeScript
function enableHotspot(): boolean
```

Enables a Wi-Fi hotspot.

&lt;p&gt;This method is asynchronous. After the Wi-Fi hotspot is enabled, Wi-Fi may be disabled.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [enableHotspot](arkts-connectivity-wifimanager-enablehotspot-f-sys.md)

**Required permissions:** ohos.permission.MANAGE_WIFI_HOTSPOT

<!--Device-wifi-function enableHotspot(): boolean--><!--Device-wifi-function enableHotspot(): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Examples**

```TypeScript
import wifi from '@ohos.wifi';

try {
    wifi.enableHotspot();    
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

