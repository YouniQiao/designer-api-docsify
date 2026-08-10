# @ohos.app.cli.cliManager

The module provides the capability to interact with cli tools in the system.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace cliManager--><!--Device-unnamed-declare namespace cliManager-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { cliManager } from 'kits/@kit.AbilityKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [clearSession](arkts-ability-climanager-clearsession-f-sys.md#clearsession) | Close session and force kill tool process. |
| [execCmd](arkts-ability-climanager-execcmd-f-sys.md#execcmd) | Execute a command. This API uses a promise to return the result. |
| [execTool](arkts-ability-climanager-exectool-f-sys.md#exectool) | Execute a CLI command |
| [getToolInfoByName](arkts-ability-climanager-gettoolinfobyname-f-sys.md#gettoolinfobyname) | Get detailed information of a single tool by its name |
| [querySession](arkts-ability-climanager-querysession-f-sys.md#querysession) | Query session status. |
| [queryToolSummaries](arkts-ability-climanager-querytoolsummaries-f-sys.md#querytoolsummaries) | Query all tool summary information. The summary information only contains the fields: name, description, version. |
| [queryTools](arkts-ability-climanager-querytools-f-sys.md#querytools) | Query all detailed information of tools |
| [sendMessage](arkts-ability-climanager-sendmessage-f-sys.md#sendmessage) | Send event to target process. |
| [subscribeSession](arkts-ability-climanager-subscribesession-f-sys.md#subscribesession) | Subscribe session event. |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [CliSessionInfo](arkts-ability-climanager-clisessioninfo-i-sys.md) | Session information of a tool execution. |
| [ExecCmdOptions](arkts-ability-climanager-execcmdoptions-i-sys.md) | Options for executing a command. |
| [ExecOptions](arkts-ability-climanager-execoptions-i-sys.md) | Tool execution options. |
| [ExecResult](arkts-ability-climanager-execresult-i-sys.md) | Execute result of a tool execution. |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 | 说明 |
| --- | --- |
| [SessionStatus](arkts-ability-climanager-sessionstatus-e-sys.md) | Enum for session status. |
<!--DelEnd-->

