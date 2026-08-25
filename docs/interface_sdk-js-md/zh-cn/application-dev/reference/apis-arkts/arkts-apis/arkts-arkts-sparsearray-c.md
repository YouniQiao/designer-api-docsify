# SparseArray

SparseArray是以Map作为底层存储的稀疏数组实现。 它仅存储非undefined的值，因此对于存在大量空位的数组更节省内存。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## at

```TypeScript
at(index: int): T | undefined
```

返回指定索引处的元素。

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
| T \| undefined |

## concat

```TypeScript
concat(items: SparseArray<T>): SparseArray<T>
```

返回由当前稀疏数组与其他数组或值连接而成的新稀疏数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| items | [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; |

## constructor

```TypeScript
constructor()
```

创建新的空SparseArray实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(arrayLen: int)
```

使用指定的初始长度创建新的SparseArray实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arrayLen | int | 是 |

## constructor

```TypeScript
constructor(first: T, ...d: T[])
```

使用给定的元素创建新的SparseArray实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| first | T | 是 |
| [d](arkts-arkts-math-decimal-decimal-c.md) | T[] | 是 |

## copyWithin

```TypeScript
copyWithin(target: int, start: int, end?: int): this
```

在稀疏数组内部复制一段连续的元素。

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

## entries

```TypeScript
entries(): IterableIterator<[int, T]>
```

返回由稀疏数组中每个条目的键值对组成的可迭代对象。

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
every(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): boolean
```

判断稀疏数组中的所有元素是否都满足指定的测试条件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: int, array: SparseArray & lt;T & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## fill

```TypeScript
fill(value: T, start?: int, end?: int): this
```

将稀疏数组中从start到end索引之间的所有元素替换为固定值， 并返回修改后的稀疏数组。

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
filter(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): SparseArray<T>
```

返回稀疏数组中满足回调函数所指定条件的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: int, array: SparseArray & lt;T & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; |

## find

```TypeScript
find(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): T | undefined
```

返回稀疏数组中第一个使predicate返回true的元素的值，若不存在则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: int, array: SparseArray & lt;T & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T \| undefined |

## findIndex

```TypeScript
findIndex(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): int
```

返回稀疏数组中第一个使predicate返回true的元素的索引，若不存在则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: int, array: SparseArray & lt;T & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## findLast

```TypeScript
findLast(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): T | undefined
```

返回稀疏数组中最后一个使predicate返回true的元素的值，若不存在则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: int, array: SparseArray & lt;T & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T \| undefined |

## findLastIndex

```TypeScript
findLastIndex(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): int
```

返回稀疏数组中最后一个使predicate返回true的元素的索引，若不存在则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: int, array: SparseArray & lt;T & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## flat

```TypeScript
flat<U = T>(depth?: int): SparseArray<U>
```

返回一个新的稀疏数组，其中所有子数组元素按指定深度 递归展开后合并到该数组中。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [depth](../../apis-ability-kit/arkts-apis/arkts-ability-pagenodeinfo-i-sys.md) | int | 否 |

**返回值：**

| 类型 |
| --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;U&gt; |

## flatMap

```TypeScript
flatMap<U = T>(fn: (v: T, k: int, arr: SparseArray<T>) => U): SparseArray<U>
```

对稀疏数组中的每个元素调用指定的回调函数。 然后将结果展开为一个新的稀疏数组。 其效果等同于先调用map()，再以深度1调用flat()。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fn | (v: T, k: int, arr: SparseArray & lt;T & gt;) = & gt; U | 是 |

**返回值：**

| 类型 |
| --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;U&gt; |

## forEach

```TypeScript
forEach(callbackfn: (value: T, index: int, array: SparseArray<T>) => void): void
```

对稀疏数组中的每个元素执行指定的操作。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackfn | (value: T, index: int, array: SparseArray & lt;T & gt;) = & gt; void | 是 |

## from

```TypeScript
static from<U>(arrayLike: ArrayLike<U> | Iterable<U>): SparseArray<U>
```

根据类数组对象或可迭代对象创建新的SparseArray实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arrayLike | ArrayLike & lt;U & gt; \ | Iterable & lt;U & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;U&gt; |

## from

```TypeScript
static from<U>(arr: ArrayLike<U>): SparseArray<U>
```

根据类数组对象创建新的SparseArray实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arr | ArrayLike & lt;U & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;U&gt; |

## includes

```TypeScript
includes(searchElement: T, fromIndex?: int): boolean
```

判断稀疏数组中是否包含指定元素，并相应地返回true或false。

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
| boolean |

## indexOf

```TypeScript
indexOf(searchElement: T, fromIndex?: int): int
```

返回指定值在稀疏数组中首次出现的索引，若不存在则返回-1。

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

## isSparseArray

```TypeScript
static isSparseArray(value: Any): boolean
```

判断指定的值是否为稀疏数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Any | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## join

```TypeScript
join(separator?: string): string
```

使用指定的分隔字符串连接稀疏数组中的所有元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| separator | string | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## keys

```TypeScript
keys(): IterableIterator<int>
```

返回由稀疏数组中所有键组成的可迭代对象。

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
lastIndexOf(searchElement: T, fromIndex?: int): int
```

返回指定值在稀疏数组中最后一次出现的索引，若不存在则返回-1。

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
map<U>(callbackfn: (value: T, index: int, array: SparseArray<T>) => U): SparseArray<U>
```

对稀疏数组中的每个元素调用指定的回调函数， 并返回包含各次调用结果的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackfn | (value: T, index: int, array: SparseArray & lt;T & gt;) = & gt; U | 是 |

**返回值：**

| 类型 |
| --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;U&gt; |

## of

```TypeScript
static of<U>(...items: U[]): SparseArray<U>
```

根据可变number的参数创建新的SparseArray实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| items | U[] | 是 |

**返回值：**

| 类型 |
| --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;U&gt; |

## pop

```TypeScript
pop(): T | undefined
```

移除稀疏数组的最后一个元素并返回该元素。

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
push(...items: T[]): int
```

在稀疏数组末尾追加新元素，并返回新的长度。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| items | T[] | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## push

```TypeScript
push(val: T): int
```

在稀疏数组末尾追加新元素，并返回新的长度。

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

## reduce

```TypeScript
reduce(callbackfn: (previousValue: T, currentValue: T, index: int, array: SparseArray<T>) => T): T
```

对稀疏数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackfn | (previousValue: T, currentValue: T, index: int, array: SparseArray & lt;T & gt;) = & gt; T | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## reduce

```TypeScript
reduce<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: SparseArray<T>) => U,
        initialValue: U): U
```

对稀疏数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: T, index: int, array: SparseArray & lt;T & gt;) = & gt; U | 是 |
| initialValue | U | 是 |

