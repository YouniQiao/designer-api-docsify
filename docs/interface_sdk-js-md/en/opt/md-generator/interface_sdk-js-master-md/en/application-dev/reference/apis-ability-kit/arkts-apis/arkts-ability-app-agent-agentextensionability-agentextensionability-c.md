# AgentExtensionAbility

The class of agent extension ability. This class cannot be used in Harmony Archive(HAR).

**Inheritance/Implementation:** AgentExtensionAbility extends ExtensionAbility

**Since:** 24

**Deprecated since:** -1

<!--Device-unnamed-declare class AgentExtensionAbility--><!--Device-unnamed-declare class AgentExtensionAbility-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

## Modules to Import

```TypeScript
import { AgentExtensionAbility } from '@kit.AbilityKit';
```

## onAuth

```TypeScript
onAuth(proxy: AgentHostProxy, handshakeData: string): void
```

Called back when authentication is sent.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-AgentExtensionAbility-onAuth(proxy: AgentHostProxy, handshakeData: string): void--><!--Device-AgentExtensionAbility-onAuth(proxy: AgentHostProxy, handshakeData: string): void-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| proxy | [AgentHostProxy](arkts-ability-agenthostproxy-i.md) | Yes |
| handshakeData | string | Yes |

## onConnect

```TypeScript
onConnect(want: Want, proxy: AgentHostProxy): void
```

Called back when an agent extension is connected to an ability.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-AgentExtensionAbility-onConnect(want: Want, proxy: AgentHostProxy): void--><!--Device-AgentExtensionAbility-onConnect(want: Want, proxy: AgentHostProxy): void-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| proxy | [AgentHostProxy](arkts-ability-agenthostproxy-i.md) | Yes |

## onCreate

```TypeScript
onCreate(want: Want): void
```

Called back when an agent extension is started for initialization.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-AgentExtensionAbility-onCreate(want: Want): void--><!--Device-AgentExtensionAbility-onCreate(want: Want): void-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

## onData

```TypeScript
onData(proxy: AgentHostProxy, data: string): void
```

Called back when data is sent.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-AgentExtensionAbility-onData(proxy: AgentHostProxy, data: string): void--><!--Device-AgentExtensionAbility-onData(proxy: AgentHostProxy, data: string): void-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| proxy | [AgentHostProxy](arkts-ability-agenthostproxy-i.md) | Yes |
| data | string | Yes |

## onDestroy

```TypeScript
onDestroy(): void
```

Called back before an agent service extension is destroyed.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-AgentExtensionAbility-onDestroy(): void--><!--Device-AgentExtensionAbility-onDestroy(): void-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

## onDisconnect

```TypeScript
onDisconnect(want: Want, proxy: AgentHostProxy): void
```

Called back when ability connected to an agent service extension is disconnected.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-AgentExtensionAbility-onDisconnect(want: Want, proxy: AgentHostProxy): void--><!--Device-AgentExtensionAbility-onDisconnect(want: Want, proxy: AgentHostProxy): void-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| proxy | [AgentHostProxy](arkts-ability-agenthostproxy-i.md) | Yes |

## context

```TypeScript
context: AgentExtensionContext
```

Context of the AgentExtensionAbility.

**Type:** [AgentExtensionContext](arkts-ability-agentextensioncontext-c.md)

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-AgentExtensionAbility-context: AgentExtensionContext--><!--Device-AgentExtensionAbility-context: AgentExtensionContext-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core
