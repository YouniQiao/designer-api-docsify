# Iterator

迭代器接口，定义了获取序列中下一个值的方法。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export interface Iterator--><!--Device-unnamed-export interface Iterator-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## next

```TypeScript
next(): IteratorResult<T>
```

返回迭代器中的下一个结果。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Iterator-next(): IteratorResult<T>--><!--Device-Iterator-next(): IteratorResult<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IteratorResult](arkts-arkts-iterator-iteratorresult-c.md)&lt;T&gt; | 包含迭代状态和值的IteratorResult对象。 |

