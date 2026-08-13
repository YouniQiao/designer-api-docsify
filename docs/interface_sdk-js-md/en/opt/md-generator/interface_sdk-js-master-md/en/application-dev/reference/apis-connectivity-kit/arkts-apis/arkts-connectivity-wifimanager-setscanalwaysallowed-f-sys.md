# setScanAlwaysAllowed (System API)

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## setScanAlwaysAllowed

```TypeScript
function setScanAlwaysAllowed(isScanAlwaysAllowed: boolean): void
```

User can trigger scan even Wi-Fi is disabled.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.SET_WIFI_CONFIG

<!--Device-wifiManager-function setScanAlwaysAllowed(isScanAlwaysAllowed: boolean): void--><!--Device-wifiManager-function setScanAlwaysAllowed(isScanAlwaysAllowed: boolean): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isScanAlwaysAllowed | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) |
