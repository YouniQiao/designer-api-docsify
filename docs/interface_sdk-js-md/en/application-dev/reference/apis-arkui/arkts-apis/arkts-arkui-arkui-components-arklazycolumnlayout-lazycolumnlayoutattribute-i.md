# LazyColumnLayoutAttribute

定义懒列布局属性。

**Inheritance/Implementation:** LazyColumnLayoutAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface LazyColumnLayoutAttribute extends CommonMethod--><!--Device-unnamed-export declare interface LazyColumnLayoutAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { LazyColumnLayoutAttribute, LazyColumnLayout } from 'kits/@kit.ArkUI';
```

## alignItems

```TypeScript
default alignItems(value: HorizontalAlign | undefined): this
```

设置行内容的水平对齐方式。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyColumnLayoutAttribute-default alignItems(value: HorizontalAlign | undefined): this--><!--Device-LazyColumnLayoutAttribute-default alignItems(value: HorizontalAlign | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [HorizontalAlign](arkts-arkui-horizontalalign-e.md) \| undefined | Yes | 行内容的水平对齐。 &lt;br&gt;默认值：HorizontalAlign.Center。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<LazyColumnLayoutAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置属性修饰符。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyColumnLayoutAttribute-default attributeModifier(modifier: AttributeModifier<LazyColumnLayoutAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-LazyColumnLayoutAttribute-default attributeModifier(modifier: AttributeModifier<LazyColumnLayoutAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[LazyColumnLayoutAttribute](arkts-arkui-arkui-components-arklazycolumnlayout-lazycolumnlayoutattribute-i.md)&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## footer

```TypeScript
default footer(builder: CustomBuilder | undefined): this
```

设置懒加载列布局的footer。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyColumnLayoutAttribute-default footer(builder: CustomBuilder | undefined): this--><!--Device-LazyColumnLayoutAttribute-default footer(builder: CustomBuilder | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| undefined | Yes | footer生成器函数 &lt;br&gt;传递undefined将移除footer。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## header

```TypeScript
default header(builder: CustomBuilder | undefined): this
```

设置懒加载列布局的header。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyColumnLayoutAttribute-default header(builder: CustomBuilder | undefined): this--><!--Device-LazyColumnLayoutAttribute-default header(builder: CustomBuilder | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| undefined | Yes | header生成器函数 &lt;br&gt;传递undefined将移除header。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onVisibleIndexesChange

```TypeScript
default onVisibleIndexesChange(callback: OnVisibleIndexesChangeCallback | undefined): this
```

当子组件在可见区域的索引发生变化时触发。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyColumnLayoutAttribute-default onVisibleIndexesChange(callback: OnVisibleIndexesChangeCallback | undefined): this--><!--Device-LazyColumnLayoutAttribute-default onVisibleIndexesChange(callback: OnVisibleIndexesChangeCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnVisibleIndexesChangeCallback](../arkts-components/arkts-arkui-onvisibleindexeschangecallback-t.md) \| undefined | Yes | 回调函数，当可见区域中子组件的索引发生变化时触发. &lt;br&gt;传递undefined将取消注册回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setLazyColumnLayoutOptions

```TypeScript
default setLazyColumnLayoutOptions(): this
```

设置LazyColumnLayout选项。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyColumnLayoutAttribute-default setLazyColumnLayoutOptions(): this--><!--Device-LazyColumnLayoutAttribute-default setLazyColumnLayoutOptions(): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## space

```TypeScript
default space(space: LengthMetrics | undefined): this
```

行之间的间距。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyColumnLayoutAttribute-default space(space: LengthMetrics | undefined): this--><!--Device-LazyColumnLayoutAttribute-default space(space: LengthMetrics | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| space | [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md) \| undefined | Yes | 行之间的间距。 &lt;br&gt;默认值为0。&lt;br&gt;范围：[0, +∞)。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## sticky

```TypeScript
default sticky(sticky: StickyStyle | undefined): this
```

设置header和footer的吸顶吸底样式。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyColumnLayoutAttribute-default sticky(sticky: StickyStyle | undefined): this--><!--Device-LazyColumnLayoutAttribute-default sticky(sticky: StickyStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sticky | [StickyStyle](../arkts-components/arkts-arkui-stickystyle-e.md) \| undefined | Yes | header和footer的吸顶吸底样式。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

