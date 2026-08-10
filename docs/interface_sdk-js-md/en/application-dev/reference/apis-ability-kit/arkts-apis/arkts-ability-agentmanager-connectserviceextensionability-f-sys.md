# connectServiceExtensionAbility (System API)

## Modules to Import

```TypeScript
import { agentManager } from 'kits/@kit.AbilityKit';
```

## connectServiceExtensionAbility

```TypeScript
function connectServiceExtensionAbility(context: AgentExtensionContext, want: Want, callback: ConnectOptions): long
```

Connects an AgentExtensionAbility to a ServiceExtensionAbility.If the target service extension ability is visible, you can connect to it.If the target service extension ability is invisible, you need to apply for permission:ohos.permission.START_INVISIBLE_ABILITY to connect to it.If the target service extension ability is on a remote device, you need to apply for permission:ohos.permission.DISTRIBUTED_DATASYNC.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-agentManager-function connectServiceExtensionAbility(context: AgentExtensionContext, want: Want, callback: ConnectOptions): long--><!--Device-agentManager-function connectServiceExtensionAbility(context: AgentExtensionContext, want: Want, callback: ConnectOptions): long-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [AgentExtensionContext](arkts-ability-agentextensioncontext-c.md) | Yes | The context of the current agent extension ability. |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | Indicates the service extension ability to connect. |
| callback | [ConnectOptions](arkts-ability-connectoptions-connectoptions-i.md) | Yes | Indicates the callback of connection. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | Returns the connection id. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. Possible causes: 1.Connect to system service failed. 2.System service failed to communicate with dependency module. |
| 202 | Not system application. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by enterprise device management (EDM). |
| 16000008 | The crowdtesting application expires. |
| 16000073 | The app clone index is invalid. |
| 16000011 | The context does not exist. |

