# acquireDataAbilityHelper

## Modules to Import

```TypeScript
import { particleAbility } from '@kit.AbilityKit';
```

## acquireDataAbilityHelper

```TypeScript
function acquireDataAbilityHelper(uri: string): DataAbilityHelper
```

Obtains a dataAbilityHelper object. > **NOTE：**> > For details about the startup rules for the components in the FA model, see > [Component Startup Rules (FA Model)](../../../application-models/component-startup-rules-fa.md). > To access a DataAbility of another application, the target application must be configured with associated > startup (**AssociateWakeUp** set to **true**).

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-particleAbility-function acquireDataAbilityHelper(uri: string): DataAbilityHelper--><!--Device-particleAbility-function acquireDataAbilityHelper(uri: string): DataAbilityHelper-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityHelper](arkts-ability-dataabilityhelper-dataabilityhelper-i.md) |

## Examples

```TypeScript
import { particleAbility } from '@kit.AbilityKit';

let uri = '';
particleAbility.acquireDataAbilityHelper(uri);
```
