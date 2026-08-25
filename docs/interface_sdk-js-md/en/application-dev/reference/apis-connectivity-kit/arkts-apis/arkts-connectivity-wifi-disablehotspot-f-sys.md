# disableHotspot (System API)

## Modules to Import

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## disableHotspot

```TypeScript
function disableHotspot(): boolean
```

Disables a Wi-Fi hotspot.<p>This method is asynchronous. If Wi-Fi is enabled after the Wi-Fi hotspot is disabled, Wi-Fi may be re-enabled.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [disableHotspot](arkts-connectivity-wifimanager-disablehotspot-f-sys.md)

**Required permissions:** ohos.permission.MANAGE_WIFI_HOTSPOT

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
