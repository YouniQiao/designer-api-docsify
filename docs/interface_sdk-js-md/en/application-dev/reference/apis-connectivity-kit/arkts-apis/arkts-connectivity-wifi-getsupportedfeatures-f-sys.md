# getSupportedFeatures (System API)

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## getSupportedFeatures

```TypeScript
function getSupportedFeatures(): number
```

Obtains the features supported by this device.

&lt;p&gt;To check whether this device supports a specified feature.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [getSupportedFeatures](ohos.wifiManager/wifiManager.getSupportedFeatures)

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function getSupportedFeatures(): number--><!--Device-wifi-function getSupportedFeatures(): number-End-->

**System capability:** SystemCapability.Communication.WiFi.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| number | Returns the features supported by this device. |

