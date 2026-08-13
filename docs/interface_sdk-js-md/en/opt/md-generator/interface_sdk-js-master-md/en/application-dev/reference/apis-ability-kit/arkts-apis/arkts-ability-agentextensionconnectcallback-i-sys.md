# AgentExtensionConnectCallback (System API)

Agent extension connect callback.

**Since:** 24

**Deprecated since:** -1

<!--Device-unnamed-export interface AgentExtensionConnectCallback--><!--Device-unnamed-export interface AgentExtensionConnectCallback-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

## onAuth

```TypeScript
onAuth(handshakeData: string): void
```

Called back when authentication is received.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AgentExtensionConnectCallback-onAuth(handshakeData: string): void--><!--Device-AgentExtensionConnectCallback-onAuth(handshakeData: string): void-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handshakeData | string | Yes |

## onData

```TypeScript
onData(data: string): void
```

Called back when data is received.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AgentExtensionConnectCallback-onData(data: string): void--><!--Device-AgentExtensionConnectCallback-onData(data: string): void-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | string | Yes |

## onDisconnect

```TypeScript
onDisconnect(): void
```

The callback interface was disconnected successfully.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AgentExtensionConnectCallback-onDisconnect(): void--><!--Device-AgentExtensionConnectCallback-onDisconnect(): void-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.
