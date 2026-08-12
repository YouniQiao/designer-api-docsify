# ArrayConstructor

**ArkTS mode:** ArkTS-Dyn only

## from

```TypeScript
from<T>(arrayLike: ArrayLike<T>): T[]
```

Creates an array from an array-like object.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-ArrayConstructor-from<T>(arrayLike: ArrayLike<T>): T[]--><!--Device-ArrayConstructor-from<T>(arrayLike: ArrayLike<T>): T[]-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arrayLike | ArrayLike&lt;T&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| T[] |  |

## from

```TypeScript
from<T, U>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => U, thisArg?: any): U[]
```

Creates an array from an iterable object.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-ArrayConstructor-from<T, U>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => U, thisArg?: any): U[]--><!--Device-ArrayConstructor-from<T, U>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => U, thisArg?: any): U[]-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arrayLike | ArrayLike&lt;T&gt; | Yes |  |
| mapfn | (v: T, k: number) =&gt; U | Yes |  |
| thisArg | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| U[] |  |

## of

```TypeScript
of<T>(...items: T[]): T[]
```

Returns a new array from a set of elements.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-ArrayConstructor-of<T>(...items: T[]): T[]--><!--Device-ArrayConstructor-of<T>(...items: T[]): T[]-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| items | T[] | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| T[] |  |

