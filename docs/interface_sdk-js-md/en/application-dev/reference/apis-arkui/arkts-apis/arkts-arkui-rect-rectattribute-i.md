# RectAttribute

矩形绘制组件。

**Inheritance/Implementation:** RectAttribute extends [CommonShapeMethod](arkts-arkui-arkui-shape-commonshapemethod-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface RectAttribute extends CommonShapeMethod--><!--Device-unnamed-export declare interface RectAttribute extends CommonShapeMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<RectAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Call attributeModifier.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RectAttribute-default attributeModifier(modifier: AttributeModifier<RectAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-RectAttribute-default attributeModifier(modifier: AttributeModifier<RectAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;RectAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## radius

```TypeScript
default radius(value: Length | Array<RadiusItem> | undefined): this
```

设置圆角半径大小，取值范围≥0，支持  
[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。异常值按照默认值处理。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RectAttribute-default radius(value: Length | Array<RadiusItem> | undefined): this--><!--Device-RectAttribute-default radius(value: Length | Array<RadiusItem> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| Array&lt;RadiusItem&gt; \| undefined | Yes | 圆角半径大小。 默认值：0 默认单位：vp 异常值undefined和null按照[[0, 0], [0, 0], [0, 0], [0, 0]]处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## radiusHeight

```TypeScript
default radiusHeight(value: Length | undefined): this
```

设置圆角的高度，仅设置高时宽高一致，支持  
[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。异常值按照默认值处理。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RectAttribute-default radiusHeight(value: Length | undefined): this--><!--Device-RectAttribute-default radiusHeight(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes | 圆角的高度，取值范围≥0。 默认值：0 默认单位：vp 异常值undefined按照默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## radiusWidth

```TypeScript
default radiusWidth(value: Length | undefined): this
```

设置圆角的宽度，仅设置宽时宽高一致，支持  
[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。异常值按照默认值处理。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RectAttribute-default radiusWidth(value: Length | undefined): this--><!--Device-RectAttribute-default radiusWidth(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes | 圆角的宽度，取值范围≥0。 默认值：0 默认单位：vp 异常值undefined按照默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setRectOptions

```TypeScript
default setRectOptions(options?: RectOptions | RoundedRectOptions): this
```

Set Rect options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RectAttribute-default setRectOptions(options?: RectOptions | RoundedRectOptions): this--><!--Device-RectAttribute-default setRectOptions(options?: RectOptions | RoundedRectOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RectOptions](arkts-arkui-rect-rectoptions-i.md) \| RoundedRectOptions | No | Rect constructor options |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the RectAttribute. |

