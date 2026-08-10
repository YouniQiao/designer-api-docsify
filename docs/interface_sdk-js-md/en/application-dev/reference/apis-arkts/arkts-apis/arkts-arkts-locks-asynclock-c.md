# AsyncLock

实现异步锁功能的类，允许在锁下执行异步操作。该类使用@Sendable装饰器装饰。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Decorator:** @Sendable

<!--Device-locks-class AsyncLock--><!--Device-locks-class AsyncLock-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { ArkTSUtils } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor()
```

默认构造函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyncLock-constructor()--><!--Device-AsyncLock-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## lockAsync

```TypeScript
lockAsync<T>(callback: AsyncLockCallback<T>): Promise<T>
```

在获取的锁下执行操作。该方法首先获取锁，然后调用回调，最后释放锁。若锁已被其他任务持有，当前请求将进入等待队列，待锁释放后按顺序获取锁。回调在调用lockAsync的同一线程中以异步方式执行。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyncLock-lockAsync<T>(callback: AsyncLockCallback<T>): Promise<T>--><!--Device-AsyncLock-lockAsync<T>(callback: AsyncLockCallback<T>): Promise<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncLockCallback](arkts-arkts-locks-asynclockcallback-t.md)&lt;T&gt; | Yes | 获取锁后要调用的函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;T&gt; | 回调执行后将解决的Promise。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200030 | The lock does not exist. |

## lockAsync

```TypeScript
lockAsync<T>(callback: AsyncLockCallback<T>, mode: AsyncLockMode): Promise<T>
```

在获取的锁下执行操作。该方法首先获取锁，然后调用回调，最后释放锁。若锁已被其他任务持有，当前请求将进入等待队列，待锁释放后按顺序获取锁。回调在调用lockAsync的同一线程中以异步方式执行。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyncLock-lockAsync<T>(callback: AsyncLockCallback<T>, mode: AsyncLockMode): Promise<T>--><!--Device-AsyncLock-lockAsync<T>(callback: AsyncLockCallback<T>, mode: AsyncLockMode): Promise<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncLockCallback](arkts-arkts-locks-asynclockcallback-t.md)&lt;T&gt; | Yes | 获取锁后要调用的函数。 |
| mode | [AsyncLockMode](arkts-arkts-locks-asynclockmode-e.md) | Yes | 锁的操作模式。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;T&gt; | 回调执行后将解决的Promise。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200030 | The lock does not exist. |

## lockAsync

```TypeScript
lockAsync<T, U>(callback: AsyncLockCallback<T>, mode: AsyncLockMode,
        options: AsyncLockOptions<U>): Promise<T | U>
```

在获取的锁下执行操作。该方法首先获取锁，然后调用回调，最后释放锁。回调在调用lockAsync的同一线程中以异步方式执行。在{@link AsyncLockOptions}中可以提供一个可选的超时值。在这种情况下，如果超时前未能获取锁，lockAsync将返回被拒绝的Promise并带上一个BusinessError实例。这种情况下，错误信息将包含持有的锁和等待的锁的信息以及可能的死锁警告。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyncLock-lockAsync<T, U>(callback: AsyncLockCallback<T>, mode: AsyncLockMode,        options: AsyncLockOptions<U>): Promise<T | U>--><!--Device-AsyncLock-lockAsync<T, U>(callback: AsyncLockCallback<T>, mode: AsyncLockMode,        options: AsyncLockOptions<U>): Promise<T | U>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncLockCallback](arkts-arkts-locks-asynclockcallback-t.md)&lt;T&gt; | Yes | 获取锁后要调用的函数。 |
| mode | [AsyncLockMode](arkts-arkts-locks-asynclockmode-e.md) | Yes | 锁的操作模式。 |
| options | [AsyncLockOptions](arkts-arkts-locks-asynclockoptions-c.md)&lt;U&gt; | Yes | 锁的操作选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;T \| U&gt; | 回调执行后解决的Promise，或者在超时情况下被拒绝。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200031 | Timeout exceeded. |
| 10200030 | The lock does not exist. |

## query

```TypeScript
static query(name: string): AsyncLockState
```

查询指定异步锁的信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyncLock-static query(name: string): AsyncLockState--><!--Device-AsyncLock-static query(name: string): AsyncLockState-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 要查询的锁的名称，仅可查询通过request接口获取的锁（即与request接口入参锁名称保持一致）。 |

**Return value:**

| Type | Description |
| --- | --- |
| [AsyncLockState](arkts-arkts-locks-asynclockstate-c.md) | 包含状态描述的异步锁状态实例。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200030 | The lock does not exist. |

## queryAll

```TypeScript
static queryAll(): AsyncLockState[]
```

查询所有现有锁的信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyncLock-static queryAll(): AsyncLockState[]--><!--Device-AsyncLock-static queryAll(): AsyncLockState[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [AsyncLockState](arkts-arkts-locks-asynclockstate-c.md)[] | 包含锁状态信息的异步锁状态数组。 |

## request

```TypeScript
static request(name: string): AsyncLock
```

使用指定的名称查找或创建AsyncLock实例。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyncLock-static request(name: string): AsyncLock--><!--Device-AsyncLock-static request(name: string): AsyncLock-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 要查找或创建的锁的名称。 |

**Return value:**

| Type | Description |
| --- | --- |
| [AsyncLock](arkts-arkts-locks-asynclock-c.md) | 返回AsyncLock实例。 |

## name

```TypeScript
readonly name: string
```

锁的名称。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyncLock-readonly name: string--><!--Device-AsyncLock-readonly name: string-End-->

**System capability:** SystemCapability.Utils.Lang

