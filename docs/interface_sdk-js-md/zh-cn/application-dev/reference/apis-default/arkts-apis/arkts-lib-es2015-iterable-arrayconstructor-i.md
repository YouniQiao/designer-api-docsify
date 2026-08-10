# ArrayConstructor

**ArkTS模式：** 仅支持ArkTS-Dyn

## from

```TypeScript
from<T>(iterable: Iterable<T> | ArrayLike<T>): T[]
```

Creates an array from an iterable object.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ArrayConstructor-from<T>(iterable: Iterable<T> | ArrayLike<T>): T[]--><!--Device-ArrayConstructor-from<T>(iterable: Iterable<T> | ArrayLike<T>): T[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| iterable | Iterable&lt;T&gt; \| ArrayLike&lt;T&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T[] |  |

## from

```TypeScript
from<T, U>(iterable: Iterable<T> | ArrayLike<T>, mapfn: (v: T, k: number) => U, thisArg?: any): U[]
```

Creates an array from an iterable object.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ArrayConstructor-from<T, U>(iterable: Iterable<T> | ArrayLike<T>, mapfn: (v: T, k: number) => U, thisArg?: any): U[]--><!--Device-ArrayConstructor-from<T, U>(iterable: Iterable<T> | ArrayLike<T>, mapfn: (v: T, k: number) => U, thisArg?: any): U[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| iterable | Iterable&lt;T&gt; \| ArrayLike&lt;T&gt; | 是 |  |
| mapfn | (v: T, k: number) =&gt; U | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U[] |  |

