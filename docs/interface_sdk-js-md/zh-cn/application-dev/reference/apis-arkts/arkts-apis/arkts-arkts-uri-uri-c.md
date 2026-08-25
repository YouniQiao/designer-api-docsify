# URI

构造一个URI对象，并提供URI比较、路径规范化、查询参数操作、路径段追加和URI类型判断等方法。

**起始版本：** 8

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { uri } from 'kits/@kit.ArkTS';
```

## addEncodedSegment

```TypeScript
addEncodedSegment(pathSegment: string): URI
```

将已编码的字段追加到当前URI的path字段中，创建新URI对象并返回，保持原有URI对象不变。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pathSegment | string | 是 |

**返回值：**

| 类型 |
| --- |
| [URI](arkts-arkts-uri-uri-c.md) |

## addQueryValue

```TypeScript
addQueryValue(key: string, value: string): URI
```

在当前URI对象上添加查询参数后返回新的URI对象，保持原有URI对象不变。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| [URI](arkts-arkts-uri-uri-c.md) |

## addSegment

```TypeScript
addSegment(pathSegment: string): URI
```

对指定字段进行编码，并将其追加到当前URI对象的path中，创建并返回新的URI对象，保持原有URI对象不变。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pathSegment | string | 是 |

**返回值：**

| 类型 |
| --- |
| [URI](arkts-arkts-uri-uri-c.md) |

## checkHierarchical

```TypeScript
checkHierarchical(): boolean
```

判断此URI是否为分层的URI，方案特定部分以“/”开头的URI为分层的URI。相对URI也是分层的。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## checkIsAbsolute

```TypeScript
checkIsAbsolute(): boolean
```

判断URI是否为绝对URI，即是否包含scheme组件。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## checkOpaque

```TypeScript
checkOpaque(): boolean
```

判断此URI是否为不透明URI，方案特定部分不以“/”开头的URI为不透明的URI。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## checkRelative

```TypeScript
checkRelative(): boolean
```

判断此URI是否为相对URI，相对URI指的是不包含协议（scheme）部分的URI。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## clearQuery

```TypeScript
clearQuery(): URI
```

清除URI查询部分，并创建一个新的URI对象返回，同时保持原有URI对象不变。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [URI](arkts-arkts-uri-uri-c.md) |

## constructor

```TypeScript
constructor(uri: string)
```

构造函数用于创建URI对象，将输入的URI字符串按照RFC3986规范解析并分解为scheme、userInfo、host、port、path、query和fragment等组件。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [uri](arkts-uri.md) | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200002](../errorcode-utils.md#10200002-参数解析错误) |

## createFromParts

```TypeScript
static createFromParts(scheme: string, ssp: string, fragment: string): URI
```

根据提供的方案（scheme）、方案特定部分（ssp）以及片段（fragment）创建一个新的URI对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [scheme](#scheme) | string | 是 |
| [ssp](arkts-arkts-uri-uri-c.md) | string | 是 |
| [fragment](arkts-arkts-uri-uri-c.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| [URI](arkts-arkts-uri-uri-c.md) |

## equals

```TypeScript
equals(other: URI): boolean
```

判断此URI是否与其他URI对象相等，通过逐组件比较scheme、authority、path、query和fragment等内容来确定两个URI是否等价。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [equalsTo](#equalsto)

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [URI](arkts-arkts-uri-uri-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## equalsTo

```TypeScript
equalsTo(other: URI): boolean
```

判断此URI是否与其他URI对象相等，通过逐组件比较scheme、authority、path、query和fragment等内容来确定两个URI是否等价。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [URI](arkts-arkts-uri-uri-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## getBooleanQueryValue

```TypeScript
getBooleanQueryValue(key: string, defaultValue: boolean): boolean
```

根据指定键名，搜索此URI查询字符串并返回其对应的布尔类型值。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| defaultValue | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## getLastSegment

```TypeScript
getLastSegment(): string
```

获取此URI路径的最后一个段。每个段代表路径中的一个部分，通常通过“/”来进行分隔。以斜杠结尾的路径段不计入段，没有路径时不计入段。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## getQueryNames

```TypeScript
getQueryNames(): string[]
```

获取URI查询部分中所有不重复的键。查询参数出现在问号“?”之后，由键值对组成，键和值用等号“=”连接，键值对间用与号“&”分隔。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string[] |

## getQueryValue

```TypeScript
getQueryValue(key: string): string
```

根据给定的查询关键词，从URI查询参数部分中提取出该关键词对应的第一个值，若查询参数中存在已编码过的内容，需将对应Key进行解码后获取Value。查询参数在问号“?”后，由键值对组成。键和值用等号“=”连接，键值对用与号“&”分隔。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## getQueryValues

```TypeScript
getQueryValues(key: string): string[]
```

获取URI中查询参数指定键的所有值。如果查询参数已编码，需先解码键再获取值。查询参数是出现在问号“?”之后的部分，由键值对组成，键和值用等号“=”连接，键值对间用与号“&”分隔。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| string[] |

## getSegment

```TypeScript
getSegment(): string[]
```

获取此URI中已解码的所有路径段。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string[] |

## normalize

```TypeScript
normalize(): URI
```

规范化此URI的路径，适用于处理包含点段（.或..）的路径场景。

> **说明：**&gt;
> 如果此URI是不透明的，或者其路径已经是规范形式，则返回该URI。否则将构造一个新的URI，该URI与当前URI相同，唯一的区别是其路径通过规范化当前URI的路径来计算，具体规则如下：&gt;
> 1.移除所有的 .（点）段。&gt;
> 2.如果 ..（双点）段前面有一个非 .. 段，则将这两个段一起移除。重复此步骤，直到不再适用为止。&gt;
> 如果路径规范化后以 ..（双点）段开头，这表明之前没有足够的非 .. 段可以移除，因此路径将以 .. 段开始。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [URI](arkts-arkts-uri-uri-c.md) |

## toString

```TypeScript
toString(): string
```

将URI转化为编码后的字符串。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## authority

```TypeScript
authority: string
```

获取和设置此URI的解码授权组件部分，若无此部分则返回null对象。此属性在API version 19之前为只读属性，不可写，修改此属性会报错。

**类型：** string

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## encodedAuthority

```TypeScript
encodedAuthority: string
```

获取和设置URI的编码授权组件部分，若无此部分则返回null对象。此属性在API version 19之前为只读属性，不可写，修改此属性会报错。

**类型：** string

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## encodedFragment

```TypeScript
encodedFragment: string
```

获取和设置URI的编码片段部分，若无此部分则返回null对象。此属性在API version 19之前为只读属性，不可写，修改此属性会报错。

**类型：** string

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## encodedPath

```TypeScript
encodedPath: string
```

获取和设置URI的编码路径部分，若无此部分则返回null对象。此属性在API version 19之前为只读属性，不可写，修改此属性会报错。

**类型：** string

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## encodedQuery

```TypeScript
encodedQuery: string
```

获取和设置URI的编码查询部分，若无此部分则返回null对象。此属性在API version 19之前为只读属性，不可写，修改此属性会报错。

**类型：** string

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## encodedSSP

```TypeScript
encodedSSP: string
```

获取和设置URI的编码方案特定部分，若无此部分则返回null对象。此属性在API version 19之前为只读属性，不可写，修改此属性会报错。

**类型：** string

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## encodedUserInfo

```TypeScript
encodedUserInfo: string
```

获取和设置URI的编码用户信息部分，若无此部分则返回null对象。此属性在API version 19之前为只读属性，不可写，修改此属性会报错。

**类型：** string

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## fragment

```TypeScript
fragment: string
```

获取和设置URI的片段部分，若无此部分则返回null对象。此属性在API version 19之前为只读属性，不可写，修改此属性会报错。

**类型：** string

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## host

```TypeScript
host: string
```

获取 URI 的主机名部分（不带端口），若无此部分则返回null对象。

**类型：** string

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## path

```TypeScript
path: string
```

获取和设置URI的路径部分，若无此部分则返回null对象。此属性在API version 19之前为只读属性，不可写，修改此属性会报错。

**类型：** string

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## port

```TypeScript
port: string
```

获取URI的端口部分，若无此部分则返回-1。

**类型：** string

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## query

```TypeScript
query: string
```

获取和设置URI的查询部分，若无此部分则返回null对象。此属性在API version 19之前为只读属性，不可写，修改此属性会报错。

**类型：** string

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## scheme

```TypeScript
scheme: string
```

获取和设置URI的方案部分，若无此部分则返回null对象。方案名以字母开头，只能包含字母、数字、加号(+)、减号(-)和点号(.)。此属性在API version 19之前为只读属性，不可写，修改此属性会报错。

**类型：** string

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## ssp

```TypeScript
ssp: string
```

获取和设置URI的解码方案特定部分，方案特定部分是URI的一部分，它包含了特定于协议或方案的信息。此属性在API version 19之前为只读属性，不可写，修改此属性会报错。

**类型：** string

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## userInfo

```TypeScript
userInfo: string
```

获取和设置URI的用户信息部分，若无此部分则返回null对象。此属性在API version 19之前为只读属性，不可写，修改此属性会报错。

**类型：** string

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang
