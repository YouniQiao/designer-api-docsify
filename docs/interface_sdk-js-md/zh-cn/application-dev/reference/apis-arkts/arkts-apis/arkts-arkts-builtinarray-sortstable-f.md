# sort_stable

## 导入模块

```TypeScript
```

## sort_stable

```TypeScript
export function sort_stable<T>(arr: FixedArray<T>, startIndex: int, endIndex: int, comp: (lhs: T, rhs: T) => int): 
    void
```

使用稳定排序算法对`arr`中的元素排序。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function sort_stable<T>(arr: FixedArray<T>, startIndex: int, endIndex: int, comp: (lhs: T, rhs: T) => int):     void--><!--Device-unnamed-export function sort_stable<T>(arr: FixedArray<T>, startIndex: int, endIndex: int, comp: (lhs: T, rhs: T) => int):     void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;T&gt; | 是 | 待排序的数组。 |
| startIndex | int | 是 | 排序范围的起始索引。 <br>取值约束：应为整数。 |
| endIndex | int | 是 | 排序范围的结束索引。 <br>取值约束：应为整数。 |
| comp | (lhs: T, rhs: T) =&gt; int | 是 | 比较函数。 |

