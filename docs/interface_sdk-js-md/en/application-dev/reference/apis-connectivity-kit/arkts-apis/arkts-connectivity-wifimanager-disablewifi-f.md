# disableWifi

## Modules to Import

```TypeScript
import { wifiManager } from 'wifiManager';
```

## disableWifi

```TypeScript
function disableWifi(): void
```

Disable Wi-Fi.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.SET_WIFI_INFO and (ohos.permission.MANAGE_WIFI_CONNECTION or ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION)

<!--Device-wifiManager-function disableWifi(): void--><!--Device-wifiManager-function disableWifi(): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [2501004](../errorcode-wifi.md#2501004-failed-to-close-the-service) | Operation failed because the service is being opened. |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) | Operation failed. |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.disableWifi();
  }catch(error){
    console.error(`disableWifi failed. ${error.message}`);
  }
```

