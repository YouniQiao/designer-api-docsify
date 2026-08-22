# iteratorForEach

## 导入模块

```TypeScript
```

## iteratorForEach

```TypeScript
export function iteratorForEach<V>(x: Iterator<V>, fn: (x: V) => void): void
```

遍历迭代器，并对每个元素执行指定的回调函数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function iteratorForEach<V>(x: Iterator<V>, fn: (x: V) => void): void--><!--Device-unnamed-export function iteratorForEach<V>(x: Iterator<V>, fn: (x: V) => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | Iterator&lt;V&gt; | 是 | 待遍历的迭代器。 |
| fn | (x: V) =&gt; void | 是 | 对迭代器每个元素执行的回调函数。 |

