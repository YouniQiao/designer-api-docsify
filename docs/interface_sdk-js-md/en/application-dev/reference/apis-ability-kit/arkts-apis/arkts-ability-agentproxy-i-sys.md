# AgentProxy (System API)

The proxy object of the AgentExtensionAbility, used to send messages to the AgentExtensionAbility, etc.@interface AgentProxy

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

## authorize

```TypeScript
authorize(handshakeData: string): void
```

Send authentication to the AgentExtensionAbility.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

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
