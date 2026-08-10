# AbilityStageContext

AbilityStageContext是AbilityStage的上下文环境，继承自[Context](arkts-ability-context-t.md)。AbilityStageContext提供允许访问特定于abilityStage的资源的能力，包括获取AbilityStage对应的ModuleInfo对象、环境变化对象。

**Inheritance/Implementation:** AbilityStageContext extends [Context](arkts-ability-context-t.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class AbilityStageContext extends Context--><!--Device-unnamed-declare class AbilityStageContext extends Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## config

```TypeScript
config: Configuration
```

环境变量。

**Type:** [Configuration](arkts-ability-app-ability-configuration-configuration-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityStageContext-config: Configuration--><!--Device-AbilityStageContext-config: Configuration-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## currentHapModuleInfo

```TypeScript
currentHapModuleInfo: HapModuleInfo
```

AbilityStage对应的ModuleInfo对象。

**Type:** [HapModuleInfo](arkts-ability-hapmoduleinfo-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityStageContext-currentHapModuleInfo: HapModuleInfo--><!--Device-AbilityStageContext-currentHapModuleInfo: HapModuleInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## launchElement

```TypeScript
launchElement?: ElementName
```

启动能力Stage的ElementName对象。

**Type:** [ElementName](arkts-ability-elementname-i.md)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-AbilityStageContext-launchElement?: ElementName--><!--Device-AbilityStageContext-launchElement?: ElementName-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

