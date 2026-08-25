# locks(Defines the utils for ArkTS)

为了解决多并发实例间的数据竞争问题，ArkTS语言基础库引入了异步锁能力。为了开发者的开发效率，AsyncLock对象支持跨并发实例引用传递。由于ArkTS语言支持异步操作，阻塞锁容易产生死锁问题，因此我们在ArkTS中仅支持异步锁（非阻塞式锁）。使用异步锁的方法需要标记为async，调用方需要使用await等待调用结果，才能保证时序正确。因此会导致外层调用函数全部标记成async。

**起始版本：** 12

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { ArkTSUtils } from 'kits/@kit.ArkTS';
```

## 汇总

### 类

| 名称 |
| --- |
| [AsyncLock(Defines the utils for ArkTS)](arkts-arkts-locks-asynclock-c.md) |
| [AsyncLockOptions(Defines the utils for ArkTS)](arkts-arkts-locks-asynclockoptions-c.md) |
| [AsyncLockState(Defines the utils for ArkTS)](arkts-arkts-locks-asynclockstate-c.md) |
| [AsyncLockInfo(Defines the utils for ArkTS)](arkts-arkts-locks-asynclockinfo-c.md) |
| [AbortSignal(Defines the utils for ArkTS)](arkts-arkts-locks-abortsignal-c.md) |
| [ConditionVariable(Defines the utils for ArkTS)](arkts-arkts-locks-conditionvariable-c.md) |

### 枚举

| 名称 |
| --- |
| [AsyncLockMode(Defines the utils for ArkTS)](arkts-arkts-locks-asynclockmode-e.md) |

### 类型

| 名称 |
| --- |
| [AsyncLockCallback(Defines the utils for ArkTS)](arkts-arkts-locks-asynclockcallback-t.md) |
