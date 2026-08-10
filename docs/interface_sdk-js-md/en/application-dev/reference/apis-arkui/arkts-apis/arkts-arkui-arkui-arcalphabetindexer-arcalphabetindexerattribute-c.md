# ArcAlphabetIndexerAttribute

除支持[通用属性](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)外，还支持以下属性：

除支持[通用事件](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)外，还支持以下事件：

**Inheritance/Implementation:** ArcAlphabetIndexerAttribute extends [CommonMethod<ArcAlphabetIndexerAttribute>](CommonMethod<ArcAlphabetIndexerAttribute>)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-declare class ArcAlphabetIndexerAttribute extends CommonMethod<ArcAlphabetIndexerAttribute>--><!--Device-unnamed-declare class ArcAlphabetIndexerAttribute extends CommonMethod<ArcAlphabetIndexerAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcAlphabetIndexerAttribute, ArcAlphabetIndexer } from 'kits/@kit.ArkUI';
```

## autoCollapse

```TypeScript
autoCollapse(enable: Optional<boolean>): ArcAlphabetIndexerAttribute
```

设置是否使用自适应折叠模式。当索引项过多时，组件会根据可用显示空间自动调整索引项的显示布局。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-autoCollapse(enable: Optional<boolean>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-autoCollapse(enable: Optional<boolean>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes | 是否使用自适应折叠模式。&lt;br/&gt;默认值：true &lt;br/&gt;true：使用自适应折叠模式。&lt;br/&gt;false：不使用自适应折叠模式。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## color

```TypeScript
color(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute
```

设置普通状态下索引项文字颜色。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-color(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-color(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[ColorMetrics](arkts-arkui-colormetrics-t.md)&gt; | Yes | 文字颜色。&lt;br/&gt;默认值：0xFFFFFF，显示为白色。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## font

```TypeScript
font(font: Optional<Font>): ArcAlphabetIndexerAttribute
```

设置弧形字母索引条默认字体样式。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-font(font: Optional<Font>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-font(font: Optional<Font>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| font | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[Font](arkts-arkui-font-i.md)&gt; | Yes | 字母索引条默认字体样式，用于设置索引条上所有字母的显示效果，包括文字大小、粗细、倾斜角度和字体族等。&lt;br/&gt;默认值：&lt;br/&gt;{&lt;br/&gt;size:'13.0fp',&lt;br/&gt; style:FontStyle.Normal,&lt;br/&gt; weight:500,&lt;br/&gt; family:'HarmonyOS Sans'&lt;br/&gt;} |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## itemSize

```TypeScript
itemSize(size: Optional<LengthMetrics>): ArcAlphabetIndexerAttribute
```

设置弧形索引条索引项区域大小。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-itemSize(size: Optional<LengthMetrics>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-itemSize(size: Optional<LengthMetrics>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[LengthMetrics](arkts-arkui-lengthmetrics-t.md)&gt; | Yes | 弧形索引条索引项区域大小，索引项区域为圆形，即圆形直径。不支持设置为百分比。&lt;br/&gt;默认值：24.0 &lt;br/&gt;单位：vp |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## onSelect

```TypeScript
onSelect(handler: Optional<OnSelectCallback>): ArcAlphabetIndexerAttribute
```

索引条选中回调，返回值为当前选中索引。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-onSelect(handler: Optional<OnSelectCallback>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-onSelect(handler: Optional<OnSelectCallback>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;OnSelectCallback&gt; | Yes | 回调函数，用于处理索引条选中事件。当用户点击或滑动索引条选中某项时触发，回调中返回当前选中项的索引值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## popupBackground

```TypeScript
popupBackground(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute
```

设置提示弹窗背景色。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-popupBackground(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-popupBackground(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[ColorMetrics](arkts-arkui-colormetrics-t.md)&gt; | Yes | 提示弹窗背景色。&lt;br/&gt;默认值：0xD8404040，显示为微透明的深灰色。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## popupBackgroundBlurStyle

```TypeScript
popupBackgroundBlurStyle(style: Optional<BlurStyle>): ArcAlphabetIndexerAttribute
```

设置提示弹窗的背景模糊材质。未通过该接口设置时，默认为关闭模糊，对应取值为BlurStyle中的NONE。

> **说明：**

> 当通过popupBackgroundBlurStyle设置弹窗气泡的背景模糊材质时，不建议再通过
> [popupBackground](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md#popupbackground)设置背景色。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-popupBackgroundBlurStyle(style: Optional<BlurStyle>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-popupBackgroundBlurStyle(style: Optional<BlurStyle>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md)&gt; | Yes | 设置提示弹窗的背景模糊材质。&lt;br/&gt;默认值：BlurStyle.NONE。 &lt;br/&gt;设置此属性后不建议再设置[popupBackground](#popupbackground)属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## popupColor

```TypeScript
popupColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute
```

设置提示弹窗文字颜色。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-popupColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-popupColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[ColorMetrics](arkts-arkui-colormetrics-t.md)&gt; | Yes | 提示弹窗文字颜色。&lt;br/&gt;默认值：0xFFFFFF，显示为白色。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## popupFont

```TypeScript
popupFont(font: Optional<Font>): ArcAlphabetIndexerAttribute
```

设置提示弹窗字体样式，用于设置提示弹窗中显示的当前选中字母的显示效果，包括文字大小、粗细、倾斜角度和字体族等。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-popupFont(font: Optional<Font>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-popupFont(font: Optional<Font>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| font | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[Font](arkts-arkui-font-i.md)&gt; | Yes | 提示弹窗字体样式。&lt;br/&gt;默认值：&lt;br/&gt;{&lt;br/&gt;size:'19.0fp',&lt;br/&gt; style:FontStyle.Normal,&lt;br/&gt; weight:500,&lt;br/&gt; family:'HarmonyOS Sans'&lt;br/&gt;} |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## selected

```TypeScript
selected(index: Optional<number>): ArcAlphabetIndexerAttribute
```

设置选中项索引值。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-selected(index: Optional<number>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-selected(index: Optional<number>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;number&gt; | Yes | 选中项索引值。若超出有效索引范围，则取默认值0。&lt;br/&gt;默认值：0 &lt;br/&gt;该参数支持 [!!](../../../ui/state-management/arkts-new-binding.md)双向绑定变量。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## selectedBackgroundColor

```TypeScript
selectedBackgroundColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute
```

设置选中项背景颜色。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-selectedBackgroundColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-selectedBackgroundColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[ColorMetrics](arkts-arkui-colormetrics-t.md)&gt; | Yes | 选中项背景颜色。&lt;br/&gt;默认值：0x1F71FF，显示为深蓝色。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## selectedColor

```TypeScript
selectedColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute
```

设置选中项文字颜色。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-selectedColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-selectedColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[ColorMetrics](arkts-arkui-colormetrics-t.md)&gt; | Yes | 选中项文字颜色。&lt;br/&gt;默认值：0xFFFFFF，显示为白色。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## selectedFont

```TypeScript
selectedFont(font: Optional<Font>): ArcAlphabetIndexerAttribute
```

设置选中项文字尺寸、粗细、字体族、倾斜等样式。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-selectedFont(font: Optional<Font>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-selectedFont(font: Optional<Font>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| font | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[Font](arkts-arkui-font-i.md)&gt; | Yes | 选中项文字样式。&lt;br/&gt;默认值：{&lt;br/&gt;size:'13.0fp',&lt;br/&gt; style:FontStyle.Normal,&lt;br/&gt; weight:500 ,&lt;br/&gt; family:'HarmonyOS Sans'&lt;br/&gt;} |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## usePopup

```TypeScript
usePopup(enabled: Optional<boolean>): ArcAlphabetIndexerAttribute
```

设置是否使用提示弹窗。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-usePopup(enabled: Optional<boolean>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-usePopup(enabled: Optional<boolean>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes | 是否使用提示弹窗。&lt;br/&gt;true表示使用提示弹窗；false表示不使用提示弹窗。&lt;br/&gt;默认值：false |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

