# LayerMask

Defines the layer mask of the node.

**Since:** 12

<!--Device-unnamed-export interface LayerMask--><!--Device-unnamed-export interface LayerMask-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## getEnabled

```TypeScript
getEnabled(index: number): boolean
```

Checks whether the mask is enabled for a layer of a given index.

**Since:** 12

<!--Device-LayerMask-getEnabled(index: int): boolean--><!--Device-LayerMask-getEnabled(index: int): boolean-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## setEnabled

```TypeScript
setEnabled(index: number, enabled: boolean): void
```

Enables the mask of a layer of a given index.

**Since:** 12

<!--Device-LayerMask-setEnabled(index: int, enabled: boolean): void--><!--Device-LayerMask-setEnabled(index: int, enabled: boolean): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| enabled | boolean | Yes |
