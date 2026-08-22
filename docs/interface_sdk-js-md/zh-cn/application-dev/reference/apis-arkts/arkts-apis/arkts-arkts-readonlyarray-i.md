# ReadonlyArray

只读数组，提供读取元素的方法。

**继承/实现关系：** ReadonlyArray extends ConcatArray<T>

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-export interface ReadonlyArray--><!--Device-unnamed-export interface ReadonlyArray-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## concat

```TypeScript
concat(...items: FixedArray<ConcatArray<T>>): Array<T>
```

合并两个或多个数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-concat(...items: FixedArray<ConcatArray<T>>): Array<T>--><!--Device-ReadonlyArray-concat(...items: FixedArray<ConcatArray<T>>): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | FixedArray&lt;ConcatArray&lt;T&gt;&gt; | 是 | 待合并的数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | 合并后的新数组。 |

## entries

```TypeScript
entries(): IterableIterator<[int, T]>
```

返回一个新的迭代器对象，其中包含数组中每个索引对应的键值对。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-entries(): IterableIterator<[int, T]>--><!--Device-ReadonlyArray-entries(): IterableIterator<[int, T]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[int, T]&gt; | 新的迭代器对象。 |

## every

```TypeScript
every(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): boolean
```

检测数组中的所有元素是否都通过指定函数实现的测试。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-every(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): boolean--><!--Device-ReadonlyArray-every(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: ReadonlyArray&lt;T&gt;) =&gt; boolean | 是 | 用于测试每个元素的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果所有元素都通过测试则返回true，否则返回false。 |

## filter

```TypeScript
filter(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): Array<T>
```

创建一个新数组，其中包含所有通过指定函数实现的测试的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-filter(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): Array<T>--><!--Device-ReadonlyArray-filter(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: ReadonlyArray&lt;T&gt;) =&gt; boolean | 是 | 用于测试每个元素的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | 由通过测试的元素组成的新数组。 |

## find

```TypeScript
find(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): T | undefined
```

返回数组中第一个满足指定测试函数的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-find(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): T | undefined--><!--Device-ReadonlyArray-find(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, obj: ReadonlyArray&lt;T&gt;) =&gt; boolean | 是 | 用于测试每个元素的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T \| undefined | 第一个满足测试条件的元素，若不存在则返回undefined。 |

## findIndex

```TypeScript
findIndex(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): int
```

返回数组中第一个满足指定测试函数的元素的索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-findIndex(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): int--><!--Device-ReadonlyArray-findIndex(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, obj: ReadonlyArray&lt;T&gt;) =&gt; boolean | 是 | 用于测试每个元素的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 第一个满足测试条件的元素的索引，若不存在则返回-1。 |

## findLast

```TypeScript
findLast(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): T | undefined
```

返回数组中最后一个满足指定测试函数的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-findLast(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): T | undefined--><!--Device-ReadonlyArray-findLast(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, obj: ReadonlyArray&lt;T&gt;) =&gt; boolean | 是 | 用于测试每个元素的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T \| undefined | 最后一个满足测试条件的元素，若不存在则返回undefined。 |

## findLastIndex

```TypeScript
findLastIndex(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): int
```

返回数组中最后一个满足指定测试函数的元素的索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-findLastIndex(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): int--><!--Device-ReadonlyArray-findLastIndex(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, obj: ReadonlyArray&lt;T&gt;) =&gt; boolean | 是 | 用于测试每个元素的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 最后一个满足测试条件的元素的索引，若不存在则返回-1。 |

## forEach

```TypeScript
forEach(action: (value: T, index: int, array: ReadonlyArray<T>) => void): void
```

