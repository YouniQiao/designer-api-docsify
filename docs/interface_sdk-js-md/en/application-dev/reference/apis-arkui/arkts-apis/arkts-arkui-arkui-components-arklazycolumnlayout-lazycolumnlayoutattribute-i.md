# LazyColumnLayoutAttribute

Defines the lazy column layout attribute.

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

Sets the horizontal alignment of the row content.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyColumnLayoutAttribute-default alignItems(value: HorizontalAlign | undefined): this--><!--Device-LazyColumnLayoutAttribute-default alignItems(value: HorizontalAlign | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [HorizontalAlign](arkts-arkui-horizontalalign-e.md) \| undefined | Yes | the horizontal alignment of the row content. &lt;br&gt;Default value: HorizontalAlign.Center. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<LazyColumnLayoutAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Sets the attribute modifier.

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

Sets the footer of the lazy column layout.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyColumnLayoutAttribute-default footer(builder: CustomBuilder | undefined): this--><!--Device-LazyColumnLayoutAttribute-default footer(builder: CustomBuilder | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| undefined | Yes | The footer builder function &lt;br&gt;Passing undefined will remove the footer. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## header

```TypeScript
default header(builder: CustomBuilder | undefined): this
```

Sets the header of the lazy column layout.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyColumnLayoutAttribute-default header(builder: CustomBuilder | undefined): this--><!--Device-LazyColumnLayoutAttribute-default header(builder: CustomBuilder | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| undefined | Yes | The header builder function &lt;br&gt;Passing undefined will remove the header. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onVisibleIndexesChange

```TypeScript
default onVisibleIndexesChange(callback: OnVisibleIndexesChangeCallback | undefined): this
```

Triggered when the index of child components in the visible area changes.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyColumnLayoutAttribute-default onVisibleIndexesChange(callback: OnVisibleIndexesChangeCallback | undefined): this--><!--Device-LazyColumnLayoutAttribute-default onVisibleIndexesChange(callback: OnVisibleIndexesChangeCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnVisibleIndexesChangeCallback](../arkts-components/arkts-arkui-onvisibleindexeschangecallback-t.md) \| undefined | Yes | callback function, triggered when the index of child components in the visible area changes. &lt;br&gt;Passing undefined will unregister the callback. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setLazyColumnLayoutOptions

```TypeScript
default setLazyColumnLayoutOptions(): this
```

Set LazyColumnLayout options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

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

The spacing between rows.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyColumnLayoutAttribute-default space(space: LengthMetrics | undefined): this--><!--Device-LazyColumnLayoutAttribute-default space(space: LengthMetrics | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| space | [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md) \| undefined | Yes | the spacing between rows. &lt;br&gt;Default value: 0. &lt;br&gt;Range: [0, +∞). |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## sticky

```TypeScript
default sticky(sticky: StickyStyle | undefined): this
```

Sets sticky style for header and footer.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyColumnLayoutAttribute-default sticky(sticky: StickyStyle | undefined): this--><!--Device-LazyColumnLayoutAttribute-default sticky(sticky: StickyStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sticky | [StickyStyle](../arkts-components/arkts-arkui-stickystyle-e.md) \| undefined | Yes | The sticky style for header and footer. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

