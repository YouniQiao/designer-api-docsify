# saveAppState

## Modules to Import

```TypeScript
import { appRecovery } from 'kits/@kit.AbilityKit';
```

## saveAppState

```TypeScript
function saveAppState(): boolean
```

Saves the application state. This API can be used together with the APIs of [errorManager](arkts-app-ability-errormanager.md).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |


## saveAppState

```TypeScript
function saveAppState(context?: UIAbilityContext): boolean
```

Saves the ability state, which will be used for recovery. This API can be used together with the APIs of [errorManager](arkts-app-ability-errormanager.md).

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIAbilityContext](arkts-ability-uiabilitycontext-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
