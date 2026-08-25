# Segments

分段迭代器类。

**继承/实现关系：** Segments implements IterableIterator<SegmentData>

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_iterator

```TypeScript
public $_iterator(): IterableIterator<SegmentData>
```

返回自身作为迭代器。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[SegmentData](arkts-arkts-intl-segmentdata-i.md)&gt; |

## constructor

```TypeScript
public constructor(parent: SegmentData[])
```

创建新的分段迭代器。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parent | [SegmentData](arkts-arkts-intl-segmentdata-i.md)[] | 是 |

## next

```TypeScript
public next(): IteratorResult<SegmentData>
```

返回分段迭代器中的下一个结果。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [IteratorResult](arkts-arkts-iterator-iteratorresult-c.md)&lt;[SegmentData](arkts-arkts-intl-segmentdata-i.md)&gt; |
