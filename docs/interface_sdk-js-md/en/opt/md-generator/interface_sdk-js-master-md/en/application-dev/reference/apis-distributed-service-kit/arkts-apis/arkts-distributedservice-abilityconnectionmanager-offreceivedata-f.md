# offReceiveData

## Modules to Import

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
```

## offReceiveData

```TypeScript
function offReceiveData(sessionId: number,
        callback?: Callback<EventCallbackInfo>): void
```

Unregisters receiveData event.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function offReceiveData(sessionId: int,        callback?: Callback<EventCallbackInfo>): void--><!--Device-abilityConnectionManager-function offReceiveData(sessionId: int,        callback?: Callback<EventCallbackInfo>): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | number | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[EventCallbackInfo](arkts-distributedservice-abilityconnectionmanager-eventcallbackinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
