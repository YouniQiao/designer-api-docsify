# saveAppState

## 导入模块

```TypeScript
import { appRecovery } from 'kits/@kit.AbilityKit';
```

## saveAppState

```TypeScript
function saveAppState(): boolean
```

保存当前App状态，可以配合[errorManager](arkts-app-ability-errormanager.md)相关接口使用。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| boolean |


## saveAppState

```TypeScript
function saveAppState(context?: UIAbilityContext): boolean
```

主动保存Ability的状态，这个状态将在下次恢复启动时使用。可以配合[errorManager](arkts-app-ability-errormanager.md)相关接口使用。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIAbilityContext](arkts-ability-uiabilitycontext-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |
