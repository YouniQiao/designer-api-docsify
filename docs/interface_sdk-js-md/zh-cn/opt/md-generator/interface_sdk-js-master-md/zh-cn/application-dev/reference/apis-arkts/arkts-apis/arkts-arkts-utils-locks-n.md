# locks

为了解决多并发实例间的数据竞争问题，ArkTS语言基础库引入了异步锁能力。为了开发者的开发效率，AsyncLock对象支持跨并发实例引用传递。 由于ArkTS语言支持异步操作，阻塞锁容易产生死锁问题，因此我们在ArkTS中仅支持异步锁（非阻塞式锁）。 使用异步锁的方法需要标记为async，调用方需要使用await等待调用结果，才能保证时序正确。因此会导致外层调用函数全部标记成async。

**起始版本：** 12

**废弃版本：** -1

<!--Device-utils-namespace locks--><!--Device-utils-namespace locks-End-->

**系统能力：** SystemCapability.Utils.Lang

## 汇总

### 类

| 名称 |
| --- |
| [AsyncLock](arkts-arkts-locks-asynclock-c.md) |
| [AsyncLockOptions](arkts-arkts-locks-asynclockoptions-c.md) |
| [AsyncLockState](arkts-arkts-locks-asynclockstate-c.md) |
| [AsyncLockInfo](arkts-arkts-locks-asynclockinfo-c.md) |
| [AbortSignal](arkts-arkts-locks-abortsignal-c.md) |
| [ConditionVariable](arkts-arkts-locks-conditionvariable-c.md) |

### 枚举

| 名称 |
| --- |
| [AsyncLockMode](arkts-arkts-locks-asynclockmode-e.md) |

### 类型

| 名称 |
| --- |
| [AsyncLockCallback](arkts-arkts-locks-asynclockcallback-t.md) |
