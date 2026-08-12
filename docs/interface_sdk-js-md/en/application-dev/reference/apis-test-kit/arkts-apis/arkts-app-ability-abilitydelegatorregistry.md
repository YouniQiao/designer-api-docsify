# @ohos.app.ability.abilityDelegatorRegistry

**AbilityDelegatorRegistry**, a module of the automatic test framework, is used to obtain  
[AbilityDelegator](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegator-i.md#AbilityDelegator) and  
[AbilityDelegatorArgs](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegatorargs-abilitydelegatorargs-i.md#AbilityDelegatorArgs) objects. **AbilityDelegator**provides APIs for creating [AbilityMonitor](../../apis-ability-kit/arkts-apis/arkts-ability-abilitymonitor-i.md#AbilityMonitor) objects, which can be used to listen for ability lifecycle changes. **AbilityDelegatorArgs** provides APIs for obtaining test parameters.

> **NOTE：**
> 
> The APIs of this module can be used only in [JsUnit](../../../application-test/unittest-guidelines.md).

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace abilityDelegatorRegistry--><!--Device-unnamed-declare namespace abilityDelegatorRegistry-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getAbilityDelegator](arkts-test-abilitydelegatorregistry-getabilitydelegator-f.md#getabilitydelegator) | Obtains an [AbilityDelegator](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegator-i.md#AbilityDelegator) object. |
| [getArguments](arkts-test-abilitydelegatorregistry-getarguments-f.md#getarguments) | Obtains an [AbilityDelegatorArgs](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegatorargs-abilitydelegatorargs-i.md#AbilityDelegatorArgs) object. |

### Enums

| Name | Description |
| --- | --- |
| [AbilityLifecycleState](arkts-test-abilitydelegatorregistry-abilitylifecyclestate-e.md) | Enumerates the ability lifecycle states. It can be used in  [getAbilityState(ability)](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegator-i.md#getAbilityState) of  [AbilityDelegator](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegator-i.md#AbilityDelegator) to return different ability lifecycle states. |

### Types

| Name | Description |
| --- | --- |
| [AbilityDelegator](arkts-test-abilitydelegatorregistry-abilitydelegator-t.md) | Represents the **AbilityDelegator** module. |
| [AbilityDelegatorArgs](arkts-test-abilitydelegatorregistry-abilitydelegatorargs-t.md) | Represents the **AbilityDelegatorArgs** module. |
| [AbilityMonitor](arkts-test-abilitydelegatorregistry-abilitymonitor-t.md) | Represents the **AbilityMonitor** module. |
| [AbilityStageMonitor](arkts-test-abilitydelegatorregistry-abilitystagemonitor-t.md) | Represents the **AbilityStageMonitor** module. |
| [InteropAbilityMonitor](arkts-test-abilitydelegatorregistry-interopabilitymonitor-t.md) | Provide methods for matching monitored Ability objects that meet specified conditions.The most recently matched Ability objects will be saved in the InteropAbilityMonitor object. |
| [ShellCmdResult](arkts-test-abilitydelegatorregistry-shellcmdresult-t.md) | Represents the **ShellCmdResult** module. |