**返回值：**

| 类型 |
| --- |
| U |

## reduceRight

```TypeScript
reduceRight(callbackfn: (previousValue: T, currentValue: T, index: int, array: SparseArray<T>) => T): T
```

按降序对稀疏数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackfn | (previousValue: T, currentValue: T, index: int, array: SparseArray & lt;T & gt;) = & gt; T | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## reduceRight

```TypeScript
reduceRight<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: SparseArray<T>) => U,
        initialValue: U): U
```

按降序对稀疏数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: T, index: int, array: SparseArray & lt;T & gt;) = & gt; U | 是 |
| initialValue | U | 是 |

**返回值：**

| 类型 |
| --- |
| U |

## reverse

```TypeScript
reverse(): this
```

原地反转稀疏数组中的元素，并返回该稀疏数组。

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
shift(): T | undefined
```

移除稀疏数组的第一个元素并返回该元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| T \| undefined |

## slice

```TypeScript
slice(start?: int, end?: int): SparseArray<T>
```

返回稀疏数组中某一部分的副本。

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
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; |

## some

```TypeScript
some(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): boolean
```

判断稀疏数组中是否存在使指定回调函数返回true的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: int, array: SparseArray & lt;T & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## sort

```TypeScript
sort(compareFn?: (a: T, b: T) => int): this
```

原地排序稀疏数组中的元素，并返回该稀疏数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| compareFn | (a: T, b: T) = & gt; int | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## splice

```TypeScript
splice(start: int, deleteCount: int, ...items: T[]): SparseArray<T>
```

通过移除或替换已有元素以及在原位置添加新元素， 改变稀疏数组的内容。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | int | 是 |
| deleteCount | int | 是 |
| items | T[] | 是 |

**返回值：**

| 类型 |
| --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; |

## toReversed

```TypeScript
toReversed(): SparseArray<T>
```

返回元素顺序反转后的新稀疏数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; |

## toSorted

```TypeScript
toSorted(compareFn?: (a: T, b: T) => int): SparseArray<T>
```

返回元素按升序排序后的新稀疏数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| compareFn | (a: T, b: T) = & gt; int | 否 |

**返回值：**

| 类型 |
| --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; |

## toSpliced

```TypeScript
toSpliced(start: int, deleteCount: int, ...items: T[]): SparseArray<T>
```

返回在指定索引处移除或替换部分元素后的新稀疏数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | int | 是 |
| deleteCount | int | 是 |
| items | T[] | 是 |

**返回值：**

| 类型 |
| --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; |

## toString

```TypeScript
toString(): string
```

返回表示该稀疏数组及其元素的字符串。

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
unshift(...items: T[]): int
```

在稀疏数组开头插入新元素，并返回新的长度。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| items | T[] | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## values

```TypeScript
values(): IterableIterator<T>
```

返回由稀疏数组中所有值组成的可迭代对象。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; |

## length

```TypeScript
get length(): int
```

获取稀疏数组的长度。

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang
