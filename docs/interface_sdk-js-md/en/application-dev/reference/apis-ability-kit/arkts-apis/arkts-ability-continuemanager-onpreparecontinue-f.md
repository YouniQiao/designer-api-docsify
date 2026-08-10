# onPrepareContinue

## Modules to Import

```TypeScript
import { continueManager } from 'kits/@kit.AbilityKit';
```

## onPrepareContinue

```TypeScript
function onPrepareContinue(context: Context, callback: AsyncCallback<ContinueResultInfo>): void
```

prepareContinue 事件，当在 continueType 中配置了“ContinueQuickStart”功能时，即可获取

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-continueManager-function onPrepareContinue(context: Context, callback: AsyncCallback<ContinueResultInfo>): void--><!--Device-continueManager-function onPrepareContinue(context: Context, callback: AsyncCallback<ContinueResultInfo>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | Yes | the ability context. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ContinueResultInfo&gt; | Yes | Used to handle ('prepareContinue') command. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16300501 | the system ability work abnormally. |

