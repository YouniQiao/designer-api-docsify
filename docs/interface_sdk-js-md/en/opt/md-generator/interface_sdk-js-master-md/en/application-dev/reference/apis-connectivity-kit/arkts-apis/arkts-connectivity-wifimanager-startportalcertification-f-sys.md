# startPortalCertification (System API)

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## startPortalCertification

```TypeScript
function startPortalCertification(): void
```

Start Portal certification.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifiManager-function startPortalCertification(): void--><!--Device-wifiManager-function startPortalCertification(): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) |
| [2501001](../errorcode-wifi.md#2501001-sta-disabled) |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

try {
  wifiManager.startPortalCertification();
} catch (error) {
  console.error("failed:" + JSON.stringify(error));
}
```
