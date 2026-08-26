# locks(Defines the utils for ArkTS)

Asynchronous lock.

**Since:** 12

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import ArkTSUtils from '@kit.ArkTS';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [AsyncLock(Defines the utils for ArkTS)](arkts-arkts-locks-asynclock-c.md) | Class to execute an asynchronous operation under lock. |
| [AsyncLockOptions(Defines the utils for ArkTS)](arkts-arkts-locks-asynclockoptions-c.md) | Lock operation's options |
| [AsyncLockState(Defines the utils for ArkTS)](arkts-arkts-locks-asynclockstate-c.md) | Information about all lock operations on the AsyncLock instance. |
| [AsyncLockInfo(Defines the utils for ArkTS)](arkts-arkts-locks-asynclockinfo-c.md) | Information about a lock. |
| [AbortSignal(Defines the utils for ArkTS)](arkts-arkts-locks-abortsignal-c.md) | Object used to abort an async operation. An instance of this class must be accessed in the same thread where the instance is created. Access to fields of this class from another thread is undefined behaviour. |
| [ConditionVariable(Defines the utils for ArkTS)](arkts-arkts-locks-conditionvariable-c.md) | Object used for thread synchronization. |

### Enums

| Name | Description |
| --- | --- |
| [AsyncLockMode(Defines the utils for ArkTS)](arkts-arkts-locks-asynclockmode-e.md) | Mode of lock operations. |

### Types

| Name | Description |
| --- | --- |
| [AsyncLockCallback(Defines the utils for ArkTS)](arkts-arkts-locks-asynclockcallback-t.md) | Type of callback for asyncLock operation. |
