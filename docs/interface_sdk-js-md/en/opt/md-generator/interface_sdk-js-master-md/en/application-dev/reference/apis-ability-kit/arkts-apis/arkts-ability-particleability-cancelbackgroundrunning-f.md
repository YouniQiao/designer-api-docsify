# cancelBackgroundRunning

## Modules to Import

```TypeScript
import { particleAbility } from '@kit.AbilityKit';
```

## cancelBackgroundRunning

```TypeScript
function cancelBackgroundRunning(callback: AsyncCallback<void>): void
```

Requests to cancel a continuous task from the system. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [stopBackgroundRunning](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-backgroundtaskmanager-stopbackgroundrunning-f.md#stopBackgroundRunning)

**Model restriction:** This API can be used only in the FA model.

<!--Device-particleAbility-function cancelBackgroundRunning(callback: AsyncCallback<void>): void--><!--Device-particleAbility-function cancelBackgroundRunning(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import { particleAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback(error: BusinessError, data: void) {
  if (error && error.code !== 0) {
    console.error(`Operation failed error: ${JSON.stringify(error)}`);
  } else {
    console.info(`Operation succeeded, data: ${data}`);
  }
}

particleAbility.cancelBackgroundRunning(callback);
```


## cancelBackgroundRunning

```TypeScript
function cancelBackgroundRunning(): Promise<void>
```

Requests to cancel a continuous task from the system. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [stopBackgroundRunning](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-backgroundtaskmanager-stopbackgroundrunning-f.md#stopBackgroundRunning)

**Model restriction:** This API can be used only in the FA model.

<!--Device-particleAbility-function cancelBackgroundRunning(): Promise<void>--><!--Device-particleAbility-function cancelBackgroundRunning(): Promise<void>-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## Examples

```TypeScript
import { particleAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

particleAbility.cancelBackgroundRunning().then(() => {
  console.info('Operation succeeded');
}).catch((err: BusinessError) => {
  console.error(`Operation failed cause: ${JSON.stringify(err)}`);
});
```
