# SparseArray

SparseArray是以Map作为底层存储的稀疏数组实现。 它仅存储非undefined的值，因此对于存在大量空位的数组更节省内存。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-export class SparseArray--><!--Device-unnamed-export class SparseArray-End-->

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

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-at(index: int): T | undefined--><!--Device-SparseArray-at(index: int): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 目标元素的索引，从0开始计数。 负数索引表示从稀疏数组末尾开始倒数。 如果index为负数，则按length + index处理（例如-1表示最后一个元素）。 如果index小于-length，则返回undefined。 如果index大于或等于length，则返回undefined。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T \| undefined | 指定索引处的元素；如果索引超出范围，则返回undefined。 |

## concat

```TypeScript
concat(items: SparseArray<T>): SparseArray<T>
```

返回由当前稀疏数组与其他数组或值连接而成的新稀疏数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-concat(items: SparseArray<T>): SparseArray<T>--><!--Device-SparseArray-concat(items: SparseArray<T>): SparseArray<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; | 是 | 待连接到结果中的其他数组或值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; | 新的SparseArray，其中先是当前稀疏数组的元素， 随后是传入稀疏数组的元素。 |

## constructor

```TypeScript
constructor()
```

创建新的空SparseArray实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-constructor()--><!--Device-SparseArray-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(arrayLen: int)
```

使用指定的初始长度创建新的SparseArray实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-constructor(arrayLen: int)--><!--Device-SparseArray-constructor(arrayLen: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLen | int | 是 | 稀疏数组的初始长度。如果arrayLen为负数，则按0处理。 正number的最大值为int_max。 <br>取值约束：应为整数。 |

## constructor

```TypeScript
constructor(first: T, ...d: T[])
```

使用给定的元素创建新的SparseArray实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-constructor(first: T, ...d: T[])--><!--Device-SparseArray-constructor(first: T, ...d: T[])-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| first | T | 是 | 稀疏数组的第一个元素。 |
| d | T[] | 是 | 用于初始化稀疏数组的其余元素。 |

## copyWithin

```TypeScript
copyWithin(target: int, start: int, end?: int): this
```

在稀疏数组内部复制一段连续的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-copyWithin(target: int, start: int, end?: int): this--><!--Device-SparseArray-copyWithin(target: int, start: int, end?: int): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | int | 是 | 复制目标位置的索引，从0开始计数。 <br>取值约束：应为整数。 |
| start | int | 是 | 开始复制元素位置的索引，从0开始计数。 <br>取值约束：应为整数。 |
| end | int | 否 | 停止复制元素位置的索引，从0开始计数。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | 修改后的稀疏数组。 |

## entries

```TypeScript
entries(): IterableIterator<[int, T]>
```

返回由稀疏数组中每个条目的键值对组成的可迭代对象。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-entries(): IterableIterator<[int, T]>--><!--Device-SparseArray-entries(): IterableIterator<[int, T]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[int, T]&gt; | 由稀疏数组中每个条目的键值对组成的可迭代对象。 |

## every

```TypeScript
every(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): boolean
```

判断稀疏数组中的所有元素是否都满足指定的测试条件。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-every(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): boolean--><!--Device-SparseArray-every(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; boolean | 是 | 最多接受三个参数的函数。every方法会对稀疏数组中的每个元素 调用predicate函数，直到predicate返回 可转换为Boolean值false的结果，或遍历完稀疏数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果回调函数对所有元素都返回true，则返回true， 否则返回false。 |

## fill

```TypeScript
fill(value: T, start?: int, end?: int): this
```

将稀疏数组中从start到end索引之间的所有元素替换为固定值， 并返回修改后的稀疏数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-fill(value: T, start?: int, end?: int): this--><!--Device-SparseArray-fill(value: T, start?: int, end?: int): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | 用于填充稀疏数组指定区间的值。 |
| start | int | 否 | 开始填充稀疏数组的索引，默认值为0。如果start为负数， 则按length + start处理。 <br>取值约束：应为整数。 |
| end | int | 否 | 停止填充稀疏数组的索引，默认值为0。如果end为负数， 则按length + end处理。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | 修改后的稀疏数组。 |

## filter

```TypeScript
filter(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): SparseArray<T>
```

返回稀疏数组中满足回调函数所指定条件的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-filter(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): SparseArray<T>--><!--Device-SparseArray-filter(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): SparseArray<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; boolean | 是 | 最多接受三个参数的函数。 filter方法会对稀疏数组中的每个元素调用一次predicate函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; | 包含满足条件的元素的稀疏数组。 |

## find

```TypeScript
find(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): T | undefined
```

返回稀疏数组中第一个使predicate返回true的元素的值，若不存在则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-find(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): T | undefined--><!--Device-SparseArray-find(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; boolean | 是 | 最多接受三个参数的函数。 find方法会对稀疏数组中的每个元素调用一次predicate函数。 调用一次回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T \| undefined | 稀疏数组中第一个使predicate返回true的元素的值， 若不存在则返回undefined。 |

## findIndex

```TypeScript
findIndex(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): int
```

返回稀疏数组中第一个使predicate返回true的元素的索引，若不存在则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-findIndex(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): int--><!--Device-SparseArray-findIndex(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; boolean | 是 | 最多接受三个参数的函数。 findIndex方法会对稀疏数组中的每个元素调用一次predicate函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 稀疏数组中第一个使predicate返回true的元素的索引，若不存在则返回-1。 |

## findLast

```TypeScript
findLast(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): T | undefined
```

返回稀疏数组中最后一个使predicate返回true的元素的值，若不存在则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-findLast(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): T | undefined--><!--Device-SparseArray-findLast(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; boolean | 是 | 最多接受三个参数的函数。findLast方法会按降序对稀疏数组中的 每个元素调用一次predicate函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T \| undefined | 稀疏数组中最后一个使predicate返回true的元素的值， 若不存在则返回undefined。 |

## findLastIndex

```TypeScript
findLastIndex(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): int
```

返回稀疏数组中最后一个使predicate返回true的元素的索引，若不存在则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-findLastIndex(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): int--><!--Device-SparseArray-findLastIndex(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; boolean | 是 | 最多接受三个参数的函数。findLastIndex方法会按降序对稀疏数组中的 每个元素调用一次predicate函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 稀疏数组中最后一个使predicate返回true的元素的索引，若不存在则返回-1。 |

## flat

```TypeScript
flat<U = T>(depth?: int): SparseArray<U>
```

返回一个新的稀疏数组，其中所有子数组元素按指定深度 递归展开后合并到该数组中。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-flat<U = T>(depth?: int): SparseArray<U>--><!--Device-SparseArray-flat<U = T>(depth?: int): SparseArray<U>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| depth | int | 否 | 指定嵌套数组结构展开的深度级别， 默认值为1。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;U&gt; | SparseArray |

## flatMap

```TypeScript
flatMap<U = T>(fn: (v: T, k: int, arr: SparseArray<T>) => U): SparseArray<U>
```

对稀疏数组中的每个元素调用指定的回调函数。 然后将结果展开为一个新的稀疏数组。 其效果等同于先调用map()，再以深度1调用flat()。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-flatMap<U = T>(fn: (v: T, k: int, arr: SparseArray<T>) => U): SparseArray<U>--><!--Device-SparseArray-flatMap<U = T>(fn: (v: T, k: int, arr: SparseArray<T>) => U): SparseArray<U>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (v: T, k: int, arr: SparseArray&lt;T&gt;) =&gt; U | 是 | 用于生成新SparseArray元素的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;U&gt; | 新的稀疏数组，其中每个元素都是回调函数的返回结果， 并已完成展开。 |

## forEach

```TypeScript
forEach(callbackfn: (value: T, index: int, array: SparseArray<T>) => void): void
```

对稀疏数组中的每个元素执行指定的操作。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-forEach(callbackfn: (value: T, index: int, array: SparseArray<T>) => void): void--><!--Device-SparseArray-forEach(callbackfn: (value: T, index: int, array: SparseArray<T>) => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; void | 是 | 最多接受三个参数的函数。forEach会对稀疏数组中的每个元素 调用一次回调函数。 |

## from

```TypeScript
static from<U>(arrayLike: ArrayLike<U> | Iterable<U>): SparseArray<U>
```

根据类数组对象或可迭代对象创建新的SparseArray实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-static from<U>(arrayLike: ArrayLike<U> | Iterable<U>): SparseArray<U>--><!--Device-SparseArray-static from<U>(arrayLike: ArrayLike<U> | Iterable<U>): SparseArray<U>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;U&gt; \| Iterable&lt;U&gt; | 是 | 待转换为稀疏数组的类数组对象或可迭代对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;U&gt; | 新的SparseArray实例。 |

## from

```TypeScript
static from<U>(arr: ArrayLike<U>): SparseArray<U>
```

根据类数组对象创建新的SparseArray实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-static from<U>(arr: ArrayLike<U>): SparseArray<U>--><!--Device-SparseArray-static from<U>(arr: ArrayLike<U>): SparseArray<U>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;U&gt; | 是 | 待转换为稀疏数组的类数组对象或可迭代对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;U&gt; | 新的SparseArray实例。 |

## includes

```TypeScript
includes(searchElement: T, fromIndex?: int): boolean
```

判断稀疏数组中是否包含指定元素，并相应地返回true或false。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-includes(searchElement: T, fromIndex?: int): boolean--><!--Device-SparseArray-includes(searchElement: T, fromIndex?: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | T | 是 | 待查找的元素。 |
| fromIndex | int | 否 | 开始查找searchElement的稀疏数组位置。 默认值为0，即查找整个数组。 如果fromIndex为负数，则将其作为相对于数组末尾的偏移量。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果找到searchElement则返回true，否则返回false。 |

## indexOf

```TypeScript
indexOf(searchElement: T, fromIndex?: int): int
```

返回指定值在稀疏数组中首次出现的索引，若不存在则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-indexOf(searchElement: T, fromIndex?: int): int--><!--Device-SparseArray-indexOf(searchElement: T, fromIndex?: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | T | 是 | 待在稀疏数组中查找的值。 |
| fromIndex | int | 否 | 开始查找的稀疏数组索引。 如果不传入fromIndex，则从索引0开始查找。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 该值在稀疏数组中首次出现的索引，未找到时返回-1。 |

## isSparseArray

```TypeScript
static isSparseArray(value: Any): boolean
```

判断指定的值是否为稀疏数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-static isSparseArray(value: Any): boolean--><!--Device-SparseArray-static isSparseArray(value: Any): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Any | 是 | 待检测的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该值是稀疏数组则返回true，否则返回false。 |

## join

```TypeScript
join(separator?: string): string
```

使用指定的分隔字符串连接稀疏数组中的所有元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-join(separator?: string): string--><!--Device-SparseArray-join(separator?: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| separator | string | 否 | 用于在结果字符串中分隔稀疏数组相邻元素的 字符串，默认值为“,”（逗号）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 由所有稀疏数组元素连接而成的字符串。 |

## keys

```TypeScript
keys(): IterableIterator<int>
```

返回由稀疏数组中所有键组成的可迭代对象。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-keys(): IterableIterator<int>--><!--Device-SparseArray-keys(): IterableIterator<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;int&gt; | 由稀疏数组中所有键组成的可迭代对象。 |

## lastIndexOf

```TypeScript
lastIndexOf(searchElement: T, fromIndex?: int): int
```

返回指定值在稀疏数组中最后一次出现的索引，若不存在则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-lastIndexOf(searchElement: T, fromIndex?: int): int--><!--Device-SparseArray-lastIndexOf(searchElement: T, fromIndex?: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | T | 是 | 待在稀疏数组中查找的值。 |
| fromIndex | int | 否 | 开始反向查找的稀疏数组索引。 如果不传入fromIndex，则从最后一个索引开始查找。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 该值在稀疏数组中最后一次出现的索引，未找到时返回-1。 |

## map

```TypeScript
map<U>(callbackfn: (value: T, index: int, array: SparseArray<T>) => U): SparseArray<U>
```

对稀疏数组中的每个元素调用指定的回调函数， 并返回包含各次调用结果的数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-map<U>(callbackfn: (value: T, index: int, array: SparseArray<T>) => U): SparseArray<U>--><!--Device-SparseArray-map<U>(callbackfn: (value: T, index: int, array: SparseArray<T>) => U): SparseArray<U>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; U | 是 | 最多接受三个参数的函数。 map方法会对稀疏数组中的每个元素调用一次callbackfn函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;U&gt; |  |

## of

```TypeScript
static of<U>(...items: U[]): SparseArray<U>
```

根据可变number的参数创建新的SparseArray实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-static of<U>(...items: U[]): SparseArray<U>--><!--Device-SparseArray-static of<U>(...items: U[]): SparseArray<U>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | U[] | 是 | 待包含在新SparseArray实例中的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;U&gt; | 包含指定元素的新SparseArray实例。 |

## pop

```TypeScript
pop(): T | undefined
```

移除稀疏数组的最后一个元素并返回该元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-pop(): T | undefined--><!--Device-SparseArray-pop(): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T \| undefined | 稀疏数组的最后一个元素；如果稀疏数组为空，则返回undefined。 |

## push

```TypeScript
push(...items: T[]): int
```

在稀疏数组末尾追加新元素，并返回新的长度。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-push(...items: T[]): int--><!--Device-SparseArray-push(...items: T[]): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | T[] | 是 | 待添加到稀疏数组末尾的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 稀疏数组的新长度。 |

## push

```TypeScript
push(val: T): int
```

在稀疏数组末尾追加新元素，并返回新的长度。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-push(val: T): int--><!--Device-SparseArray-push(val: T): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | T | 是 | 待添加到稀疏数组末尾的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 稀疏数组的新长度。 |

## reduce

```TypeScript
reduce(callbackfn: (previousValue: T, currentValue: T, index: int, array: SparseArray<T>) => T): T
```

对稀疏数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-reduce(callbackfn: (previousValue: T, currentValue: T, index: int, array: SparseArray<T>) => T): T--><!--Device-SparseArray-reduce(callbackfn: (previousValue: T, currentValue: T, index: int, array: SparseArray<T>) => T): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: T, currentValue: T, index: int, array: SparseArray&lt;T&gt;) =&gt; T | 是 | 最多接受四个参数的函数。 reduce方法会对稀疏数组中的每个元素调用一次callbackfn函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 累加得到的结果。 |

## reduce

```TypeScript
reduce<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: SparseArray<T>) => U,
        initialValue: U): U
