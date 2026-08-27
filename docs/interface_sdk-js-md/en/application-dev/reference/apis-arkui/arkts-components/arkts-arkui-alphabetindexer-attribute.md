# AlphabetIndexer properties/events

When the width attribute is set to **"auto"**, the width is adaptive. This means that the width will adjust according to the maximum width of the index items.

The default value of the padding attribute is 4 vp.

The maxFontScale and minFontScale attributes are both set to a constant value of 1, which means that they do not change with the system font size.

In addition to the universal attributes, the following attributes are supported.

In addition to the universal events, the following events are supported.

**Inheritance/Implementation:** AlphabetIndexerAttribute extends CommonMethod<AlphabetIndexerAttribute>

**Since:** 7

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## alignStyle

```TypeScript
alignStyle(value: IndexerAlign, offset?: Length)
```

Sets the alignment style of the indexer pop-up window.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [IndexerAlign](arkts-arkui-indexeralign-e.md) | Yes | Alignment style of the indexer pop-up window. The pop-up window can be displayed on the right or left of the indexer.Default value: **IndexerAlign.END |
| offset | [Length](../arkts-apis/arkts-arkui-length-t.md) | No | Spacing between the pop-up window and the alphabetic index bar. A value greater than or equal to **0** is valid. If this parameter is set to a value less than **0** or is not set, the spacing is the same as **popupPosition**. When this parameter and [popupPosition](#popupposition) are set at the same time, **offset** takes effect in the horizontal direction, and **popupPosition.y** takes effect in the vertical direction.<br>**Since:** 10 |

## autoCollapse

```TypeScript
autoCollapse(value: boolean)
```

Sets whether to enable the adaptive collapse behavior for the indexer.

When the first index item is **"#"**: Remaining items ≤ 9: Full display mode; 9 &lt; Remaining items ≤ 13: Adapts between full display and short collapse modes based on the indexer height; remaining items &gt; 13: Adapts between short and number collapse modes based on the indexer height.

When the first index item is not **"#"**: All items ≤ 9: Full display mode; 9 &lt; All items ≤ 13: Adapts between full display and short collapse modes based on the indexer height; all items &gt; 13: Adapts between short and number collapse modes based on the indexer height.

> **NOTE：**

> This API can be called within attributeModifier since API version 12.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | Whether to auto-collapse or expand the indexer bar.Default value:Before API version 12: **false**Since API version 12: **true**   **true**: Enable the adaptive collapse behavior.    **false**: Disable the adaptive collapse behavior. |

## color

```TypeScript
color(value: ResourceColor)
```

Sets the text color for unselected items.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | Text color of unselected items.Default value: **0x99182431**, which is a slightly transparent brown. |

## enableHapticFeedback

```TypeScript
enableHapticFeedback(value: boolean)
```

Sets whether to enable haptic feedback.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | Whether to enable haptic feedback.   **true**: To enable haptic feedback.   **false**: Not to enable haptic feedback.Default value: **true**To enable haptic feedback, you must declare the **ohos.permission.VIBRATE** permission under **requestPermissions** in the [module.json5](../../../quick-start/module-configuration-file.md) file of the project."requestPermissions": [{"name": "ohos.permission.VIBRATE"}] |

## font

```TypeScript
font(value: Font)
```

Sets the text style for unselected items.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Font | Yes | Text style of unselected items.Default value:API version 11 and earlier:{size:'12.0fp',style:FontStyle.Normal,weight:FontWeight.Regular,family:'HarmonyOS Sans'}API version 12 and later:{size:'10.0vp',style:FontStyle.Normal,weight:FontWeight.Medium,family:'HarmonyOS Sans'} |

## itemBorderRadius

```TypeScript
itemBorderRadius(value: number)
```

Sets the radius of the index background border corners in the alphabetic index bar.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number | Yes | Unit: vp.   - Radius of the index background border corners in the alphabetic index bar.   Default value: **8vp**This parameter cannot be set in percentage. If the value specified is less than **0**, **0** is used.The radius of the index background border corners in the alphabetic index bar is automatically adaptive (radius of the index corners + 4 vp). |

## itemSize

```TypeScript
itemSize(value: string | number)
```

Sets the size of the index item area.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| number | Yes | Size of the index item area, which is a square, meaning the side length of the square. This attribute cannot be set in percentage.The actual value is restricted by the component size. The maximum width of an index item is the component width minus the left and right padding, and the maximum height of an index item is (component height minus the top and bottom padding)/number of index items. If the input value is less than or equal to 0, the default value is used.Default value: **16.0**Unit: vp |

## onPopupSelect

```TypeScript
onPopupSelect(callback: OnAlphabetIndexerPopupSelectCallback)
```

Triggered when a secondary index item in the pop-up window is selected. The callback parameter is the index of the selected secondary index item.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnAlphabetIndexerPopupSelectCallback](arkts-arkui-onalphabetindexerpopupselectcallback-t.md) | Yes | Event triggered when a secondary index item in the pop- up window is selected.<br>**Since:** 18 |

