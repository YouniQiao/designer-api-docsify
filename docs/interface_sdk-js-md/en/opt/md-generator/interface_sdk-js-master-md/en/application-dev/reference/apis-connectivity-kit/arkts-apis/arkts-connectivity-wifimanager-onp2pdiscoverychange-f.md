# onP2pDiscoveryChange

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## onP2pDiscoveryChange

```TypeScript
function onP2pDiscoveryChange(callback: Callback<number>): void
```

Subscribe P2P discovery events.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function onP2pDiscoveryChange(callback: Callback<int>): void--><!--Device-wifiManager-function onP2pDiscoveryChange(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [2801000](../errorcode-wifi.md#2801000-p2p-module-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
