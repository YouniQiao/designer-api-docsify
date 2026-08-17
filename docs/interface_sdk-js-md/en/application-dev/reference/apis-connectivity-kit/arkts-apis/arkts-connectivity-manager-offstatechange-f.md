# offStateChange

## Modules to Import

```TypeScript
import { manager } from 'manager';
```

## offStateChange

```TypeScript
function offStateChange(callback?: Callback<NearlinkState>): void
```

Unsubscribes from state change events.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-manager-function offStateChange(callback?: Callback<NearlinkState>): void--><!--Device-manager-function offStateChange(callback?: Callback<NearlinkState>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NearlinkState](arkts-connectivity-manager-nearlinkstate-e.md)&gt; | No | Callback used to listen for the state change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because the chip does not support it. |
| 36100099 | Operation failed. |

