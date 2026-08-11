# createRunningLock

## Modules to Import

```TypeScript
import { runningLock } from 'kits/@kit.BasicServicesKit';
```

## createRunningLock

```TypeScript
function createRunningLock(name: string, type: RunningLockType, callback: AsyncCallback<RunningLock>): void
```

Creates a {@link RunningLock} object. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [runningLock.create](arkts-basicservices-runninglock-create-f.md#create)

**Required permissions:** ohos.permission.RUNNING_LOCK

<!--Device-runningLock-function createRunningLock(name: string, type: RunningLockType, callback: AsyncCallback<RunningLock>): void--><!--Device-runningLock-function createRunningLock(name: string, type: RunningLockType, callback: AsyncCallback<RunningLock>): void-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| type | [RunningLockType](arkts-basicservices-runninglock-runninglocktype-e.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;RunningLock&gt; | Yes |

## Examples

```TypeScript
runningLock.createRunningLock('running_lock_test', runningLock.RunningLockType.BACKGROUND, (err: Error, lock: runningLock.RunningLock) => {
    if (typeof err === 'undefined') {
        console.info('created running lock: ' + lock);
    } else {
        console.error('create running lock failed, err: ' + err);
    }
});
```


## createRunningLock

```TypeScript
function createRunningLock(name: string, type: RunningLockType): Promise<RunningLock>
```

Creates a {@link RunningLock} object. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [runningLock.create](arkts-basicservices-runninglock-create-f.md#create)

**Required permissions:** ohos.permission.RUNNING_LOCK

<!--Device-runningLock-function createRunningLock(name: string, type: RunningLockType): Promise<RunningLock>--><!--Device-runningLock-function createRunningLock(name: string, type: RunningLockType): Promise<RunningLock>-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| type | [RunningLockType](arkts-basicservices-runninglock-runninglocktype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;RunningLock&gt; |

## Examples

```TypeScript
runningLock.createRunningLock('running_lock_test', runningLock.RunningLockType.BACKGROUND)
.then((lock: runningLock.RunningLock) => {
    console.info('created running lock: ' + lock);
})
.catch((err: Error) => {
    console.error('create running lock failed, err: ' + err);
});
```