对数组中的每个元素执行一次指定的函数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-forEach(action: (value: T, index: int, array: ReadonlyArray<T>) => void): void--><!--Device-ReadonlyArray-forEach(action: (value: T, index: int, array: ReadonlyArray<T>) => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | (value: T, index: int, array: ReadonlyArray&lt;T&gt;) =&gt; void | 是 | 对每个元素执行的函数。 |

## includes

```TypeScript
includes(searchElement: T, fromIndex?: int): boolean
```

判断数组中是否包含指定的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-includes(searchElement: T, fromIndex?: int): boolean--><!--Device-ReadonlyArray-includes(searchElement: T, fromIndex?: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | T | 是 | 待查找的值。 |
| fromIndex | int | 否 | 开始查找的数组位置。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果找到该值则返回true，否则返回false。 |

## indexOf

```TypeScript
indexOf(searchElement: T, fromIndex?: int): int
```

返回指定元素在数组中首次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-indexOf(searchElement: T, fromIndex?: int): int--><!--Device-ReadonlyArray-indexOf(searchElement: T, fromIndex?: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | T | 是 | 待查找的元素。 |
| fromIndex | int | 否 | 开始查找的数组位置。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 该元素首次出现的索引，未找到时返回-1。 |

## join

```TypeScript
join(separator?: string): string
```

将数组中的所有元素连接为一个字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-join(separator?: string): string--><!--Device-ReadonlyArray-join(separator?: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| separator | string | 否 | 用于分隔相邻元素的字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 由所有数组元素连接而成的字符串。 |

## keys

```TypeScript
keys(): IterableIterator<int>
```

返回一个新的迭代器对象，其中包含数组中每个索引对应的键。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-keys(): IterableIterator<int>--><!--Device-ReadonlyArray-keys(): IterableIterator<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;int&gt; | 包含所有键的新迭代器对象。 |

## lastIndexOf

```TypeScript
lastIndexOf(searchElement: T): int
```

返回指定元素在数组中最后一次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-lastIndexOf(searchElement: T): int--><!--Device-ReadonlyArray-lastIndexOf(searchElement: T): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | T | 是 | 待查找的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 该元素最后一次出现的索引，未找到时返回-1。 |

## lastIndexOf

```TypeScript
lastIndexOf(searchElement: T, fromIndex?: int): int
```

返回指定元素在数组中最后一次出现的索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-lastIndexOf(searchElement: T, fromIndex?: int): int--><!--Device-ReadonlyArray-lastIndexOf(searchElement: T, fromIndex?: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | T | 是 | 待查找的元素。 |
| fromIndex | int | 否 | 开始反向查找的数组位置。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 该元素最后一次出现的索引，未找到时返回-1。 |

## map

```TypeScript
map<U>(mapper: (value: T, index: int, array: ReadonlyArray<T>) => U): Array<U>
```

使用映射函数转换数组中的每个元素，并返回新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-map<U>(mapper: (value: T, index: int, array: ReadonlyArray<T>) => U): Array<U>--><!--Device-ReadonlyArray-map<U>(mapper: (value: T, index: int, array: ReadonlyArray<T>) => U): Array<U>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mapper | (value: T, index: int, array: ReadonlyArray&lt;T&gt;) =&gt; U | 是 | 用于转换每个元素的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;U&gt; | 由转换后的元素组成的新数组。 |

## reduce

```TypeScript
reduce(reducer: (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => T): T
```

对累加器和数组中的每个元素应用指定函数，将数组归约为单个值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-reduce(reducer: (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => T): T--><!--Device-ReadonlyArray-reduce(reducer: (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => T): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reducer | (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray&lt;T&gt;) =&gt; T | 是 | 对每个元素执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 归约后得到的值。 |

## reduce

```TypeScript
reduce<U>(reducer: (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => U,
      initialValue: U): U
```

对累加器和数组中的每个元素应用指定函数，将数组归约为单个值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-reduce<U>(reducer: (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => U,      initialValue: U): U--><!--Device-ReadonlyArray-reduce<U>(reducer: (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => U,      initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reducer | (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray&lt;T&gt;) =&gt; U | 是 | 对每个元素执行的函数。 |
| initialValue | U | 是 | 累加器的初始值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | 归约后得到的值。 |

## reduceRight

```TypeScript
reduceRight(reducer: (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => T): T
```

对累加器和数组中的每个元素从右向左应用指定函数，将数组归约为单个值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-reduceRight(reducer: (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => T): T--><!--Device-ReadonlyArray-reduceRight(reducer: (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => T): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reducer | (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray&lt;T&gt;) =&gt; T | 是 | 对每个元素执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 归约后得到的值。 |

## reduceRight

```TypeScript
reduceRight<U>(reducer: (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => U,
      initialValue: U): U
```

对累加器和数组中的每个元素从右向左应用指定函数，将数组归约为单个值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-reduceRight<U>(reducer: (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => U,      initialValue: U): U--><!--Device-ReadonlyArray-reduceRight<U>(reducer: (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => U,      initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reducer | (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray&lt;T&gt;) =&gt; U | 是 | 对每个元素执行的函数。 |
| initialValue | U | 是 | 累加器的初始值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | 归约后得到的值。 |

## slice

```TypeScript
slice(start?: int, end?: int): Array<T>
```

将数组的一部分浅拷贝到新数组中并返回。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-slice(start?: int, end?: int): Array<T>--><!--Device-ReadonlyArray-slice(start?: int, end?: int): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | int | 否 | 起始索引（包含），默认值为0。 <br>取值约束：应为整数。 |
| end | int | 否 | 结束索引（不包含），默认值为数组长度。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | 包含所提取元素的新数组。 |

## some

```TypeScript
some(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): boolean
```

检测数组中是否至少有一个元素通过指定函数实现的测试。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-some(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): boolean--><!--Device-ReadonlyArray-some(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: int, array: ReadonlyArray&lt;T&gt;) =&gt; boolean | 是 | 用于测试每个元素的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果至少有一个元素通过测试则返回true，否则返回false。 |

## values

```TypeScript
values(): IterableIterator<T>
```

返回一个新的迭代器对象，其中包含数组中每个索引对应的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadonlyArray-values(): IterableIterator<T>--><!--Device-ReadonlyArray-values(): IterableIterator<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; | 包含所有值的新迭代器对象。 |

