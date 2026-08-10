# ReadonlySet

ReadonlySet implementation.

**Inheritance/Implementation:** ReadonlySet extends [Iterable<T>](Iterable<T>)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export interface ReadonlySet<T> extends Iterable<T>--><!--Device-unnamed-export interface ReadonlySet<T> extends Iterable<T>-End-->

**System capability:** SystemCapability.Utils.Lang

## entries

```TypeScript
entries(): IterableIterator<[T, T]>
```

Returns an iterable of [v, v] pairs for every value in the Set.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlySet-entries(): IterableIterator<[T, T]>--><!--Device-ReadonlySet-entries(): IterableIterator<[T, T]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[T, T]&gt; | an iterable of [v, v] pairs. |

## forEach

```TypeScript
forEach(callbackfn: (value: T, value2: T, set: ReadonlySet<T>) => void): void
```

Executes a provided function once per each value in the Set object, in insertion order.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlySet-forEach(callbackfn: (value: T, value2: T, set: ReadonlySet<T>) => void): void--><!--Device-ReadonlySet-forEach(callbackfn: (value: T, value2: T, set: ReadonlySet<T>) => void): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (value: T, value2: T, set: ReadonlySet&lt;T&gt;) =&gt; void | Yes | the function to apply. |

## has

```TypeScript
has(value: T): boolean
```

Checks if a value is in the Set.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlySet-has(value: T): boolean--><!--Device-ReadonlySet-has(value: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | the value to find in the Set. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the value is in the Set. |

## keys

```TypeScript
keys(): IterableIterator<T>
```

Despite name, returns elements from the Set.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlySet-keys(): IterableIterator<T>--><!--Device-ReadonlySet-keys(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | an iterable of the values in the Set. |

## values

```TypeScript
values(): IterableIterator<T>
```

Returns elements from the Set.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlySet-values(): IterableIterator<T>--><!--Device-ReadonlySet-values(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | an iterable of the values in the Set. |

## size

```TypeScript
get size(): int
```

Returns the number of unique elements in the Set.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlySet-get size(): int--><!--Device-ReadonlySet-get size(): int-End-->

**System capability:** SystemCapability.Utils.Lang

