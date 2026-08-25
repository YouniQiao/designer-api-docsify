# completeArkTSScriptInApp

## 导入模块

```TypeScript
import { scriptManager } from '@kit.AbilityKit';
```

## completeArkTSScriptInApp

```TypeScript
function completeArkTSScriptInApp(context: Context, requestCode: string, result: ExecuteResult): Promise<void>
```

完成应用的ArkTS脚本执行，上报执行结果。使用Promise异步回调。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | 是 |
| requestCode | string | 是 |
| result | [ExecuteResult](arkts-ability-scriptmanager-executeresult-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000020](../errorcode-ability.md#16000020-传入的context对象不是ability级别context) |
| [16000003](../errorcode-ability.md#16000003-指定的id不存在) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
