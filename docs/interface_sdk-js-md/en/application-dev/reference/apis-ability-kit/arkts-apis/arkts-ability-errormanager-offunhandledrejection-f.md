# offUnhandledRejection

## Modules to Import

```TypeScript
import { errorManager } from 'kits/@kit.AbilityKit';
```

## offUnhandledRejection

```TypeScript
function offUnhandledRejection(observer?: UnhandledRejectionObserver): void
```

Unregister unhandled rejection observer.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-errorManager-function offUnhandledRejection(observer?: UnhandledRejectionObserver): void--><!--Device-errorManager-function offUnhandledRejection(observer?: UnhandledRejectionObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | [UnhandledRejectionObserver](arkts-ability-errormanager-unhandledrejectionobserver-t.md) | No | the registered observer |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 参数错误。可能的原因：1. 必填参数未填写； 2. 参数类型不正确；3. 参数校验失败。 |
| 16300004 | 观测器不存在。 |

