# getSupportedFeatures (System API)

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## getSupportedFeatures

```TypeScript
function getSupportedFeatures(): number
```

Obtain the features supported by the device.To check whether this device supports a specified feature.

**Since:** 9

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function getSupportedFeatures(): long--><!--Device-wifiManager-function getSupportedFeatures(): long-End-->

**System capability:** SystemCapability.Communication.WiFi.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2401000](../errorcode-wifi.md#2401000-sta-internal-error) |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

try {
    let ret = wifiManager.getSupportedFeatures();
    console.info("supportedFeatures:" + ret);
} catch (error) {
    console.error("failed:" + JSON.stringify(error));
}
```
