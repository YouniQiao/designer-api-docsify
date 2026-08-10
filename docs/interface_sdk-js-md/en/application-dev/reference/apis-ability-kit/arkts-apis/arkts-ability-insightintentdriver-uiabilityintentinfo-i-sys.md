# UIAbilityIntentInfo (System API)

用于描述[使用配置文件开发的意图](../../../application-models/insight-intent-config-development.md)所绑定的UIAbility组件信息。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-insightIntentDriver-interface UIAbilityIntentInfo--><!--Device-insightIntentDriver-interface UIAbilityIntentInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { insightIntentDriver } from 'kits/@kit.AbilityKit';
```

## abilityName

```TypeScript
readonly abilityName: string
```

意图绑定的UIAbility组件名称。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityIntentInfo-readonly abilityName: string--><!--Device-UIAbilityIntentInfo-readonly abilityName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## executeMode

```TypeScript
readonly executeMode: ExecuteModeForConfiguration[]
```

意图调用执行模式。

**Type:** [ExecuteModeForConfiguration](arkts-ability-insightintentdriver-executemodeforconfiguration-e-sys.md)[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityIntentInfo-readonly executeMode: ExecuteModeForConfiguration[]--><!--Device-UIAbilityIntentInfo-readonly executeMode: ExecuteModeForConfiguration[]-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

