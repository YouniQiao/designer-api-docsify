# unregisterApplicationStateObserver (System API)

## Modules to Import

```TypeScript
```

## unregisterApplicationStateObserver

```TypeScript
function unregisterApplicationStateObserver(observerId: number, callback: AsyncCallback<void>): void
```

Unregister application state observer.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [off](arkts-ability-appmanager-off-f.md#offapplicationstate)

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| observerId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## unregisterApplicationStateObserver

```TypeScript
function unregisterApplicationStateObserver(observerId: number): Promise<void>
```

Unregister application state observer.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [off](arkts-ability-appmanager-off-f.md#offapplicationstate)

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| observerId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
