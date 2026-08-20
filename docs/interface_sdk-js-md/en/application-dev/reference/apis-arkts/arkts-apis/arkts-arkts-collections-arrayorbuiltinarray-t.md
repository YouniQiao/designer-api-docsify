# ArrayOrBuiltinArray

```TypeScript
type ArrayOrBuiltinArray<T> = Array<T> | BuiltinArray<T>
```

Defines the type for ArkTS Array APIs that accept either an ArkTS Array or a built-in Array.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-collections-type ArrayOrBuiltinArray<T> = Array<T> | BuiltinArray<T>--><!--Device-collections-type ArrayOrBuiltinArray<T> = Array<T> | BuiltinArray<T>-End-->

**System capability:** SystemCapability.Utils.Lang

| Type | Description |
| --- | --- |
| Array&lt;T&gt; | ArkTS Array. |
| BuiltinArray&lt;T&gt; | Built-in Array. |

