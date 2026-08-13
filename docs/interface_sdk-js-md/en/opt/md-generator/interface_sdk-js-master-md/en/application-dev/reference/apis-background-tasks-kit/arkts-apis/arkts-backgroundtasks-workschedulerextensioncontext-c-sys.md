# WorkSchedulerExtensionContext

The **WorkSchedulerExtensionContext** module, inherited from [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md#ExtensionContext), provides a context environment for the **WorkSchedulerExtensionAbility**. This module provides APIs for accessing the resources of a **WorkSchedulerExtensionAbility**.

**Inheritance/Implementation:** WorkSchedulerExtensionContext extends ExtensionContext

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare class WorkSchedulerExtensionContext--><!--Device-unnamed-declare class WorkSchedulerExtensionContext-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## startServiceExtensionAbility

```TypeScript
startServiceExtensionAbility(want: Want): Promise<void>
```

Starts a **ServiceExtensionAbility**. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkSchedulerExtensionContext-startServiceExtensionAbility(want: Want): Promise<void>--><!--Device-WorkSchedulerExtensionContext-startServiceExtensionAbility(want: Want): Promise<void>-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000004](../../apis-ability-kit/errorcode-ability.md#16000004-visibility-verification-failure) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000005](../../apis-ability-kit/errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../../apis-ability-kit/errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000001](../../apis-ability-kit/errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../../apis-ability-kit/errorcode-ability.md#16000002-incorrect-ability-type) |
| [16200001](../../apis-ability-kit/errorcode-ability.md#16200001-caller-released) |
| [16000012](../../apis-ability-kit/errorcode-ability.md#16000012-application-under-control) |
| [16000013](../../apis-ability-kit/errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000008](../../apis-ability-kit/errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-context-does-not-exist) |

## Examples

```TypeScript
import { WorkSchedulerExtensionAbility, workScheduler } from '@kit.BackgroundTasksKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let want : Want = {
  bundleName: 'com.example.workscheduler',
  abilityName: 'ServiceExtAbility'
}

export default class MyWorkSchedulerExtensionAbility extends WorkSchedulerExtensionAbility {
  onWorkStart(workInfo: workScheduler.WorkInfo) {
    console.info(`onWorkStart, workInfo = ${JSON.stringify(workInfo)}`);
      // Start the corresponding service.
      this.context.startServiceExtensionAbility(want).then(() => {
        console.info('succeeded in starting ServiceExtensionAbility.');
      }).catch ((err: BusinessError) => {
        console.error('failed to start ServiceExtensionAbility.');
      });
  }

  onWorkStop(workInfo: workScheduler.WorkInfo) {
    console.info(`onWorkStop, workInfo is ${JSON.stringify(workInfo)}`);
  }
}
```

## stopServiceExtensionAbility

```TypeScript
stopServiceExtensionAbility(want: Want): Promise<void>
```

Stops a **ServiceExtensionAbility**. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkSchedulerExtensionContext-stopServiceExtensionAbility(want: Want): Promise<void>--><!--Device-WorkSchedulerExtensionContext-stopServiceExtensionAbility(want: Want): Promise<void>-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000004](../../apis-ability-kit/errorcode-ability.md#16000004-visibility-verification-failure) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000005](../../apis-ability-kit/errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../../apis-ability-kit/errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000001](../../apis-ability-kit/errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../../apis-ability-kit/errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [16200001](../../apis-ability-kit/errorcode-ability.md#16200001-caller-released) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-context-does-not-exist) |

## Examples

```TypeScript
import { WorkSchedulerExtensionAbility, workScheduler } from '@kit.BackgroundTasksKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let want : Want = {
  bundleName: 'com.example.workscheduler',
  abilityName: 'ServiceExtAbility'
}

export default class MyWorkSchedulerExtensionAbility extends WorkSchedulerExtensionAbility {
  onWorkStart(workInfo: workScheduler.WorkInfo) {
    console.info(`onWorkStart, workInfo = ${JSON.stringify(workInfo)}`);
  }

  onWorkStop(workInfo: workScheduler.WorkInfo) {
    console.info(`onWorkStop, workInfo is ${JSON.stringify(workInfo)}`);
      // Stop the corresponding service.
      this.context.stopServiceExtensionAbility(want).then(() => {
        console.info('succeeded in stopping ServiceExtensionAbility.');
      }).catch ((err: BusinessError) => {
        console.error('failed to stop ServiceExtensionAbility.');
      });
  }
}
```
