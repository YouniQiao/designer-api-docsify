# ArrayConstructor

## from

```TypeScript
from<T>(arrayLike: ArrayLike<T>): T[]
```

Creates an array from an array-like object.

<!--Device-ArrayConstructor-from<T>(arrayLike: ArrayLike<T>): T[]--><!--Device-ArrayConstructor-from<T>(arrayLike: ArrayLike<T>): T[]-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | [ArrayLike](arkts-lib-es5-arraylike-i.md)&lt;T&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T[] |

## from

```TypeScript
from<T, U>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => U, thisArg?: any): U[]
```

Creates an array from an iterable object.

<!--Device-ArrayConstructor-from<T, U>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => U, thisArg?: any): U[]--><!--Device-ArrayConstructor-from<T, U>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => U, thisArg?: any): U[]-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | [ArrayLike](arkts-lib-es5-arraylike-i.md)&lt;T&gt; | Yes |
| mapfn | (v: T, k: number) = & gt; U | Yes |
| thisArg | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| U[] |

## of

```TypeScript
of<T>(...items: T[]): T[]
```

Returns a new array from a set of elements.

<!--Device-ArrayConstructor-of<T>(...items: T[]): T[]--><!--Device-ArrayConstructor-of<T>(...items: T[]): T[]-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| items | T[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T[] |
