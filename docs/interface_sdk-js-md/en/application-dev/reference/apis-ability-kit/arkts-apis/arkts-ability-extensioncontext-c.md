# ExtensionContext

ExtensionContext是[ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md)的上下文环境，继承自  
[Context](../../../reference/apis-ability-kit/js-apis-inner-application-context.md#context)。ExtensionContext模块提供访问特定[ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md)的资源的能力。

**Inheritance/Implementation:** ExtensionContext extends [Context](arkts-ability-context-t.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class ExtensionContext extends Context--><!--Device-unnamed-declare class ExtensionContext extends Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## config

```TypeScript
config: Configuration
```

所属Module的配置信息。

**Type:** [Configuration](arkts-ability-app-ability-configuration-configuration-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ExtensionContext-config: Configuration--><!--Device-ExtensionContext-config: Configuration-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## currentHapModuleInfo

```TypeScript
currentHapModuleInfo: HapModuleInfo
```

所属Hap包的信息。

**Type:** [HapModuleInfo](arkts-ability-hapmoduleinfo-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ExtensionContext-currentHapModuleInfo: HapModuleInfo--><!--Device-ExtensionContext-currentHapModuleInfo: HapModuleInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## extensionAbilityInfo

```TypeScript
extensionAbilityInfo: ExtensionAbilityInfo
```

所属[ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md)的信息。

**Type:** [ExtensionAbilityInfo](arkts-ability-extensionabilityinfo-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ExtensionContext-extensionAbilityInfo: ExtensionAbilityInfo--><!--Device-ExtensionContext-extensionAbilityInfo: ExtensionAbilityInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

