# Segments

Segments iterator class.

**Inheritance/Implementation:** Segments implements [IterableIterator<SegmentData>](IterableIterator<SegmentData>)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-Intl-export class Segments implements IterableIterator<SegmentData>--><!--Device-Intl-export class Segments implements IterableIterator<SegmentData>-End-->

**System capability:** SystemCapability.Utils.Lang

## $_iterator

```TypeScript
public $_iterator(): IterableIterator<SegmentData>
```

Returns itself as the iterator.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Segments-public $_iterator(): IterableIterator<SegmentData>--><!--Device-Segments-public $_iterator(): IterableIterator<SegmentData>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;SegmentData&gt; | the iterator. |

## constructor

```TypeScript
public constructor(parent: SegmentData[])
```

Creates a new Segments iterator.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Segments-public constructor(parent: SegmentData[])--><!--Device-Segments-public constructor(parent: SegmentData[])-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| parent | \_\_\_MD\_LINK\_USD\_0\_\_\_[] | Yes | the parent segments array. |

## next

```TypeScript
public next(): IteratorResult<SegmentData>
```

Returns the next result in the segments iterator.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Segments-public next(): IteratorResult<SegmentData>--><!--Device-Segments-public next(): IteratorResult<SegmentData>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;SegmentData&gt; | the next iteration result. |

