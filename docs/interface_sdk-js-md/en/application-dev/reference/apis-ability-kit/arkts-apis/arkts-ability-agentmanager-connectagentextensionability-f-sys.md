# connectAgentExtensionAbility (System API)

## Modules to Import

```TypeScript
import { agentManager } from 'kits/@kit.AbilityKit';
```

## connectAgentExtensionAbility

```TypeScript
function connectAgentExtensionAbility(want: Want, agentId: string,
    callback: AgentExtensionConnectCallback): Promise<AgentProxy>
```

Connects to an AgentExtensionAbility.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.CONNECT_AGENT

**Model restriction:** This API can be used only in the stage model.

<!--Device-agentManager-function connectAgentExtensionAbility(want: Want, agentId: string,    callback: AgentExtensionConnectCallback): Promise<AgentProxy>--><!--Device-agentManager-function connectAgentExtensionAbility(want: Want, agentId: string,    callback: AgentExtensionConnectCallback): Promise<AgentProxy>-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | Indicates the want info to connect. |
| agentId | string | Yes | The agent id to connect. |
| callback | [AgentExtensionConnectCallback](arkts-ability-agentextensionconnectcallback-i-sys.md) | Yes | The callback of connection. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AgentProxy](arkts-ability-agentproxy-i-sys.md)&gt; | The promise to get AgentProxy. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. Possible causes: 1.Connect to system service failed. 2.System service failed to communicate with dependency module. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000012 | The application is controlled. |
| 35600007 | The specified LOW_CODE agent is already active and is not yet completed. |
| 16000013 | The application is controlled by enterprise device management (EDM). |
| 16000008 | The crowdtesting application expires. |
| 35600003 | Maximum connections from the same caller have been reached. Please disconnect at least one agent extension beforehand. |
| 16000073 | The app clone index is invalid. |
| 35600001 | The specified agentId does not exist. |

