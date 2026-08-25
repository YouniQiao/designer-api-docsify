# execCmd（系统接口）

## 导入模块

```TypeScript
import { cliManager } from 'kits/@kit.AbilityKit';
```

## execCmd

```TypeScript
function execCmd(cmd: string, execCmdOptions?: ExecCmdOptions): Promise<CliSessionInfo>
```

执行Shell命令，返回会话信息。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.EXEC_CLI_TOOL

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cmd | string | 是 |
| execCmdOptions | [ExecCmdOptions](arkts-ability-climanager-execcmdoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CliSessionInfo](arkts-ability-climanager-clisessioninfo-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [35600031](../errorcode-ability.md#35600031-工具并发数已达上限) |
| [35600050](../errorcode-ability.md#35600050-偶发性报错) |
