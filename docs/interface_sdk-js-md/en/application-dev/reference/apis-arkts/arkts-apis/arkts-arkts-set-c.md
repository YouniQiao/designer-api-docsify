# Set

Set implementation.

**Inheritance/Implementation:** Set implements ReadonlySet<K>

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

<!--Device-unnamed-export class Set--><!--Device-unnamed-export class Set-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<K>
```

Returns the default iterator of the Set, which is the values() iterator.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Set-$_iterator(): IterableIterator<K>--><!--Device-Set-$_iterator(): IterableIterator<K>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;K&gt; | The default iterator of the Set. |

## add

```TypeScript
add(val: K): this
```

Puts a value into the Set.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Set-add(val: K): this--><!--Device-Set-add(val: K): this-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | K | Yes | the value to put into the Set. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Add value Set. |

## clear

```TypeScript
clear(): void
```

Deletes all elements from the Set.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Set-clear(): void--><!--Device-Set-clear(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(bucketsCount: int)
```

Creates a new Set instance with the specified number of buckets.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Set-constructor(bucketsCount: int)--><!--Device-Set-constructor(bucketsCount: int)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bucketsCount | int | Yes | The number of buckets for the internal map. <br>The value should be an integer. |

## constructor

```TypeScript
constructor(set: Set<K>)
```

Creates a new Set instance from another Set.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Set-constructor(set: Set<K>)--><!--Device-Set-constructor(set: Set<K>)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| set | Set&lt;K&gt; | Yes | Another Set instance used for initialization. |

## constructor

```TypeScript
constructor(values: K[])
```

Creates a new Set instance from an array.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Set-constructor(values: K[])--><!--Device-Set-constructor(values: K[])-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| values | K[] | Yes | The array used for initialization. |

## constructor

```TypeScript
constructor(elements?: Iterable<K> | FixedArray<K> | null)
```

Creates a new Set instance from an iterable object or FixedArray.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Set-constructor(elements?: Iterable<K> | FixedArray<K> | null)--><!--Device-Set-constructor(elements?: Iterable<K> | FixedArray<K> | null)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elements | Iterable&lt;K&gt; \| FixedArray&lt;K&gt; \| null | No | The iterable object, FixedArray, or null used for initialization. |

## delete

```TypeScript
delete(val: K): boolean
```

Removes a value from the Set.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Set-delete(val: K): boolean--><!--Device-Set-delete(val: K): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | K | Yes | the value to remove. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the value was removed. |

## entries

```TypeScript
entries(): IterableIterator<[K, K]>
```

Returns an iterable of [v, v] pairs for every value in the Set.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Set-entries(): IterableIterator<[K, K]>--><!--Device-Set-entries(): IterableIterator<[K, K]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;[K, K]&gt; | an iterable of [v, v] pairs. |

## forEach

```TypeScript
forEach(callbackfn: (k: K, v: K, set: Set<K>) => void): void
```

Executes a provided function once per each value in the Set object, in insertion order.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Set-forEach(callbackfn: (k: K, v: K, set: Set<K>) => void): void--><!--Device-Set-forEach(callbackfn: (k: K, v: K, set: Set<K>) => void): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (k: K, v: K, set: Set&lt;K&gt;) =&gt; void | Yes | the function to apply. |

## has

```TypeScript
has(val: K): boolean
```

Checks if a value is in the Set.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Set-has(val: K): boolean--><!--Device-Set-has(val: K): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | K | Yes | the value to find in the Set. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the value is in the Set. |

## keys

```TypeScript
keys(): IterableIterator<K>
```

Despite name, returns elements from the Set.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Set-keys(): IterableIterator<K>--><!--Device-Set-keys(): IterableIterator<K>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;K&gt; | an iterable of the values in the Set. |

## toString

```TypeScript
toString(): string
```

Converts this Set to a String.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Set-toString(): string--><!--Device-Set-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | A string representing the Set. |

## values

```TypeScript
values(): IterableIterator<K>
```

Returns elements from the Set.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Set-values(): IterableIterator<K>--><!--Device-Set-values(): IterableIterator<K>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;K&gt; | an iterable of the values in the Set. |

