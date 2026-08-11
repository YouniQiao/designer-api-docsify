# UIServiceExtensionConnectCallback

UIServiceExtensionConnectCallback provides callbacks for the connection to a UIServiceExtensionAbility.

> **NOTE：**
> 
> - The APIs of this module must be used in the main thread, but not in child threads such as Worker and TaskPool.

**Since:** 14

<!--Device-unnamed-export default interface UIServiceExtensionConnectCallback--><!--Device-unnamed-export default interface UIServiceExtensionConnectCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onData

```TypeScript
onData(data: Record<string, Object>): void
```

Called to receive data when a connection to the UIServiceExtensionAbility is established.

> **NOTE：**
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-UIServiceExtensionConnectCallback-onData(data: Record<string, Object>): void--><!--Device-UIServiceExtensionConnectCallback-onData(data: Record<string, Object>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt; | Yes |

## onDisconnect

```TypeScript
onDisconnect(): void
```

Called when the connection to the UIServiceExtensionAbility is interrupted.

> **NOTE：**
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-UIServiceExtensionConnectCallback-onDisconnect(): void--><!--Device-UIServiceExtensionConnectCallback-onDisconnect(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core
