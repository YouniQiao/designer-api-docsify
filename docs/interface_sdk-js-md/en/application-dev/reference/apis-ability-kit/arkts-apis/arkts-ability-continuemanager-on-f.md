# on

## Modules to Import

```TypeScript
import { continueManager } from 'kits/@kit.AbilityKit';
```

## on('prepareContinue')

```TypeScript
function on(type: 'prepareContinue', context: Context, callback: AsyncCallback<ContinueResultInfo>): void
```

Registers a callback to obtain the quick start result when an application is launched quickly. This API uses an asynchronous callback to return the result.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'prepareContinue' | Yes |
| context | [Context](arkts-ability-context-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ContinueResultInfo](arkts-ability-continuemanager-continueresultinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16300501](../errorcode-DistributedSchedule.md#16300501-the-system-ability-works-abnormally) |
