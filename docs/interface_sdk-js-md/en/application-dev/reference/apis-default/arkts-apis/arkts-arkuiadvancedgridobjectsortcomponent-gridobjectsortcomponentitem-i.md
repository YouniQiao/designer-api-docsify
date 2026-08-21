# GridObjectSortComponentItem

Provides data item configuration for the **GridObjectSortComponent** component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export interface GridObjectSortComponentItem--><!--Device-unnamed-export interface GridObjectSortComponentItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## id

```TypeScript
id: int | string
```

Data ID, which must be unique.

The default value is an empty string.

**Type:** int \| string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridObjectSortComponentItem-id: int | string--><!--Device-GridObjectSortComponentItem-id: int | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## order

```TypeScript
order: int
```

Sequence number. The value must be greater than or equal to 0. Default value: **0**.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridObjectSortComponentItem-order: int--><!--Device-GridObjectSortComponentItem-order: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selected

```TypeScript
selected: boolean
```

Whether the grid object has been added. The value **true** means that the grid object has been added, and **false** means the opposite.

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridObjectSortComponentItem-selected: boolean--><!--Device-GridObjectSortComponentItem-selected: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolStyle

```TypeScript
symbolStyle?: SymbolGlyphModifier
```

Symbol resource of the image. Required when **GridObjectSortComponentType** is set to **IMAGE_TEXT**. The priority of this property is higher than that of **url**.

**Type:** [SymbolGlyphModifier](../../apis-arkui/arkts-apis/arkts-arkui-symbolglyphmodifier-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridObjectSortComponentItem-symbolStyle?: SymbolGlyphModifier--><!--Device-GridObjectSortComponentItem-symbolStyle?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
text: ResourceStr
```

Text information.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridObjectSortComponentItem-text: ResourceStr--><!--Device-GridObjectSortComponentItem-text: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## url

```TypeScript
url?: ResourceStr
```

URL of the image. Required when **GridObjectSortComponentType** is set to **IMAGE_TEXT**.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridObjectSortComponentItem-url?: ResourceStr--><!--Device-GridObjectSortComponentItem-url?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

