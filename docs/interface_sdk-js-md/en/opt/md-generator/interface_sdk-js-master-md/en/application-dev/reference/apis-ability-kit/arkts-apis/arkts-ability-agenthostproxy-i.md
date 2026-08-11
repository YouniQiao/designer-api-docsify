# AgentHostProxy

The proxy object of the connected party for the AgentExtensionAbility,used to send messages to the connected party, etc.

**Since:** 24

<!--Device-unnamed-export interface AgentHostProxy--><!--Device-unnamed-export interface AgentHostProxy-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

## authorize

```TypeScript
authorize(handshakeData: string): void
```

Send authentication to an agent service host.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-AgentHostProxy-authorize(handshakeData: string): void--><!--Device-AgentHostProxy-authorize(handshakeData: string): void-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

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

Send data to an agent service host.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-AgentHostProxy-sendData(data: string): void--><!--Device-AgentHostProxy-sendData(data: string): void-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [35600002](../errorcode-ability.md#35600002-failed-to-send-ipc-messages) |
