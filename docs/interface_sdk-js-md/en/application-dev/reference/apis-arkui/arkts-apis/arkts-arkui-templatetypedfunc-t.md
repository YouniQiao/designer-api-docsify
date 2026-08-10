# TemplateTypedFunc

```TypeScript
declare type TemplateTypedFunc<T> = (item: T, index: number) => string
```

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-declare type TemplateTypedFunc<T> = (item: T, index: number) => string--><!--Device-unnamed-declare type TemplateTypedFunc<T> = (item: T, index: number) => string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item | T | Yes | arr中每一个数据项。T为开发者传入的数据类型。 <br>缺省时默认忽略该参数，请勿在闭包函数的实现中使用该参数，否则会编译报错。 |
| index | number | Yes | 当前数据项对应的索引。 <br>缺省时默认忽略该参数，请勿在闭包函数的实现中使用该参数，否则会编译报错。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 当前数据项生成的template type。 |

