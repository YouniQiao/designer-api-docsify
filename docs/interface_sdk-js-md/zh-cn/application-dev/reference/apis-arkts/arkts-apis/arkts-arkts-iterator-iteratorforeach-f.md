# iteratorForEach

## iteratorForEach

```TypeScript
export function iteratorForEach<V>(x: Iterator<V>, fn: (x: V) => void): void
```

Iterates over an iterator and executes the specified callback function for each element

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function iteratorForEach<V>(x: Iterator<V>, fn: (x: V) => void): void--><!--Device-unnamed-export function iteratorForEach<V>(x: Iterator<V>, fn: (x: V) => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | Iterator&lt;V&gt; | 是 | The iterator to iterate over |
| fn | (x: V) =&gt; void | 是 | The callback function to execute for each element of the iterator |

