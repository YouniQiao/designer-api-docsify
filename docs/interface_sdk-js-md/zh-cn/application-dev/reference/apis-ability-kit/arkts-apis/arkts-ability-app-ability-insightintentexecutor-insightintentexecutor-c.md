# InsightIntentExecutor

本模块提供意图执行基类，开发者通过本模块对接端侧[意图框架](../../../application-models/insight-intent-overview.md)， [通过配置文件开发意图][configuration files](../../../application-models/insight-intent-config-development.md)实现意图的业务逻辑。除了可以通过配置文件开发意图，还可以通过装饰器开发意图。对于API version 20及以后的版本，推荐使用 [通过装饰器开发意图](../../../application-models/insight-intent-decorator-development.md)。

**起始版本：** 11

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { InsightIntentExecutor } from 'kits/@kit.AbilityKit';
```

## onExecuteInServiceExtensionAbility

```TypeScript
onExecuteInServiceExtensionAbility(name: string, param: Record<string, Object>):
    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>
```

当意图执行依赖ServiceExtensionAbility组件启动时，会在ServiceExtensionAbility组件生命周期执行中触发本意图执行接口。支持同步返回和使用Promise异步返回。  
- 意图执行时ServiceExtensionAbility生命周期触发顺序：onCreate、onRequest、onExecuteInServiceExtensionAbility。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| param | Record & lt;string, Object & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| insightIntent.ExecuteResult \| Promise & lt;insightIntent.ExecuteResult & gt; |

## onExecuteInUIAbilityBackgroundMode

```TypeScript
onExecuteInUIAbilityBackgroundMode(name: string, param: Record<string, Object>):
    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>
```

当意图执行依赖[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)组件后台启动时，会在UIAbility组件生命周期执行中触发本意图执行接口。支持同步返回和使用Promise异步返回。  
- 若UIAbility组件冷启动，意图执行时UIAbility组件生命周期触发顺序：[onCreate](arkts-ability-app-ability-uiability-uiability-c.md#oncreate)、  
onExecuteInUIAbilityBackgroundMode、[onBackground](arkts-ability-app-ability-uiability-uiability-c.md#onbackground)。  
- 若UIAbility组件热启动，意图执行时UIAbility组件生命周期触发顺序：onExecuteInUIAbilityBackgroundMode。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| param | Record & lt;string, Object & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| insightIntent.ExecuteResult \| Promise & lt;insightIntent.ExecuteResult & gt; |

## onExecuteInUIAbilityForegroundMode

```TypeScript
onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>, pageLoader: window.WindowStage):
    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>
```

当意图执行依赖[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)组件前台启动时，会在UIAbility组件生命周期执行中触发本意图执行接口。支持同步返回和使用Promise异步返回。  
- 若UIAbility组件冷启动，意图执行时UIAbility组件生命周期触发顺序：[onCreate](arkts-ability-app-ability-uiability-uiability-c.md#oncreate)、  
[onWindowStageCreate](arkts-ability-app-ability-uiability-uiability-c.md#onwindowstagecreate)、 onExecuteInUIAbilityForegroundMode、[onForeground](arkts-ability-app-ability-uiability-uiability-c.md#onforeground)。  
- 若UIAbility组件热启动，且启动时UIAbility组件处于后台，意图执行时UIAbility组件生命周期触发顺序：  
[onNewWant](arkts-ability-app-ability-uiability-uiability-c.md#onnewwant)、onExecuteInUIAbilityForegroundMode、 [onForeground](arkts-ability-app-ability-uiability-uiability-c.md#onforeground)。  
- 若UIAbility组件热启动，且启动时UIAbility组件处于前台，意图执行时UIAbility组件生命周期触发顺序：onExecuteInUIAbilityForegroundMode。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| param | Record & lt;string, Object & gt; | 是 |
| pageLoader | window.WindowStage | 是 |

**返回值：**

| 类型 |
| --- |
| insightIntent.ExecuteResult \| Promise & lt;insightIntent.ExecuteResult & gt; |

## onExecuteInUIExtensionAbility

```TypeScript
onExecuteInUIExtensionAbility(name: string, param: Record<string, Object>, pageLoader: UIExtensionContentSession):
    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>
```

当意图执行依赖[UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md)启动时，会在UIExtensionAbility组 件生命周期执行中触发本意图执行接口。支持同步返回和使用Promise异步返回。  
- 意图执行时UIExtensionAbility生命周期触发顺序：  
[onCreate](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#oncreate)、 [onSessionCreate](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#onsessioncreate)、 onExecuteInUIExtensionAbility、 [onForeground](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#onforeground)。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| param | Record & lt;string, Object & gt; | 是 |
| pageLoader | [UIExtensionContentSession](arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| insightIntent.ExecuteResult \| Promise & lt;insightIntent.ExecuteResult & gt; |

## context

```TypeScript
context: InsightIntentContext
```

意图执行上下文。

**类型：** [InsightIntentContext](arkts-ability-app-ability-insightintentcontext-insightintentcontext-c.md)

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core
