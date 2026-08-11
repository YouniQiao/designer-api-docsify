# UIServiceProxy

UIServiceProxy functions as a proxy to send data from the UIServiceExtensionAbility client to the server.

> **NOTE：**
> 
> - The APIs of this module must be used in the main thread, but not in child threads such as Worker and TaskPool.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-unnamed-export default interface UIServiceProxy--><!--Device-unnamed-export default interface UIServiceProxy-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## sendData

```TypeScript
sendData(data: Record<string, Object>): void
```

Sends data to the UIServiceExtensionAbility server.

> **NOTE：**
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-UIServiceProxy-sendData(data: Record<string, Object>): void--><!--Device-UIServiceProxy-sendData(data: Record<string, Object>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt; | Yes | Data to be sent to the UIServiceExtensionAbility server. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |

## sendData

```TypeScript
sendData(data: Record<string, RecordData>): void
```

Sends data to the UIServiceExtensionAbility server.

> **NOTE：**
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceProxy-sendData(data: Record<string, RecordData>): void--><!--Device-UIServiceProxy-sendData(data: Record<string, RecordData>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, RecordData&gt; | Yes | Data to be sent to the UIServiceExtensionAbility server. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. Possible cause: Connect to stub failed. |

