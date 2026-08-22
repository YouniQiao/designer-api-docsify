# ArcAlphabetIndexerAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** ArcAlphabetIndexerAttribute extends CommonMethod

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-export declare interface ArcAlphabetIndexerAttribute--><!--Device-unnamed-export declare interface ArcAlphabetIndexerAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## 导入模块

```TypeScript
```

## autoCollapse

```TypeScript
autoCollapse(enable: Optional<boolean>): this
```

设置是否使用自适应折叠模式。未通过该接口设置时，默认使用自适应折叠模式。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArcAlphabetIndexerAttribute-autoCollapse(enable: Optional<boolean>): this--><!--Device-ArcAlphabetIndexerAttribute-autoCollapse(enable: Optional<boolean>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | Optional&lt;boolean&gt; | 是 | 是否使用自适应折叠模式。<br/>true表示使用自适应折叠模式；false表示不使用自适应折叠模式。<br/>取值为undefined时，使用自适应折叠 模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## color

```TypeScript
color(color: Optional<ColorMetrics>): this
```

设置普通状态下索引项文字颜色。未通过该接口设置时，默认0xFFFFFF，显示为白色。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArcAlphabetIndexerAttribute-color(color: Optional<ColorMetrics>): this--><!--Device-ArcAlphabetIndexerAttribute-color(color: Optional<ColorMetrics>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Optional&lt;ColorMetrics&gt; | 是 | 文字颜色。<br/>取值为undefined时，普通状态下索引项文字颜色为0xFFFFFF，显示为白色。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## font

```TypeScript
font(font: Optional<Font>): this
```

设置字母索引条默认字体样式。未通过该接口设置时，默认样式为{size: '13.0fp', style: FontStyle.Normal, weight:500, family: 'HarmonyOS Sans'}。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArcAlphabetIndexerAttribute-font(font: Optional<Font>): this--><!--Device-ArcAlphabetIndexerAttribute-font(font: Optional<Font>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| font | Optional&lt;Font&gt; | 是 | 字母索引条默认字体样式。<br/>取值为undefined时，字母索引条默认字体样式为：<br/>{<br/>size:'13.0fp',<br/> style: FontStyle.Normal,<br/> weight:500,<br/> family:'HarmonyOS Sans'<br/>} |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## itemSize

```TypeScript
itemSize(size: Optional<LengthMetrics>): this
```

设置字母索引条字母区域大小。未通过该接口设置时，默认字母索引条区域大小为24.0vp。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArcAlphabetIndexerAttribute-itemSize(size: Optional<LengthMetrics>): this--><!--Device-ArcAlphabetIndexerAttribute-itemSize(size: Optional<LengthMetrics>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | Optional&lt;LengthMetrics&gt; | 是 | 字母索引条字母区域大小，字母区域为圆形，即圆形直径。不支持设置为百分比。<br/>取值为undefined时，字母索引条字母区域大小为24.0。 <br/>单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## onSelect

```TypeScript
onSelect(handler: Optional<OnSelectCallback>): this
```

索引条选中回调，返回值为当前选中索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArcAlphabetIndexerAttribute-onSelect(handler: Optional<OnSelectCallback>): this--><!--Device-ArcAlphabetIndexerAttribute-onSelect(handler: Optional<OnSelectCallback>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | Optional&lt;[OnSelectCallback](../../apis-arkui/arkts-apis/arkts-arkui-onselectcallback-t.md)&gt; | 是 | 回调函数类型。<br>取值为undefined时，无回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## popupBackground

```TypeScript
popupBackground(color: Optional<ColorMetrics>): this
```

设置提示弹窗背景色。未通过该接口设置时，默认0xD8404040，显示为灰色。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArcAlphabetIndexerAttribute-popupBackground(color: Optional<ColorMetrics>): this--><!--Device-ArcAlphabetIndexerAttribute-popupBackground(color: Optional<ColorMetrics>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Optional&lt;ColorMetrics&gt; | 是 | 提示弹窗背景色。<br/>取值为undefined时，提示弹窗背景色为0xD8404040，显示为灰色。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## popupBackgroundBlurStyle

```TypeScript
popupBackgroundBlurStyle(style: Optional<BlurStyle>): this
```

设置提示弹窗的背景模糊材质。未通过该接口设置时，默认取值为BlurStyle.NONE，表示无模糊。

> **说明：**
> 
> 当通过popupBackgroundBlurStyle设置弹窗气泡的背景模糊材质时，不建议再通过
> [popupBackground](../../apis-arkui/arkts-apis/arkts-arkui-arkuiarcalphabetindexer-arcalphabetindexerattribute-c.md#popupbackground)设置背景色。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArcAlphabetIndexerAttribute-popupBackgroundBlurStyle(style: Optional<BlurStyle>): this--><!--Device-ArcAlphabetIndexerAttribute-popupBackgroundBlurStyle(style: Optional<BlurStyle>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | Optional&lt;BlurStyle&gt; | 是 | 设置提示弹窗的背景模糊材质。<br/>取值为undefined时，提示弹窗的背景模糊材质为BlurStyle.NONE，无模糊效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## popupColor

```TypeScript
popupColor(color: Optional<ColorMetrics>): this
```

设置提示弹窗文字颜色。未通过该接口设置时，默认0xFFFFFF，显示为白色。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArcAlphabetIndexerAttribute-popupColor(color: Optional<ColorMetrics>): this--><!--Device-ArcAlphabetIndexerAttribute-popupColor(color: Optional<ColorMetrics>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Optional&lt;ColorMetrics&gt; | 是 | 提示弹窗文字颜色。<br/>取值为undefined时，提示弹窗文字颜色为0xFFFFFF，显示为白色。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## popupFont

```TypeScript
popupFont(font: Optional<Font>): this
```

设置提示弹窗字体样式。未通过该接口设置时，默认样式为{size: '13.0fp', style: FontStyle.Normal, weight:500, family: 'HarmonyOS Sans'}。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArcAlphabetIndexerAttribute-popupFont(font: Optional<Font>): this--><!--Device-ArcAlphabetIndexerAttribute-popupFont(font: Optional<Font>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| font | Optional&lt;Font&gt; | 是 | 提示弹窗字体样式。<br/>取值为undefined时，弹窗字体样式为：<br/>{<br/>size:'13.0fp',<br/> style: FontStyle.Normal,<br/> weight:500,<br/> family:'HarmonyOS Sans'<br/>} |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## selected

```TypeScript
selected(index: Optional<int> | Bindable<int>): this
```

设置选中项索引值。未通过该接口设置时，选中项索引值默认为0。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArcAlphabetIndexerAttribute-selected(index: Optional<int> | Bindable<int>): this--><!--Device-ArcAlphabetIndexerAttribute-selected(index: Optional<int> | Bindable<int>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | Optional&lt;int&gt; \| [Bindable](arkts-common-bindable-i.md)&lt;int&gt; | 是 | 选中项索引值。<br/>取值为undefined时，选中项索引值为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## selectedBackgroundColor

```TypeScript
selectedBackgroundColor(color: Optional<ColorMetrics>): this
```

设置选中项背景颜色。未通过该接口设置时，默认0x1F71FF，显示为蓝色。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArcAlphabetIndexerAttribute-selectedBackgroundColor(color: Optional<ColorMetrics>): this--><!--Device-ArcAlphabetIndexerAttribute-selectedBackgroundColor(color: Optional<ColorMetrics>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Optional&lt;ColorMetrics&gt; | 是 | 选中项背景颜色。<br/>取值为undefined时，选中项背景颜色为0x1F71FF，显示为蓝色。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## selectedColor

```TypeScript
selectedColor(color: Optional<ColorMetrics>): this
```

设置选中项文字颜色。未通过该接口设置时，默认0xFFFFFF，显示为白色。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArcAlphabetIndexerAttribute-selectedColor(color: Optional<ColorMetrics>): this--><!--Device-ArcAlphabetIndexerAttribute-selectedColor(color: Optional<ColorMetrics>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Optional&lt;ColorMetrics&gt; | 是 | 选中项文字颜色。<br/>取值为undefined时，选中项文字颜色为0xFFFFFF，显示为白色。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## selectedFont

```TypeScript
selectedFont(font: Optional<Font>): this
```

设置选中项文字尺寸、粗细、字体族、倾斜等样式。未通过该接口设置时，默认样式为{size: '13.0fp', style: FontStyle.Normal, weight:500, family: 'HarmonyOS Sans ' }。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArcAlphabetIndexerAttribute-selectedFont(font: Optional<Font>): this--><!--Device-ArcAlphabetIndexerAttribute-selectedFont(font: Optional<Font>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| font | Optional&lt;Font&gt; | 是 | 选中项文字样式。<br/>取值为undefined时，选中项文字尺寸、粗细、字体族、倾斜等样式为：<br/>{<br/>size:'13.0fp',<br/> style:FontStyle.Normal,<br/> weight:500,<br/> family:'HarmonyOS Sans'<br/>} |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## setArcAlphabetIndexerOptions

```TypeScript
setArcAlphabetIndexerOptions(info: ArcAlphabetIndexerInitInfo): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ArcAlphabetIndexerAttribute-setArcAlphabetIndexerOptions(info: ArcAlphabetIndexerInitInfo): this--><!--Device-ArcAlphabetIndexerAttribute-setArcAlphabetIndexerOptions(info: ArcAlphabetIndexerInitInfo): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [ArcAlphabetIndexerInitInfo](../../apis-arkui/arkts-apis/arkts-arkui-arkuiarcalphabetindexer-arcalphabetindexerinitinfo-i.md) | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## usePopup

```TypeScript
usePopup(enabled: Optional<boolean>): this
```

设置是否使用提示弹窗。未通过该接口设置时，默认为false，不使用提示弹窗。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArcAlphabetIndexerAttribute-usePopup(enabled: Optional<boolean>): this--><!--Device-ArcAlphabetIndexerAttribute-usePopup(enabled: Optional<boolean>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | Optional&lt;boolean&gt; | 是 | 是否使用提示弹窗。<br/>true表示使用提示弹窗；false表示不使用提示弹窗。<br/>取值为undefined时，不使用提示弹窗。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## default

```TypeScript
default
```

设置arcAlphabetIndexer选项。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArcAlphabetIndexerAttribute-default--><!--Device-ArcAlphabetIndexerAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

