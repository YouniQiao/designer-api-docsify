# onHotspotStateChange

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## onHotspotStateChange

```TypeScript
function onHotspotStateChange(callback: Callback<number>): void
```

Subscribe Wi-Fi hotspot state change events.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function onHotspotStateChange(callback: Callback<int>): void--><!--Device-wifiManager-function onHotspotStateChange(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2601000](../errorcode-wifi.md#2601000-hotspot-module-error) |
