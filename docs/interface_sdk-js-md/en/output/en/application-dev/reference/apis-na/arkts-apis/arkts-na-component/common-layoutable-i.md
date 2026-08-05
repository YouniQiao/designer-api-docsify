# Layoutable

Provides the child component layout information.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface Layoutable--><!--Device-unnamed-export declare interface Layoutable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getBorderWidth

```TypeScript
getBorderWidth(): DirectionalEdgesT<double> | undefined
```

Obtains the border width of the child component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Layoutable-getBorderWidth(): DirectionalEdgesT<double> | undefined--><!--Device-Layoutable-getBorderWidth(): DirectionalEdgesT<double> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;double&gt; | the borderWidth of sub component, unit is vp. If some errors |

## getMargin

```TypeScript
getMargin(): DirectionalEdgesT<double> | undefined
```

Obtains the margin of the child component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Layoutable-getMargin(): DirectionalEdgesT<double> | undefined--><!--Device-Layoutable-getMargin(): DirectionalEdgesT<double> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;double&gt; | the margin of sub component, unit is vp. If some errors |

## getPadding

```TypeScript
getPadding(): DirectionalEdgesT<double> | undefined
```

Call this method to get the padding of sub component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Layoutable-getPadding(): DirectionalEdgesT<double> | undefined--><!--Device-Layoutable-getPadding(): DirectionalEdgesT<double> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;double&gt; | Padding of the child component, unit is vp. If some errors |

## layout

```TypeScript
layout(position: Position | undefined): void
```

Applies the specified position information to the child component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Layoutable-layout(position: Position | undefined): void--><!--Device-Layoutable-layout(position: Position | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes |  |

## measureResult

```TypeScript
measureResult: MeasureResult
```

Measurement result of the child component.

**Type:** MeasureResult

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Layoutable-measureResult: MeasureResult--><!--Device-Layoutable-measureResult: MeasureResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## uniqueId

```TypeScript
uniqueId?: int
```

Unique ID of the child component.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Layoutable-uniqueId?: int--><!--Device-Layoutable-uniqueId?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

