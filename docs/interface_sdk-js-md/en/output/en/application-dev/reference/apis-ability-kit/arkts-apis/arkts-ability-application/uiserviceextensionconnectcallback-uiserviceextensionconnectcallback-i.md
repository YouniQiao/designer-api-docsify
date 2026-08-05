# UIServiceExtensionConnectCallback

UIServiceExtensionConnectCallback provides callbacks for the connection to a UIServiceExtensionAbility. > **NOTE** > > - The APIs of this module must be used in the main thread, but not in child threads such as Worker and TaskPool.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-unnamed-export default interface UIServiceExtensionConnectCallback--><!--Device-unnamed-export default interface UIServiceExtensionConnectCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onData

```TypeScript
onData(data: Record<string, Object>): void
```

Called to receive data when a connection to the UIServiceExtensionAbility is established. > **NOTE** > > For details about the startup rules for the components in the stage model, see > \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-UIServiceExtensionConnectCallback-onData(data: Record<string, Object>): void--><!--Device-UIServiceExtensionConnectCallback-onData(data: Record<string, Object>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, Object&gt; | Yes | Data about the UIServiceExtensionAbility connection. |

## onData

```TypeScript
onData(data: Record<string, RecordData>): void
```

Called back when data is sent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionConnectCallback-onData(data: Record<string, RecordData>): void--><!--Device-UIServiceExtensionConnectCallback-onData(data: Record<string, RecordData>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, \_\_\_MD\_LINK\_USD\_1\_\_\_&gt; | Yes | Indicates the received data. |

## onDisconnect

```TypeScript
onDisconnect(): void
```

Called when the connection to the UIServiceExtensionAbility is interrupted. > **NOTE** > > For details about the startup rules for the components in the stage model, see > \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-UIServiceExtensionConnectCallback-onDisconnect(): void--><!--Device-UIServiceExtensionConnectCallback-onDisconnect(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

