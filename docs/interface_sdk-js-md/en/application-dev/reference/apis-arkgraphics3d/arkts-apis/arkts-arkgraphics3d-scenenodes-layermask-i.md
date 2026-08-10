# LayerMask

定义节点的图层掩码.

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

获取图层掩码是否启用.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-LayerMask-getEnabled(index: int): boolean--><!--Device-LayerMask-getEnabled(index: int): boolean-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 图层掩码 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 图层掩码是否启用 |

## setEnabled

ArkTS-Dyn:
```TypeScript
setEnabled(index: number, enabled: boolean): void
```

ArkTS-Sta:
```TypeScript
setEnabled(index: int, enabled: boolean): void
```

设置图层掩码是否启用.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-LayerMask-setEnabled(index: int, enabled: boolean): void--><!--Device-LayerMask-setEnabled(index: int, enabled: boolean): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 图层掩码 |
| enabled | boolean | Yes | 图层掩码是否启用 |

