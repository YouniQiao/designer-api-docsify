# AbilityMonitor

本模块提供监听指定[UIAbility](arkts-app-ability-uiability.md)生命周期状态变化的能力。开发者可以将AbilityMonitor作为  
[abilityDelegator.addAbilityMonitor](arkts-ability-abilitydelegator-i.md#addabilitymonitor)的入参来注册监听。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface AbilityMonitor--><!--Device-unnamed-export interface AbilityMonitor-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onAbilityBackground

```TypeScript
onAbilityBackground?: (ability: UIAbility) => void
```

UIAbility对象状态变成后台时，触发该回调函数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityMonitor-onAbilityBackground?: (ability: UIAbility) => void--><!--Device-AbilityMonitor-onAbilityBackground?: (ability: UIAbility) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes |  |

## onAbilityCreate

```TypeScript
onAbilityCreate?: (ability: UIAbility) => void
```

UIAbility对象被创建时，触发该回调函数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityMonitor-onAbilityCreate?: (ability: UIAbility) => void--><!--Device-AbilityMonitor-onAbilityCreate?: (ability: UIAbility) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes |  |

## onAbilityDestroy

```TypeScript
onAbilityDestroy?: (ability: UIAbility) => void
```

UIAbility对象被销毁前，触发该回调函数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityMonitor-onAbilityDestroy?: (ability: UIAbility) => void--><!--Device-AbilityMonitor-onAbilityDestroy?: (ability: UIAbility) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes |  |

## onAbilityForeground

```TypeScript
onAbilityForeground?: (ability: UIAbility) => void
```

UIAbility对象状态变成前台时，触发该回调函数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityMonitor-onAbilityForeground?: (ability: UIAbility) => void--><!--Device-AbilityMonitor-onAbilityForeground?: (ability: UIAbility) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes |  |

## onWindowStageCreate

```TypeScript
onWindowStageCreate?: (ability: UIAbility) => void
```

当WindowStage实例被创建时，触发该回调函数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityMonitor-onWindowStageCreate?: (ability: UIAbility) => void--><!--Device-AbilityMonitor-onWindowStageCreate?: (ability: UIAbility) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes |  |

## onWindowStageDestroy

```TypeScript
onWindowStageDestroy?: (ability: UIAbility) => void
```

当WindowStage被销毁前，触发该回调函数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityMonitor-onWindowStageDestroy?: (ability: UIAbility) => void--><!--Device-AbilityMonitor-onWindowStageDestroy?: (ability: UIAbility) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes |  |

## onWindowStageRestore

```TypeScript
onWindowStageRestore?: (ability: UIAbility) => void
```

当UIAbility跨端迁移时，目标端UIAbility恢复页面栈时，触发该回调函数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityMonitor-onWindowStageRestore?: (ability: UIAbility) => void--><!--Device-AbilityMonitor-onWindowStageRestore?: (ability: UIAbility) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes |  |

## abilityName

```TypeScript
abilityName: string
```

被监听的UIAbility对象名称。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityMonitor-abilityName: string--><!--Device-AbilityMonitor-abilityName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## moduleName

```TypeScript
moduleName?: string
```

被监听的UIAbility对象所属模块名称。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityMonitor-moduleName?: string--><!--Device-AbilityMonitor-moduleName?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

