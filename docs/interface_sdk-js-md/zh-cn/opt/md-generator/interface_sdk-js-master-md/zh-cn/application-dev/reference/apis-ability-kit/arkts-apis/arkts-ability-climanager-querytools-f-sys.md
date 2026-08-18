# queryTools（系统接口）

## 导入模块

```TypeScript
```

## queryTools

```TypeScript
function queryTools(): Promise<Array<ToolInfo>>
```

查询所有CLI工具的详细信息，使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.QUERY_CLI_TOOL

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-cliManager-function queryTools(): Promise<Array<ToolInfo>>--><!--Device-cliManager-function queryTools(): Promise<Array<ToolInfo>>-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[ToolInfo](arkts-ability-toolinfo-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [35600050](../errorcode-ability.md#35600050-偶发性报错) |
