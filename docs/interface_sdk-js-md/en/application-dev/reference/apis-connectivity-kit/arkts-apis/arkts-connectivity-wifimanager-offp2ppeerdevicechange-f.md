# offP2pPeerDeviceChange

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## offP2pPeerDeviceChange

```TypeScript
function offP2pPeerDeviceChange(callback?: Callback<WifiP2pDevice[]>): void
```

Unsubscribe P2P peer device change events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-wifiManager-function offP2pPeerDeviceChange(callback?: Callback<WifiP2pDevice[]>): void--><!--Device-wifiManager-function offP2pPeerDeviceChange(callback?: Callback<WifiP2pDevice[]>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;WifiP2pDevice[]&gt; | No | the callback of off |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [2801000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-connectivity-kit/errorcode-wifi.md#2801000-p2p-module-error) | Operation failed. |

