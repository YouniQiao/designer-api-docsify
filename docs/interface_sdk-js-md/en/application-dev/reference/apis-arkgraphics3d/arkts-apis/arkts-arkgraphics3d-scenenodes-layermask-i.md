# LayerMask

Defines the layer mask of a node.@interface LayerMask

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## getEnabled

```TypeScript
getEnabled(index: number): boolean
```

Checks whether the mask is enabled for a layer of a given index.

**Since:** 12

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

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| enabled | boolean | Yes |
