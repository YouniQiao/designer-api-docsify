# sendMessage（系统接口）

## 导入模块

```TypeScript
import { cliManager } from 'kits/@kit.AbilityKit';
```

## sendMessage

```TypeScript
function sendMessage(sessionId: string, message: string): Promise<void>
```

向指定CLI工具会话对应的进程发送消息。

> **说明：**&gt;
> 会话仅限创建进程管理：只有调用`execTool`创建该会话的进程可以调用本接口。其他进程即使获取到`sessionId`，调用本接口也会抛出错误码201（Permission denied）。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.EXEC_CLI_TOOL

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | string | 是 |
| message | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [35600032](../errorcode-ability.md#35600032-指定的session不存在) |
| [35600033](../errorcode-ability.md#35600033-向工具进程写入消息失败) |
| [35600050](../errorcode-ability.md#35600050-偶发性报错) |
