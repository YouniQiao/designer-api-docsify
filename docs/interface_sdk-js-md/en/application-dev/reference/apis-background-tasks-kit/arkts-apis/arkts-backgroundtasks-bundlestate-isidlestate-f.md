# isIdleState

## Modules to Import

```TypeScript
import { bundleState } from 'kits/@kit.BackgroundTasksKit';
```

## isIdleState

```TypeScript
function isIdleState(bundleName: string, callback: AsyncCallback<boolean>): void
```

Checks whether the application specified by **bundleName** is in the idle state. A third-party application can only check the idle state of itself. A system application can check the idle state of other applications only when it is granted with the ohos.permission.BUNDLE_ACTIVE_INFO permission. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |


## isIdleState

```TypeScript
function isIdleState(bundleName: string): Promise<boolean>
```

Checks whether the application specified by **bundleName** is in the idle state. A third-party application can only check the idle state of itself. A system application can check the idle state of other applications only when it is granted with the ohos.permission.BUNDLE_ACTIVE_INFO permission. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |
