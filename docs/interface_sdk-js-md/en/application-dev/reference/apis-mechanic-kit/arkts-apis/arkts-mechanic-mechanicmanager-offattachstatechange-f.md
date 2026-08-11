# offAttachStateChange

## Modules to Import

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## offAttachStateChange

```TypeScript
function offAttachStateChange(callback?: Callback<AttachStateChangeInfo>): void
```

Unsubscribes from device attachment state change events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-mechanicManager-function offAttachStateChange(callback?: Callback<AttachStateChangeInfo>): void--><!--Device-mechanicManager-function offAttachStateChange(callback?: Callback<AttachStateChangeInfo>): void-End-->

**System capability:** SystemCapability.Mechanic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AttachStateChangeInfo&gt; | No | Callback used to return the state change. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [33300001](../errorcode-mechanic.md#33300001-system-error) | Service exception. |

