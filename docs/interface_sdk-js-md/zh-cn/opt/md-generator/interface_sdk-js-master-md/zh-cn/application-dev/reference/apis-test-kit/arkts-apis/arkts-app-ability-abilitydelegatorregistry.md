# @ohos.app.ability.abilityDelegatorRegistry

AbilityDelegatorRegistry是自动化测试框架使用指南模块，该模块用于获取[AbilityDelegator](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegator-i.md#AbilityDelegator) 和[AbilityDelegatorArgs](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegatorargs-abilitydelegatorargs-i.md#AbilityDelegatorArgs)对象，其中 [AbilityDelegator](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegator-i.md#AbilityDelegator)对象提供添加用于监视指定ability的生命周期状态更改的 [AbilityMonitor](../../apis-ability-kit/arkts-apis/arkts-ability-abilitymonitor-i.md#AbilityMonitor)对象的能力， [AbilityDelegatorArgs](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegatorargs-abilitydelegatorargs-i.md#AbilityDelegatorArgs)对象提供获取当前测试参数的能力。 > **说明：** > > 本模块接口仅可在[单元测试框架](../../../application-test/unittest-guidelines.md)中使用。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace abilityDelegatorRegistry--><!--Device-unnamed-declare namespace abilityDelegatorRegistry-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 汇总

### 函数

| 名称 |
| --- |
| [getAbilityDelegator](arkts-test-abilitydelegatorregistry-getabilitydelegator-f.md#getAbilityDelegator) |
| [getArguments](arkts-test-abilitydelegatorregistry-getarguments-f.md#getArguments) |

### 枚举

| 名称 |
| --- |
| [AbilityLifecycleState](arkts-test-abilitydelegatorregistry-abilitylifecyclestate-e.md) |

### 类型

| 名称 |
| --- |
| [AbilityDelegator](arkts-test-abilitydelegatorregistry-abilitydelegator-t.md) |
| [AbilityDelegatorArgs](arkts-test-abilitydelegatorregistry-abilitydelegatorargs-t.md) |
| [AbilityMonitor](arkts-test-abilitydelegatorregistry-abilitymonitor-t.md) |
| [AbilityStageMonitor](arkts-test-abilitydelegatorregistry-abilitystagemonitor-t.md) |
| [InteropAbilityMonitor](arkts-test-abilitydelegatorregistry-interopabilitymonitor-t.md) |
| [ShellCmdResult](arkts-test-abilitydelegatorregistry-shellcmdresult-t.md) |
