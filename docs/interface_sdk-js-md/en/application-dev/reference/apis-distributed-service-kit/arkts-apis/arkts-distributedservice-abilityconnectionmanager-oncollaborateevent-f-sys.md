# onCollaborateEvent (System API)

## Modules to Import

```TypeScript
import { abilityConnectionManager } from 'abilityConnectionManager';
```

## onCollaborateEvent

```TypeScript
function onCollaborateEvent(sessionId: int,
        callback: Callback<CollaborateEventInfo>): void
```

Registers collaborateEvent event.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function onCollaborateEvent(sessionId: int,        callback: Callback<CollaborateEventInfo>): void--><!--Device-abilityConnectionManager-function onCollaborateEvent(sessionId: int,        callback: Callback<CollaborateEventInfo>): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | int | Yes | Ability connection Session id. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CollaborateEventInfo](arkts-distributedservice-abilityconnectionmanager-collaborateeventinfo-i.md)&gt; | Yes | Called when an error event comes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.2. Incorrect parameter types. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system App. |

