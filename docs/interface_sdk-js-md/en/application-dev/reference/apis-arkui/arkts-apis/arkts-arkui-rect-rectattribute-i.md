# RectAttribute

rect attribute declaration.

**Inheritance/Implementation:** RectAttribute extends CommonShapeMethod

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface RectAttribute--><!--Device-unnamed-export declare interface RectAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<RectAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-RectAttribute-attributeModifier(modifier: AttributeModifier<RectAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-RectAttribute-attributeModifier(modifier: AttributeModifier<RectAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[RectAttribute](arkts-arkui-rect-rectattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## radius

```TypeScript
radius(value: Length | Array<RadiusItem> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-RectAttribute-radius(value: Length | Array<RadiusItem> | undefined): this--><!--Device-RectAttribute-radius(value: Length | Array<RadiusItem> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| Array&lt;[RadiusItem](arkts-arkui-radiusitem-t.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## radiusHeight

```TypeScript
radiusHeight(value: Length | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-RectAttribute-radiusHeight(value: Length | undefined): this--><!--Device-RectAttribute-radiusHeight(value: Length | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## radiusWidth

```TypeScript
radiusWidth(value: Length | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-RectAttribute-radiusWidth(value: Length | undefined): this--><!--Device-RectAttribute-radiusWidth(value: Length | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setRectOptions

```TypeScript
setRectOptions(options?: RectOptions | RoundedRectOptions): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-RectAttribute-setRectOptions(options?: RectOptions | RoundedRectOptions): this--><!--Device-RectAttribute-setRectOptions(options?: RectOptions | RoundedRectOptions): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RectOptions](arkts-arkui-rect-rectoptions-i.md) \| [RoundedRectOptions](arkts-arkui-rect-roundedrectoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Call attributeModifier.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RectAttribute-default--><!--Device-RectAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

