# @ohos.app.ability.abilityDelegatorRegistry

AbilityDelegatorRegistry是自动化测试框架使用指南模块，该模块用于获取[AbilityDelegator](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegator-i.md/arkts-ability-abilitydelegator-i.md)和[AbilityDelegatorArgs](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegatorargs-abilitydelegatorargs-i.md/arkts-ability-abilitydelegatorargs-abilitydelegatorargs-i.md)对象，其中  
[AbilityDelegator](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegator-i.md/arkts-ability-abilitydelegator-i.md)对象提供添加用于监视指定ability的生命周期状态更改的  
[AbilityMonitor](../../apis-ability-kit/arkts-apis/arkts-ability-abilitymonitor-i.md/arkts-ability-abilitymonitor-i.md)对象的能力，  
[AbilityDelegatorArgs](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegatorargs-abilitydelegatorargs-i.md/arkts-ability-abilitydelegatorargs-abilitydelegatorargs-i.md)对象提供获取当前测试参数的能力。

> **说明：**
> 
> 本模块接口仅可在[单元测试框架](../../../application-test/unittest-guidelines.md)中使用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace abilityDelegatorRegistry--><!--Device-unnamed-declare namespace abilityDelegatorRegistry-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { abilityDelegatorRegistry } from 'kits/@kit.TestKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getAbilityDelegator](arkts-test-abilitydelegatorregistry-getabilitydelegator-f.md#getabilitydelegator) | 获取应用程序的[AbilityDelegator](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegator-i.md/arkts-ability-abilitydelegator-i.md)对象，该对象能够使用调度测试框架的相关功能。 |
| [getArguments](arkts-test-abilitydelegatorregistry-getarguments-f.md#getarguments) | 获取单元测试参数[AbilityDelegatorArgs](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegatorargs-abilitydelegatorargs-i.md/arkts-ability-abilitydelegatorargs-abilitydelegatorargs-i.md)对象。 |

### Enums

| Name | Description |
| --- | --- |
| [AbilityLifecycleState](arkts-test-abilitydelegatorregistry-abilitylifecyclestate-e.md) | Ability生命周期状态，该类型为枚举，可配合[AbilityDelegator](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegator-i.md/arkts-ability-abilitydelegator-i.md)的  [getAbilityState(ability)](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegator-i.md/arkts-ability-abilitydelegator-i.md#getabilitystate)方法返回不同ability生命周期。 |

### Types

| Name | Description |
| --- | --- |
| [AbilityDelegator](arkts-test-abilitydelegatorregistry-abilitydelegator-t.md) | AbilityDelegator模块。 |
| [AbilityDelegatorArgs](arkts-test-abilitydelegatorregistry-abilitydelegatorargs-t.md) | AbilityDelegatorArgs模块。 |
| [AbilityMonitor](arkts-test-abilitydelegatorregistry-abilitymonitor-t.md) | AbilityMonitor模块。 |
| [AbilityStageMonitor](arkts-test-abilitydelegatorregistry-abilitystagemonitor-t.md) | AbilityStageMonitor模块。 |
| [InteropAbilityMonitor](arkts-test-abilitydelegatorregistry-interopabilitymonitor-t.md) | 提供匹配满足指定条件的监控对象的方法。最近匹配的Ability对象将保存在InteropAbilityMonitor对象中。 |
| [ShellCmdResult](arkts-test-abilitydelegatorregistry-shellcmdresult-t.md) | ShellCmdResult模块。 |

