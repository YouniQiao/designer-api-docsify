# InsightIntentContext

本模块提供意图执行上下文，是[意图执行基类](arkts-ability-app-ability-insightintentexecutor-insightintentexecutor-c.md)和 [@InsightIntentEntry的意图执行基类](arkts-ability-app-ability-insightintententryexecutor-insightintententryexecutor-c.md)的属性，为意图执行提 供基础能力，例如启动本应用内的[UIAbility组件](arkts-ability-app-ability-uiability-uiability-c.md)。

**起始版本：** 11

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { InsightIntentContext } from 'kits/@kit.AbilityKit';
```

## setReturnModeForUIAbilityForeground

```TypeScript
setReturnModeForUIAbilityForeground(returnMode: insightIntent.ReturnMode): void
```

设置意图执行结果的返回形式，适用于执行模式为[UI_ABILITY_FOREGROUND](arkts-ability-insightintent-executemode-e.md)的意图。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| returnMode | insightIntent.ReturnMode | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## setReturnModeForUIExtensionAbility

```TypeScript
setReturnModeForUIExtensionAbility(returnMode: insightIntent.ReturnMode): void
```

设置意图执行结果的返回形式，适用于执行模式为[UI_EXTENSION_ABILITY](arkts-ability-insightintent-executemode-e.md)的意图。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| returnMode | insightIntent.ReturnMode | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## startAbility

```TypeScript
startAbility(want: Want, callback: AsyncCallback<void>): void
```

启动UIAbility组件，仅支持启动本应用内的UIAbility组件。使用callback异步回调。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16000061](../errorcode-ability.md#16000061-不支持的操作) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |

## startAbility

```TypeScript
startAbility(want: Want): Promise<void>
```

启动UIAbility组件，仅支持启动本应用内的UIAbility组件。使用Promise异步回调。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16000061](../errorcode-ability.md#16000061-不支持的操作) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |

## instanceId

```TypeScript
instanceId: number
```

意图实例唯一ID。用于通过 [insightIntentProvider.sendExecuteResult接口] sendExecuteResult 和 [insightIntentProvider.sendIntentResult接口] sendIntentResult返回指定意图的执行结果。

**类型：** number

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core
