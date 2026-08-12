# IndicatorComponentAttribute

Defines the IndicatorComponent attribute functions.

**Inheritance/Implementation:** IndicatorComponentAttribute extends [CommonMethod](CommonMethod)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface IndicatorComponentAttribute extends CommonMethod--><!--Device-unnamed-export declare interface IndicatorComponentAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
count(totalCount: int | undefined): this
```

Sets the total number of indicator.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentAttribute-count(totalCount: int | undefined): this--><!--Device-IndicatorComponentAttribute-count(totalCount: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| totalCount | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## initialIndex

```TypeScript
initialIndex(index: int | undefined): this
```

Called when the index value of the displayed subcomponent is set in the container.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentAttribute-initialIndex(index: int | undefined): this--><!--Device-IndicatorComponentAttribute-initialIndex(index: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## loop

```TypeScript
loop(isLoop: boolean | undefined): this
```

Called when setting whether to turn on cyclic sliding.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentAttribute-loop(isLoop: boolean | undefined): this--><!--Device-IndicatorComponentAttribute-loop(isLoop: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isLoop | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
onChange(event: Callback<int> | undefined): this
```

Called when the index value changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentAttribute-onChange(event: Callback<int> | undefined): this--><!--Device-IndicatorComponentAttribute-onChange(event: Callback<int> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;int&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setIndicatorComponentOptions

```TypeScript
default setIndicatorComponentOptions(controller?: IndicatorComponentController): this
```

Set indicatorComponent options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentAttribute-default setIndicatorComponentOptions(controller?: IndicatorComponentController): this--><!--Device-IndicatorComponentAttribute-default setIndicatorComponentOptions(controller?: IndicatorComponentController): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controller | [IndicatorComponentController](arkts-arkui-indicatorcomponent-indicatorcomponentcontroller-c.md) | No | IndicatorComponent constructor options |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the IndicatorComponentAttribute. |

## style

```TypeScript
style(indicatorStyle: DotIndicator | DigitIndicator | undefined): this
```

Sets the indicator style.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentAttribute-style(indicatorStyle: DotIndicator | DigitIndicator | undefined): this--><!--Device-IndicatorComponentAttribute-style(indicatorStyle: DotIndicator | DigitIndicator | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| indicatorStyle | [DotIndicator](../arkts-components/arkts-arkui-dotindicator-c.md) \| [DigitIndicator](../arkts-components/arkts-arkui-digitindicator-c.md) \| undefined | Yes | the style value |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## vertical

```TypeScript
vertical(isVertical: boolean | undefined): this
```

Called when setting whether to slide vertically.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentAttribute-vertical(isVertical: boolean | undefined): this--><!--Device-IndicatorComponentAttribute-vertical(isVertical: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isVertical | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

