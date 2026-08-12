# WorkSchedulerExtensionContext

The **WorkSchedulerExtensionContext** module, inherited from   
[ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md#ExtensionContext), provides a context environment for the   
**WorkSchedulerExtensionAbility**.

This module provides APIs for accessing the resources of a **WorkSchedulerExtensionAbility**.

**Inheritance/Implementation:** WorkSchedulerExtensionContext extends [ExtensionContext](ExtensionContext)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class WorkSchedulerExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class WorkSchedulerExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## startServiceExtensionAbility

```TypeScript
startServiceExtensionAbility(want: Want): Promise<void>
```

Starts a **ServiceExtensionAbility**. This API uses a promise to return the result.

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkSchedulerExtensionContext-startServiceExtensionAbility(want: Want): Promise<void>--><!--Device-WorkSchedulerExtensionContext-startServiceExtensionAbility(want: Want): Promise<void>-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Information about the **Want** used for starting an ability. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) | Internal error. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [16000004](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000004-visibility-verification-failure) | Can not start invisible component. |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000005](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16200001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [16000012](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000012-application-under-control) | The application is controlled. |
| [16000013](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000013-application-controlled-by-edm) | The application is controlled by EDM. |
| [16000008](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires. |
| [16000011](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

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

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkSchedulerExtensionContext-stopServiceExtensionAbility(want: Want): Promise<void>--><!--Device-WorkSchedulerExtensionContext-stopServiceExtensionAbility(want: Want): Promise<void>-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Information about the **Want** used for stopping an ability. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000004](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000004-visibility-verification-failure) | Can not start invisible component. |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000005](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16000050](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16200001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [16000011](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

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

