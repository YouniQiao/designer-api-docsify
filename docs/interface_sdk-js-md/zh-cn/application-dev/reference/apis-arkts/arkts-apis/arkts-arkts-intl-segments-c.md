# Segments

Segments iterator class.

**继承/实现关系：** Segments implements [IterableIterator<SegmentData>](IterableIterator<SegmentData>)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-Intl-export class Segments implements IterableIterator<SegmentData>--><!--Device-Intl-export class Segments implements IterableIterator<SegmentData>-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_iterator

```TypeScript
public $_iterator(): IterableIterator<SegmentData>
```

Returns itself as the iterator.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Segments-public $_iterator(): IterableIterator<SegmentData>--><!--Device-Segments-public $_iterator(): IterableIterator<SegmentData>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;SegmentData&gt; | the iterator. |

## constructor

```TypeScript
public constructor(parent: SegmentData[])
```

Creates a new Segments iterator.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Segments-public constructor(parent: SegmentData[])--><!--Device-Segments-public constructor(parent: SegmentData[])-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parent | [SegmentData](arkts-arkts-intl-segmentdata-i.md)[] | 是 | the parent segments array. |

## next

```TypeScript
public next(): IteratorResult<SegmentData>
```

Returns the next result in the segments iterator.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Segments-public next(): IteratorResult<SegmentData>--><!--Device-Segments-public next(): IteratorResult<SegmentData>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IteratorResult](arkts-arkts-iterator-iteratorresult-c.md)&lt;SegmentData&gt; | the next iteration result. |