## onRequestPopupData

```TypeScript
onRequestPopupData(callback: OnAlphabetIndexerRequestPopupDataCallback)
```

Triggered for a secondary index item content event in the pop-up window. The callback parameter is the index of the selected secondary index item. The return value is the secondary index item content to be displayed in the pop-up window.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnAlphabetIndexerRequestPopupDataCallback](arkts-arkui-onalphabetindexerrequestpopupdatacallback-t.md) | Yes | Callback for setting the secondary index item content event in the pop-up window.<br>**Since:** 18 |

## onSelect

```TypeScript
onSelect(callback: OnAlphabetIndexerSelectCallback)
```

Triggered when an index item is selected, with the callback parameter being the index of the currently selected item.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnAlphabetIndexerSelectCallback](arkts-arkui-onalphabetindexerselectcallback-t.md) | Yes | Event triggered when an index item is selected.<br>**Since:** 18 |

## onSelected

```TypeScript
onSelected(callback: (index: number) => void)
```

Triggered when an index item is selected, with the callback parameter being the index of the currently selected item.

> **NOTE：**

**Since:** 7

**Deprecated since:** 8

**Substitutes:** [onSelect](#onselect)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (index: number) =&gt; void | Yes | Index of the selected item. |

## popupBackground

```TypeScript
popupBackground(value: ResourceColor)
```

Sets the background color for the pop-up window.

If this API is not called or the **value** parameter is set to **undefined**:

In API version 11 and earlier versions, the default background color of the pop-up is **0xFFFFFFFF**, which is white.

In API versions 12 to 24, the default background color is **#66808080**, which is translucent gray.

Since API version 26.0.0, if neither **popupBackground** nor [popupBackgroundBlurStyle](#popupbackgroundblurstyle) is called or the **value** parameter is set to **undefined**, the **THIN** style of **[ImmersiveStyle](../../../reference/apis-arkui/arkts-apis-uimaterial.md#immersivestyle)** is displayed by default on devices with high- and mid-level computing power, and the white background is displayed by default on devices with low-level computing power. If **popupBackgroundBlurStyle** is called and the **value** parameter is set to a valid value, the background color of the pop-up is **#66808080** by default, which is translucent gray.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | Background color of the pop-up window.The background blur effect of the pop-up text can affect the background color. You can disable the effect by setting [popupBackgroundBlurStyle](#popupbackgroundblurstyle) to **NONE**. |

## popupBackgroundBlurStyle

```TypeScript
popupBackgroundBlurStyle(value: BlurStyle)
```

Sets the background blur style of the pop-up window. In versions earlier than API version 26.0.0, if this API is not called, the **COMPONENT_REGULAR** value in **BlurStyle** is used by default. Since API version 26.0.0, if neither [popupBackground](#popupbackground) nor **popupBackgroundBlurStyle** is called or the value is **undefined**, the **THIN** style of [ImmersiveStyle](../../../reference/apis-arkui/arkts-apis-uimaterial.md#immersivestyle) is used by default on devices with high- and mid-level computing power, and the white background is used by default on devices with low- level computing power.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | BlurStyle | Yes | Background blur style of the pop-up window.The background blur effect can affect [popupBackground](#popupbackground). You can disable the effect by setting it to **NONE**. |

## popupColor

```TypeScript
popupColor(value: ResourceColor)
```

Sets the text color for the primary index item in the pop-up window.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | Text color of the primary index item in the pop-up window.Default value: **0xFF007DFF**, which is blue. |

## popupFont

```TypeScript
popupFont(value: Font)
```

Sets the text style for the primary index item in the pop-up window.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Font | Yes | Text style of the primary index item in the pop-up window.Default value:{size:'24.0vp',style:FontStyle.Normal,weight:FontWeight.Medium,family:'HarmonyOS Sans'} |

## popupItemBackgroundColor

```TypeScript
popupItemBackgroundColor(value: ResourceColor)
```

Sets the background color for the secondary index item in the pop-up window.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | Background color of the secondary index item in the pop-up window.Default value:API version 11 and earlier: **#FFFFFFFF**, which is white.API version 12 and later: **#00000000**, which is transparent. |

## popupItemBorderRadius

```TypeScript
popupItemBorderRadius(value: number)
```

Sets the radius of the index border corners in the pop-up window.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number | Yes | Radius of the index background border corners in the pop-up window. Unit: vp. **24vp**.This parameter cannot be set in percentage. If the value specified is less than **0**, **0** is used.The radius of the index background border corners in the pop-up window is automatically adaptive (radius of the index corners + 4 vp). |

## popupItemFont

```TypeScript
popupItemFont(value: Font)
```

Sets the text style for the secondary index item in the pop-up window.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Font | Yes | Text style of the secondary index item in the pop-up window.Default value:{size:24,weight:FontWeight.Medium} |

## popupPosition

```TypeScript
popupPosition(value: Position)
```

Sets the position of the pop-up window relative to the center of the indexer's top border.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Position | Yes | Position of the pop-up window relative to the center of the indexer's top border.Default value: **{x: 60.0, y: 48.0} |

## popupSelectedColor

```TypeScript
popupSelectedColor(value: ResourceColor)
```

Sets the text color for the selected secondary index item in the pop-up window.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | Text color of the selected secondary index items in the pop-up window.Default value: **#FF182431**, which is dark blue. |

## popupTitleBackground

```TypeScript
popupTitleBackground(value: ResourceColor)
```

Sets the background color for the primary index item in the pop-up window.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | Background color for the primary index item in the pop-up window.Default value:If the pop-up window has only one index: **#00FFFFFF**.If the pop-up window has multiple indexes: **#0c182431**. |

## popupUnselectedColor

```TypeScript
popupUnselectedColor(value: ResourceColor)
```

Sets the text color for the unselected secondary index items in the pop-up window.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | Text color of the unselected secondary index items in the pop-up window.Default value: **#FF182431**, which is dark blue. |

## selected

```TypeScript
selected(index: number)
```

Sets the index of the selected item.

Since API version 10, this parameter supports two-way binding through [\$\$](../../../ui/state-management/arkts-two-way-sync.md).

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | Index of the selected item.Value range: [0, [arrayValue](arkts-arkui-alphabetindexeroptions-i.md).length – 1]Default value: **0 |

## selectedBackgroundColor

```TypeScript
selectedBackgroundColor(value: ResourceColor)
```

Sets the background color of the selected item.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | Background color of the selected item.Default value: **0x1A007DFF**, which is semi-transparent blue-green. |

## selectedColor

```TypeScript
selectedColor(value: ResourceColor)
```

Sets the text color for the selected item.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | Text color of the selected item.Default value: **0xFF007DFF**, which is blue. |

## selectedFont

```TypeScript
selectedFont(value: Font)
```

Sets the text style for the selected item.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Font | Yes | Text style of the selected item.Default value:API version 11 and earlier:{size:'12.0fp',style:FontStyle.Normal,weight:FontWeight.Regular,family:'HarmonyOS Sans'}API version 12 and later:{size:'10.0vp',style:FontStyle.Normal,weight:FontWeight.Medium,family:'HarmonyOS Sans'} |

## usingPopup

```TypeScript
usingPopup(value: boolean)
```

Sets whether to display the pop-up window.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | Whether to display the pop-up window.Default value: **false**.   **true**: Display the pop-up window.   **false**: Do not display the pop-up window. |
