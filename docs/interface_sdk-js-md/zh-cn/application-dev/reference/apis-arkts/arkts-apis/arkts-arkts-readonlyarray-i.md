# ReadonlyArray

只读数组，提供读取元素的方法。

**继承/实现关系：** ReadonlyArray extends ConcatArray<T>

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

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

## entries

```TypeScript
entries(): IterableIterator<[int, T]>
```

返回一个新的迭代器对象，其中包含数组中每个索引对应的键值对。

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
every(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): boolean
```

检测数组中的所有元素是否都通过指定函数实现的测试。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: int, array: ReadonlyArray & lt;T & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## filter

```TypeScript
filter(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): Array<T>
```

创建一个新数组，其中包含所有通过指定函数实现的测试的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: int, array: ReadonlyArray & lt;T & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;T & gt; |

## find

```TypeScript
find(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): T | undefined
```

返回数组中第一个满足指定测试函数的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: int, obj: ReadonlyArray & lt;T & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T \| undefined |

## findIndex

```TypeScript
findIndex(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): int
```

返回数组中第一个满足指定测试函数的元素的索引。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: int, obj: ReadonlyArray & lt;T & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## findLast

```TypeScript
findLast(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): T | undefined
```

返回数组中最后一个满足指定测试函数的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: int, obj: ReadonlyArray & lt;T & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T \| undefined |

## findLastIndex

```TypeScript
findLastIndex(predicate: (value: T, index: int, obj: ReadonlyArray<T>) => boolean): int
```

返回数组中最后一个满足指定测试函数的元素的索引。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: int, obj: ReadonlyArray & lt;T & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## forEach

```TypeScript
forEach(action: (value: T, index: int, array: ReadonlyArray<T>) => void): void
```

对数组中的每个元素执行一次指定的函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| action | (value: T, index: int, array: ReadonlyArray & lt;T & gt;) = & gt; void | 是 |

## includes

```TypeScript
includes(searchElement: T, fromIndex?: int): boolean
```

判断数组中是否包含指定的值。

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

返回指定元素在数组中首次出现的索引。

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

## join

```TypeScript
join(separator?: string): string
```

将数组中的所有元素连接为一个字符串。

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

返回一个新的迭代器对象，其中包含数组中每个索引对应的键。

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
lastIndexOf(searchElement: T): int
```

返回指定元素在数组中最后一次出现的索引。

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
lastIndexOf(searchElement: T, fromIndex?: int): int
```

返回指定元素在数组中最后一次出现的索引。

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
map<U>(mapper: (value: T, index: int, array: ReadonlyArray<T>) => U): Array<U>
```

使用映射函数转换数组中的每个元素，并返回新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mapper | (value: T, index: int, array: ReadonlyArray & lt;T & gt;) = & gt; U | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;U & gt; |

## reduce

```TypeScript
reduce(reducer: (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => T): T
```

对累加器和数组中的每个元素应用指定函数，将数组归约为单个值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reducer | (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray & lt;T & gt;) = & gt; T | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## reduce

```TypeScript
reduce<U>(reducer: (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => U,
      initialValue: U): U
```

对累加器和数组中的每个元素应用指定函数，将数组归约为单个值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reducer | (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray & lt;T & gt;) = & gt; U | 是 |
| initialValue | U | 是 |

**返回值：**

| 类型 |
| --- |
| U |

## reduceRight

```TypeScript
reduceRight(reducer: (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => T): T
```

对累加器和数组中的每个元素从右向左应用指定函数，将数组归约为单个值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reducer | (previousValue: T, currentValue: T, currentIndex: int, array: ReadonlyArray & lt;T & gt;) = & gt; T | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## reduceRight

```TypeScript
reduceRight<U>(reducer: (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray<T>) => U,
      initialValue: U): U
```

对累加器和数组中的每个元素从右向左应用指定函数，将数组归约为单个值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reducer | (previousValue: U, currentValue: T, currentIndex: int, array: ReadonlyArray & lt;T & gt;) = & gt; U | 是 |
| initialValue | U | 是 |

**返回值：**

| 类型 |
| --- |
| U |

## slice

```TypeScript
slice(start?: int, end?: int): Array<T>
```

将数组的一部分浅拷贝到新数组中并返回。

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
some(predicate: (value: T, index: int, array: ReadonlyArray<T>) => boolean): boolean
```

检测数组中是否至少有一个元素通过指定函数实现的测试。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: T, index: int, array: ReadonlyArray & lt;T & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## values

```TypeScript
values(): IterableIterator<T>
```

返回一个新的迭代器对象，其中包含数组中每个索引对应的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; |
