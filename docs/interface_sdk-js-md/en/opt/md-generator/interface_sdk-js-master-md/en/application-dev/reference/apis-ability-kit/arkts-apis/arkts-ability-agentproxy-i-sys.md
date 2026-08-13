# AgentProxy (System API)

The proxy object of the AgentExtensionAbility, used to send messages to the AgentExtensionAbility, etc.

**Since:** 24

**Deprecated since:** -1

<!--Device-unnamed-export interface AgentProxy--><!--Device-unnamed-export interface AgentProxy-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

## authorize

```TypeScript
authorize(handshakeData: string): void
```

Send authentication to the AgentExtensionAbility.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AgentProxy-authorize(handshakeData: string): void--><!--Device-AgentProxy-authorize(handshakeData: string): void-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handshakeData | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [35600002](../errorcode-ability.md#35600002-failed-to-send-ipc-messages) |

## sendData

```TypeScript
sendData(data: string): void
```

Send data to the AgentExtensionAbility.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AgentProxy-sendData(data: string): void--><!--Device-AgentProxy-sendData(data: string): void-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [35600002](../errorcode-ability.md#35600002-failed-to-send-ipc-messages) |
