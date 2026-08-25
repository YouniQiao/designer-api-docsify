# AsyncLock

实现异步锁功能的类，允许在锁下执行异步操作。该类使用@Sendable装饰器装饰。

**起始版本：** 12

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { ArkTSUtils } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor()
```

默认构造函数。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## lockAsync

```TypeScript
lockAsync<T>(callback: AsyncLockCallback<T>): Promise<T>
```

在获取的锁下执行操作。该方法首先获取锁，然后调用回调，最后释放锁。若锁已被其他任务持有，当前请求将进入等待队列，待锁释放后按顺序获取锁。回调在调用lockAsync的同一线程中以异步方式执行。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncLockCallback](arkts-arkts-locks-asynclockcallback-t.md)&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;T & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200030](../errorcode-utils.md#10200030-锁不存在) |

## lockAsync

```TypeScript
lockAsync<T>(callback: AsyncLockCallback<T>, mode: AsyncLockMode): Promise<T>
```

在获取的锁下执行操作。该方法首先获取锁，然后调用回调，最后释放锁。若锁已被其他任务持有，当前请求将进入等待队列，待锁释放后按顺序获取锁。回调在调用lockAsync的同一线程中以异步方式执行。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncLockCallback](arkts-arkts-locks-asynclockcallback-t.md)&lt;T&gt; | 是 |
| mode | [AsyncLockMode](arkts-arkts-locks-asynclockmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;T & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200030](../errorcode-utils.md#10200030-锁不存在) |

## lockAsync

```TypeScript
lockAsync<T, U>(callback: AsyncLockCallback<T>, mode: AsyncLockMode,
        options: AsyncLockOptions<U>): Promise<T | U>
```

在获取的锁下执行操作。该方法首先获取锁，然后调用回调，最后释放锁。回调在调用lockAsync的同一线程中以异步方式执行。 在[AsyncLockOptions](arkts-arkts-locks-asynclockoptions-c.md)中可以提供一个可选的超时值。在这种情况下，如果超时前未能获取锁，lockAsync将返回被拒绝的Promise并带上一个BusinessError实例。 这种情况下，错误信息将包含持有的锁和等待的锁的信息以及可能的死锁警告。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncLockCallback](arkts-arkts-locks-asynclockcallback-t.md)&lt;T&gt; | 是 |
| mode | [AsyncLockMode](arkts-arkts-locks-asynclockmode-e.md) | 是 |
| options | [AsyncLockOptions](arkts-arkts-locks-asynclockoptions-c.md)&lt;U&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;T \ | U & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200030](../errorcode-utils.md#10200030-锁不存在) |
| [10200031](../errorcode-utils.md#10200031-lockasync超时) |

## query

```TypeScript
static query(name: string): AsyncLockState
```

查询指定异步锁的信息。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [name](#name) | string | 是 |

**返回值：**

| 类型 |
| --- |
| [AsyncLockState](arkts-arkts-locks-asynclockstate-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [10200030](../errorcode-utils.md#10200030-锁不存在) |

## queryAll

```TypeScript
static queryAll(): AsyncLockState[]
```

查询所有现有锁的信息。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [AsyncLockState](arkts-arkts-locks-asynclockstate-c.md)[] |

## request

```TypeScript
static request(name: string): AsyncLock
```

使用指定的名称查找或创建AsyncLock实例。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [name](#name) | string | 是 |

**返回值：**

| 类型 |
| --- |
| [AsyncLock](arkts-arkts-locks-asynclock-c.md) |

## name

```TypeScript
readonly name: string
```

锁的名称。

**类型：** string

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang
