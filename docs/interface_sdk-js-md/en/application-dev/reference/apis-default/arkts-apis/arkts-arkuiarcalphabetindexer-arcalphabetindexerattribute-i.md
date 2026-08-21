# ArcAlphabetIndexerAttribute

Defines the arc alphabet index bar attribute functions.

**Inheritance/Implementation:** ArcAlphabetIndexerAttribute extends CommonMethod

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare interface ArcAlphabetIndexerAttribute--><!--Device-unnamed-export declare interface ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
```

## autoCollapse

```TypeScript
autoCollapse(enable: Optional<boolean>): this
```

Automatically collapses the characters when the indexer bar not enough to display all characters.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcAlphabetIndexerAttribute-autoCollapse(enable: Optional<boolean>): this--><!--Device-ArcAlphabetIndexerAttribute-autoCollapse(enable: Optional<boolean>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | Optional&lt;boolean&gt; | Yes | Indicates whether to use the adaptive folding mode. Default value: true true: The adaptive folding mode is used. false: The adaptive folding mode is not used. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## color

```TypeScript
color(color: Optional<ColorMetrics>): this
```

Definitions text color.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcAlphabetIndexerAttribute-color(color: Optional<ColorMetrics>): this--><!--Device-ArcAlphabetIndexerAttribute-color(color: Optional<ColorMetrics>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | Optional&lt;ColorMetrics&gt; | Yes | Text color. Default value: 0xFFFFFF. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## font

```TypeScript
font(font: Optional<Font>): this
```

Definitions fonts.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcAlphabetIndexerAttribute-font(font: Optional<Font>): this--><!--Device-ArcAlphabetIndexerAttribute-font(font: Optional<Font>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| font | Optional&lt;Font&gt; | Yes | Default font style of the letter index bar. Default value: { size: '13.0fp', style:FontStyle.Normal, weight:500, family:'HarmonyOS Sans' } |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## itemSize

```TypeScript
itemSize(size: Optional<LengthMetrics>): this
```

Sets the size of the letter area of the letter index bar.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcAlphabetIndexerAttribute-itemSize(size: Optional<LengthMetrics>): this--><!--Device-ArcAlphabetIndexerAttribute-itemSize(size: Optional<LengthMetrics>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | Optional&lt;LengthMetrics&gt; | Yes | Letter index bar letter area size, letter area is circular, i.e. circular diameter. The value cannot be set to a percentage. Default value: 24.0 Unit: vp |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onSelect

```TypeScript
onSelect(handler: Optional<OnSelectCallback>): this
```

Index bar selection callback.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcAlphabetIndexerAttribute-onSelect(handler: Optional<OnSelectCallback>): this--><!--Device-ArcAlphabetIndexerAttribute-onSelect(handler: Optional<OnSelectCallback>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | Optional&lt;[OnSelectCallback](../../apis-arkui/arkts-apis/arkts-arkui-onselectcallback-t.md)&gt; | Yes | Callback function type. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## popupBackground

```TypeScript
popupBackground(color: Optional<ColorMetrics>): this
```

Background color of the pop-up window.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcAlphabetIndexerAttribute-popupBackground(color: Optional<ColorMetrics>): this--><!--Device-ArcAlphabetIndexerAttribute-popupBackground(color: Optional<ColorMetrics>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | Optional&lt;ColorMetrics&gt; | Yes | Background color of the pop-up. Default value: 0xD8404040. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## popupBackgroundBlurStyle

```TypeScript
popupBackgroundBlurStyle(style: Optional<BlurStyle>): this
```

Set the background blurStyle of the pop-up window.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcAlphabetIndexerAttribute-popupBackgroundBlurStyle(style: Optional<BlurStyle>): this--><!--Device-ArcAlphabetIndexerAttribute-popupBackgroundBlurStyle(style: Optional<BlurStyle>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | Optional&lt;BlurStyle&gt; | Yes | Set the background blur material of the pop-up prompt. If this parameter is not set, the blur is disabled by default, and the corresponding value is NONE in BlurStyle. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## popupColor

```TypeScript
popupColor(color: Optional<ColorMetrics>): this
```

Font color of the pop-up prompt text.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcAlphabetIndexerAttribute-popupColor(color: Optional<ColorMetrics>): this--><!--Device-ArcAlphabetIndexerAttribute-popupColor(color: Optional<ColorMetrics>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | Optional&lt;ColorMetrics&gt; | Yes | Text color of the pop-up prompt. Default value: 0xFFFFFF. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## popupFont

```TypeScript
popupFont(font: Optional<Font>): this
```

Popup text style.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcAlphabetIndexerAttribute-popupFont(font: Optional<Font>): this--><!--Device-ArcAlphabetIndexerAttribute-popupFont(font: Optional<Font>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| font | Optional&lt;Font&gt; | Yes | Font style of the prompt pop-up. Default value: { size: '19.0fp', style:FontStyle.Normal, weight:500, family:'HarmonyOS Sans' } |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selected

```TypeScript
selected(index: Optional<int> | Bindable<int>): this
```

Sets the selected index.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcAlphabetIndexerAttribute-selected(index: Optional<int> | Bindable<int>): this--><!--Device-ArcAlphabetIndexerAttribute-selected(index: Optional<int> | Bindable<int>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | Optional&lt;int&gt; \| [Bindable](arkts-common-bindable-i.md)&lt;int&gt; | Yes | Index value of the selected item. Default value: 0 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selectedBackgroundColor

```TypeScript
selectedBackgroundColor(color: Optional<ColorMetrics>): this
```

Select the text background color.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcAlphabetIndexerAttribute-selectedBackgroundColor(color: Optional<ColorMetrics>): this--><!--Device-ArcAlphabetIndexerAttribute-selectedBackgroundColor(color: Optional<ColorMetrics>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | Optional&lt;ColorMetrics&gt; | Yes | Background color of the selected item. Default value: 0x1F71FF. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selectedColor

```TypeScript
selectedColor(color: Optional<ColorMetrics>): this
```

Selected text color.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcAlphabetIndexerAttribute-selectedColor(color: Optional<ColorMetrics>): this--><!--Device-ArcAlphabetIndexerAttribute-selectedColor(color: Optional<ColorMetrics>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | Optional&lt;ColorMetrics&gt; | Yes | Text color of the selected item. Default value: 0xFFFFFF. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selectedFont

```TypeScript
selectedFont(font: Optional<Font>): this
```

Selected text style.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcAlphabetIndexerAttribute-selectedFont(font: Optional<Font>): this--><!--Device-ArcAlphabetIndexerAttribute-selectedFont(font: Optional<Font>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| font | Optional&lt;Font&gt; | Yes | Text style of the selected item. Default value: { size: '13.0fp', style:FontStyle.Normal, weight:500, family:'HarmonyOS Sans' } |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setArcAlphabetIndexerOptions

```TypeScript
setArcAlphabetIndexerOptions(info: ArcAlphabetIndexerInitInfo): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-ArcAlphabetIndexerAttribute-setArcAlphabetIndexerOptions(info: ArcAlphabetIndexerInitInfo): this--><!--Device-ArcAlphabetIndexerAttribute-setArcAlphabetIndexerOptions(info: ArcAlphabetIndexerInitInfo): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [ArcAlphabetIndexerInitInfo](../../apis-arkui/arkts-apis/arkts-arkui-arkuiarcalphabetindexer-arcalphabetindexerinitinfo-i.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## usePopup

```TypeScript
usePopup(enabled: Optional<boolean>): this
```

Whether to use pop-up index hints.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcAlphabetIndexerAttribute-usePopup(enabled: Optional<boolean>): this--><!--Device-ArcAlphabetIndexerAttribute-usePopup(enabled: Optional<boolean>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | Optional&lt;boolean&gt; | Yes | Indicates whether to use the pop-up. The value true indicates that the pop-up is used. The value false indicates that the pop-up is not used. Default value: false |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## default

```TypeScript
default
```

Set arcAlphabetIndexer options.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcAlphabetIndexerAttribute-default--><!--Device-ArcAlphabetIndexerAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

