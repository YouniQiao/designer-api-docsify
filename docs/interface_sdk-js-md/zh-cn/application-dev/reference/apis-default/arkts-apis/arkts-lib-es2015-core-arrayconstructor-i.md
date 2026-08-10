# ArrayConstructor

**ArkTS模式：** 仅支持ArkTS-Dyn

## from

```TypeScript
from<T>(arrayLike: ArrayLike<T>): T[]
```

Creates an array from an array-like object.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ArrayConstructor-from<T>(arrayLike: ArrayLike<T>): T[]--><!--Device-ArrayConstructor-from<T>(arrayLike: ArrayLike<T>): T[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](../../apis-arkts/arkts-apis/arkts-arkts-arraylike-i.md)&lt;T&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T[] |  |

## from

```TypeScript
from<T, U>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => U, thisArg?: any): U[]
```

Creates an array from an iterable object.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ArrayConstructor-from<T, U>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => U, thisArg?: any): U[]--><!--Device-ArrayConstructor-from<T, U>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => U, thisArg?: any): U[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](../../apis-arkts/arkts-apis/arkts-arkts-arraylike-i.md)&lt;T&gt; | 是 |  |
| mapfn | (v: T, k: number) =&gt; U | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U[] |  |

## of

```TypeScript
of<T>(...items: T[]): T[]
```

Returns a new array from a set of elements.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ArrayConstructor-of<T>(...items: T[]): T[]--><!--Device-ArrayConstructor-of<T>(...items: T[]): T[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | T[] | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T[] |  |

