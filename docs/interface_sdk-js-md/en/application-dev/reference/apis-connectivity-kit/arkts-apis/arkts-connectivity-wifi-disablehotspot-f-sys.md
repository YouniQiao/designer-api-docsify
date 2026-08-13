# disableHotspot (System API)

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## disableHotspot

```TypeScript
function disableHotspot(): boolean
```

Disables a Wi-Fi hotspot. &lt;p&gt;This method is asynchronous. If Wi-Fi is enabled after the Wi-Fi hotspot is disabled, Wi-Fi may be re-enabled.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [disableHotspot](arkts-connectivity-wifimanager-disablehotspot-f-sys.md#disableHotspot-(System-API))

**Required permissions:** ohos.permission.MANAGE_WIFI_HOTSPOT

<!--Device-wifi-function disableHotspot(): boolean--><!--Device-wifi-function disableHotspot(): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

## Examples

```TypeScript
import wifi from '@ohos.wifi';

try {
    wifi.disableHotspot();    
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

