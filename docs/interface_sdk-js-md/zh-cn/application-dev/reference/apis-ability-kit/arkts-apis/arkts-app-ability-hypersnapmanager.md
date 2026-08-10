# @ohos.app.ability.hyperSnapManager

This module provides the capability to manage HyperSnap.

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace hyperSnapManager--><!--Device-unnamed-declare namespace hyperSnapManager-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { hyperSnapManager } from 'kits/@kit.AbilityKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [requestRebuildHyperSnap](arkts-ability-hypersnapmanager-requestrebuildhypersnap-f.md#requestrebuildhypersnap) | Requests the recreation of the Hyper Snap process snapshot for the application.  When compatibility issues arise with an existing snapshot, this method triggers destruction of the current snapshot process. The system will subsequently generate a new snapshot at an optimal time to resolve compatibility problems while maintaining launch performance benefits.  **Notes:**  - The system ultimately determines whether and when to recreate the snapshot. Invoking this method only submits   a request; actual snapshot recreation depends on system policies and resource availability.  - Recreation occurs during optimal system idle periods to minimize performance impact.  - Primarily for resolving specific compatibility issues identified after initial snapshot creation.   Most applications don't require manual intervention for snapshot management. |
| [setHyperSnapEnabled](arkts-ability-hypersnapmanager-sethypersnapenabled-f.md#sethypersnapenabled) | Enables or disables the Hyper Snap performance optimization for the application.  When enabled, the system will create a snapshot of the application process at an appropriate time.Subsequent launched resume directly from this snapshot, bypassing the full cold start sequence,resulting in significantly improved application launch performance.  **Notes:**  - The system ultimately determines whether to create or use snapshots based on   application compatibility, resource availability, and system policies. Enabling this feature only indicates the application's readiness for optimization.  - Hyper Snap is enabled by default for applications meeting system compatibility requirements.  - If issues arise after enabling Hyper Snap, disable this feature to revert   to standard cold start processes.  - Settings persist across reboots. |

