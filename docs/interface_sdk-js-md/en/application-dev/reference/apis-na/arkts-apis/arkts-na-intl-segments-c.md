# Segments

Segments iterator class.

**Inheritance/Implementation:** Segments implements IterableIterator<SegmentData>

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-Intl-export class Segments--><!--Device-Intl-export class Segments-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## $_iterator

```TypeScript
public $_iterator(): IterableIterator<SegmentData>
```

Returns itself as the iterator.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Segments-public $_iterator(): IterableIterator<SegmentData>--><!--Device-Segments-public $_iterator(): IterableIterator<SegmentData>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;[SegmentData](arkts-na-intl-segmentdata-i.md)&gt; | the iterator. |

## constructor

```TypeScript
public constructor(parent: SegmentData[])
```

Creates a new Segments iterator.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Segments-public constructor(parent: SegmentData[])--><!--Device-Segments-public constructor(parent: SegmentData[])-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| parent | [SegmentData](arkts-na-intl-segmentdata-i.md)[] | Yes | the parent segments array. |

## next

```TypeScript
public next(): IteratorResult<SegmentData>
```

Returns the next result in the segments iterator.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Segments-public next(): IteratorResult<SegmentData>--><!--Device-Segments-public next(): IteratorResult<SegmentData>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IteratorResult&lt;[SegmentData](arkts-na-intl-segmentdata-i.md)&gt; | the next iteration result. |

