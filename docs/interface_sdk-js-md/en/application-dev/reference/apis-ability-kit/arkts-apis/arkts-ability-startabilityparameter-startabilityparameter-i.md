# StartAbilityParameter

定义启动Ability参数，可以作为入参，调用  
[startAbility](arkts-ability-featureability-startability-f.md#startability)启动指定的Ability。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

<!--Device-unnamed-export interface StartAbilityParameter--><!--Device-unnamed-export interface StartAbilityParameter-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

## abilityStartSetting

```TypeScript
abilityStartSetting?: { [key: string]: any }
```

启动Ability的特殊属性，当开发者启动Ability时，该属性可以作为调用中的输入参数传递。

**Type:** { [key: string]: any }

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Model restriction:** This API can be used only in the FA model.

<!--Device-StartAbilityParameter-abilityStartSetting?: { [key: string]: any }--><!--Device-StartAbilityParameter-abilityStartSetting?: { [key: string]: any }-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

## abilityStartSettings

```TypeScript
abilityStartSettings?: Record<string, Object>
```

启动Ability的特殊属性，当开发者启动Ability时，该属性可以作为调用中的输入参数传递。推荐使用该属性替代abilityStartSetting，设置该属性后，abilityStartSetting不再生效。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the FA model.

<!--Device-StartAbilityParameter-abilityStartSettings?: Record<string, Object>--><!--Device-StartAbilityParameter-abilityStartSettings?: Record<string, Object>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

## want

```TypeScript
want: Want
```

启动Ability的want信息。

**Type:** [Want](arkts-ability-app-ability-want-want-c.md)

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Model restriction:** This API can be used only in the FA model.

<!--Device-StartAbilityParameter-want: Want--><!--Device-StartAbilityParameter-want: Want-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

