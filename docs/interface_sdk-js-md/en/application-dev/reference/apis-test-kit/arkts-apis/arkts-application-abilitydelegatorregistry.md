# @ohos.application.abilityDelegatorRegistry

AbilityDelegatorRegistry模块提供用于存储已注册的[AbilityDelegator](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegator-i.md/arkts-ability-abilitydelegator-i.md)和  
[AbilityDelegatorArgs](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegatorargs-abilitydelegatorargs-i.md/arkts-ability-abilitydelegatorargs-abilitydelegatorargs-i.md)对象的全局寄存器的能力，包括获取应用程序的AbilityDelegator对象、获取单元测试参数AbilityDelegatorArgs对象。该模块中的接口只能用于测试框架中。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.app.ability.abilityDelegatorRegistry:abilityDelegatorRegistry](arkts-application-abilitydelegatorregistry.md)

<!--Device-unnamed-declare namespace abilityDelegatorRegistry--><!--Device-unnamed-declare namespace abilityDelegatorRegistry-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getAbilityDelegator](arkts-test-abilitydelegatorregistry-getabilitydelegator-depr-f.md#getabilitydelegator) | 获取应用程序的AbilityDelegator对象。 |
| [getArguments](arkts-test-abilitydelegatorregistry-getarguments-depr-f.md#getarguments) | 获取单元测试参数AbilityDelegatorArgs对象。 |

### Enums

| Name | Description |
| --- | --- |
| [AbilityLifecycleState](arkts-test-abilitydelegatorregistry-abilitylifecyclestate-depr-e.md) | Ability生命周期状态。 |

