# ConditionVariable

实现异步等待功能的类，支持异步等待通知操作。该类使用@Sendable装饰器装饰。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Decorator:** @Sendable

<!--Device-locks-class ConditionVariable--><!--Device-locks-class ConditionVariable-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { ArkTSUtils } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor()
```

默认构造函数。创建一个异步等待通知操作的对象。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ConditionVariable-constructor()--><!--Device-ConditionVariable-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## notifyAll

```TypeScript
notifyAll(): void
```

通知所有等待的线程。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ConditionVariable-notifyAll(): void--><!--Device-ConditionVariable-notifyAll(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## notifyOne

```TypeScript
notifyOne(): void
```

通知第一个等待的线程。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ConditionVariable-notifyOne(): void--><!--Device-ConditionVariable-notifyOne(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## request

```TypeScript
static request(name: string): ConditionVariable
```

使用指定的名称查找或创建（如果未找到）异步等待通知操作的对象。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ConditionVariable-static request(name: string): ConditionVariable--><!--Device-ConditionVariable-static request(name: string): ConditionVariable-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 按指定名称查找或创建等待通知操作的对象名称，字符串无特别限制。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ConditionVariable](arkts-arkts-locks-conditionvariable-c.md) | 返回查找到或创建后的异步等待通知操作的实例。 |

## wait

```TypeScript
wait(): Promise<void>
```

异步调用进入等待中，将在被唤醒后继续执行。使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ConditionVariable-wait(): Promise<void>--><!--Device-ConditionVariable-wait(): Promise<void>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

## waitFor

```TypeScript
waitFor(timeout: number): Promise<void>
```

异步调用进入等待中，将在被唤醒或者等待时间结束后继续执行。使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ConditionVariable-waitFor(timeout: number): Promise<void>--><!--Device-ConditionVariable-waitFor(timeout: number): Promise<void>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeout | number | Yes | 等待时间，单位为毫秒，正整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

