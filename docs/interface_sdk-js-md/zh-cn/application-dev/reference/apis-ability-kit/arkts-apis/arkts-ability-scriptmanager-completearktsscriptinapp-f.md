# completeArkTSScriptInApp

## 导入模块

```TypeScript
import { scriptManager } from 'kits/@kit.AbilityKit';
```

## completeArkTSScriptInApp

```TypeScript
function completeArkTSScriptInApp(context: Context, requestCode: string, result: ExecuteResult): Promise<void>
```

complete arkTS script for in-app skills.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-scriptManager-function completeArkTSScriptInApp(context: Context, requestCode: string, result: ExecuteResult): Promise<void>--><!--Device-scriptManager-function completeArkTSScriptInApp(context: Context, requestCode: string, result: ExecuteResult): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | 是 | Ability context, Used for temporary file authorization. |
| requestCode | string | 是 | Identifying the current operation. It is from ArkTSScriptInfo.requestCode. |
| result | [ExecuteResult](arkts-ability-scriptmanager-executeresult-i.md) | 是 | The result of arkTS script execution. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16000020 | The context is not ability context. |
| 16000050 | Internal error. Possible causes: 1. Connect to system service failed; 2.Send restart message to system service failed; 3.System service failed to communicate with dependency module. |
| 16000003 | The specified ID does not exist. |

