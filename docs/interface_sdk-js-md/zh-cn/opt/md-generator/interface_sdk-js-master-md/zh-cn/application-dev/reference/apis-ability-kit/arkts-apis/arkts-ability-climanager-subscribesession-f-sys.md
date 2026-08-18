# subscribeSession（系统接口）

## 导入模块

```TypeScript
```

## subscribeSession

```TypeScript
function subscribeSession(sessionId: string, callback: ToolEventCallback): Promise<void>
```

订阅指定CLI工具会话的事件。会话运行期间，CLI工具产生的标准输出、标准错误、退出或错误事件通过回调返回。 > **说明：** > > 会话仅限创建进程管理：只有调用`execTool`创建该会话的进程可以调用本接口。其他进程即使获取到`sessionId`，调用本接口也会抛出错误码201（Permission denied）。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.EXEC_CLI_TOOL

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-cliManager-function subscribeSession(sessionId: string, callback: ToolEventCallback): Promise<void>--><!--Device-cliManager-function subscribeSession(sessionId: string, callback: ToolEventCallback): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | string | 是 |
| callback | [ToolEventCallback](arkts-ability-tooleventcallback-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [35600050](../errorcode-ability.md#35600050-偶发性报错) |
| [35600032](../errorcode-ability.md#35600032-指定的session不存在) |
