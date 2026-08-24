# AlphabetIndexerAttribute

width属性设置"auto"时表示自适应宽度，宽度会随索引项最大宽度变 化。  
padding属性默认为4vp。文本最大的字体缩放倍数maxFontScale和最小的字体缩放 倍数minFontScale皆为1，不跟随系统字体大小调节变化 。除支持通用属性外，还支持以下属性：

**继承/实现关系：** AlphabetIndexerAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface AlphabetIndexerAttribute--><!--Device-unnamed-export declare interface AlphabetIndexerAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## alignStyle

```TypeScript
alignStyle(value: IndexerAlign | undefined, offset?: Length | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-alignStyle(value: IndexerAlign | undefined, offset?: Length | undefined): this--><!--Device-AlphabetIndexerAttribute-alignStyle(value: IndexerAlign | undefined, offset?: Length | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [IndexerAlign](arkts-alphabetindexer-indexeralign-e.md) \| undefined | 是 |  |
| offset | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<AlphabetIndexerAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-attributeModifier(modifier: AttributeModifier<AlphabetIndexerAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-AlphabetIndexerAttribute-attributeModifier(modifier: AttributeModifier<AlphabetIndexerAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[AlphabetIndexerAttribute](arkts-alphabetindexer-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## autoCollapse

```TypeScript
autoCollapse(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-autoCollapse(value: boolean | undefined): this--><!--Device-AlphabetIndexerAttribute-autoCollapse(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## color

```TypeScript
color(value: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-color(value: ResourceColor | undefined): this--><!--Device-AlphabetIndexerAttribute-color(value: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableHapticFeedback

```TypeScript
enableHapticFeedback(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-enableHapticFeedback(value: boolean | undefined): this--><!--Device-AlphabetIndexerAttribute-enableHapticFeedback(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## font

```TypeScript
font(value: Font | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-font(value: Font | undefined): this--><!--Device-AlphabetIndexerAttribute-font(value: Font | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](../../apis-arkui/arkts-apis/arkts-arkui-font-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## itemBorderRadius

```TypeScript
itemBorderRadius(value: double | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-itemBorderRadius(value: double | undefined): this--><!--Device-AlphabetIndexerAttribute-itemBorderRadius(value: double | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## itemSize

```TypeScript
itemSize(value: string | double | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-itemSize(value: string | double | undefined): this--><!--Device-AlphabetIndexerAttribute-itemSize(value: string | double | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string \| double \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onPopupSelect

```TypeScript
onPopupSelect(callback: OnAlphabetIndexerPopupSelectCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-onPopupSelect(callback: OnAlphabetIndexerPopupSelectCallback | undefined): this--><!--Device-AlphabetIndexerAttribute-onPopupSelect(callback: OnAlphabetIndexerPopupSelectCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnAlphabetIndexerPopupSelectCallback](arkts-onalphabetindexerpopupselectcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onRequestPopupData

```TypeScript
onRequestPopupData(callback: OnAlphabetIndexerRequestPopupDataCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-onRequestPopupData(callback: OnAlphabetIndexerRequestPopupDataCallback | undefined): this--><!--Device-AlphabetIndexerAttribute-onRequestPopupData(callback: OnAlphabetIndexerRequestPopupDataCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnAlphabetIndexerRequestPopupDataCallback](arkts-onalphabetindexerrequestpopupdatacallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onSelect

```TypeScript
onSelect(callback: OnAlphabetIndexerSelectCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-onSelect(callback: OnAlphabetIndexerSelectCallback | undefined): this--><!--Device-AlphabetIndexerAttribute-onSelect(callback: OnAlphabetIndexerSelectCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnAlphabetIndexerSelectCallback](arkts-onalphabetindexerselectcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## popupBackground

```TypeScript
popupBackground(value: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-popupBackground(value: ResourceColor | undefined): this--><!--Device-AlphabetIndexerAttribute-popupBackground(value: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## popupBackgroundBlurStyle

```TypeScript
popupBackgroundBlurStyle(value: BlurStyle | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-popupBackgroundBlurStyle(value: BlurStyle | undefined): this--><!--Device-AlphabetIndexerAttribute-popupBackgroundBlurStyle(value: BlurStyle | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BlurStyle](../../apis-arkui/arkts-components/arkts-arkui-blurstyle-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## popupColor

```TypeScript
popupColor(value: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-popupColor(value: ResourceColor | undefined): this--><!--Device-AlphabetIndexerAttribute-popupColor(value: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## popupFont

```TypeScript
popupFont(value: Font | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-popupFont(value: Font | undefined): this--><!--Device-AlphabetIndexerAttribute-popupFont(value: Font | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](../../apis-arkui/arkts-apis/arkts-arkui-font-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## popupItemBackgroundColor

```TypeScript
popupItemBackgroundColor(value: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-popupItemBackgroundColor(value: ResourceColor | undefined): this--><!--Device-AlphabetIndexerAttribute-popupItemBackgroundColor(value: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## popupItemBorderRadius

```TypeScript
popupItemBorderRadius(value: double | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-popupItemBorderRadius(value: double | undefined): this--><!--Device-AlphabetIndexerAttribute-popupItemBorderRadius(value: double | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## popupItemFont

```TypeScript
popupItemFont(value: Font | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-popupItemFont(value: Font | undefined): this--><!--Device-AlphabetIndexerAttribute-popupItemFont(value: Font | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](../../apis-arkui/arkts-apis/arkts-arkui-font-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## popupPosition

```TypeScript
popupPosition(value: Position | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-popupPosition(value: Position | undefined): this--><!--Device-AlphabetIndexerAttribute-popupPosition(value: Position | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Position](../../apis-arkui/arkts-apis/arkts-arkui-position-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## popupSelectedColor

```TypeScript
popupSelectedColor(value: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-popupSelectedColor(value: ResourceColor | undefined): this--><!--Device-AlphabetIndexerAttribute-popupSelectedColor(value: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## popupTitleBackground

```TypeScript
popupTitleBackground(value: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-popupTitleBackground(value: ResourceColor | undefined): this--><!--Device-AlphabetIndexerAttribute-popupTitleBackground(value: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## popupUnselectedColor

```TypeScript
popupUnselectedColor(value: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-popupUnselectedColor(value: ResourceColor | undefined): this--><!--Device-AlphabetIndexerAttribute-popupUnselectedColor(value: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## selected

```TypeScript
selected(index: int | Bindable<int> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-selected(index: int | Bindable<int> | undefined): this--><!--Device-AlphabetIndexerAttribute-selected(index: int | Bindable<int> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int \| [Bindable](../arkts-apis/arkts-common-bindable-i.md)&lt;int&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## selectedBackgroundColor

```TypeScript
selectedBackgroundColor(value: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-selectedBackgroundColor(value: ResourceColor | undefined): this--><!--Device-AlphabetIndexerAttribute-selectedBackgroundColor(value: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## selectedColor

```TypeScript
selectedColor(value: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-selectedColor(value: ResourceColor | undefined): this--><!--Device-AlphabetIndexerAttribute-selectedColor(value: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## selectedFont

```TypeScript
selectedFont(value: Font | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-selectedFont(value: Font | undefined): this--><!--Device-AlphabetIndexerAttribute-selectedFont(value: Font | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](../../apis-arkui/arkts-apis/arkts-arkui-font-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setAlphabetIndexerOptions

```TypeScript
setAlphabetIndexerOptions(info: AlphabetIndexerOptions): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-setAlphabetIndexerOptions(info: AlphabetIndexerOptions): this--><!--Device-AlphabetIndexerAttribute-setAlphabetIndexerOptions(info: AlphabetIndexerOptions): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [AlphabetIndexerOptions](arkts-alphabetindexer-alphabetindexeroptions-i.md) | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## usingPopup

```TypeScript
usingPopup(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-AlphabetIndexerAttribute-usingPopup(value: boolean | undefined): this--><!--Device-AlphabetIndexerAttribute-usingPopup(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

设置字母索引器选项。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AlphabetIndexerAttribute-default--><!--Device-AlphabetIndexerAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

