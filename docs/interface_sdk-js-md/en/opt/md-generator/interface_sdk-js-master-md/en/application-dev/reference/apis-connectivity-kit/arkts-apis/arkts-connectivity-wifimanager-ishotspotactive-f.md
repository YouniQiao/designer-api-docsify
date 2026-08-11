# isHotspotActive

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## isHotspotActive

```TypeScript
function isHotspotActive(): boolean
```

Check whether Wi-Fi hotspot is active on a device.

**Since:** 15

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function isHotspotActive(): boolean--><!--Device-wifiManager-function isHotspotActive(): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2601000](../errorcode-wifi.md#2601000-hotspot-module-error) |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let ret = wifiManager.isHotspotActive();
    console.info("result:" + ret);    
  } catch(error) {
    console.error("failed:" + JSON.stringify(error));
  }
```
