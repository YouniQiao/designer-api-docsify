# Iterable

可迭代接口，表示其元素可被遍历的对象。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-export interface Iterable--><!--Device-unnamed-export interface Iterable-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_iterator

```TypeScript
$_iterator(): Iterator<T>
```

返回该对象的迭代器。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Iterable-$_iterator(): Iterator<T>--><!--Device-Iterable-$_iterator(): Iterator<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Iterator&lt;T&gt; | 该可迭代对象的迭代器实例。 |

