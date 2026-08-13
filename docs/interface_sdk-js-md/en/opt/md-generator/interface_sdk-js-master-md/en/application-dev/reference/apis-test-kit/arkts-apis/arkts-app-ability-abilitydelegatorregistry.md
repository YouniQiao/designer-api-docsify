# @ohos.app.ability.abilityDelegatorRegistry

**AbilityDelegatorRegistry**, a module of the automatic test framework, is used to obtain [AbilityDelegator](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegator-i.md#AbilityDelegator) and [AbilityDelegatorArgs](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegatorargs-abilitydelegatorargs-i.md#AbilityDelegatorArgs) objects. **AbilityDelegator** provides APIs for creating [AbilityMonitor](../../apis-ability-kit/arkts-apis/arkts-ability-abilitymonitor-i.md#AbilityMonitor) objects, which can be used to listen for ability lifecycle changes. **AbilityDelegatorArgs** provides APIs for obtaining test parameters. > **NOTE：**> > The APIs of this module can be used only in [JsUnit](../../../application-test/unittest-guidelines.md).

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace abilityDelegatorRegistry--><!--Device-unnamed-declare namespace abilityDelegatorRegistry-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getAbilityDelegator](arkts-test-abilitydelegatorregistry-getabilitydelegator-f.md#getAbilityDelegator) |
| [getArguments](arkts-test-abilitydelegatorregistry-getarguments-f.md#getArguments) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AbilityLifecycleState](arkts-test-abilitydelegatorregistry-abilitylifecyclestate-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AbilityDelegator](arkts-test-abilitydelegatorregistry-abilitydelegator-t.md) |
| [AbilityDelegatorArgs](arkts-test-abilitydelegatorregistry-abilitydelegatorargs-t.md) |
| [AbilityMonitor](arkts-test-abilitydelegatorregistry-abilitymonitor-t.md) |
| [AbilityStageMonitor](arkts-test-abilitydelegatorregistry-abilitystagemonitor-t.md) |
| [InteropAbilityMonitor](arkts-test-abilitydelegatorregistry-interopabilitymonitor-t.md) |
| [ShellCmdResult](arkts-test-abilitydelegatorregistry-shellcmdresult-t.md) |
