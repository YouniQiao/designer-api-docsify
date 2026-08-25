# connectAbility

## Modules to Import

```TypeScript
import { particleAbility } from 'kits/@kit.AbilityKit';
```

## connectAbility

```TypeScript
function connectAbility(request: Want, options: ConnectOptions): number
```

Connects this ability to a ServiceAbility.

> **NOTE：**&gt;
> For details about the startup rules for the components in the FA model, see
> [Component Startup Rules (FA Model)](../../../application-models/component-startup-rules-fa.md).
> 
> To connect to a ServiceAbility of another application, the target application must be configured with
> associated startup (**AssociateWakeUp** set to **true**).

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| options | [ConnectOptions](arkts-ability-connectoptions-connectoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |
