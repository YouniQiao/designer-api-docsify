# @ohos.app.cli.cliManager

本模块提供与系统命令行工具（CLI）的交互能力，可以查询工具信息、调用并执行CLI命令，以及管理会话。会话在调用execTool接口时创建，用于跟踪CLI工具的执行状态和结果。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace cliManager--><!--Device-unnamed-declare namespace cliManager-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [clearSession](arkts-ability-climanager-clearsession-f-sys.md#clearsession系统接口) |
| [execCmd](arkts-ability-climanager-execcmd-f-sys.md#execcmd系统接口) |
| [execTool](arkts-ability-climanager-exectool-f-sys.md#exectool系统接口) |
| [getToolInfoByName](arkts-ability-climanager-gettoolinfobyname-f-sys.md#gettoolinfobyname系统接口) |
| [querySession](arkts-ability-climanager-querysession-f-sys.md#querysession系统接口) |
| [queryToolSummaries](arkts-ability-climanager-querytoolsummaries-f-sys.md#querytoolsummaries系统接口) |
| [queryTools](arkts-ability-climanager-querytools-f-sys.md#querytools系统接口) |
| [sendMessage](arkts-ability-climanager-sendmessage-f-sys.md#sendmessage系统接口) |
| [subscribeSession](arkts-ability-climanager-subscribesession-f-sys.md#subscribesession系统接口) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [CliSessionInfo](arkts-ability-climanager-clisessioninfo-i-sys.md) |
| [ExecCmdOptions](arkts-ability-climanager-execcmdoptions-i-sys.md) |
| [ExecOptions](arkts-ability-climanager-execoptions-i-sys.md) |
| [ExecResult](arkts-ability-climanager-execresult-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [SessionStatus](arkts-ability-climanager-sessionstatus-e-sys.md) |
<!--DelEnd-->
