# getDisconnectedReason (System API)

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## getDisconnectedReason

```TypeScript
function getDisconnectedReason(): DisconnectedReason
```

Obtain the latest disconnected reason.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_WIFI_INFO and ohos.permission.GET_WIFI_CONFIG

<!--Device-wifiManager-function getDisconnectedReason(): DisconnectedReason--><!--Device-wifiManager-function getDisconnectedReason(): DisconnectedReason-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DisconnectedReason](arkts-connectivity-wifimanager-disconnectedreason-e-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

try {
  let disconnectedReason = wifiManager.getDisconnectedReason();  
    console.info("disconnectedReason:" + disconnectedReason);
} catch (error) {
  console.error("failed:" + JSON.stringify(error));
}
```
