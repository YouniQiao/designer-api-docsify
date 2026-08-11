# ReadonlyArray

## find

```TypeScript
find<S extends T>(predicate: (this: void, value: T, index: number, obj: readonly T[]) => value is S, thisArg?: any): S | undefined
```

Returns the value of the first element in the array where predicate is true, and undefined otherwise.

<!--Device-ReadonlyArray-find<S extends T>(predicate: (this: void, value: T, index: number, obj: readonly T[]) => value is S, thisArg?: any): S | undefined--><!--Device-ReadonlyArray-find<S extends T>(predicate: (this: void, value: T, index: number, obj: readonly T[]) => value is S, thisArg?: any): S | undefined-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicate | (this: void, value: T, index: number, obj: readonly T[]) =&gt; value is S | Yes |
| thisArg | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| S |

## find

```TypeScript
find(predicate: (value: T, index: number, obj: readonly T[]) => unknown, thisArg?: any): T | undefined
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicate | (value: T, index: number, obj: readonly T[]) =&gt; unknown | Yes |
| thisArg | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## findIndex

```TypeScript
findIndex(predicate: (value: T, index: number, obj: readonly T[]) => unknown, thisArg?: any): number
```

Returns the index of the first element in the array where predicate is true, and -1otherwise.

<!--Device-ReadonlyArray-findIndex(predicate: (value: T, index: number, obj: readonly T[]) => unknown, thisArg?: any): number--><!--Device-ReadonlyArray-findIndex(predicate: (value: T, index: number, obj: readonly T[]) => unknown, thisArg?: any): number-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicate | (value: T, index: number, obj: readonly T[]) =&gt; unknown | Yes |
| thisArg | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |
