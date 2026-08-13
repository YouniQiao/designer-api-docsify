# isHotspotDualBandSupported (System API)

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## isHotspotDualBandSupported

```TypeScript
function isHotspotDualBandSupported(): boolean
```

Check whether a device serving as a Wi-Fi hotspot supports both the 2.4 GHz and 5 GHz Wi-Fi.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_WIFI_INFO and ohos.permission.MANAGE_WIFI_HOTSPOT

<!--Device-wifiManager-function isHotspotDualBandSupported(): boolean--><!--Device-wifiManager-function isHotspotDualBandSupported(): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2601000](../errorcode-wifi.md#2601000-hotspot-module-error) |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

try {
  let ret = wifiManager.isHotspotDualBandSupported();
  console.info("result:" + ret);    
} catch (error) {
  console.error("failed:" + JSON.stringify(error));
}
```
