# onStateChange

## Modules to Import

```TypeScript
import { access } from '@kit.ConnectivityKit';
```

## onStateChange

```TypeScript
function onStateChange(callback: Callback<BluetoothState>): void
```

Subscribe the event reported when the Bluetooth state changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-access-function onStateChange(callback: Callback<BluetoothState>): void--><!--Device-access-function onStateChange(callback: Callback<BluetoothState>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;BluetoothState&gt; | Yes | Callback used to listen for the Bluetooth state event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| 2900099 | Operation failed. |

