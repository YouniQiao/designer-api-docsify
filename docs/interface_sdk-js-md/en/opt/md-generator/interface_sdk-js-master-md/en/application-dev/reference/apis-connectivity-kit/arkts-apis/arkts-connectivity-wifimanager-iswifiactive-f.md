# isWifiActive

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## isWifiActive

```TypeScript
function isWifiActive(): boolean
```

Query the Wi-Fi status

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-wifiManager-function isWifiActive(): boolean--><!--Device-wifiManager-function isWifiActive(): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let isWifiActive = wifiManager.isWifiActive();
    console.info("isWifiActive:" + isWifiActive);
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```
