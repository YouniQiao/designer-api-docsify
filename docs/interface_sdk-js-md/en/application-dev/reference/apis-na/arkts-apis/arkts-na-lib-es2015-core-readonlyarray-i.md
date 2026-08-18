# ReadonlyArray

**Since:** -1

<!--Device-unnamed-interface ReadonlyArray--><!--Device-unnamed-interface ReadonlyArray-End-->

## Modules to Import

```TypeScript
```

## find

```TypeScript
find<S extends T>(predicate: (this: void, value: T, index: number, obj: readonly T[]) => value is S, thisArg?: any): S | undefined
```

Returns the value of the first element in the array where predicate is true, and undefined otherwise.

**Since:** -1

<!--Device-ReadonlyArray-find<S extends T>(predicate: (this: void, value: T, index: number, obj: readonly T[]) => value is S, thisArg?: any): S | undefined--><!--Device-ReadonlyArray-find<S extends T>(predicate: (this: void, value: T, index: number, obj: readonly T[]) => value is S, thisArg?: any): S | undefined-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (this: void, value: T, index: number, obj: readonly T[]) =&gt; value is S | Yes |  |
| thisArg | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| S |  |

## find

```TypeScript
find(predicate: (value: T, index: number, obj: readonly T[]) => unknown, thisArg?: any): T | undefined
```

**Since:** -1

<!--Device-ReadonlyArray-find(predicate: (value: T, index: number, obj: readonly T[]) => unknown, thisArg?: any): T | undefined--><!--Device-ReadonlyArray-find(predicate: (value: T, index: number, obj: readonly T[]) => unknown, thisArg?: any): T | undefined-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: T, index: number, obj: readonly T[]) =&gt; unknown | Yes |  |
| thisArg | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## findIndex

```TypeScript
findIndex(predicate: (value: T, index: number, obj: readonly T[]) => unknown, thisArg?: any): number
```

Returns the index of the first element in the array where predicate is true, and -1 otherwise.

**Since:** -1

<!--Device-ReadonlyArray-findIndex(predicate: (value: T, index: number, obj: readonly T[]) => unknown, thisArg?: any): number--><!--Device-ReadonlyArray-findIndex(predicate: (value: T, index: number, obj: readonly T[]) => unknown, thisArg?: any): number-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicate | (value: T, index: number, obj: readonly T[]) =&gt; unknown | Yes |  |
| thisArg | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

