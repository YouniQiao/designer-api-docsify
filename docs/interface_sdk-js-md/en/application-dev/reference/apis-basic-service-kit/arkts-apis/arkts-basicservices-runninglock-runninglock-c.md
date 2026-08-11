# RunningLock

Defines a **RunningLock** object.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-runningLock-class RunningLock--><!--Device-runningLock-class RunningLock-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

## Modules to Import

```TypeScript
import { runningLock } from 'kits/@kit.BasicServicesKit';
```

## hold

ArkTS-Dyn:
```TypeScript
hold(timeout: number): void
```

ArkTS-Sta:
```TypeScript
hold(timeout: int): void
```

Holds a running lock.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.RUNNING_LOCK

<!--Device-RunningLock-hold(timeout: int): void--><!--Device-RunningLock-hold(timeout: int): void-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeout | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Duration for locking and holding the **RunningLock** object, in ms.&lt;br&gt;The value must be a number:&lt;br&gt;**-1**: The lock is permanently held and needs to be released automatically.&lt;br&gt;**0**: The lock is released 3 seconds after the timer expires by default.&lt;br&gt;> 0: The lock is released based on the input value after the timer expires. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Incorrect parameter types; |
| [201](../../errorcode-universal.md#201-permission-denied) | If the permission is denied. |

## Examples

```TypeScript
// RunningLockTest.ets
class RunningLockTest {
    public static recordLock: runningLock.RunningLock;

    public static holdRunningLock(): void {
        if (RunningLockTest.recordLock) {
            RunningLockTest.recordLock.hold(500);
            console.info('hold running lock success');
        } else {
            runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL, (err: Error, lock: runningLock.RunningLock) => {
                if (typeof err === 'undefined') {
                    console.info('create running lock: ' + lock);
                    RunningLockTest.recordLock = lock;
                    try {
                        lock.hold(500);
                        console.info('hold running lock success');
                    } catch(err) {
                        console.error('hold running lock failed, err: ' + err);
                    }
                } else {
                    console.error('create running lock failed, err: ' + err);
                }
            });
        }
    }
}
```

## isHolding

```TypeScript
isHolding(): boolean
```

Checks whether this running lock is being held.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RunningLock-isHolding(): boolean--><!--Device-RunningLock-isHolding(): boolean-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | The value **true** indicates that the **RunningLock** object is held; and the value **false** indicates that the **RunningLock** object is released. |

## Examples

```TypeScript
// RunningLockTest.ets
class RunningLockTest {
    public static recordLock: runningLock.RunningLock;

    public static isHoldingRunningLock(): void {
        if (RunningLockTest.recordLock) {
            let isHolding = RunningLockTest.recordLock.isHolding();
            console.info('check running lock holding status: ' + isHolding);
        } else {
            runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL, (err: Error, lock: runningLock.RunningLock) => {
                if (typeof err === 'undefined') {
                    console.info('create running lock: ' + lock);
                    RunningLockTest.recordLock = lock;
                    let isHolding = lock.isHolding();
                    console.info('check running lock holding status: ' + isHolding);
                } else {
                    console.error('create running lock failed, err: ' + err);
                }
            });
        }
    }
}
```

## isUsed

```TypeScript
isUsed(): boolean
```

Checks whether this running lock is used.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [runningLock.RunningLock.isHolding](arkts-basicservices-runninglock-runninglock-c.md#isholding)

<!--Device-RunningLock-isUsed(): boolean--><!--Device-RunningLock-isUsed(): boolean-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the lock is held or in use; returns false if the lock has been released. |

## Examples

```TypeScript
runningLock.createRunningLock('running_lock_test', runningLock.RunningLockType.BACKGROUND)
.then((lock: runningLock.RunningLock) => {
    let isUsed = lock.isUsed();
    console.info('check running lock used status: ' + isUsed);
})
.catch((err: Error) => {
    console.error('check running lock used status failed, err: ' + err);
});
```

## lock

```TypeScript
lock(timeout: number): void
```

Locks and holds a **RunningLock** object.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [runningLock.RunningLock.hold](arkts-basicservices-runninglock-runninglock-c.md#hold)

**Required permissions:** ohos.permission.RUNNING_LOCK

<!--Device-RunningLock-lock(timeout: number): void--><!--Device-RunningLock-lock(timeout: number): void-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeout | number | Yes | Duration for locking and holding the **RunningLock** object, in ms. |

## Examples

```TypeScript
runningLock.createRunningLock('running_lock_test', runningLock.RunningLockType.BACKGROUND)
.then((lock: runningLock.RunningLock) => {
    lock.lock(500);
    console.info('create running lock and lock success');
})
.catch((err: Error) => {
    console.error('create running lock failed, err: ' + err);
});
```

## unhold

```TypeScript
unhold(): void
```

Releases this running lock.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.RUNNING_LOCK

<!--Device-RunningLock-unhold(): void--><!--Device-RunningLock-unhold(): void-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | If the permission is denied. |

## Examples

```TypeScript
// RunningLockTest.ets
class RunningLockTest {
    public static recordLock: runningLock.RunningLock;

    public static unholdRunningLock(): void {
        if (RunningLockTest.recordLock) {
            RunningLockTest.recordLock.unhold();
            console.info('unhold running lock success');
        } else {
            runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL, (err: Error, lock: runningLock.RunningLock) => {
                if (typeof err === 'undefined') {
                    console.info('create running lock: ' + lock);
                    RunningLockTest.recordLock = lock;
                    try {
                        lock.unhold();
                        console.info('unhold running lock success');
                    } catch(err) {
                        console.error('unhold running lock failed, err: ' + err);
                    }
                } else {
                    console.error('create running lock failed, err: ' + err);
                }
            });
        }
    }
}
```

## unlock

```TypeScript
unlock(): void
```

Releases this running lock.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [runningLock.RunningLock.unhold](arkts-basicservices-runninglock-runninglock-c.md#unhold)

**Required permissions:** ohos.permission.RUNNING_LOCK

<!--Device-RunningLock-unlock(): void--><!--Device-RunningLock-unlock(): void-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

## Examples

```TypeScript
runningLock.createRunningLock('running_lock_test', runningLock.RunningLockType.BACKGROUND)
.then((lock: runningLock.RunningLock) => {
    lock.unlock();
    console.info('create running lock and unlock success');
})
.catch((err: Error) => {
    console.error('create running lock failed, err: ' + err);
});
```

