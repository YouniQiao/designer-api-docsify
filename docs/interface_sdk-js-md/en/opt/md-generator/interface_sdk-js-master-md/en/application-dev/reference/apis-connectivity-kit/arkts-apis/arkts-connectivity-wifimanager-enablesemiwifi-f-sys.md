# enableSemiWifi (System API)

## Modules to Import

```TypeScript
```

## enableSemiWifi

```TypeScript
function enableSemiWifi(): void
```

Enable semi - Wifi.

**Since:** 23

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifiManager-function enableSemiWifi(): void--><!--Device-wifiManager-function enableSemiWifi(): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2501004](../errorcode-wifi.md#2501004-failed-to-close-the-service) |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) |

**Examples**

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.enableSemiWifi();
  } catch(error) {
    console.error("failed:" + JSON.stringify(error));
  }
```
