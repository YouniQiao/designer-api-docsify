# ExtensionContext

ExtensionContext provides the context environment for an [ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md). It inherits from [Context](arkts-ability-context-c.md). This module provides APIs for accessing resources of a specific [ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md).

**Inheritance/Implementation:** ExtensionContext extends Context

**Since:** 23

<!--Device-unnamed-declare class ExtensionContext--><!--Device-unnamed-declare class ExtensionContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## config

```TypeScript
config: Configuration
```

Indicates configuration information.

**Type:** [Configuration](arkts-ability-app-ability-configuration-configuration-i.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ExtensionContext-config: Configuration--><!--Device-ExtensionContext-config: Configuration-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## currentHapModuleInfo

```TypeScript
currentHapModuleInfo: HapModuleInfo
```

Indicates configuration information about an module.

**Type:** [HapModuleInfo](arkts-ability-hapmoduleinfo-i.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ExtensionContext-currentHapModuleInfo: HapModuleInfo--><!--Device-ExtensionContext-currentHapModuleInfo: HapModuleInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## extensionAbilityInfo

```TypeScript
extensionAbilityInfo: ExtensionAbilityInfo
```

Extension information.

**Type:** [ExtensionAbilityInfo](arkts-ability-extensionabilityinfo-i.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ExtensionContext-extensionAbilityInfo: ExtensionAbilityInfo--><!--Device-ExtensionContext-extensionAbilityInfo: ExtensionAbilityInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

