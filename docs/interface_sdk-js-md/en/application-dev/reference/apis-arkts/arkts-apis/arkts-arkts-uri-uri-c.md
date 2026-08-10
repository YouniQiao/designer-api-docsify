# URI

构造一个URI对象，并提供URI比较、路径规范化、查询参数操作、路径段追加和URI类型判断等方法。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-uri-export class URI--><!--Device-uri-export class URI-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { uri } from 'kits/@kit.ArkTS';
```

## addEncodedSegment

```TypeScript
addEncodedSegment(pathSegment: string): URI
```

将已编码的字段追加到当前URI的path字段中，创建新URI对象并返回，保持原有URI对象不变。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-URI-addEncodedSegment(pathSegment: string): URI--><!--Device-URI-addEncodedSegment(pathSegment: string): URI-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathSegment | string | Yes | 需要追加到路径部分的编码字段。 |

**Return value:**

| Type | Description |
| --- | --- |
| [URI](arkts-arkts-uri-uri-c.md) | 返回已追加字段的URI对象。 |

## Examples

```TypeScript
const uriInstance = new uri.URI("http://www.test.com");
const newRoute = uriInstance.addEncodedSegment("my%20image.jpg");
console.info(newRoute.toString()); // http://www.test.com/my%20image.jpg
```

## addQueryValue

```TypeScript
addQueryValue(key: string, value: string): URI
```

在当前URI对象上添加查询参数后返回新的URI对象，保持原有URI对象不变。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-URI-addQueryValue(key: string, value: string): URI--><!--Device-URI-addQueryValue(key: string, value: string): URI-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 需要添加查询参数的名称。 |
| value | string | Yes | 需要添加查询参数的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [URI](arkts-arkts-uri-uri-c.md) | 返回添加查询部分后的URI对象。 |

## Examples

```TypeScript
const uriInstance = new uri.URI("https://www.test.com");
const newRoute = uriInstance.addQueryValue("param1", "hello world");
console.info(newRoute.toString()); // https://www.test.com?param1=hello%20world
```

## addSegment

```TypeScript
addSegment(pathSegment: string): URI
```

对指定字段进行编码，并将其追加到当前URI对象的path中，创建并返回新的URI对象，保持原有URI对象不变。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-URI-addSegment(pathSegment: string): URI--><!--Device-URI-addSegment(pathSegment: string): URI-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathSegment | string | Yes | 需要追加到路径部分的字段。 |

**Return value:**

| Type | Description |
| --- | --- |
| [URI](arkts-arkts-uri-uri-c.md) | 返回已追加字段的URI对象。 |

## Examples

```TypeScript
const uriInstance = new uri.URI("http://www.test.com");
const newRoute = uriInstance.addSegment("my image.jpg");
console.info(newRoute.toString()); // http://www.test.com/my%20image.jpg
```

## checkHierarchical

```TypeScript
checkHierarchical(): boolean
```

判断此URI是否为分层的URI，方案特定部分以“/”开头的URI为分层的URI。相对URI也是分层的。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-URI-checkHierarchical(): boolean--><!--Device-URI-checkHierarchical(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 如果是分层的URI返回true，否则返回false。 |

## Examples

```TypeScript
const uriInstance = new uri.URI("http://www.test.com/images/pic.jpg");
console.info(`${uriInstance.checkHierarchical()}`); // true
const uriInstance1 = new uri.URI("mailto:user@example.com");
console.info(`${uriInstance1.checkHierarchical()}`); // false
```

## checkIsAbsolute

```TypeScript
checkIsAbsolute(): boolean
```

判断URI是否为绝对URI，即是否包含scheme组件。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URI-checkIsAbsolute(): boolean--><!--Device-URI-checkIsAbsolute(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 如果是绝对URI返回true，否则返回false。 |

## Examples

```TypeScript
const uriInstance = new uri.URI('https://username:password@www.qwer.com:8080?query=pppppp');
console.info(`${uriInstance.checkIsAbsolute()}`); // true
const uriInstance1 = new uri.URI('xxx.com/suppliers.htm');
console.info(`${uriInstance1.checkIsAbsolute()}`); // false
```

## checkOpaque

```TypeScript
checkOpaque(): boolean
```

判断此URI是否为不透明URI，方案特定部分不以“/”开头的URI为不透明的URI。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-URI-checkOpaque(): boolean--><!--Device-URI-checkOpaque(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 如果是不透明的URI返回true，否则返回false。 |

## Examples

```TypeScript
const uriInstance = new uri.URI("http://www.test.com/images/pic.jpg");
console.info(`${uriInstance.checkOpaque()}`); // false
const uriInstance1 = new uri.URI("mailto:user@example.com");
console.info(`${uriInstance1.checkOpaque()}`); // true
```

## checkRelative

```TypeScript
checkRelative(): boolean
```

判断此URI是否为相对URI，相对URI指的是不包含协议(scheme)部分的URI。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-URI-checkRelative(): boolean--><!--Device-URI-checkRelative(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 如果是相对URI返回true，否则返回false。 |

## Examples

```TypeScript
const uriInstance = new uri.URI("https://username:password@www.qwer.com:8080?query=p");
console.info(`${uriInstance.checkRelative()}`); // false
const uriInstance1 = new uri.URI("/images/pic.jpg");
console.info(`${uriInstance1.checkRelative()}`); // true
```

## clearQuery

```TypeScript
clearQuery(): URI
```

清除URI路径查询部分，并创建一个新的URI对象返回，同时保持原有URI对象不变。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-URI-clearQuery(): URI--><!--Device-URI-clearQuery(): URI-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [URI](arkts-arkts-uri-uri-c.md) | 返回一个已被清除查询部分的URI对象。 |

## Examples

```TypeScript
const uriInstance = new uri.URI("https://www.test.com?param1=value1");
console.info(uriInstance.clearQuery().toString()); // https://www.test.com
```

## constructor

```TypeScript
constructor(uri: string)
```

构造函数用于创建URI对象，将输入的URI字符串按照RFC3986规范解析并分解为scheme、userInfo、host、port、path、query和fragment等组件。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URI-constructor(uri: string)--><!--Device-URI-constructor(uri: string)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 需要解析的URI字符串，需符合RFC3986规范标准。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200002 | Invalid uri string. |

## Examples

```TypeScript
let mm = 'https://username:password@host:8080/directory/file?foo=1&bar=2#fragment';
new uri.URI(mm);
```

```TypeScript
new uri.URI('https://username:password@host:8080');
```

## createFromParts

```TypeScript
static createFromParts(scheme: string, ssp: string, fragment: string): URI
```

根据提供的协议、方案以及片段创建一个新的URI对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-URI-static createFromParts(scheme: string, ssp: string, fragment: string): URI--><!--Device-URI-static createFromParts(scheme: string, ssp: string, fragment: string): URI-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scheme | string | Yes | 此URI协议部分。该参数需符合URI协议标准。 |
| ssp | string | Yes | 此URI的方案特定部分，即位于协议分隔符“:”和片段分隔符“#”之间的所有内容，这部分将被编码。 |
| fragment | string | Yes | 此URI的片段部分，即“#”符号后面的内容，如果未定义则为空，这部分也将被编码。 |

**Return value:**

| Type | Description |
| --- | --- |
| [URI](arkts-arkts-uri-uri-c.md) | 返回由给定协议、协议特定部分和片段创建的URI对象。 |

## Examples

```TypeScript
const uriInstance = uri.URI.createFromParts("mailto", "no body", "top");
console.info(uriInstance.toString()); // mailto:no%20body#top
```

## equals

```TypeScript
equals(other: URI): boolean
```

判断此URI是否与其他URI对象相等。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.uri.URI.equalsTo

<!--Device-URI-equals(other: URI): boolean--><!--Device-URI-equals(other: URI): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [URI](arkts-arkts-uri-uri-c.md) | Yes | 需要比较的URI对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回true表示相等，否则返回false。 |

## Examples

```TypeScript
const uriInstance = new uri.URI('https://username:password@host:8080/directory/file?query=pppppp#qwer=da');
const uriInstance1 = new uri.URI('https://username:password@host:8080/directory/file?query=pppppp#qwer=da');
uriInstance.equals(uriInstance1); // true
```

## equalsTo

```TypeScript
equalsTo(other: URI): boolean
```

判断此URI是否与其他URI对象相等。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URI-equalsTo(other: URI): boolean--><!--Device-URI-equalsTo(other: URI): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [URI](arkts-arkts-uri-uri-c.md) | Yes | 需要比较的URI对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回true表示相等，否则返回false。 |

## Examples

```TypeScript
const uriInstance = new uri.URI('https://username:password@host:8080/directory/file?query=pppppp#qwer=da');
const uriInstance1 = new uri.URI('https://username:password@host:8080/directory/file?query=pppppp#qwer=da');
let result = uriInstance.equalsTo(uriInstance1); // true
```

## getBooleanQueryValue

```TypeScript
getBooleanQueryValue(key: string, defaultValue: boolean): boolean
```

根据指定键名，搜索此URI查询字符串并返回其对应的布尔类型值。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-URI-getBooleanQueryValue(key: string, defaultValue: boolean): boolean--><!--Device-URI-getBooleanQueryValue(key: string, defaultValue: boolean): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 要获取的查询参数的名称。 |
| defaultValue | boolean | Yes | 设置查询参数中未包含指定键时返回的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 如果指定的查询参数不存在，则返回defaultValue的值；查询参数对应第一个值为“false”或者“0”返回false，否则返回true。 |

## Examples

```TypeScript
const uriInstance = new uri.URI("https://www.test.com/search?active=true");
console.info(`${uriInstance.getBooleanQueryValue("active", false)}`); // true
const uriInstance1 = new uri.URI("https://www.test.com/search");
console.info(`${uriInstance1.getBooleanQueryValue("active", false)}`); // false
const uriInstance2 = new uri.URI("https://www.test.com/search?active=aa&active=false");
console.info(`${uriInstance2.getBooleanQueryValue("active", false)}`); // true
const uriInstance3 = new uri.URI("https://www.test.com/search?active=0");
console.info(`${uriInstance3.getBooleanQueryValue("active", true)}`); // false
const uriInstance4 = new uri.URI("https://www.test.com/search");
console.info(`${uriInstance4.getBooleanQueryValue("active", true)}`); // true
```

## getLastSegment

```TypeScript
getLastSegment(): string
```

获取此URI路径的最后一个段。每个段代表路径中的一个部分，通常通过“/”来进行分隔。对于以斜杠结尾的或者没有路径的部分不计入段。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-URI-getLastSegment(): string--><!--Device-URI-getLastSegment(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回此URI路径中的最后一个段，如果路径为空则返回null。 |

## Examples

```TypeScript
const uriInstance = new uri.URI("content://com.test.provider/files/image.jpg");
console.info(uriInstance.getLastSegment()); // image.jpg
```

## getQueryNames

```TypeScript
getQueryNames(): string[]
```

获取URI查询部分中所有不重复的键。查询参数出现在问号“?”之后，由键值对组成，键和值用等号“=”连接，键值对间用与号“&”分隔。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-URI-getQueryNames(): string[]--><!--Device-URI-getQueryNames(): string[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string[] | 返回URI查询部分中所有不重复的已解码参数名集合。 |

## Examples

```TypeScript
const uriInstance = new uri.URI("https://www.test.com?param1=value1&param2=value2");
const paramNames = uriInstance.getQueryNames();
console.info(paramNames.toString()); // param1,param2
```

## getQueryValue

```TypeScript
getQueryValue(key: string): string
```

根据给定的查询关键词，从URI查询参数部分中提取出该关键词对应的第一个值，若查询参数中存在已编码过的内容，需将对应Key进行解码后获取Value。

查询参数在问号“?”后，由键值对组成。键和值用等号“=”连接，键值对用与号“&”分隔。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-URI-getQueryValue(key: string): string--><!--Device-URI-getQueryValue(key: string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 此URI查询参数的名称。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回经解码处理后的URI查询参数的第一个值，若未找到对应值则返回null对象。 |

## Examples

```TypeScript
const uriInstance = new uri.URI("https://www.com?param1=value1&param2=value2");
console.info(uriInstance.getQueryValue("param1")); // value1
let uriInstance1 = new uri.URI('https://www.zyy.ss?sa%3D=po%7E');
console.info(uriInstance1.getQueryValue('sa=')) // po~
console.info(uriInstance1.getQueryValue('abc')) // null
```

## getQueryValue

```TypeScript
getQueryValue(key: string): string | null
```

从当前 URI 的查询组件中获取指定键的第一个值。如果查询组件包含编码内容，此 API 会在获取值之前对键进行解码。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-URI-getQueryValue(key: string): string | null--><!--Device-URI-getQueryValue(key: string): string | null-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 查询参数的键。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回解码后的值，如果未找到对应的值则返回 null 对象。 |

## getQueryValues

```TypeScript
getQueryValues(key: string): string[]
```

获取URI中查询参数指定键的所有值。如果查询参数已编码，需先解码键再获取值。

查询参数是出现在问号“?”之后的部分，由键值对组成，键和值用等号“=”连接，键值对间用与号“&”分隔。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-URI-getQueryValues(key: string): string[]--><!--Device-URI-getQueryValues(key: string): string[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 指定键的名称。 |

**Return value:**

| Type | Description |
| --- | --- |
| string[] | 返回此URI中查询参数内指定键对应所有值的集合，若没有找到则返回一个空字符串数组[]。 |

## Examples

```TypeScript
const uriInstance = new uri.URI("https://www.test.com/search?query=name&query=my");
console.info(uriInstance.getQueryValues("query").toString()); // name,my
console.info(JSON.stringify(uriInstance.getQueryValues("abc"))); // []
```

## getSegment

```TypeScript
getSegment(): string[]
```

获取此URI中已解码的所有路径段。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-URI-getSegment(): string[]--><!--Device-URI-getSegment(): string[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string[] | 返回此URI中已解码的所有路径段，各段前后均不含 “/”。 |

## Examples

```TypeScript
const uriInstance = new uri.URI("http://www.test.com/path/to/image.jpg");
console.info(uriInstance.getSegment().toString()); // path,to,image.jpg
```

## normalize

```TypeScript
normalize(): URI
```

规范化此URI的路径。

> **说明：**
> 
> 如果此URI是不透明的，或者其路径已经是规范形式，则返回该URI。否则将构造一个新的URI，该URI与当前URI相同，唯一的区别是其路径通过规范化当前URI的路径来计算，具体规则如下：
> 
> 1.移除所有的 .（点）段。
> 
> 2.如果 ..（双点）段前面有一个非 .. 段，则将这两个段一起移除。重复此步骤，直到不再适用为止。
> 
> 如果路径规范化后以 ..（双点）段开头，这表明之前没有足够的非 .. 段可以移除，因此路径将以 .. 段开始。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URI-normalize(): URI--><!--Device-URI-normalize(): URI-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [URI](arkts-arkts-uri-uri-c.md) | 返回一个path被规范化后的URI对象。 |

## Examples

```TypeScript
const uriInstance = new uri.URI('https://username:password@www.qwer.com:8080/path/path1/../path2/./path3?query=pppppp');
console.info(uriInstance.path); // /path/path1/../path2/./path3
// Following path normalization, all . (dot) segments are removed. If a .. (double-dot) segment is immediately preceded by a segment that is not .., both segments are removed.
let uriInstance1 = uriInstance.normalize();
console.info(uriInstance1.path); // /path/path2/path3
let uri1 = new uri.URI('http://www.test.com/../../patch/path1/../path2/path3/./path4/../');
console.info(uri1.path); // /../../patch/path1/../path2/path3/./path4/../
// If normalization result in a path starting with a .. (double-dot) segment, it indicates that there were insufficient preceding non-.. segments for removal. As a result, the path will start with a .. segment.
let uri2 = uri1.normalize();
console.info(uri2.path); // /../../patch/path2/path3
```

## toString

```TypeScript
toString(): string
```

将URI转化为编码后的字符串。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URI-toString(): string--><!--Device-URI-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回URI的字符串序列化。 |

## Examples

```TypeScript
const result = new uri.URI('https://username:password@host:8080/directory/file?ab=pppppp#qwer da');
let result1 = result.toString(); // https://username:password@host:8080/directory/file?ab=pppppp#qwer%20da
```

## authority

```TypeScript
authority: string
```

获取和设置此URI的解码授权组件部分，若无此部分则返回null对象。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URI-authority: string--><!--Device-URI-authority: string-End-->

**System capability:** SystemCapability.Utils.Lang

## encodedAuthority

```TypeScript
encodedAuthority: string
```

获取和设置URI的编码授权组件部分，若无此部分则返回null对象。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-URI-encodedAuthority: string--><!--Device-URI-encodedAuthority: string-End-->

**System capability:** SystemCapability.Utils.Lang

## encodedFragment

```TypeScript
encodedFragment: string
```

获取和设置URI的编码片段部分，若无此部分则返回null对象。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-URI-encodedFragment: string--><!--Device-URI-encodedFragment: string-End-->

**System capability:** SystemCapability.Utils.Lang

## encodedPath

```TypeScript
encodedPath: string
```

获取和设置URI的编码路径部分，若无此部分则返回null对象。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-URI-encodedPath: string--><!--Device-URI-encodedPath: string-End-->

**System capability:** SystemCapability.Utils.Lang

## encodedQuery

```TypeScript
encodedQuery: string
```

获取和设置URI的编码查询部分，若无此部分则返回null对象。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-URI-encodedQuery: string--><!--Device-URI-encodedQuery: string-End-->

**System capability:** SystemCapability.Utils.Lang

## encodedSSP

```TypeScript
encodedSSP: string
```

获取和设置URI的编码方案特定部分，若无此部分则返回null对象。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-URI-encodedSSP: string--><!--Device-URI-encodedSSP: string-End-->

**System capability:** SystemCapability.Utils.Lang

## encodedUserInfo

```TypeScript
encodedUserInfo: string
```

获取和设置URI的编码用户信息部分，若无此部分则返回null对象。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-URI-encodedUserInfo: string--><!--Device-URI-encodedUserInfo: string-End-->

**System capability:** SystemCapability.Utils.Lang

## fragment

```TypeScript
fragment: string
```

获取和设置URI的片段部分，若无此部分则返回null对象。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URI-fragment: string--><!--Device-URI-fragment: string-End-->

**System capability:** SystemCapability.Utils.Lang

## host

```TypeScript
host: string
```

获取 URI 的主机名部分（不带端口），若无此部分则返回null对象。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URI-host: string--><!--Device-URI-host: string-End-->

**System capability:** SystemCapability.Utils.Lang

## path

```TypeScript
path: string
```

获取和设置URI的路径部分，若无此部分则返回null对象。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URI-path: string--><!--Device-URI-path: string-End-->

**System capability:** SystemCapability.Utils.Lang

## port

```TypeScript
port: string
```

获取URI的端口部分，若无此部分则返回-1。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URI-port: string--><!--Device-URI-port: string-End-->

**System capability:** SystemCapability.Utils.Lang

## query

```TypeScript
query: string
```

获取和设置URI的查询部分，若无此部分则返回null对象。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URI-query: string--><!--Device-URI-query: string-End-->

**System capability:** SystemCapability.Utils.Lang

## scheme

```TypeScript
scheme: string
```

获取和设置URI的方案部分，若无此部分则返回null对象。方案名以字母开头，只能包含字母、数字、加号(+)、减号(-)和点号(.)。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URI-scheme: string--><!--Device-URI-scheme: string-End-->

**System capability:** SystemCapability.Utils.Lang

## ssp

```TypeScript
ssp: string
```

获取和设置URI的解码方案特定部分，方案特定部分是URI的一部分，它包含了特定于协议或方案的信息。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URI-ssp: string--><!--Device-URI-ssp: string-End-->

**System capability:** SystemCapability.Utils.Lang

## userInfo

```TypeScript
userInfo: string
```

获取和设置URI的用户信息部分，若无此部分则返回null对象。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URI-userInfo: string--><!--Device-URI-userInfo: string-End-->

**System capability:** SystemCapability.Utils.Lang

