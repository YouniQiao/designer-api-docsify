# offHotspotStateChange

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## offHotspotStateChange

```TypeScript
function offHotspotStateChange(callback?: Callback<number>): void
```

Unsubscribe Wi-Fi hotspot state change events. All callback functions will be deregistered If there is no specific callback parameter.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function offHotspotStateChange(callback?: Callback<int>): void--><!--Device-wifiManager-function offHotspotStateChange(callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2601000](../errorcode-wifi.md#2601000-hotspot-module-error) |
