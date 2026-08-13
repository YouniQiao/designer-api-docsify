# setDefaultResourceUsageObserver

## Modules to Import

```TypeScript
import { errorManager } from '@kit.AbilityKit';
```

## setDefaultResourceUsageObserver

```TypeScript
function setDefaultResourceUsageObserver(defaultObserver?: ResourceUsageObserver): ResourceUsageObserver
```

Set the default resource usage observer. You can use it to implement chain calls. If an empty observer is set for a certain module, it will cause the call chain to be interrupted. This API must be called on the main thread.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-errorManager-function setDefaultResourceUsageObserver(defaultObserver?: ResourceUsageObserver): ResourceUsageObserver--><!--Device-errorManager-function setDefaultResourceUsageObserver(defaultObserver?: ResourceUsageObserver): ResourceUsageObserver-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| defaultObserver | [ResourceUsageObserver](arkts-ability-errormanager-resourceusageobserver-t.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ResourceUsageObserver](arkts-ability-errormanager-resourceusageobserver-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [16000205](../errorcode-ability.md#16000205-api-not-called-in-main-thread) |
