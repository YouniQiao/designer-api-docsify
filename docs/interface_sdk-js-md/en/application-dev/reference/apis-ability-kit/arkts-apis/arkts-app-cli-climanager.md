# @ohos.app.cli.cliManager

The module provides the capability to interact with cli tools in the system.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace cliManager--><!--Device-unnamed-declare namespace cliManager-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cliManager } from 'cliManager';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [clearSession](arkts-ability-climanager-clearsession-f-sys.md#clearSession) | Close session and force kill tool process. |
| [execCmd](arkts-ability-climanager-execcmd-f-sys.md#execCmd) | Execute a command. This API uses a promise to return the result. |
| [execTool](arkts-ability-climanager-exectool-f-sys.md#execTool) | Execute a CLI command |
| [getToolInfoByName](arkts-ability-climanager-gettoolinfobyname-f-sys.md#getToolInfoByName) | Get detailed information of a single tool by its name |
| [querySession](arkts-ability-climanager-querysession-f-sys.md#querySession) | Query session status. |
| [queryToolSummaries](arkts-ability-climanager-querytoolsummaries-f-sys.md#queryToolSummaries) | Query all tool summary information. The summary information only contains the fields: name, description, version. |
| [queryTools](arkts-ability-climanager-querytools-f-sys.md#queryTools) | Query all detailed information of tools |
| [sendMessage](arkts-ability-climanager-sendmessage-f-sys.md#sendMessage) | Send event to target process. |
| [subscribeSession](arkts-ability-climanager-subscribesession-f-sys.md#subscribeSession) | Subscribe session event. |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [CliSessionInfo](arkts-ability-climanager-clisessioninfo-i-sys.md) | Session information of a tool execution. |
| [ExecCmdOptions](arkts-ability-climanager-execcmdoptions-i-sys.md) | Options for executing a command. |
| [ExecOptions](arkts-ability-climanager-execoptions-i-sys.md) | Tool execution options. |
| [ExecResult](arkts-ability-climanager-execresult-i-sys.md) | Execute result of a tool execution. |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [SessionStatus](arkts-ability-climanager-sessionstatus-e-sys.md) | Enum for session status. |
<!--DelEnd-->

