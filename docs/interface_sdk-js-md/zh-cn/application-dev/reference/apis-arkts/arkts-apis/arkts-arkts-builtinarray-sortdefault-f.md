# sort_default

## 导入模块

```TypeScript
```

## sort_default

```TypeScript
export function sort_default<T>(arr: FixedArray<T>, arrStr: FixedArray<buffStr>, startIndex: int, endIndex: int): 
    void
```

使用默认排序方式对`arr`中的元素排序。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function sort_default<T>(arr: FixedArray<T>, arrStr: FixedArray<buffStr>, startIndex: int, endIndex: int):     void--><!--Device-unnamed-export function sort_default<T>(arr: FixedArray<T>, arrStr: FixedArray<buffStr>, startIndex: int, endIndex: int):     void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;T&gt; | 是 | 待排序的数组。 |
| arrStr | FixedArray&lt;buffStr&gt; | 是 | 用于比较的数组字符串表示。 |
| startIndex | int | 是 | 排序范围的起始索引。 <br>取值约束：应为整数。 |
| endIndex | int | 是 | 排序范围的结束索引。 <br>取值约束：应为整数。 |

