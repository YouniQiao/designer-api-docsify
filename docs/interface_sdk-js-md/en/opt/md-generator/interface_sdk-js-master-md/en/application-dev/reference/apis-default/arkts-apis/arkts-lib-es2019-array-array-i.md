# Array

## flat

```TypeScript
flat<A, D extends number = 1>(
        this: A,
        depth?: D
    ): FlatArray<A, D>[]
```

Returns a new array with all sub-array elements concatenated into it recursively up to the specified depth.

<!--Device-Array-flat<A, D extends number = 1>(        this: A,        depth?: D    ): FlatArray<A, D>[]--><!--Device-Array-flat<A, D extends number = 1>(        this: A,        depth?: D    ): FlatArray<A, D>[]-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| this | A | Yes |
| depth | D | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| FlatArray&lt;A, D&gt;[] |

## flatMap

```TypeScript
flatMap<U, This = undefined> (
        callback: (this: This, value: T, index: number, array: T[]) => U | ReadonlyArray<U>,
        thisArg?: This
    ): U[]
```

Calls a defined callback function on each element of an array. Then, flattens the result into a new array.This is identical to a map followed by flat with depth 1.

<!--Device-Array-flatMap<U, This = undefined> (        callback: (this: This, value: T, index: number, array: T[]) => U | ReadonlyArray<U>,        thisArg?: This    ): U[]--><!--Device-Array-flatMap<U, This = undefined> (        callback: (this: This, value: T, index: number, array: T[]) => U | ReadonlyArray<U>,        thisArg?: This    ): U[]-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (this: This, value: T, index: number, array: T[]) =&gt; U \| [ReadonlyArray&lt;U&gt;](../../apis-arkts/arkts-apis/arkts-arkts-readonlyarray-i.md) | Yes |
| thisArg | This | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| U[] |
