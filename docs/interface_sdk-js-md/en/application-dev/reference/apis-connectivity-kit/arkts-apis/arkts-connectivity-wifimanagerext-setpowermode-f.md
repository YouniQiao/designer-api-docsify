# setPowerMode

## Modules to Import

```TypeScript
import { wifiManagerExt } from 'kits/@kit.ConnectivityKit';
```

## setPowerMode

```TypeScript
function setPowerMode(mode: PowerMode): void
```

Set the current Wi-Fi power mode.

**Since:** 9

**Deprecated since:** 10

**Required permissions:** ohos.permission.MANAGE_WIFI_HOTSPOT_EXT

**System capability:** SystemCapability.Communication.WiFi.AP.Extension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [PowerMode](arkts-connectivity-wifimanagerext-powermode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [2701000](../errorcode-wifi.md#2701000-ap-extension-module-error) |
