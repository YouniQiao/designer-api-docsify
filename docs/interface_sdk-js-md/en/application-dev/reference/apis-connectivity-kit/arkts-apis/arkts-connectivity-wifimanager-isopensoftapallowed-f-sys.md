# isOpenSoftApAllowed (System API)

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## isOpenSoftApAllowed

```TypeScript
function isOpenSoftApAllowed(): boolean
```

Check whether Wi-Fi hotspot is can be operated under some situation. When the airplane mode is turned on and does not support the coexistence of softap and sta, nor does it support signal bridge, the hotspot switch cannot be operated.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_WIFI_INFO and ohos.permission.MANAGE_WIFI_HOTSPOT

<!--Device-wifiManager-function isOpenSoftApAllowed(): boolean--><!--Device-wifiManager-function isOpenSoftApAllowed(): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | System API is not allowed called by Non-system application. |
| [2601000](../errorcode-wifi.md#2601000-hotspot-module-error) | Operation failed. |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

try {
  let ret = wifiManager.isOpenSoftApAllowed();
  console.info("result:" + ret);
}catch (error) {
  console.error("failed:" + JSON.stringify(error));
}
```

