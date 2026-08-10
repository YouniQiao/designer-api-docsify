# AbilityResult

定义UIAbility被拉起并退出后返回给调用方的结果码和数据。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface AbilityResult--><!--Device-unnamed-export interface AbilityResult-End-->

**System capability:** SystemCapability.Ability.AbilityBase

## resultCode

```TypeScript
resultCode: int
```

目标方的UIAbility被拉起并退出后，目标方返回给拉起方的结果码。&lt;br/&gt;-?正常情况下，返回目标方传递的结果码。&lt;br/&gt;-?异常情况下，返回-1。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityResult-resultCode: int--><!--Device-AbilityResult-resultCode: int-End-->

**System capability:** SystemCapability.Ability.AbilityBase

## want

```TypeScript
want?: Want
```

表示UIAbility被拉起并退出后返回的数据。

**Type:** [Want](arkts-ability-app-ability-want-want-c.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityResult-want?: Want--><!--Device-AbilityResult-want?: Want-End-->

**System capability:** SystemCapability.Ability.AbilityBase

