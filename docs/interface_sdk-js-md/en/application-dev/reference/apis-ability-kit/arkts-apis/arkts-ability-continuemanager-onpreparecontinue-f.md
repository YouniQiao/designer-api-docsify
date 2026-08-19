# onPrepareContinue

## Modules to Import

```TypeScript
import { continueManager } from '@kit.AbilityKit';
```

## onPrepareContinue

```TypeScript
function onPrepareContinue(context: Context, callback: AsyncCallback<ContinueResultInfo>): void
```

Register prepareContinue event, when the ability is configured with 'ContinueQuickStart' in the continueType, then can get the result of LaunchReason.PREPARE_CONTINUATION.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-continueManager-function onPrepareContinue(context: Context, callback: AsyncCallback<ContinueResultInfo>): void--><!--Device-continueManager-function onPrepareContinue(context: Context, callback: AsyncCallback<ContinueResultInfo>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | Yes | the ability context. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[ContinueResultInfo](arkts-ability-continuemanager-continueresultinfo-i.md)&gt; | Yes | Used to handle ('prepareContinue') command. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16300501](../errorcode-DistributedSchedule.md#16300501-the-system-ability-works-abnormally) | the system ability work abnormally. |

