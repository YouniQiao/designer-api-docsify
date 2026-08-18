# offPairingStateChange

## Modules to Import

```TypeScript
import { remoteDevice } from '@kit.ConnectivityKit';
```

## offPairingStateChange

```TypeScript
function offPairingStateChange(callback?: Callback<PairingStateParam>): void
```

Unsubscribes from NearLink pairing state change events.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-remoteDevice-function offPairingStateChange(callback?: Callback<PairingStateParam>): void--><!--Device-remoteDevice-function offPairingStateChange(callback?: Callback<PairingStateParam>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[PairingStateParam](arkts-connectivity-remotedevice-pairingstateparam-i.md)&gt; | No | Callback function used to listen for the pairing state event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because the chip does not support it. |
| 36100099 | Operation failed. |

