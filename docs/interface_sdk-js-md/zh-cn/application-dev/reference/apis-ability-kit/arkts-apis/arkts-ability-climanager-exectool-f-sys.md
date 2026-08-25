# execTool（系统接口）

## 导入模块

```TypeScript
import { cliManager } from 'kits/@kit.AbilityKit';
```

## execTool

```TypeScript
function execTool(toolName: string, subCommand: string, args: Record<string, Object>, challenge: string,
    execOptions?: ExecOptions): Promise<CliSessionInfo>
```

执行CLI命令

**起始版本：** 26.0.0

**需要权限：** ohos.permission.EXEC_CLI_TOOL

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [toolName](arkts-ability-climanager-clisessioninfo-i-sys.md) | string | 是 |
| subCommand | string | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Record & lt;string, Object & gt; | 是 |
| challenge | string | 是 |
| execOptions | [ExecOptions](arkts-ability-climanager-execoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CliSessionInfo](arkts-ability-climanager-clisessioninfo-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [35600030](../errorcode-ability.md#35600030-cli工具不存在) |
| [35600031](../errorcode-ability.md#35600031-工具并发数已达上限) |
| [35600050](../errorcode-ability.md#35600050-偶发性报错) |
