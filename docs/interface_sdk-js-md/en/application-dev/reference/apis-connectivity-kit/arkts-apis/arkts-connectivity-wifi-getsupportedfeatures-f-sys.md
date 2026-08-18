# getSupportedFeatures (System API)

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
import { wifiext } from '@kit.ConnectivityKit';
import { wifiManager } from '@kit.ConnectivityKit';
import { wifiManagerExt } from '@kit.ConnectivityKit';
```

## getSupportedFeatures

```TypeScript
function getSupportedFeatures(): number
```

Obtains the features supported by this device. &lt;p&gt;To check whether this device supports a specified feature.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getSupportedFeatures](arkts-connectivity-wifimanager-getsupportedfeatures-f-sys.md#getsupportedfeatures-system-api)

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function getSupportedFeatures(): number--><!--Device-wifi-function getSupportedFeatures(): number-End-->

**System capability:** SystemCapability.Communication.WiFi.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| number | Returns the features supported by this device. |

