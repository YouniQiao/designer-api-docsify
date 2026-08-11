# LayerMask

Defines the layer mask of the node.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface LayerMask--><!--Device-unnamed-export interface LayerMask-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## getEnabled

ArkTS-Dyn:
```TypeScript
getEnabled(index: number): boolean
```

ArkTS-Sta:
```TypeScript
getEnabled(index: int): boolean
```

Checks whether the mask is enabled for a layer of a given index.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-LayerMask-getEnabled(index: int): boolean--><!--Device-LayerMask-getEnabled(index: int): boolean-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Index of the layer. The value is an integer greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for whether the layer mask is enabled. true if enabled, false otherwise. |

## setEnabled

ArkTS-Dyn:
```TypeScript
setEnabled(index: number, enabled: boolean): void
```

ArkTS-Sta:
```TypeScript
setEnabled(index: int, enabled: boolean): void
```

Enables the mask of a layer of a given index.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-LayerMask-setEnabled(index: int, enabled: boolean): void--><!--Device-LayerMask-setEnabled(index: int, enabled: boolean): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Index of the layer. The value is an integer greater than or equal to 0. |
| enabled | boolean | Yes | Whether to enable the layer mask. true to enable, false otherwise. |

