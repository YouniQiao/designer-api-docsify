# AbilityLifecycleCallback

[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md#UIAbility)从创建到销毁过程其生命周期是动态变化的。AbilityLifecycleCallback模块提供监听[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md#UIAbility)生命周期变化的能力，可用于统计每个UIAbility的运行时长、执行与UIAbility业务逻辑解耦的数据加载等场景。

**起始版本：** 9

<!--Device-unnamed-declare class AbilityLifecycleCallback--><!--Device-unnamed-declare class AbilityLifecycleCallback-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onAbilityBackground

```TypeScript
onAbilityBackground(ability: UIAbility): void
```

在UIAbility的[onBackground](arkts-ability-app-ability-uiability-uiability-c.md#onBackground)触发后回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onAbilityBackground(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityBackground(ability: UIAbility): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。

## onAbilityContinue

```TypeScript
onAbilityContinue(ability: UIAbility): void
```

在UIAbility的[onContinue](arkts-ability-app-ability-uiability-uiability-c.md#onContinue)触发后回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onAbilityContinue(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityContinue(ability: UIAbility): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。

## onAbilityCreate

```TypeScript
onAbilityCreate(ability: UIAbility): void
```

在UIAbility的[onCreate](arkts-ability-app-ability-uiability-uiability-c.md#onCreate)触发后回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onAbilityCreate(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityCreate(ability: UIAbility): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。

## onAbilityDestroy

```TypeScript
onAbilityDestroy(ability: UIAbility): void
```

在UIAbility的[onDestroy](arkts-ability-app-ability-uiability-uiability-c.md#onDestroy)触发后回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onAbilityDestroy(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityDestroy(ability: UIAbility): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。

## onAbilityForeground

```TypeScript
onAbilityForeground(ability: UIAbility): void
```

在UIAbility的[onForeground](arkts-ability-app-ability-uiability-uiability-c.md#onForeground)触发后回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onAbilityForeground(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityForeground(ability: UIAbility): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。

## onAbilitySaveState

```TypeScript
onAbilitySaveState?(ability: UIAbility): void
```

在UIAbility的[onSaveState](arkts-ability-app-ability-uiability-uiability-c.md#onSaveState)触发后回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onAbilitySaveState?(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilitySaveState?(ability: UIAbility): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。

## onAbilityWillBackground

```TypeScript
onAbilityWillBackground?(ability: UIAbility): void
```

在UIAbility的[onBackground](arkts-ability-app-ability-uiability-uiability-c.md#onBackground)触发前回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onAbilityWillBackground?(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityWillBackground?(ability: UIAbility): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。

## onAbilityWillContinue

```TypeScript
onAbilityWillContinue?(ability: UIAbility): void
```

在UIAbility的[onContinue](arkts-ability-app-ability-uiability-uiability-c.md#onContinue)触发前回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onAbilityWillContinue?(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityWillContinue?(ability: UIAbility): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。

## onAbilityWillCreate

```TypeScript
onAbilityWillCreate?(ability: UIAbility): void
```

在UIAbility的[onCreate](arkts-ability-app-ability-uiability-uiability-c.md#onCreate)触发前回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onAbilityWillCreate?(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityWillCreate?(ability: UIAbility): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。

## onAbilityWillDestroy

```TypeScript
onAbilityWillDestroy?(ability: UIAbility): void
```

在UIAbility的[onDestroy](arkts-ability-app-ability-uiability-uiability-c.md#onDestroy)触发前回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onAbilityWillDestroy?(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityWillDestroy?(ability: UIAbility): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。

## onAbilityWillForeground

```TypeScript
onAbilityWillForeground?(ability: UIAbility): void
```

在UIAbility的[onForeground](arkts-ability-app-ability-uiability-uiability-c.md#onForeground)触发前回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onAbilityWillForeground?(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityWillForeground?(ability: UIAbility): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。

## onAbilityWillSaveState

```TypeScript
onAbilityWillSaveState?(ability: UIAbility): void
```

在UIAbility的[onSaveState](arkts-ability-app-ability-uiability-uiability-c.md#onSaveState)触发前回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onAbilityWillSaveState?(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityWillSaveState?(ability: UIAbility): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。

## onNewWant

```TypeScript
onNewWant?(ability: UIAbility): void
```

在UIAbility的[onNewWant](arkts-ability-app-ability-uiability-uiability-c.md#onNewWant)触发后回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onNewWant?(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onNewWant?(ability: UIAbility): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。

## onWillNewWant

```TypeScript
onWillNewWant?(ability: UIAbility): void
```

在UIAbility的[onNewWant](arkts-ability-app-ability-uiability-uiability-c.md#onNewWant)触发前回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onWillNewWant?(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onWillNewWant?(ability: UIAbility): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。

## onWindowStageActive

```TypeScript
onWindowStageActive(ability: UIAbility, windowStage: window.WindowStage): void
```

在UIAbility主窗获焦时触发回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onWindowStageActive(ability: UIAbility, windowStage: window.WindowStage): void--><!--Device-AbilityLifecycleCallback-onWindowStageActive(ability: UIAbility, windowStage: window.WindowStage): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |
| [windowStage](arkts-ability-uiabilitycontext-c.md) | window.WindowStage | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。

## onWindowStageCreate

```TypeScript
onWindowStageCreate(ability: UIAbility, windowStage: window.WindowStage): void
```

在UIAbility的[onWindowStageCreate](arkts-ability-app-ability-uiability-uiability-c.md#onWindowStageCreate)触发后回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onWindowStageCreate(ability: UIAbility, windowStage: window.WindowStage): void--><!--Device-AbilityLifecycleCallback-onWindowStageCreate(ability: UIAbility, windowStage: window.WindowStage): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |
| [windowStage](arkts-ability-uiabilitycontext-c.md) | window.WindowStage | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。

## onWindowStageDestroy

```TypeScript
onWindowStageDestroy(ability: UIAbility, windowStage: window.WindowStage): void
```

在UIAbility的[onWindowStageDestroy](arkts-ability-app-ability-uiability-uiability-c.md#onWindowStageDestroy)触发后回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onWindowStageDestroy(ability: UIAbility, windowStage: window.WindowStage): void--><!--Device-AbilityLifecycleCallback-onWindowStageDestroy(ability: UIAbility, windowStage: window.WindowStage): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |
| [windowStage](arkts-ability-uiabilitycontext-c.md) | window.WindowStage | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。

## onWindowStageInactive

```TypeScript
onWindowStageInactive(ability: UIAbility, windowStage: window.WindowStage): void
```

在UIAbility主窗失焦时触发回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onWindowStageInactive(ability: UIAbility, windowStage: window.WindowStage): void--><!--Device-AbilityLifecycleCallback-onWindowStageInactive(ability: UIAbility, windowStage: window.WindowStage): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |
| [windowStage](arkts-ability-uiabilitycontext-c.md) | window.WindowStage | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。

## onWindowStageRestore

```TypeScript
onWindowStageRestore?(ability: UIAbility, windowStage: window.WindowStage): void
```

在UIAbility的[onWindowStageRestore](arkts-ability-app-ability-uiability-uiability-c.md#onWindowStageRestore)触发后回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onWindowStageRestore?(ability: UIAbility, windowStage: window.WindowStage): void--><!--Device-AbilityLifecycleCallback-onWindowStageRestore?(ability: UIAbility, windowStage: window.WindowStage): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |
| [windowStage](arkts-ability-uiabilitycontext-c.md) | window.WindowStage | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。

## onWindowStageWillCreate

```TypeScript
onWindowStageWillCreate?(ability: UIAbility, windowStage: window.WindowStage): void
```

在UIAbility的[onWindowStageCreate](arkts-ability-app-ability-uiability-uiability-c.md#onWindowStageCreate)触发前回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onWindowStageWillCreate?(ability: UIAbility, windowStage: window.WindowStage): void--><!--Device-AbilityLifecycleCallback-onWindowStageWillCreate?(ability: UIAbility, windowStage: window.WindowStage): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |
| [windowStage](arkts-ability-uiabilitycontext-c.md) | window.WindowStage | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。

## onWindowStageWillDestroy

```TypeScript
onWindowStageWillDestroy?(ability: UIAbility, windowStage: window.WindowStage): void
```

在UIAbility的[onWindowStageDestroy](arkts-ability-app-ability-uiability-uiability-c.md#onWindowStageDestroy)触发前回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onWindowStageWillDestroy?(ability: UIAbility, windowStage: window.WindowStage): void--><!--Device-AbilityLifecycleCallback-onWindowStageWillDestroy?(ability: UIAbility, windowStage: window.WindowStage): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |
| [windowStage](arkts-ability-uiabilitycontext-c.md) | window.WindowStage | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。

## onWindowStageWillRestore

```TypeScript
onWindowStageWillRestore?(ability: UIAbility, windowStage: window.WindowStage): void
```

在UIAbility的[onWindowStageRestore](arkts-ability-app-ability-uiability-uiability-c.md#onWindowStageRestore)触发前回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityLifecycleCallback-onWindowStageWillRestore?(ability: UIAbility, windowStage: window.WindowStage): void--><!--Device-AbilityLifecycleCallback-onWindowStageWillRestore?(ability: UIAbility, windowStage: window.WindowStage): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |
| [windowStage](arkts-ability-uiabilitycontext-c.md) | window.WindowStage | 是 |

## 示例

参见[AbilityLifecycleCallback使用示例](#abilitylifecyclecallback使用示例)。
