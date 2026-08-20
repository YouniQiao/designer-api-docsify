# Segments

分段迭代器类。

**继承/实现关系：** Segments implements IterableIterator<SegmentData>

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-Intl-export class Segments--><!--Device-Intl-export class Segments-End-->

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

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Segments-public $_iterator(): IterableIterator<SegmentData>--><!--Device-Segments-public $_iterator(): IterableIterator<SegmentData>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[SegmentData](arkts-arkts-intl-segmentdata-i.md)&gt; | 迭代器。 |

## constructor

```TypeScript
public constructor(parent: SegmentData[])
```

创建新的分段迭代器。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Segments-public constructor(parent: SegmentData[])--><!--Device-Segments-public constructor(parent: SegmentData[])-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parent | [SegmentData](arkts-arkts-intl-segmentdata-i.md)[] | 是 | 所属的分段数组。 |

## next

```TypeScript
public next(): IteratorResult<SegmentData>
```

返回分段迭代器中的下一个结果。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Segments-public next(): IteratorResult<SegmentData>--><!--Device-Segments-public next(): IteratorResult<SegmentData>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IteratorResult](arkts-arkts-iterator-iteratorresult-c.md)&lt;[SegmentData](arkts-arkts-intl-segmentdata-i.md)&gt; | 下一次迭代的结果。 |

