# AnimatableArithmetic

The **AnimatableArithmetic** API defines the animation operation rules for non-number data types. To animate non-number data (such as arrays, structs, and colors), implement the addition, subtraction, multiplication, and equality judgment functions in the **AnimatableArithmetic\&lt;T\&gt;** API. In this way, the data can be involved in an interpolation operation of the animation and identify whether the data changes, that is, the non-number data is defined as the types that implement the **AnimatableArithmetic\&lt;T\&gt;** API.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface AnimatableArithmetic--><!--Device-unnamed-export declare interface AnimatableArithmetic-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## equals

```TypeScript
equals(rhs: AnimatableArithmetic<T>): boolean
```

Defines the equality judgment rule of the data type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatableArithmetic-equals(rhs: AnimatableArithmetic<T>): boolean--><!--Device-AnimatableArithmetic-equals(rhs: AnimatableArithmetic<T>): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rhs | [AnimatableArithmetic](arkts-common-animatablearithmetic-i.md)&lt;T&gt; | Yes | another value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | is equals |

## multiply

```TypeScript
multiply(scale: double): AnimatableArithmetic<T>
```

Defines the multiplication rule of the data type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatableArithmetic-multiply(scale: double): AnimatableArithmetic<T>--><!--Device-AnimatableArithmetic-multiply(scale: double): AnimatableArithmetic<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scale | double | Yes | scale value |

**Return value:**

| Type | Description |
| --- | --- |
| [AnimatableArithmetic](arkts-common-animatablearithmetic-i.md)&lt;T&gt; | new value which implements AnimatableArithmetic&lt;T&gt; interface |

## plus

```TypeScript
plus(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>
```

Defines the addition rule of the data type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatableArithmetic-plus(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>--><!--Device-AnimatableArithmetic-plus(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rhs | [AnimatableArithmetic](arkts-common-animatablearithmetic-i.md)&lt;T&gt; | Yes | another value |

**Return value:**

| Type | Description |
| --- | --- |
| [AnimatableArithmetic](arkts-common-animatablearithmetic-i.md)&lt;T&gt; | new value which implements AnimatableArithmetic&lt;T&gt; interface |

## subtract

```TypeScript
subtract(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>
```

Defines the subtraction rule of the data type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatableArithmetic-subtract(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>--><!--Device-AnimatableArithmetic-subtract(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rhs | [AnimatableArithmetic](arkts-common-animatablearithmetic-i.md)&lt;T&gt; | Yes | another value |

**Return value:**

| Type | Description |
| --- | --- |
| [AnimatableArithmetic](arkts-common-animatablearithmetic-i.md)&lt;T&gt; | new value which implements AnimatableArithmetic&lt;T&gt; interface |

