# sort_default

## sort_default

```TypeScript
export function sort_default<T>(arr: FixedArray<T>, arrStr: FixedArray<buffStr>, startIndex: int, endIndex: int): 
    void
```

Sorts elements of `arr` using default sort.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function sort_default<T>(arr: FixedArray<T>, arrStr: FixedArray<buffStr>, startIndex: int, endIndex: int):     void--><!--Device-unnamed-export function sort_default<T>(arr: FixedArray<T>, arrStr: FixedArray<buffStr>, startIndex: int, endIndex: int):     void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;T&gt; | 是 | The array to sort. |
| arrStr | FixedArray&lt;buffStr&gt; | 是 | Stringified array for comparison. |
| startIndex | int | 是 | The start index of sorting range. &lt;br&gt;The value should be an integer. |
| endIndex | int | 是 | The end index of sorting range. &lt;br&gt;The value should be an integer. |

