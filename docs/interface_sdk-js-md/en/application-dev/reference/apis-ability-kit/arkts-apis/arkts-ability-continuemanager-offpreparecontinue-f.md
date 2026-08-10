# offPrepareContinue

## Modules to Import

```TypeScript
import { continueManager } from 'kits/@kit.AbilityKit';
```

## offPrepareContinue

```TypeScript
function offPrepareContinue(context: Context, callback?: AsyncCallback<ContinueResultInfo>): void
```

Unregister prepareContinue event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-continueManager-function offPrepareContinue(context: Context, callback?: AsyncCallback<ContinueResultInfo>): void--><!--Device-continueManager-function offPrepareContinue(context: Context, callback?: AsyncCallback<ContinueResultInfo>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | Yes | the ability context. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ContinueResultInfo&gt; | No | Used to handle ('prepareContinue') command. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16300501 | the system ability work abnormally. |

