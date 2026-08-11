# offReceiveMessage

## Modules to Import

```TypeScript
import { abilityConnectionManager } from 'kits/@kit.DistributedServiceKit';
```

## offReceiveMessage

```TypeScript
function offReceiveMessage(sessionId: int,
        callback?: Callback<EventCallbackInfo>): void
```

Unregisters receiveMessage event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function offReceiveMessage(sessionId: int,        callback?: Callback<EventCallbackInfo>): void--><!--Device-abilityConnectionManager-function offReceiveMessage(sessionId: int,        callback?: Callback<EventCallbackInfo>): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | int | Yes | Ability connection Session id. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;EventCallbackInfo&gt; | No | Used to handle ('receiveMessage') command. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.2. Incorrect parameter types. |

