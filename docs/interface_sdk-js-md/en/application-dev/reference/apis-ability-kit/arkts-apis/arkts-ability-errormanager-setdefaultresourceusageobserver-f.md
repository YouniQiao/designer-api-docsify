# setDefaultResourceUsageObserver

## Modules to Import

```TypeScript
import { errorManager } from 'kits/@kit.AbilityKit';
```

## setDefaultResourceUsageObserver

```TypeScript
function setDefaultResourceUsageObserver(defaultObserver?: ResourceUsageObserver): ResourceUsageObserver
```

设置资源占用观察者，应用资源超基线时，支持链式回调，返回上一次注册的资源占用观察者，仅限主线程调用。

如果传入非法参数或在子线程调用，将抛出错误码并返回undefined，因此建议使用try-catch逻辑进行处理。

若接口参数为空，后续注册的观察者将无法与前序已注册的观察者建立关联，从而中断链式调用。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-errorManager-function setDefaultResourceUsageObserver(defaultObserver?: ResourceUsageObserver): ResourceUsageObserver--><!--Device-errorManager-function setDefaultResourceUsageObserver(defaultObserver?: ResourceUsageObserver): ResourceUsageObserver-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| defaultObserver | [ResourceUsageObserver](arkts-ability-errormanager-resourceusageobserver-t.md) | No | 新注册的资源观察者，默认值为空。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ResourceUsageObserver](arkts-ability-errormanager-resourceusageobserver-t.md) | 返回上一次注册的资源观察者。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000205 | API未在主线程中调用。 |

