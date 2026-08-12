# AlphabetIndexer properties/events

When the [width](CommonMethod#width(value: Length)) attribute is set to **"auto"**, the width is adaptive. This means that the width will adjust according to the maximum width of the index items.

The default value of the [padding](CommonMethod#padding) attribute is 4 vp.

The [maxFontScale](TextAttribute#maxFontScale) and [minFontScale](TextAttribute#minFontScale) attributes are both set to a constant value of 1, which means that they do not change with the system font size.

In addition to the [universal attributes](common), the following attributes are supported.

In addition to the [universal events](common), the following events are supported.

**Inheritance/Implementation:** AlphabetIndexerAttribute extends [CommonMethod<AlphabetIndexerAttribute>](CommonMethod<AlphabetIndexerAttribute>)

**Since:** 7

<!--Device-unnamed-declare class AlphabetIndexerAttribute extends CommonMethod<AlphabetIndexerAttribute>--><!--Device-unnamed-declare class AlphabetIndexerAttribute extends CommonMethod<AlphabetIndexerAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alignStyle

```TypeScript
alignStyle(value: IndexerAlign, offset?: Length)
```

Sets the alignment style of the indexer pop-up window.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlphabetIndexerAttribute-alignStyle(value: IndexerAlign, offset?: Length): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-alignStyle(value: IndexerAlign, offset?: Length): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [IndexerAlign](arkts-arkui-indexeralign-e.md) | Yes |
| offset | [Length](../arkts-apis/arkts-arkui-length-t.md) | No |

## autoCollapse

```TypeScript
autoCollapse(value: boolean)
```

Sets whether to enable the adaptive collapse behavior for the indexer.

When the first index item is **"#"**: Remaining items ≤ 9: Full display mode; 9 &lt; Remaining items ≤ 13: Adapts between full display and short collapse modes based on the indexer height; remaining items &gt; 13: Adapts between short and long collapse modes based on the indexer height.

When the first index item is not **"#"**: All items ≤ 9: Full display mode; 9 &lt; All items ≤ 13: Adapts between full display and short collapse modes based on the indexer height; all items &gt; 13: Adapts between short and long collapse modes based on the indexer height.

> **NOTE：**

> This API can be called within [attributeModifier](CommonMethod#attributeModifier) since API version 12.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlphabetIndexerAttribute-autoCollapse(value: boolean): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-autoCollapse(value: boolean): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## color

```TypeScript
color(value: ResourceColor)
```

Sets the text color for unselected items.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlphabetIndexerAttribute-color(value: ResourceColor): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-color(value: ResourceColor): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## enableHapticFeedback

```TypeScript
enableHapticFeedback(value: boolean)
```

Sets whether to enable haptic feedback.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlphabetIndexerAttribute-enableHapticFeedback(value: boolean): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-enableHapticFeedback(value: boolean): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## font

```TypeScript
font(value: Font)
```

Sets the text style for unselected items.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlphabetIndexerAttribute-font(value: Font): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-font(value: Font): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Font](#font) | Yes |

## itemBorderRadius

```TypeScript
itemBorderRadius(value: number)
```

Sets the radius of the index background border corners in the alphabetic index bar.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlphabetIndexerAttribute-itemBorderRadius(value: number): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-itemBorderRadius(value: number): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

## itemSize

```TypeScript
itemSize(value: string | number)
```

Sets the size of the index item area.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlphabetIndexerAttribute-itemSize(value: string | number): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-itemSize(value: string | number): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| number | Yes |

## onPopupSelect

```TypeScript
onPopupSelect(callback: OnAlphabetIndexerPopupSelectCallback)
```

Triggered when a secondary index item in the pop-up window is selected. The callback parameter is the index of the selected secondary index item.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlphabetIndexerAttribute-onPopupSelect(callback: OnAlphabetIndexerPopupSelectCallback): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-onPopupSelect(callback: OnAlphabetIndexerPopupSelectCallback): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnAlphabetIndexerPopupSelectCallback](arkts-arkui-onalphabetindexerpopupselectcallback-t.md) | Yes |

## onRequestPopupData

```TypeScript
onRequestPopupData(callback: OnAlphabetIndexerRequestPopupDataCallback)
```

Triggered for a secondary index item content event in the pop-up window. The callback parameter is the index of the selected secondary index item. The return value is the secondary index item content to be displayed in the pop-up window.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlphabetIndexerAttribute-onRequestPopupData(callback: OnAlphabetIndexerRequestPopupDataCallback): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-onRequestPopupData(callback: OnAlphabetIndexerRequestPopupDataCallback): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnAlphabetIndexerRequestPopupDataCallback](arkts-arkui-onalphabetindexerrequestpopupdatacallback-t.md) | Yes |

## onSelect

```TypeScript
onSelect(callback: OnAlphabetIndexerSelectCallback)
```

Triggered when an index item is selected, with the callback parameter being the index of the currently selected item.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlphabetIndexerAttribute-onSelect(callback: OnAlphabetIndexerSelectCallback): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-onSelect(callback: OnAlphabetIndexerSelectCallback): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnAlphabetIndexerSelectCallback](arkts-arkui-onalphabetindexerselectcallback-t.md) | Yes |

## onSelected

```TypeScript
onSelected(callback: (index: number) => void)
```

Triggered when an index item is selected, with the callback parameter being the index of the currently selected item.

> **NOTE：**

**Since:** 7

**Deprecated since:** 8

**Substitutes:** [onSelect](onSelect)

<!--Device-AlphabetIndexerAttribute-onSelected(callback: (index: number) => void): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-onSelected(callback: (index: number) => void): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (index: number) = & gt; void | Yes |

## popupBackground

```TypeScript
popupBackground(value: ResourceColor)
```

Sets the background color for the pop-up window.

If this API is not called or the **value** parameter is set to **undefined**:

In API version 11 and earlier versions, the default background color of the pop-up is **0xFFFFFFFF**, which is white.

In API versions 12 to 24, the default background color is **#66808080**, which is translucent gray.

Since API version 26.0.0, if neither **popupBackground** nor  
[popupBackgroundBlurStyle](AlphabetIndexerAttribute#popupBackgroundBlurStyle) is called or the **value**parameter is set to **undefined**, the **THIN** style of  
**[ImmersiveStyle](../../../reference/apis-arkui/arkts-apis-uimaterial.md#immersivestyle)** is displayed by default on devices with high- and mid-level computing power, and the white background is displayed by default on devices with low-level computing power. If **popupBackgroundBlurStyle** is called and the **value** parameter is set to a valid value, the background color of the pop-up is **#66808080** by default, which is translucent gray.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlphabetIndexerAttribute-popupBackground(value: ResourceColor): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-popupBackground(value: ResourceColor): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## popupBackgroundBlurStyle

```TypeScript
popupBackgroundBlurStyle(value: BlurStyle)
```

Sets the background blur style of the pop-up window. In versions earlier than API version 26.0.0, if this API is not called, the **COMPONENT_REGULAR** value in **BlurStyle** is used by default. Since API version 26.0.0, if neither [popupBackground](AlphabetIndexerAttribute#popupBackground) nor **popupBackgroundBlurStyle** is called or the value is **undefined**, the **THIN** style of  
[ImmersiveStyle](../../../reference/apis-arkui/arkts-apis-uimaterial.md#immersivestyle) is used by default on devices with high- and mid-level computing power, and the white background is used by default on devices with low-level computing power.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlphabetIndexerAttribute-popupBackgroundBlurStyle(value: BlurStyle): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-popupBackgroundBlurStyle(value: BlurStyle): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BlurStyle](arkts-arkui-blurstyle-e.md) | Yes |

## popupColor

```TypeScript
popupColor(value: ResourceColor)
```

Sets the text color for the primary index item in the pop-up window.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlphabetIndexerAttribute-popupColor(value: ResourceColor): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-popupColor(value: ResourceColor): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## popupFont

```TypeScript
popupFont(value: Font)
```

Sets the text style for the primary index item in the pop-up window.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlphabetIndexerAttribute-popupFont(value: Font): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-popupFont(value: Font): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Font](#font) | Yes |

## popupItemBackgroundColor

```TypeScript
popupItemBackgroundColor(value: ResourceColor)
```

Sets the background color for the secondary index item in the pop-up window.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlphabetIndexerAttribute-popupItemBackgroundColor(value: ResourceColor): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-popupItemBackgroundColor(value: ResourceColor): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## popupItemBorderRadius

```TypeScript
popupItemBorderRadius(value: number)
```

Sets the radius of the index border corners in the pop-up window.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlphabetIndexerAttribute-popupItemBorderRadius(value: number): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-popupItemBorderRadius(value: number): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

## popupItemFont

```TypeScript
popupItemFont(value: Font)
```

Sets the text style for the secondary index item in the pop-up window.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlphabetIndexerAttribute-popupItemFont(value: Font): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-popupItemFont(value: Font): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Font](#font) | Yes |

## popupPosition

```TypeScript
popupPosition(value: Position)
```

Sets the position of the pop-up window relative to the center of the indexer's top border.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlphabetIndexerAttribute-popupPosition(value: Position): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-popupPosition(value: Position): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Position](../arkts-apis/arkts-arkui-display-position-i.md) | Yes |

## popupSelectedColor

```TypeScript
popupSelectedColor(value: ResourceColor)
```

Sets the text color for the selected secondary index item in the pop-up window.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlphabetIndexerAttribute-popupSelectedColor(value: ResourceColor): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-popupSelectedColor(value: ResourceColor): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## popupTitleBackground

```TypeScript
popupTitleBackground(value: ResourceColor)
```

Sets the background color for the primary index item in the pop-up window.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlphabetIndexerAttribute-popupTitleBackground(value: ResourceColor): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-popupTitleBackground(value: ResourceColor): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## popupUnselectedColor

```TypeScript
popupUnselectedColor(value: ResourceColor)
```

Sets the text color for the unselected secondary index items in the pop-up window.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlphabetIndexerAttribute-popupUnselectedColor(value: ResourceColor): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-popupUnselectedColor(value: ResourceColor): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## selected

```TypeScript
selected(index: number)
```

Sets the index of the selected item.

Since API version 10, this parameter supports two-way binding through  
[\$\$](../../../ui/state-management/arkts-two-way-sync.md).

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlphabetIndexerAttribute-selected(index: number): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-selected(index: number): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

## selectedBackgroundColor

```TypeScript
selectedBackgroundColor(value: ResourceColor)
```

Sets the background color of the selected item.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlphabetIndexerAttribute-selectedBackgroundColor(value: ResourceColor): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-selectedBackgroundColor(value: ResourceColor): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## selectedColor

```TypeScript
selectedColor(value: ResourceColor)
```

Sets the text color for the selected item.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlphabetIndexerAttribute-selectedColor(value: ResourceColor): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-selectedColor(value: ResourceColor): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## selectedFont

```TypeScript
selectedFont(value: Font)
```

Sets the text style for the selected item.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlphabetIndexerAttribute-selectedFont(value: Font): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-selectedFont(value: Font): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Font](#font) | Yes |

## usingPopup

```TypeScript
usingPopup(value: boolean)
```

Sets whether to display the pop-up window.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlphabetIndexerAttribute-usingPopup(value: boolean): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerAttribute-usingPopup(value: boolean): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |
