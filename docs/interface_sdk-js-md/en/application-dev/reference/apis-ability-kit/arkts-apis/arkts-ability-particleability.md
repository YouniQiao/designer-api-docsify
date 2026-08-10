# @ohos.ability.particleAbility

particleAbility模块提供了操作Data和Service类型的Ability的能力，包括启动、停止指定的particleAbility，获取dataAbilityHelper，连接、断连指定的ServiceAbility等。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-unnamed-declare namespace particleAbility--><!--Device-unnamed-declare namespace particleAbility-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

## Modules to Import

```TypeScript
import { particleAbility } from 'kits/@kit.AbilityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [acquireDataAbilityHelper](arkts-ability-particleability-acquiredataabilityhelper-f.md#acquiredataabilityhelper) | 获取dataAbilityHelper对象。 |
| [cancelBackgroundRunning](arkts-ability-particleability-cancelbackgroundrunning-f.md#cancelbackgroundrunning) | 向系统申请取消长时任务。使用callback异步回调。 |
| [cancelBackgroundRunning](arkts-ability-particleability-cancelbackgroundrunning-f.md#cancelbackgroundrunning-1) | 向系统申请取消长时任务。使用Promise异步回调。 |
| [connectAbility](arkts-ability-particleability-connectability-f.md#connectability) | 将当前ability与指定的ServiceAbility进行连接。 |
| [disconnectAbility](arkts-ability-particleability-disconnectability-f.md#disconnectability) | 断开当前ability与指定ServiceAbility的连接。使用callback异步回调。 |
| [disconnectAbility](arkts-ability-particleability-disconnectability-f.md#disconnectability-1) | 断开当前ability与指定ServiceAbility的连接。使用Promise异步回调。 |
| [startAbility](arkts-ability-particleability-startability-f.md#startability) | 启动指定的particleAbility。使用callback异步回调。 |
| [startAbility](arkts-ability-particleability-startability-f.md#startability-1) | 启动指定的particleAbility。使用Promise异步回调。 |
| [startBackgroundRunning](arkts-ability-particleability-startbackgroundrunning-f.md#startbackgroundrunning) | 向系统申请长时任务。使用callback异步回调。 |
| [startBackgroundRunning](arkts-ability-particleability-startbackgroundrunning-f.md#startbackgroundrunning-1) | 向系统申请长时任务。使用Promise异步回调。 |
| [terminateSelf](arkts-ability-particleability-terminateself-f.md#terminateself) | 销毁当前particleAbility。使用callback异步回调。 |
| [terminateSelf](arkts-ability-particleability-terminateself-f.md#terminateself-1) | 销毁当前particleAbility。使用Promise异步回调。 |

### Enums

| Name | Description |
| --- | --- |
| [ErrorCode](arkts-ability-particleability-errorcode-e.md) | 定义启动Ability时返回的错误码。 |

