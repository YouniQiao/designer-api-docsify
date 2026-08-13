# Indicator

Sets the distance between the navigation indicator and the **Swiper** component. Note that due to its default interaction area height of 32 vp, the navigation indicator cannot be placed flush against the bottom edge. To implement the function of completely attaching to the bottom, you can use the IndicatorComponent component to adjust the position more flexibly.

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare class Indicator--><!--Device-unnamed-declare class Indicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## bottom

```TypeScript
bottom(value: Length): T
```

Sets the position of the navigation indicator relative to the bottom edge of the **Swiper** component.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-Indicator-bottom(value: Length): T--><!--Device-Indicator-bottom(value: Length): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## bottom

```TypeScript
bottom(bottom: LengthMetrics | Length, ignoreSize: boolean): T
```

Sets the position of the navigation indicator relative to the bottom edge of the **Swiper** component. You can also choose to ignore the size of the navigation indicator using the **ignoreSize** property.

**Since:** 19

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**Widget capability:** This API can be used in ArkTS widgets since API version 19.

<!--Device-Indicator-bottom(bottom: LengthMetrics | Length, ignoreSize: boolean): T--><!--Device-Indicator-bottom(bottom: LengthMetrics | Length, ignoreSize: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [bottom](#bottom) | LengthMetrics \| [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |
| ignoreSize | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## digit

```TypeScript
static digit(): DigitIndicator
```

Returns a **DigitIndicator** object.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-Indicator-static digit(): DigitIndicator--><!--Device-Indicator-static digit(): DigitIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DigitIndicator](arkts-arkui-digitindicator-c.md) |

## dot

```TypeScript
static dot(): DotIndicator
```

Returns a **DotIndicator** object.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-Indicator-static dot(): DotIndicator--><!--Device-Indicator-static dot(): DotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |

## end

```TypeScript
end(value: LengthMetrics): T
```

Sets the distance between the navigation point indicator and the left edge (in right-to-left scripts) or the right edge (in left-to-right scripts) of the **Swiper** component.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-Indicator-end(value: LengthMetrics): T--><!--Device-Indicator-end(value: LengthMetrics): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [LengthMetrics](../../apis-na/arkts-apis/arkts-na-lengthmetrics-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## left

```TypeScript
left(value: Length): T
```

Sets the position of the navigation indicator relative to the left edge of the **Swiper** component.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-Indicator-left(value: Length): T--><!--Device-Indicator-left(value: Length): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## right

```TypeScript
right(value: Length): T
```

Sets the position of the navigation indicator relative to the right edge of the **Swiper** component.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-Indicator-right(value: Length): T--><!--Device-Indicator-right(value: Length): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## start

```TypeScript
start(value: LengthMetrics): T
```

Sets the distance between the navigation indicator and the right edge (in [RTL](../arkts-apis/arkts-arkui-layoutdirection-e.md#LayoutDirection) scripts) or the left edge (in [LTR](../arkts-apis/arkts-arkui-layoutdirection-e.md#LayoutDirection) scripts) of the **Swiper** component.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-Indicator-start(value: LengthMetrics): T--><!--Device-Indicator-start(value: LengthMetrics): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [LengthMetrics](../../apis-na/arkts-apis/arkts-na-lengthmetrics-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## top

```TypeScript
top(value: Length): T
```

Sets the position of the navigation indicator relative to the top edge of the **Swiper** component.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-Indicator-top(value: Length): T--><!--Device-Indicator-top(value: Length): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |
