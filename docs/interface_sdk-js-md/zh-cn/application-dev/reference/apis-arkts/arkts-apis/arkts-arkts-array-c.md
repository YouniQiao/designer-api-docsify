# Array

表示与JS API兼容的数组。

**继承/实现关系：** Array implements ReadonlyArray<T>, Iterable<T>

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_get

```TypeScript
$_get(idx: int): T
```

获取指定索引处的元素。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| idx | int | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## $_invoke

```TypeScript
static $_invoke<T>(...items: T[]): Array<T>
```

使用给定的元素创建一个Array实例。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| items | T[] | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

## $_iterator

```TypeScript
$_iterator(): IterableIterator<T>
```

返回遍历所有值的迭代器。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; |

## $_set

```TypeScript
$_set(idx: int, val: T): void
```

设置指定索引处的元素。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| idx | int | 是 |
| val | T | 是 |

## at

```TypeScript
public at(index: int): T
```

接受一个整数值并返回该索引处的元素，支持正整数和负整数。 负整数表示从数组的最后一个元素开始向前计数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## concat

```TypeScript
public concat(...items: FixedArray<ConcatArray<T>>): Array<T>
```

将当前`Array`实例与给定的数组和/或值合并，创建一个新的`Array`。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| items | FixedArray & lt;ConcatArray & lt;T & gt; & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

## constructor

```TypeScript
public constructor()
```

创建一个空的Array实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(first: T, ...d: T[])
```

使用给定的元素创建一个Array实例。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| first | T | 是 |
| [d](arkts-arkts-math-decimal-decimal-c.md) | T[] | 是 |

## constructor

```TypeScript
constructor(arrayLen: int, initializer: (index: int) => T)
```

创建一个指定长度的Array实例，并使用函数初始化每个元素。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arrayLen | int | 是 |
| initializer | (index: int) = & gt; T | 是 |

## copyWithin

```TypeScript
public copyWithin(target: int): this
```

将数组的一部分浅拷贝到同一数组的另一位置并返回该数组， 不改变其长度。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | int | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## copyWithin

```TypeScript
public copyWithin(target: int, start: int): this
```

将数组的一部分浅拷贝到同一数组的另一位置并返回该数组， 不改变其长度。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | int | 是 |
| start | int | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## copyWithin

```TypeScript
public copyWithin(target: int, start: int, end?: int): this
```

将数组的一部分浅拷贝到同一数组的另一位置并返回该数组， 不改变其长度。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | int | 是 |
| start | int | 是 |
| end | int | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## create

```TypeScript
public static create<T>(arrayLength: int, initialValue: T): Array<T>
```

创建一个指定长度的数组，并使用指定的初始值填充。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arrayLength | int | 是 |
| initialValue | T | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

## entries

```TypeScript
public entries(): IterableIterator<[int, T]>
```

返回一个新的数组迭代器对象，其中包含数组每个索引的键值对。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[int, T]&gt; |

## every

```TypeScript
public every(predicate: (value: T, index: int, array: Array<T>) => boolean): boolean
```

判断数组中的所有元素是否都满足指定的测试条件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: int, array: Array & lt;T & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## extendTo

```TypeScript
public extendTo(arrayLength: int, initialValue: T): void
```

使用新元素将数组扩展到指定长度。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arrayLength | int | 是 |
| initialValue | T | 是 |

## fill

```TypeScript
public fill(value: T, start?: int, end?: int): this
```

将数组中从start索引到end索引的所有元素修改为固定值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | T | 是 |
| start | int | 否 |
| end | int | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## filter

```TypeScript
public filter(predicate: (value: T, index: int, array: Array<T>) => boolean): Array<T>
```

返回数组中满足回调函数指定条件的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: int, array: Array & lt;T & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

## find

```TypeScript
public find(predicate: (value: T, index: int, array: Array<T>) => boolean): T | undefined
```

遍历数组，返回满足给定测试函数的第一个元素的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: int, array: Array & lt;T & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T \| undefined |

## findIndex

```TypeScript
public findIndex(predicate: (value: T, index: int, array: Array<T>) => boolean): int
```

返回数组中第一个使predicate为true的元素的索引，如果不存在则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: int, array: Array & lt;T & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## findLast

```TypeScript
public findLast(predicate: (elem: T, index: int, array: Array<T>) => boolean): T | undefined
```

按逆序遍历数组，返回满足给定测试函数的 第一个元素的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (elem: T, index: int, array: Array & lt;T & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T \| undefined |

## findLastIndex

```TypeScript
public findLastIndex(predicate: (element: T, index: int, array: Array<T>) => boolean): int
```

按逆序遍历数组，返回满足给定测试函数的第一个元素的索引。 如果没有元素满足测试函数，则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (element: T, index: int, array: Array & lt;T & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## flat

```TypeScript
public flat<U = T>(depth: int): Array<U>
```

创建一个新数组，将所有子数组元素按指定深度递归拼接到其中。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [depth](../../apis-ability-kit/arkts-apis/arkts-ability-pagenodeinfo-i-sys.md) | int | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;U & gt; |

## flat

```TypeScript
public flat<U = T>(): Array<U>
```

创建一个新数组，将所有子数组元素按默认深度1递归拼接到其中。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Array & lt;U & gt; |

## flatMap

```TypeScript
public flatMap<U=T>(fn: (v: T, k: int, arr: Array<T>) => U | ReadonlyArray<U>): Array<U>
```

对数组的每个元素调用指定的回调函数，然后将结果展平到一个新数组中。 等价于先调用map()，再调用深度为1的flat()。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fn | (v: T, k: int, arr: Array & lt;T & gt;) = & gt; U \ | ReadonlyArray & lt;U & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;U & gt; |

## forEach

```TypeScript
forEach(callbackfn: (value: T, index: int, array: Array<T>) => void): void
```

对数组中的每个元素执行指定的操作。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackfn | (value: T, index: int, array: Array & lt;T & gt;) = & gt; void | 是 |

## from

```TypeScript
static from<T>(arr: FixedArray<T>): Array<T>
```

根据`FixedArray`创建一个新的`Array`实例。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arr | FixedArray & lt;T & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

## from

```TypeScript
static from<T>(arr: ArrayLike<T>): Array<T>
```

根据`ArrayLike`对象创建一个新的`Array`实例。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arr | ArrayLike & lt;T & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

## from

```TypeScript
static from<T>(iterable: ArrayLike<T> | Iterable<T>): Array<T>
```

根据可迭代对象或类数组对象创建一个新的`Array`实例。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| iterable | ArrayLike & lt;T & gt; \ | Iterable & lt;T & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

## from

```TypeScript
static from<T, U>(values: FixedArray<T>, mapfn: (v: T, k: int) => U): Array<U>
```

根据`FixedArray`创建一个新的`Array`实例，并对每个元素应用映射函数。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [values](#values) | FixedArray & lt;T & gt; | 是 |
| mapfn | (v: T, k: int) = & gt; U | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;U & gt; |

## from

```TypeScript
static from<T, U>(iterable: ArrayLike<T> | Iterable<T>, mapfn: (v: T, k: int) => U): Array<U>
```

根据可迭代对象创建一个新的`Array`实例，并对每个元素应用映射函数。 每个待添加到数组的值都会先经过该函数处理，最终添加到数组中的是`mapfn`的返回值， 而不是原始值。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| iterable | ArrayLike & lt;T & gt; \ | Iterable & lt;T & gt; | 是 |
| mapfn | (v: T, k: int) = & gt; U | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;U & gt; |

## includes

```TypeScript
public includes(val: T, fromIndex?: int): boolean
```

判断数组的元素中是否包含某个值，并相应地返回true或false。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | T | 是 |
| fromIndex | int | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |

## indexOf

```TypeScript
public indexOf(val: T): int
```

返回给定元素在数组中首次出现的索引，如果不存在则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | T | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## indexOf

```TypeScript
public indexOf(val: T, fromIndex?: int): int
```

返回给定元素在数组中首次出现的索引，如果不存在则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | T | 是 |
| fromIndex | int | 否 |

**返回值：**

| 类型 |
| --- |
| int |

## isArray

```TypeScript
static isArray(o: Any): boolean
```

检查传入的值是否为数组。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| o | Any | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## join

```TypeScript
public join(sep?: string): string
```

使用指定的分隔符字符串连接`Array`中的所有元素， 创建并返回一个新字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sep | string | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## keys

```TypeScript
public keys(): IterableIterator<int>
```

返回一个新的数组迭代器对象，其中包含数组每个索引的键。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;int&gt; |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: T): int
```

返回给定元素在数组中最后一次出现的索引，如果不存在则返回-1。 数组按逆序进行搜索。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchElement | T | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## lastIndexOf

```TypeScript
public lastIndexOf(searchElement: T, fromIndex?: int): int
```

返回给定元素在数组中最后一次出现的索引，如果不存在则返回-1。 数组从fromIndex开始按逆序进行搜索。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchElement | T | 是 |
| fromIndex | int | 否 |

**返回值：**

| 类型 |
| --- |
| int |

## map

```TypeScript
public map<U>(callbackfn: (value: T, index: int, array: Array<T>) => U): Array<U>
```

创建一个新数组，其元素为对原数组每个元素调用给定函数后的 返回结果。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackfn | (value: T, index: int, array: Array & lt;T & gt;) = & gt; U | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;U & gt; |

## pop

```TypeScript
public pop(): T | undefined
```

从数组中删除最后一个元素并返回该元素。该方法会改变数组的长度。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| T \| undefined |

## push

```TypeScript
public push(...val: T[]): int
```

将指定元素添加到数组末尾，并返回数组的新长度。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | T[] | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## reduce

```TypeScript
public reduce(callbackfn: (previousValue: T, currentValue: T, index: int, array: Array<T>) => T): T
```

对数组中所有元素调用指定的回调函数。回调函数的返回值为 累加结果，并作为参数传入下一次回调函数的调用。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackfn | (previousValue: T, currentValue: T, index: int, array: Array & lt;T & gt;) = & gt; T | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## reduce

```TypeScript
public reduce<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: Array<T>) => U,
                         initialValue: U): U
```

对数组中所有元素调用指定的回调函数。回调函数的返回值为 累加结果，并作为参数传入下一次回调函数的调用。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: T, index: int, array: Array & lt;T & gt;) = & gt; U | 是 |
| initialValue | U | 是 |

**返回值：**

| 类型 |
| --- |
| U |

## reduceRight

```TypeScript
public reduceRight<U>(callbackfn: (previousValue: U, currentValue: T, index: int, array: Array<T>) => U,
                          initialValue: U): U
```

按逆序对数组中所有元素调用指定的回调函数。 回调函数的返回值为累加结果，并作为参数传入下一次回调 函数的调用。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: T, index: int, array: Array & lt;T & gt;) = & gt; U | 是 |
| initialValue | U | 是 |

**返回值：**

| 类型 |
| --- |
| U |

## reduceRight

```TypeScript
public reduceRight(callbackfn: (previousValue: T, currentValue: T, index: int, array: Array<T>) => T): T
```

按逆序对数组中所有元素调用指定的回调函数。 回调函数的返回值为累加结果，并作为参数传入下一次回调 函数的调用。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackfn | (previousValue: T, currentValue: T, index: int, array: Array & lt;T & gt;) = & gt; T | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## reverse

```TypeScript
public reverse(): this
```

原地反转数组。数组的第一个元素变为最后一个元素，最后一个元素变为 第一个元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| this |

## shift

```TypeScript
public shift(): T | undefined
```

从数组中删除第一个元素，并返回被删除的元素。 该方法会改变数组的长度。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| T \| undefined |

## shrinkTo

```TypeScript
public shrinkTo(arrayLength: int): void
```

将数组收缩到指定长度，超出新长度的元素将被删除。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arrayLength | int | 是 |

## slice

```TypeScript
public slice(start: int): Array<T>
```

返回数组中某一部分的副本。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | int | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

## slice

```TypeScript
public slice(start?: int, end?: int): Array<T>
```

返回数组中某一部分的副本。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | int | 否 |
| end | int | 否 |

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

## some

```TypeScript
public some(predicate: (value: T, index: int, array: Array<T>) => boolean): boolean
```

判断数组中是否存在任一元素使指定的回调函数返回true。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: int, array: Array & lt;T & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## sort

```TypeScript
public sort(comparator?: (a: T, b: T) => int): this
```

对数组元素进行原地排序，并返回排序后同一数组的引用。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| comparator | (a: T, b: T) = & gt; int | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## splice

```TypeScript
public splice(start: int, del: int | undefined, ...items: T[]): Array<T>
```

通过原地删除、替换已有元素或添加新元素来修改数组内容。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | int | 是 |
| del | int \| undefined | 是 |
| items | T[] | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

## splice

```TypeScript
public splice(start: int): Array<T>
```

通过原地删除从start索引到末尾的已有元素来修改数组内容。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | int | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

返回表示数组元素的字符串。元素通过各自的 toLocaleString方法转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locales | Intl.LocalesArgument | 否 |
| options | object | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## toReversed

```TypeScript
public toReversed(): Array<T>
```

返回一个元素顺序反转后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

## toSorted

```TypeScript
public toSorted(): Array<T>
```

按升序排序，返回包含这些元素的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

## toSorted

```TypeScript
public toSorted(comparator: (a: T, b: T) => int): Array<T>
```

返回一个使用给定比较函数排序后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| comparator | (a: T, b: T) = & gt; int | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

## toSpliced

```TypeScript
public toSpliced(start: int): Array<T>
```

返回一个在指定索引处删除和/或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | int | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

## toSpliced

```TypeScript
public toSpliced(start: int, del: int, ...items: FixedArray<T>): Array<T>
```

返回一个在指定索引处删除和/或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | int | 是 |
| del | int | 是 |
| items | FixedArray & lt;T & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

## toSpliced

```TypeScript
public toSpliced(start?: int, del?: int): Array<T>
```

返回一个在指定索引处删除和/或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | int | 否 |
| del | int | 否 |

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

## toString

```TypeScript
public toString(): string
```

返回表示指定数组及其元素的字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## unshift

```TypeScript
public unshift(...values: T[]): int
```

将指定元素添加到数组开头，并返回数组的新长度。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [values](#values) | T[] | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## values

```TypeScript
public values(): IterableIterator<T>
```

返回一个新的数组迭代器对象，其中包含数组每个索引的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; |

## with

```TypeScript
public with(index: int, value: T): Array<T>
```

返回一个将给定索引处的元素替换为给定值后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| value | T | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

## length

```TypeScript
set length(newLen: int)
```

设置数组的长度。

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang
