# Segments

Segments iterator class.

**Inheritance/Implementation:** Segments implements IterableIterator<SegmentData>

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

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

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| IterableIterator&lt;[SegmentData](arkts-arkts-intl-segmentdata-i.md)&gt; |

## constructor

```TypeScript
public constructor(parent: SegmentData[])
```

Creates a new Segments iterator.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parent | [SegmentData](arkts-arkts-intl-segmentdata-i.md)[] | Yes |

## next

```TypeScript
public next(): IteratorResult<SegmentData>
```

Returns the next result in the segments iterator.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| IteratorResult&lt;[SegmentData](arkts-arkts-intl-segmentdata-i.md)&gt; |
