# offP2pPeerDeviceChange

## Modules to Import

```TypeScript
```

## offP2pPeerDeviceChange

```TypeScript
function offP2pPeerDeviceChange(callback?: Callback<WifiP2pDevice[]>): void
```

Unsubscribe P2P peer device change events.

**Since:** 23

<!--Device-wifiManager-function offP2pPeerDeviceChange(callback?: Callback<WifiP2pDevice[]>): void--><!--Device-wifiManager-function offP2pPeerDeviceChange(callback?: Callback<WifiP2pDevice[]>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WifiP2pDevice[]&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [2801000](../errorcode-wifi.md#2801000-p2p-module-error) |
