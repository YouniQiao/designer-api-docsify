# ArrayConstructor

**Since:** -1

<!--Device-unnamed-interface ArrayConstructor--><!--Device-unnamed-interface ArrayConstructor-End-->

## Modules to Import

```TypeScript
```

## from

```TypeScript
from<T>(iterable: Iterable<T> | ArrayLike<T>): T[]
```

Creates an array from an iterable object.

**Since:** -1

<!--Device-ArrayConstructor-from<T>(iterable: Iterable<T> | ArrayLike<T>): T[]--><!--Device-ArrayConstructor-from<T>(iterable: Iterable<T> | ArrayLike<T>): T[]-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| iterable | Iterable & lt;T & gt; \ | [ArrayLike](arkts-na-lib-es5-arraylike-i.md)&lt;T&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T[] |

## from

```TypeScript
from<T, U>(iterable: Iterable<T> | ArrayLike<T>, mapfn: (v: T, k: number) => U, thisArg?: any): U[]
```

Creates an array from an iterable object.

**Since:** -1

<!--Device-ArrayConstructor-from<T, U>(iterable: Iterable<T> | ArrayLike<T>, mapfn: (v: T, k: number) => U, thisArg?: any): U[]--><!--Device-ArrayConstructor-from<T, U>(iterable: Iterable<T> | ArrayLike<T>, mapfn: (v: T, k: number) => U, thisArg?: any): U[]-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| iterable | Iterable & lt;T & gt; \ | [ArrayLike](arkts-na-lib-es5-arraylike-i.md)&lt;T&gt; | Yes |
| mapfn | (v: T, k: number) = & gt; U | Yes |
| thisArg | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| U[] |
