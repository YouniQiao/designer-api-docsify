# RepeatArray

```TypeScript
declare type RepeatArray<T> = Array<T> | ReadonlyArray<T> | Readonly<Array<T>>
```

Repeat数据源参数联合类型。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-unnamed-declare type RepeatArray<T> = Array<T> | ReadonlyArray<T> | Readonly<Array<T>>--><!--Device-unnamed-declare type RepeatArray<T> = Array<T> | ReadonlyArray<T> | Readonly<Array<T>>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| --- | --- |
| Array&lt;T&gt; | 常规数组类型。 |
| ReadonlyArray&lt;T&gt; | 只读数组类型，不允许数组对象变更。 |
| Readonly&lt;Array&lt;T&gt;&gt; | 只读数组类型，不允许数组对象变更。 |

