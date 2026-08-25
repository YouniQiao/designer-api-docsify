# isRunningInStabilityTest

## Modules to Import

```TypeScript
```

## isRunningInStabilityTest

```TypeScript
function isRunningInStabilityTest(callback: AsyncCallback<boolean>): void
```

Checks whether the system is undergoing a stability test. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> A stability test scenario refers to a specific testing environment designed to verify application reliability
> under complex, extreme, or number-term operating conditions.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isRunningInStabilityTest](arkts-ability-appmanager-isrunninginstabilitytest-f.md)

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |


## isRunningInStabilityTest

```TypeScript
function isRunningInStabilityTest(): Promise<boolean>
```

Checks whether the system is undergoing a stability test. This API uses a promise to return the result.

> **NOTE：**&gt;
> A stability test scenario refers to a specific testing environment designed to verify application reliability
> under complex, extreme, or number-term operating conditions.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isRunningInStabilityTest](arkts-ability-appmanager-isrunninginstabilitytest-f.md)

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |
