# ConcatArray

An array-like object that can be concatenated. This API extends **ISendable**. > **NOTE：**> > - This module can be imported only to ArkTS files (with the file name extension .ets). > This section uses the following to identify the use of generics: - T: type, which can be any of the [sendable data types](../../../arkts-utils/arkts-sendable.md#sendable-data-types).

**Inheritance/Implementation:** ConcatArray extends [ISendable](arkts-arkts-collections-isendable-t.md#isendable)

**Since:** 12

<!--Device-collections-interface ConcatArray--><!--Device-collections-interface ConcatArray-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## join

```TypeScript
join(separator?: string): string
```

Concatenates all elements in this array into a string, with a given separator.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ConcatArray-join(separator?: string): string--><!--Device-ConcatArray-join(separator?: string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| separator | string | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## slice

```TypeScript
slice(start?: number, end?: number): ConcatArray<T>
```

Selects a range of elements in this array to create an array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ConcatArray-slice(start?: number, end?: number): ConcatArray<T>--><!--Device-ConcatArray-slice(start?: number, end?: number): ConcatArray<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | No |
| end | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| ConcatArray & lt;T & gt; |

## length

```TypeScript
readonly length: number
```

Number of elements in a ConcatArray.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ConcatArray-readonly length: number--><!--Device-ConcatArray-readonly length: number-End-->

**System capability:** SystemCapability.Utils.Lang
