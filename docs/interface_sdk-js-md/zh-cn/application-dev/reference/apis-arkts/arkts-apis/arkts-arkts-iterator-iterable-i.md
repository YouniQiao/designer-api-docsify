# Iterable

Iterable interface representing an object whose elements can be traversed

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export interface Iterable<out T>--><!--Device-unnamed-export interface Iterable<out T>-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_iterator

```TypeScript
$_iterator(): Iterator<T>
```

Returns an iterator for this object

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Iterable-$_iterator(): Iterator<T>--><!--Device-Iterable-$_iterator(): Iterator<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Iterator&lt;T&gt; | An iterator instance for this iterable object |

