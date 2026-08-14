# EmbeddedUIExtensionAbility

EmbeddedUIExtensionAbility is a component that enables cross-process UI embedding. It inherits from [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#UIExtensionAbility). You can implement this class to add cross-process UI embedding capabilities to your applications. A typical use case is embedding a UI, provided by the application's own EmbeddedUIExtensionAbility, into a [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md#UIAbility) page using an EmbeddedComponent. For details about the inheritance relationship of each ability, see Inheritance Relationship . This API can be properly called on PCs/2-in-1 devices and tablets. It is unavailable on other devices.

**Inheritance/Implementation:** EmbeddedUIExtensionAbility extends [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#UIExtensionAbility)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export default class EmbeddedUIExtensionAbility--><!--Device-unnamed-export default class EmbeddedUIExtensionAbility-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { EmbeddedUIExtensionAbility } from 'EmbeddedUIExtensionAbility';
```

