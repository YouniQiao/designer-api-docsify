# URLParams

URLParams是一个用于解析、构造和操作URL参数的实用类。该类提供了统一的接口来处理URL查询参数。

**起始版本：** 9

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { url } from 'kits/@kit.ArkTS';
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<[string, string]>
```

获取一个迭代器，迭代器的每一项都是一个JavaScript数组，数组的第一项和第二项分别是键和值。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;[string, string] & gt; |

## append

```TypeScript
append(name: string, value: string): void
```

将新的键值对插入到查询字符串。与[set](#set)方法不同，append不会替换已存在的键名对应的值， 而是追加一个新的键值对，允许同一键名存在多个值。如需替换已有键值，请使用set方法。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| value | string | 是 |

## constructor

```TypeScript
constructor(init?: string[][] | Record<string, string> | string | URLParams)
```

ArkTS-Sta: constructor(init?: [string, string][] | Record&lt;string, string&gt; | string | URLParams)URLParams的构造函数，用于创建URL参数对象，适用于需要解析、构造或操作URL查询参数的场景。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| init | string[][] \| Record & lt;string, string & gt; \ | string \| [URLParams](arkts-arkts-url-urlparams-c.md) | 否 |

## delete

```TypeScript
delete(name: string): void
```

删除指定名称的所有键值对。如果指定名称不存在，则不做任何操作。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

## entries

```TypeScript
entries(): IterableIterator<[string, string]>
```

返回一个ES6的迭代器，迭代器的每一项都是一个Array。Array的第一项是name，Array的第二项是value。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;[string, string] & gt; |

## forEach

```TypeScript
forEach(callbackFn: (value: string, key: string, searchParams: URLParams) => void, thisArg?: Object): void
```

通过回调函数按照插入顺序遍历URLParams实例对象上的键值对。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackFn | (value: string, key: string, searchParams: URLParams) = & gt; void | 是 |
| thisArg | Object | 否 |

## get

```TypeScript
get(name: string): string | null
```

获取指定名称对应的第一个值。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| string \| null |

## getAll

```TypeScript
getAll(name: string): string[]
```

获取指定名称的所有键对应值的集合。若查找一个不存在的键值对名称时返回值为空数组。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| string[] |

## has

```TypeScript
has(name: string): boolean
```

判断一个指定的键名对应的值是否存在。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## keys

```TypeScript
keys(): IterableIterator<string>
```

返回一个包含所有键值对的name的迭代器。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;string & gt; |

## set

```TypeScript
set(name: string, value: string): void
```

将与name关联的URLParams对象中的值设置为value。如果存在名称为name的键值对，请将第一个键值对的值设置为value并删除所有其他值。如果不存在该键名，则将键值对附加到查询字符串。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| value | string | 是 |

## sort

```TypeScript
sort(): void
```

对包含在此对象中的所有键值对进行排序，适用于URL规范化场景（如URL签名、缓存键生成等需要参数顺序一致的场景）。 排序顺序是根据键的Unicode代码点。该方法使用稳定的排序算法（保留具有相等键的键值对之间的相对顺序）。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## toString

```TypeScript
toString(): string
```

返回序列化为字符串的搜索参数，必要时对字符进行百分比编码。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## values

```TypeScript
values(): IterableIterator<string>
```

返回一个包含所有键值对的value的迭代器。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;string & gt; |
