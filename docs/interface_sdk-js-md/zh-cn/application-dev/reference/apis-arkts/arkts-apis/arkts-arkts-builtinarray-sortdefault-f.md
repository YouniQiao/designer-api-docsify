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

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arr | FixedArray & lt;T & gt; | 是 |
| arrStr | FixedArray & lt;buffStr & gt; | 是 |
| startIndex | int | 是 |
| endIndex | int | 是 |
