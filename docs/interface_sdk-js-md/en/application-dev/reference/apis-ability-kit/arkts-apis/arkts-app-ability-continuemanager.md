# @ohos.app.ability.continueManager

continueManager提供了应用跨端迁移的管理能力，如获取应用跨端迁移过程中快速拉起目标应用的结果。

> 本模块接口仅可在Stage模型下使用。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace continueManager--><!--Device-unnamed-declare namespace continueManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

## Modules to Import

```TypeScript
import { continueManager } from 'kits/@kit.AbilityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [off](arkts-ability-continuemanager-off-f.md#off) | 在应用快速拉起时，注销回调函数，不再获取快速拉起结果。使用callback异步回调。 |
| [offPrepareContinue](arkts-ability-continuemanager-offpreparecontinue-f.md#offpreparecontinue) | Unregister prepareContinue event. |
| [on](arkts-ability-continuemanager-on-f.md#on) | 在应用快速拉起时，注册回调函数以获取快速拉起结果。使用callback异步回调。 |
| [onPrepareContinue](arkts-ability-continuemanager-onpreparecontinue-f.md#onpreparecontinue) | prepareContinue 事件，当在 continueType 中配置了“ContinueQuickStart”功能时，即可获取 |

### Interfaces

| Name | Description |
| --- | --- |
| [ContinueResultInfo](arkts-ability-continuemanager-continueresultinfo-i.md) | 注册或注销回调函数返回的快速拉起的结果。 |

### Enums

| Name | Description |
| --- | --- |
| [ContinueStateCode](arkts-ability-continuemanager-continuestatecode-e.md) | 快速拉起的结果状态码的枚举值。 |

