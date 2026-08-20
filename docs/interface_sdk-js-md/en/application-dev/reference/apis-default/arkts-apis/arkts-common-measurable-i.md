# Measurable

Sub component info passed from framework when measure happens.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface Measurable--><!--Device-unnamed-export declare interface Measurable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getBorderWidth

```TypeScript
getBorderWidth(): DirectionalEdgesT<double> | undefined
```

Obtains the border width of the child component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Measurable-getBorderWidth(): DirectionalEdgesT<double> | undefined--><!--Device-Measurable-getBorderWidth(): DirectionalEdgesT<double> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [DirectionalEdgesT](../../apis-arkui/arkts-apis/arkts-arkui-directionaledgest-i.md)&lt;double&gt; \| undefined | Border width of the child component, unit is vp. If some errors occur in the internal runtime environment, returns undefined. |

## getMargin

```TypeScript
getMargin(): DirectionalEdgesT<double> | undefined
```

Obtains the margin of the child component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Measurable-getMargin(): DirectionalEdgesT<double> | undefined--><!--Device-Measurable-getMargin(): DirectionalEdgesT<double> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [DirectionalEdgesT](../../apis-arkui/arkts-apis/arkts-arkui-directionaledgest-i.md)&lt;double&gt; \| undefined | Margin of the child component, unit is vp. If some errors occur in the internal runtime environment, returns undefined. |

## getPadding

```TypeScript
getPadding(): DirectionalEdgesT<double> | undefined
```

Obtains the padding of the child component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Measurable-getPadding(): DirectionalEdgesT<double> | undefined--><!--Device-Measurable-getPadding(): DirectionalEdgesT<double> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [DirectionalEdgesT](../../apis-arkui/arkts-apis/arkts-arkui-directionaledgest-i.md)&lt;double&gt; \| undefined | the padding of sub component, unit is vp. If some errors occur in the internal runtime environment, returns undefined. |

## measure

```TypeScript
measure(constraint: ConstraintSizeOptions | undefined): MeasureResult | undefined
```

Applies the size constraint to the child component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Measurable-measure(constraint: ConstraintSizeOptions | undefined): MeasureResult | undefined--><!--Device-Measurable-measure(constraint: ConstraintSizeOptions | undefined): MeasureResult | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| constraint | [ConstraintSizeOptions](../../apis-arkui/arkts-apis/arkts-arkui-constraintsizeoptions-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [MeasureResult](arkts-common-measureresult-i.md) \| undefined | Provides the measurement result of the component. If some errors occur in the internal runtime environment, returns undefined. |

## uniqueId

```TypeScript
uniqueId?: int
```

Unique ID that the system assigns to the child component.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Measurable-uniqueId?: int--><!--Device-Measurable-uniqueId?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

