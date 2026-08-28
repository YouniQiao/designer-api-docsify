# getAbilityDelegator

## Modules to Import

```TypeScript
```

## getAbilityDelegator

```TypeScript
function getAbilityDelegator(): AbilityDelegator
```

Obtains the **AbilityDelegator** object of the application.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getAbilityDelegator](arkts-test-abilitydelegatorregistry-getabilitydelegator-f.md)

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Test API:** This is a test API.

**Return value:**

| Type | Description |
| --- | --- |
| [AbilityDelegator](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegator-i.md) | [AbilityDelegator]{ |

**Examples**

```TypeScript
import AbilityDelegatorRegistry from '@ohos.application.abilityDelegatorRegistry';

let abilityDelegator = AbilityDelegatorRegistry.getAbilityDelegator();
```
