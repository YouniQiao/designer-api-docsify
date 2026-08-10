# offFreeze

## Modules to Import

```TypeScript
import { errorManager } from 'kits/@kit.AbilityKit';
```

## offFreeze

```TypeScript
function offFreeze(observer?: FreezeObserver): void
```

注销冻屏事件观测器。此函数只能在主线程中调用。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-errorManager-function offFreeze(observer?: FreezeObserver): void--><!--Device-errorManager-function offFreeze(observer?: FreezeObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | [FreezeObserver](arkts-ability-errormanager-freezeobserver-t.md) | No | 冻屏事件观测器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 参数错误。可能的原因：1. 必填参数未填写； 2. 参数类型不正确；3. 参数校验失败。 |
| 16200001 | 调用者无效。 |
| 16300004 | 观测器不存在。 |

