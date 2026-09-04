# AbilityLifecycleCallback

[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)从创建到销毁过程其生命周期是动态变化的。AbilityLifecycleCallback模块提供监听[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)生命周期变化的能力，可用于统计每个UIAbility的运行时长、执行与UIAbility业务逻辑解耦的数据加载等场景。

**起始版本：** 9

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## 导入模块

```TypeScript
import { AbilityLifecycleCallback } from '@kit.AbilityKit';
```

## onAbilityBackground

```TypeScript
onAbilityBackground(ability: UIAbility): void
```

在UIAbility的[onBackground](arkts-ability-app-ability-uiability-uiability-c.md#onbackground)触发后回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:

## onAbilityContinue

```TypeScript
onAbilityContinue(ability: UIAbility): void
```

在UIAbility的[onContinue](arkts-ability-app-ability-uiability-uiability-c.md#oncontinue)触发后回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:

## onAbilityCreate

```TypeScript
onAbilityCreate(ability: UIAbility): void
```

在UIAbility的[onCreate](arkts-ability-app-ability-uiability-uiability-c.md#oncreate)触发后回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:

## onAbilityDestroy

```TypeScript
onAbilityDestroy(ability: UIAbility): void
```

在UIAbility的[onDestroy](arkts-ability-app-ability-uiability-uiability-c.md#ondestroy)触发后回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:

## onAbilityForeground

```TypeScript
onAbilityForeground(ability: UIAbility): void
```

在UIAbility的[onForeground](arkts-ability-app-ability-uiability-uiability-c.md#onforeground)触发后回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:

## onAbilitySaveState

```TypeScript
onAbilitySaveState?(ability: UIAbility): void
```

在UIAbility的[onSaveState](arkts-ability-app-ability-uiability-uiability-c.md#onsavestate)触发后回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:

## onAbilityWillBackground

```TypeScript
onAbilityWillBackground?(ability: UIAbility): void
```

在UIAbility的[onBackground](arkts-ability-app-ability-uiability-uiability-c.md#onbackground)触发前回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:

## onAbilityWillContinue

```TypeScript
onAbilityWillContinue?(ability: UIAbility): void
```

在UIAbility的[onContinue](arkts-ability-app-ability-uiability-uiability-c.md#oncontinue)触发前回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:

## onAbilityWillCreate

```TypeScript
onAbilityWillCreate?(ability: UIAbility): void
```

在UIAbility的[onCreate](arkts-ability-app-ability-uiability-uiability-c.md#oncreate)触发前回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:

## onAbilityWillDestroy

```TypeScript
onAbilityWillDestroy?(ability: UIAbility): void
```

在UIAbility的[onDestroy](arkts-ability-app-ability-uiability-uiability-c.md#ondestroy)触发前回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:

## onAbilityWillForeground

```TypeScript
onAbilityWillForeground?(ability: UIAbility): void
```

在UIAbility的[onForeground](arkts-ability-app-ability-uiability-uiability-c.md#onforeground)触发前回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:

## onAbilityWillSaveState

```TypeScript
onAbilityWillSaveState?(ability: UIAbility): void
```

在UIAbility的[onSaveState](arkts-ability-app-ability-uiability-uiability-c.md#onsavestate)触发前回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:

## onNewWant

```TypeScript
onNewWant?(ability: UIAbility): void
```

在UIAbility的[onNewWant](arkts-ability-app-ability-uiability-uiability-c.md#onnewwant)触发后回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:

## onWillNewWant

```TypeScript
onWillNewWant?(ability: UIAbility): void
```

在UIAbility的[onNewWant](arkts-ability-app-ability-uiability-uiability-c.md#onnewwant)触发前回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:

## onWindowStageActive

```TypeScript
onWindowStageActive(ability: UIAbility, windowStage: window.WindowStage): void
```

在UIAbility主窗获焦时触发回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象。 |
| windowStage | [window.WindowStage](../../apis-arkui/arkts-apis/arkts-arkui-window-windowstage-i.md) | 是 | 回调事件对应的UIAbility主窗管理器。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:

## onWindowStageCreate

```TypeScript
onWindowStageCreate(ability: UIAbility, windowStage: window.WindowStage): void
```

在UIAbility的[onWindowStageCreate](arkts-ability-app-ability-uiability-uiability-c.md#onwindowstagecreate)触发后回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象。 |
| windowStage | [window.WindowStage](../../apis-arkui/arkts-apis/arkts-arkui-window-windowstage-i.md) | 是 | 回调事件对应的UIAbility主窗管理器。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:

## onWindowStageDestroy

```TypeScript
onWindowStageDestroy(ability: UIAbility, windowStage: window.WindowStage): void
```

在UIAbility的[onWindowStageDestroy](arkts-ability-app-ability-uiability-uiability-c.md#onwindowstagedestroy)触发后回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象 |
| windowStage | [window.WindowStage](../../apis-arkui/arkts-apis/arkts-arkui-window-windowstage-i.md) | 是 | 回调事件对应的UIAbility主窗管理器。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:

## onWindowStageInactive

```TypeScript
onWindowStageInactive(ability: UIAbility, windowStage: window.WindowStage): void
```

在UIAbility主窗失焦时触发回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象。 |
| windowStage | [window.WindowStage](../../apis-arkui/arkts-apis/arkts-arkui-window-windowstage-i.md) | 是 | 回调事件对应的UIAbility主窗管理器。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:

## onWindowStageRestore

```TypeScript
onWindowStageRestore?(ability: UIAbility, windowStage: window.WindowStage): void
```

在UIAbility的[onWindowStageRestore](arkts-ability-app-ability-uiability-uiability-c.md#onwindowstagerestore)触发后回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象。 |
| windowStage | [window.WindowStage](../../apis-arkui/arkts-apis/arkts-arkui-window-windowstage-i.md) | 是 | 回调事件对应的UIAbility主窗管理器。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:

## onWindowStageWillCreate

```TypeScript
onWindowStageWillCreate?(ability: UIAbility, windowStage: window.WindowStage): void
```

在UIAbility的[onWindowStageCreate](arkts-ability-app-ability-uiability-uiability-c.md#onwindowstagecreate)触发前回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象。 |
| windowStage | [window.WindowStage](../../apis-arkui/arkts-apis/arkts-arkui-window-windowstage-i.md) | 是 | 回调事件对应的UIAbility主窗管理器。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:

## onWindowStageWillDestroy

```TypeScript
onWindowStageWillDestroy?(ability: UIAbility, windowStage: window.WindowStage): void
```

在UIAbility的[onWindowStageDestroy](arkts-ability-app-ability-uiability-uiability-c.md#onwindowstagedestroy)触发前回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象。 |
| windowStage | [window.WindowStage](../../apis-arkui/arkts-apis/arkts-arkui-window-windowstage-i.md) | 是 | 回调事件对应的UIAbility主窗管理器。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:

## onWindowStageWillRestore

```TypeScript
onWindowStageWillRestore?(ability: UIAbility, windowStage: window.WindowStage): void
```

在UIAbility的[onWindowStageRestore](arkts-ability-app-ability-uiability-uiability-c.md#onwindowstagerestore)触发前回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 | 回调事件对应的UIAbility对象。 |
| windowStage | [window.WindowStage](../../apis-arkui/arkts-apis/arkts-arkui-window-windowstage-i.md) | 是 | 回调事件对应的UIAbility主窗管理器。 |

**示例**

参见AbilityLifecycleCallback使用示例。
- simpleType:
