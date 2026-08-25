# Circle properties/events

In addition to the [universal attributes](arkts-arkui-commonmethod-c.md), the following attributes are supported.

**Inheritance/Implementation:** CircleAttribute extends CommonShapeMethod<CircleAttribute>

**Since:** 7

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## fill

```TypeScript
fill(value: ResourceColor | ColorMetrics)
```

Sets the color of the fill area. An invalid value is handled as the default value. If this attribute and the universal attribute foregroundColor are both set, whichever is set later takes effect.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) \| [ColorMetrics](../arkts-apis/arkts-arkui-graphics-colormetrics-c.md) | Yes |

## stroke

```TypeScript
stroke(value: ResourceColor | ColorMetrics)
```

Sets the stroke color. This attribute can be dynamically set using attributeModifier. If this attribute is not set, the default stroke opacity is 0, meaning no stroke is displayed.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) \| [ColorMetrics](../arkts-apis/arkts-arkui-graphics-colormetrics-c.md) | Yes |
