# offConnect

## Modules to Import

```TypeScript
import { abilityConnectionManager } from 'abilityConnectionManager';
```

## offConnect

```TypeScript
function offConnect(sessionId: int,
        callback?: Callback<EventCallbackInfo>): void
```

Unregisters connect event.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function offConnect(sessionId: int,        callback?: Callback<EventCallbackInfo>): void--><!--Device-abilityConnectionManager-function offConnect(sessionId: int,        callback?: Callback<EventCallbackInfo>): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | int | Yes | Ability connection Session id. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[EventCallbackInfo](arkts-distributedservice-abilityconnectionmanager-eventcallbackinfo-i.md)&gt; | No | Used to handle ('connect') command. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.2. Incorrect parameter types. |

