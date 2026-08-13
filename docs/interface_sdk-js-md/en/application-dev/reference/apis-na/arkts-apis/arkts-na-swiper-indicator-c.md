# Indicator

Defines the indicator class.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare class Indicator--><!--Device-unnamed-export declare class Indicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## bottom

```TypeScript
bottom(value: Length | undefined): this
```

Set the indicator to the bottom.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Indicator-bottom(value: Length | undefined): this--><!--Device-Indicator-bottom(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | Yes | the indicator to the bottom, default value is adaptive size layout, centered alignment in the spindle direction according to the size of the indicator itself and the size of the swiper, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## bottom

```TypeScript
bottom(bottom: LengthMetrics | Length | undefined, ignoreSize: boolean): this
```

Sets the position of the navigation indicator relative to the bottom edge of the Swiper component. You can also choose to ignore the size of the navigation indicator using the ignoreSize property.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Indicator-bottom(bottom: LengthMetrics | Length | undefined, ignoreSize: boolean): this--><!--Device-Indicator-bottom(bottom: LengthMetrics | Length | undefined, ignoreSize: boolean): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bottom | [LengthMetrics](../../apis-arkui/arkts-apis/arkts-arkui-lengthmetrics-t.md) \| [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | Yes | the offset of indicator to the bottom, default value is adaptive size layout, centered alignment in the spindle direction according to the size of the indicator itself and the size of the swiper, undefined means setting to default value. |
| ignoreSize | boolean | Yes | ignore the size of the indicator. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## digit

```TypeScript
static digit(): DigitIndicator
```

DigitIndicator class object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Indicator-static digit(): DigitIndicator--><!--Device-Indicator-static digit(): DigitIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [DigitIndicator](arkts-na-swiper-digitindicator-c.md) |  |

## dot

```TypeScript
static dot(): DotIndicator
```

DotIndicator class object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Indicator-static dot(): DotIndicator--><!--Device-Indicator-static dot(): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [DotIndicator](arkts-na-swiper-dotindicator-c.md) |  |

## end

```TypeScript
end(value: LengthMetrics | undefined): this
```

Set the indicator to the left in RTL Set the indicator to the right in LTR

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Indicator-end(value: LengthMetrics | undefined): this--><!--Device-Indicator-end(value: LengthMetrics | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [LengthMetrics](../../apis-arkui/arkts-apis/arkts-arkui-lengthmetrics-t.md) \| undefined | Yes | the indicator to the left in RTL, Set the indicator to the right in LTR, default value is 0.0_vp, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## left

```TypeScript
left(value: Length | undefined): this
```

Set the indicator to the left.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Indicator-left(value: Length | undefined): this--><!--Device-Indicator-left(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | Yes | the indicator to the left, default value is adaptive size layout, centered alignment in the spindle direction according to the size of the indicator itself and the size of the swiper, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## right

```TypeScript
right(value: Length | undefined): this
```

Set the indicator to the right.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Indicator-right(value: Length | undefined): this--><!--Device-Indicator-right(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | Yes | the indicator to the right, default value is adaptive size layout, centered alignment in the spindle direction according to the size of the indicator itself and the size of the swiper, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## start

```TypeScript
start(value: LengthMetrics | undefined): this
```

Set the indicator to the left in LTR Set the indicator to the right in RTL

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Indicator-start(value: LengthMetrics | undefined): this--><!--Device-Indicator-start(value: LengthMetrics | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [LengthMetrics](../../apis-arkui/arkts-apis/arkts-arkui-lengthmetrics-t.md) \| undefined | Yes | the indicator to the right in LTR, indicator to the left in RTL, default value is 0.0_vp, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## top

```TypeScript
top(value: Length | undefined): this
```

Set the indicator to the top.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Indicator-top(value: Length | undefined): this--><!--Device-Indicator-top(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | Yes | the indicator to the top, default value is adaptive size layout, centered alignment in the spindle direction according to the size of the indicator itself and the size of the swiper, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

