# GridLayoutOptions

The options to help grid layout

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onGetIrregularSizeByIndex

```TypeScript
onGetIrregularSizeByIndex?: (index: int) => [
        int,
        int
    ]
```

Called to return the size of the irregular grid items with the specified index in [rows, columns].

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | int | Yes |

## onGetRectByIndex

```TypeScript
onGetRectByIndex?: (index: int) => [
        int,
        int,
        int,
        int
    ]
```

Called to return the size of the grid items with the specified index in [rowStart, columnStart, rowSpan, columnSpan].

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | int | Yes |

## irregularIndexes

```TypeScript
irregularIndexes?: int[]
```

The indexes of grid items with irregular size.

**Type:** int[]

**Default:** int[] no irregular grid item

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## regularSize

```TypeScript
regularSize: [
        int,
        int
    ]
```

The size of most grid items, in [rows, columns], generally [1, 1]

**Type:** [         int,         int     ]

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