```

对稀疏数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-reduce<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: SparseArray<T>) => U,        initialValue: U): U--><!--Device-SparseArray-reduce<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: SparseArray<T>) => U,        initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: T, index: int, array: SparseArray&lt;T&gt;) =&gt; U | 是 | 最多接受四个参数的函数。reduce方法会对稀疏数组中的每个元素 调用一次callbackfn函数。 |
| initialValue | U | 是 | 如果指定了initialValue， 则将其作为累加的初始值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | 累加得到的结果。 |

## reduceRight

```TypeScript
reduceRight(callbackfn: (previousValue: T, currentValue: T, index: int, array: SparseArray<T>) => T): T
```

按降序对稀疏数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-reduceRight(callbackfn: (previousValue: T, currentValue: T, index: int, array: SparseArray<T>) => T): T--><!--Device-SparseArray-reduceRight(callbackfn: (previousValue: T, currentValue: T, index: int, array: SparseArray<T>) => T): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: T, currentValue: T, index: int, array: SparseArray&lt;T&gt;) =&gt; T | 是 | 最多接受四个参数的函数。reduceRight方法会按降序对稀疏数组中的 每个元素调用一次callbackfn函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 累加得到的结果。 |

## reduceRight

```TypeScript
reduceRight<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: SparseArray<T>) => U,
        initialValue: U): U
