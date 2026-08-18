# enableHotspot (System API)

## Modules to Import

```TypeScript
```

## enableHotspot

```TypeScript
function enableHotspot(): void
```

Enable Wi-Fi hotspot function. This method is asynchronous. After the Wi-Fi hotspot is enabled, Wi-Fi may be disabled.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_WIFI_HOTSPOT

<!--Device-wifiManager-function enableHotspot(): void--><!--Device-wifiManager-function enableHotspot(): void-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2601000](../errorcode-wifi.md#2601000-hotspot-module-error) |

**Examples**

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

try {
    wifiManager.enableHotspot();
} catch (error) {
    console.error("failed:" + JSON.stringify(error));
}
```
