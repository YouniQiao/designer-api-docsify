# offPrepareContinue

## Modules to Import

```TypeScript
import { continueManager } from 'continueManager';
```

## offPrepareContinue

```TypeScript
function offPrepareContinue(context: Context, callback?: AsyncCallback<ContinueResultInfo>): void
```

Unregister prepareContinue event.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-continueManager-function offPrepareContinue(context: Context, callback?: AsyncCallback<ContinueResultInfo>): void--><!--Device-continueManager-function offPrepareContinue(context: Context, callback?: AsyncCallback<ContinueResultInfo>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | Yes | the ability context. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ContinueResultInfo](arkts-ability-continuemanager-continueresultinfo-i.md)&gt; | No | Used to handle ('prepareContinue') command. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16300501](../errorcode-DistributedSchedule.md#16300501-the-system-ability-works-abnormally) | the system ability work abnormally. |

