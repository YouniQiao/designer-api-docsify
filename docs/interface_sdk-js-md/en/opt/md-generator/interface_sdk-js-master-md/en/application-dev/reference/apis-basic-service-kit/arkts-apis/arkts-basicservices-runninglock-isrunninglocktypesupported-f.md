# isRunningLockTypeSupported

## Modules to Import

```TypeScript
import { runningLock } from 'kits/@kit.BasicServicesKit';
```

## isRunningLockTypeSupported

```TypeScript
function isRunningLockTypeSupported(type: RunningLockType, callback: AsyncCallback<boolean>): void
```

Checks whether a specified type of {@link RunningLock} is supported. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [runningLock.isSupported](arkts-basicservices-runninglock-issupported-f.md#issupported)

<!--Device-runningLock-function isRunningLockTypeSupported(type: RunningLockType, callback: AsyncCallback<boolean>): void--><!--Device-runningLock-function isRunningLockTypeSupported(type: RunningLockType, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [RunningLockType](arkts-basicservices-runninglock-runninglocktype-e.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## Examples

```TypeScript
runningLock.isRunningLockTypeSupported(runningLock.RunningLockType.BACKGROUND, (err: Error, data: boolean) => {
    if (typeof err === 'undefined') {
        console.info('BACKGROUND lock support status: ' + data);
    } else {
        console.error('check BACKGROUND lock support status failed, err: ' + err);
    }
});
```


## isRunningLockTypeSupported

```TypeScript
function isRunningLockTypeSupported(type: RunningLockType): Promise<boolean>
```

Checks whether a specified type of {@link RunningLock} is supported. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [runningLock.isSupported](arkts-basicservices-runninglock-issupported-f.md#issupported)

<!--Device-runningLock-function isRunningLockTypeSupported(type: RunningLockType): Promise<boolean>--><!--Device-runningLock-function isRunningLockTypeSupported(type: RunningLockType): Promise<boolean>-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [RunningLockType](arkts-basicservices-runninglock-runninglocktype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

## Examples

```TypeScript
runningLock.isRunningLockTypeSupported(runningLock.RunningLockType.BACKGROUND)
.then((data: boolean) => {
    console.info('BACKGROUND lock support status: ' + data);
})
.catch((err: Error) => {
    console.error('check BACKGROUND lock support status failed, err: ' + err);
});
```
