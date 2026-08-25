# run

## 导入模块

```TypeScript
import { startupManager } from 'kits/@kit.AbilityKit';
```

## run

```TypeScript
function run(startupTasks: Array<string>, config?: StartupConfig): Promise<void>
```

执行启动框架启动任务或加载so文件。

> **说明：**&gt;
> 本接口不支持执行feature类型HAP中的启动任务，如需要使用相关能力请调用
> [startupManager.run](#run)
> 接口。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AppStartup

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| startupTasks | Array & lt;string & gt; | 是 |
| config | [StartupConfig](arkts-ability-app-appstartup-startupconfig-startupconfig-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [28800001](../errorcode-ability.md#28800001-启动任务或其依赖项不存在) |
| [28800002](../errorcode-ability.md#28800002-启动任务之间存在循环依赖关系) |
| [28800003](../errorcode-ability.md#28800003-运行启动任务时发生错误) |
| [28800004](../errorcode-ability.md#28800004-执行启动任务超时) |


## run

```TypeScript
function run(startupTasks: Array<string>, context: common.AbilityStageContext, config: StartupConfig): Promise<void>
```

执行启动框架启动任务或加载so文件。支持指定[AbilityStageContext](arkts-ability-abilitystagecontext-c.md)用于启动任务的加载。使 用Promise异步回调。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AppStartup

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| startupTasks | Array & lt;string & gt; | 是 |
| context | common.AbilityStageContext | 是 |
| config | [StartupConfig](arkts-ability-app-appstartup-startupconfig-startupconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [28800001](../errorcode-ability.md#28800001-启动任务或其依赖项不存在) |
| [28800002](../errorcode-ability.md#28800002-启动任务之间存在循环依赖关系) |
| [28800003](../errorcode-ability.md#28800003-运行启动任务时发生错误) |
| [28800004](../errorcode-ability.md#28800004-执行启动任务超时) |
