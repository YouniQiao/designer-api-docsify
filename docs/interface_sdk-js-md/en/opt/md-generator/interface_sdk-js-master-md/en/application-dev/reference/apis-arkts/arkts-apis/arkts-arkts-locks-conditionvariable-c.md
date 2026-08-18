# ConditionVariable

Object used for thread synchronization.

**Since:** 18

<!--Device-locks-class ConditionVariable--><!--Device-locks-class ConditionVariable-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

Default constructor.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ConditionVariable-constructor()--><!--Device-ConditionVariable-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## notifyAll

```TypeScript
notifyAll(): void
```

Notify all waiting promise.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ConditionVariable-notifyAll(): void--><!--Device-ConditionVariable-notifyAll(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## notifyOne

```TypeScript
notifyOne(): void
```

Notify one waiting promise.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ConditionVariable-notifyOne(): void--><!--Device-ConditionVariable-notifyOne(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## request

```TypeScript
static request(name: string): ConditionVariable
```

Find or create an instance of ConditionVariable using the specified name.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ConditionVariable-static request(name: string): ConditionVariable--><!--Device-ConditionVariable-static request(name: string): ConditionVariable-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [ConditionVariable](arkts-arkts-locks-conditionvariable-c.md) |

## wait

```TypeScript
wait(): Promise<void>
```

Waits for the ConditionVariable to be notified.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ConditionVariable-wait(): Promise<void>--><!--Device-ConditionVariable-wait(): Promise<void>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## waitFor

```TypeScript
waitFor(timeout: number): Promise<void>
```

Waits for the ConditionVariable to be notified, or until the specified time limit is reached.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ConditionVariable-waitFor(timeout: number): Promise<void>--><!--Device-ConditionVariable-waitFor(timeout: number): Promise<void>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeout | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
