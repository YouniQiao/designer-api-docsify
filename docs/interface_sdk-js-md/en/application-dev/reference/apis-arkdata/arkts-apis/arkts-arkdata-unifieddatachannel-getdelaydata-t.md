# GetDelayData

```TypeScript
type GetDelayData = (type: string) => UnifiedData
```

Defines a function used to obtain a deferred **UnifiedData** object. Currently, it can be used only in the pasteboard application of the same device.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unifiedDataChannel-type GetDelayData = (type: string) => UnifiedData--><!--Device-unifiedDataChannel-type GetDelayData = (type: string) => UnifiedData-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | Identifier of the deferred encapsulation. |

**Return value:**

| Type | Description |
| --- | --- |
| UnifiedData | UnifiedData** object. |

