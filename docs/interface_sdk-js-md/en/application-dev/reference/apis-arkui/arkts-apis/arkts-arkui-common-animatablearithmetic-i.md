# AnimatableArithmetic

该接口定义非number数据类型的动画运算规则。对非number类型的数据（如数组、结构体、颜色等）做动画，需要实现AnimatableArithmetic\&lt;T\&gt;接口中加法、减法、乘法和判断相等函数，使得该数据能参与动画的插值运算和识别该数据是否发生改变。即定义它们为实现了AnimatableArithmetic\&lt;T\&gt;接口的类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface AnimatableArithmetic<T>--><!--Device-unnamed-export declare interface AnimatableArithmetic<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## equals

```TypeScript
equals(rhs: AnimatableArithmetic<T>): boolean
```

定义该数据类型的相等判断规则。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatableArithmetic-equals(rhs: AnimatableArithmetic<T>): boolean--><!--Device-AnimatableArithmetic-equals(rhs: AnimatableArithmetic<T>): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rhs | [AnimatableArithmetic](../arkts-components/arkts-arkui-animatablearithmetic-i.md)&lt;T&gt; | Yes | 和自身比较相等的另一个数据对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 是否相等。返回true表示相等，返回false表示不相等。 |

## multiply

```TypeScript
multiply(scale: double): AnimatableArithmetic<T>
```

定义该数据类型的乘法运算规则。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatableArithmetic-multiply(scale: double): AnimatableArithmetic<T>--><!--Device-AnimatableArithmetic-multiply(scale: double): AnimatableArithmetic<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scale | double | Yes | 乘法运算的系数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [AnimatableArithmetic](../arkts-components/arkts-arkui-animatablearithmetic-i.md)&lt;T&gt; | 乘法运算的结果。 |

## plus

```TypeScript
plus(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>
```

定义数据类型的加法运算规则。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatableArithmetic-plus(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>--><!--Device-AnimatableArithmetic-plus(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rhs | [AnimatableArithmetic](../arkts-components/arkts-arkui-animatablearithmetic-i.md)&lt;T&gt; | Yes | 加法运算的对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| [AnimatableArithmetic](../arkts-components/arkts-arkui-animatablearithmetic-i.md)&lt;T&gt; | 加法运算的结果。 |

## subtract

```TypeScript
subtract(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>
```

定义该数据类型的减法运算规则。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatableArithmetic-subtract(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>--><!--Device-AnimatableArithmetic-subtract(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rhs | [AnimatableArithmetic](../arkts-components/arkts-arkui-animatablearithmetic-i.md)&lt;T&gt; | Yes | 减法运算的对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| [AnimatableArithmetic](../arkts-components/arkts-arkui-animatablearithmetic-i.md)&lt;T&gt; | 减法运算的结果。 |