```

按降序对稀疏数组中的所有元素调用指定的回调函数。 回调函数的返回值即为累加结果。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-reduceRight<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: SparseArray<T>) => U,        initialValue: U): U--><!--Device-SparseArray-reduceRight<U = T>(callbackfn: (previousValue: U, currentValue: T, index: int, array: SparseArray<T>) => U,        initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (previousValue: U, currentValue: T, index: int, array: SparseArray&lt;T&gt;) =&gt; U | 是 | 最多接受四个参数的函数。reduceRight方法会按降序对稀疏数组中的 每个元素调用一次callbackfn函数。 |
| initialValue | U | 是 | 如果指定了initialValue，则将其作为累加的初始值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U |  |

## reverse

```TypeScript
reverse(): this
```

原地反转稀疏数组中的元素，并返回该稀疏数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-reverse(): this--><!--Device-SparseArray-reverse(): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | 反转后的稀疏数组。 |

## shift

```TypeScript
shift(): T | undefined
```

移除稀疏数组的第一个元素并返回该元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-shift(): T | undefined--><!--Device-SparseArray-shift(): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T \| undefined | 稀疏数组的第一个元素；如果稀疏数组为空，则返回undefined。 |

## slice

```TypeScript
slice(start?: int, end?: int): SparseArray<T>
```

返回稀疏数组中某一部分的副本。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-slice(start?: int, end?: int): SparseArray<T>--><!--Device-SparseArray-slice(start?: int, end?: int): SparseArray<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | int | 否 | 稀疏数组中指定部分的起始索引。 默认值为0，即查找整个数组。 如果fromIndex为负数，则将其作为相对于数组末尾的偏移量。 <br>取值约束：应为整数。 |
| end | int | 否 | 稀疏数组中指定部分的结束索引。 默认值为0，即查找整个数组。 如果fromIndex为负数，则将其作为相对于数组末尾的偏移量。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; | 包含所提取元素的新SparseArray对象。 |

## some

```TypeScript
some(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): boolean
```

判断稀疏数组中是否存在使指定回调函数返回true的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-some(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): boolean--><!--Device-SparseArray-some(predicate: (value: T, index: int, array: SparseArray<T>) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: SparseArray&lt;T&gt;) =&gt; boolean | 是 | 最多接受三个参数的函数。 some方法会对稀疏数组中的每个元素调用predicate函数， 直到predicate返回可转换为Boolean值true的结果，或遍历完稀疏数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果回调函数对任一元素返回true，则返回true， 否则返回false。 |

## sort

```TypeScript
sort(compareFn?: (a: T, b: T) => int): this
```

原地排序稀疏数组中的元素，并返回该稀疏数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-sort(compareFn?: (a: T, b: T) => int): this--><!--Device-SparseArray-sort(compareFn?: (a: T, b: T) => int): this-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| compareFn | (a: T, b: T) =&gt; int | 否 | 用于确定元素顺序的函数。 如果不传入该参数，则将元素转换为字符串后，按其UTF-16码元 升序排序（默认排序行为）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | 排序后的稀疏数组。 |

## splice

```TypeScript
splice(start: int, deleteCount: int, ...items: T[]): SparseArray<T>
```

通过移除或替换已有元素以及在原位置添加新元素， 改变稀疏数组的内容。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-splice(start: int, deleteCount: int, ...items: T[]): SparseArray<T>--><!--Device-SparseArray-splice(start: int, deleteCount: int, ...items: T[]): SparseArray<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | int | 是 | 开始移除元素的位置，从0开始计数。 如果start为负数，则按length + start处理（例如-1表示最后一个元素）。 如果start小于-length，则按0处理。 如果start大于或等于length，则不移除任何元素，新元素被添加到末尾。 <br>取值约束：应为整数。 |
| deleteCount | int | 是 | 待移除元素的number。 如果deleteCount为负数，则按0处理，即不移除任何元素。 如果deleteCount大于从start到数组末尾的元素number， 则仅移除实际存在的元素。 <br>取值约束：应为整数。 |
| items | T[] | 是 | 用于替换被删除元素而插入稀疏数组的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; | 包含被删除元素的稀疏数组。 |

## toReversed

```TypeScript
toReversed(): SparseArray<T>
```

返回元素顺序反转后的新稀疏数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-toReversed(): SparseArray<T>--><!--Device-SparseArray-toReversed(): SparseArray<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; | 元素顺序反转后的新稀疏数组。 |

## toSorted

```TypeScript
toSorted(compareFn?: (a: T, b: T) => int): SparseArray<T>
```

返回元素按升序排序后的新稀疏数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-toSorted(compareFn?: (a: T, b: T) => int): SparseArray<T>--><!--Device-SparseArray-toSorted(compareFn?: (a: T, b: T) => int): SparseArray<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| compareFn | (a: T, b: T) =&gt; int | 否 | 用于确定元素顺序的函数。 如果不传入该参数，则将元素转换为字符串后，按其UTF-16码元 升序排序（默认排序行为）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; |  |

## toSpliced

```TypeScript
toSpliced(start: int, deleteCount: int, ...items: T[]): SparseArray<T>
```

返回在指定索引处移除或替换部分元素后的新稀疏数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-toSpliced(start: int, deleteCount: int, ...items: T[]): SparseArray<T>--><!--Device-SparseArray-toSpliced(start: int, deleteCount: int, ...items: T[]): SparseArray<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | int | 是 | 开始移除元素的位置，从0开始计数。 如果start为负数，则按length + start处理（例如-1表示最后一个元素）。 如果start小于-length，则按0处理。 如果start大于或等于length，则不移除任何元素，新元素被添加到末尾。 如果start不是整数，则向零取整。 <br>取值约束：应为整数。 |
| deleteCount | int | 是 | 待移除元素的number。 如果deleteCount为负数，则按0处理，即不移除任何元素。 如果deleteCount大于从start到数组末尾的元素number， 则仅移除实际存在的元素。 如果deleteCount不是整数，则向零取整。 <br>取值约束：应为整数。 |
| items | T[] | 是 | 用于替换被删除元素而插入稀疏数组的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SparseArray](arkts-arkts-sparsearray-c.md)&lt;T&gt; | 移除或替换指定元素后的新稀疏数组。 |

## toString

```TypeScript
toString(): string
```

返回表示该稀疏数组及其元素的字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-toString(): string--><!--Device-SparseArray-toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 以逗号分隔稀疏数组元素所形成的字符串。 |

## unshift

```TypeScript
unshift(...items: T[]): int
```

在稀疏数组开头插入新元素，并返回新的长度。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-unshift(...items: T[]): int--><!--Device-SparseArray-unshift(...items: T[]): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | T[] | 是 | 待插入稀疏数组开头的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 稀疏数组的新长度。 |

## values

```TypeScript
values(): IterableIterator<T>
```

返回由稀疏数组中所有值组成的可迭代对象。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SparseArray-values(): IterableIterator<T>--><!--Device-SparseArray-values(): IterableIterator<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | 由稀疏数组中所有值组成的可迭代对象。 |

