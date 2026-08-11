# AnimatableArithmetic

The **AnimatableArithmetic** API defines animation calculation rules for non-number data types. To animate non-number data (such as arrays, structs, and colors), you need to implement the addition, subtraction, multiplication, and equality checking functions in the **AnimatableArithmetic\&lt;T\&gt;** API. This enables the data to participate in animation interpolation calculations and to detect whether the data has changed. In other words, the non-number data is defined as types that implement the **AnimatableArithmetic\&lt;T\&gt;** API.

**Since:** 10

<!--Device-unnamed-declare interface AnimatableArithmetic<T>--><!--Device-unnamed-declare interface AnimatableArithmetic<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## equals

```TypeScript
equals(rhs: AnimatableArithmetic<T>): boolean
```

Defines the equality check rule for the data type.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AnimatableArithmetic-equals(rhs: AnimatableArithmetic<T>): boolean--><!--Device-AnimatableArithmetic-equals(rhs: AnimatableArithmetic<T>): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rhs | [AnimatableArithmetic](arkts-arkui-animatablearithmetic-i.md)&lt;T&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## multiply

```TypeScript
multiply(scale: number): AnimatableArithmetic<T>
```

Defines the multiplication rule for the data type.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AnimatableArithmetic-multiply(scale: number): AnimatableArithmetic<T>--><!--Device-AnimatableArithmetic-multiply(scale: number): AnimatableArithmetic<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scale | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AnimatableArithmetic](arkts-arkui-animatablearithmetic-i.md)&lt;T&gt; |

## plus

```TypeScript
plus(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>
```

Defines the addition rule for the data type.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AnimatableArithmetic-plus(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>--><!--Device-AnimatableArithmetic-plus(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rhs | [AnimatableArithmetic](arkts-arkui-animatablearithmetic-i.md)&lt;T&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AnimatableArithmetic](arkts-arkui-animatablearithmetic-i.md)&lt;T&gt; |

## subtract

```TypeScript
subtract(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>
```

Defines the subtraction rule for the data type.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AnimatableArithmetic-subtract(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>--><!--Device-AnimatableArithmetic-subtract(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rhs | [AnimatableArithmetic](arkts-arkui-animatablearithmetic-i.md)&lt;T&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AnimatableArithmetic](arkts-arkui-animatablearithmetic-i.md)&lt;T&gt; |
