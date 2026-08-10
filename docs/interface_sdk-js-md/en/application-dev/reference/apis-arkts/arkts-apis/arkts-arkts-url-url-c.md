# URL

用于解析和构造完整URL。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-url-class URL--><!--Device-url-class URL-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { url } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor(url: string, base?: string | URL)
```

URL的构造函数。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.url.URL.parseURL

<!--Device-URL-constructor(url: string, base?: string | URL)--><!--Device-URL-constructor(url: string, base?: string | URL)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | 一个表示绝对URL或相对URL的字符串。 &lt;br/&gt;如果 url 是相对URL，则需要指定 base，用于解析最终的URL。 &lt;br/&gt;如果 url 是绝对URL，则给定的 base 将不会生效。 |
| base | string \| URL | No | 入参字符串或者对象，默认值是undefined。&lt;br/&gt;- string：字符串。&lt;br/&gt;- URL：URL对象。 |

## constructor

```TypeScript
constructor()
```

URL的无参构造函数。parseURL调用后返回一个URL对象，不单独使用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URL-constructor()--><!--Device-URL-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## parseURL

```TypeScript
static parseURL(url: string, base?: string | URL): URL
```

解析URL字符串，返回解析后的URL对象。该对象包含协议、主机、端口、路径和查询参数等URL组成部分。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URL-static parseURL(url: string, base?: string | URL): URL--><!--Device-URL-static parseURL(url: string, base?: string | URL): URL-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | 一个表示绝对URL或相对URL的字符串。 &lt;br/&gt;如果 url 是相对URL，则需要指定 base，用于解析最终的URL。 &lt;br/&gt;如果 url 是绝对URL，则给定的 base 将不会生效。 |
| base | string \| URL | No | 入参字符串或者对象，默认值是undefined。&lt;br/&gt;- string：字符串。当第一个参数是相对URL时，该参数需符合URL标准。&lt;br/&gt;- URL：URL对象。&lt;br/&gt;- 在url是相对URL时使用，url为绝对URL时此参数不会生效。 |

**Return value:**

| Type | Description |
| --- | --- |
| [URL](arkts-arkts-url-url-c.md) | 返回解析后的URL对象，包含URL的各组成部分（如协议、主机和路径等属性）。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200002 | Invalid url string. |

## Examples

```TypeScript
let mm = 'https://username:password@host:8080/test/test1/test3';
let urlObject = url.URL.parseURL(mm);
let result = urlObject.toString(); // Output 'https://username:password@host:8080/test/test1/test3'
// If url is a relative path, the path in the base parameter is test/test1, and the path of the parsed URL is /test/path2/path3.
let url1 = url.URL.parseURL('path2/path3', 'https://www.example.com/test/test1'); // Output 'https://www.example.com/test/path2/path3'
// If url is a root directory, the path in the base parameter is /test/test1/test3, and the path of the parsed URL is /path1/path2.
let url2 = url.URL.parseURL('/path1/path2', urlObject); // Output 'https://username:password@host:8080/path1/path2'
url.URL.parseURL('/path/path1', "https://www.exampleUrl/fr-FR/toot"); // Output 'https://www.exampleUrl/path/path1'
url.URL.parseURL('/path/path1', ''); // Raises a TypeError exception as '' is not a valid URL
url.URL.parseURL('/path/path1'); // Raises a TypeError exception as '/path/path1' is not a valid URL
url.URL.parseURL('https://www.example.com', ); // Output 'https://www.example.com/'
url.URL.parseURL('https://www.example.com', urlObject); // Output 'https://www.example.com/'
```

## toJSON

```TypeScript
toJSON(): string
```

将解析过后的URL转化为JSON字符串。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URL-toJSON(): string--><!--Device-URL-toJSON(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | URL对象的JSON序列化字符串。 |

## Examples

```TypeScript
const urlObject = url.URL.parseURL('https://username:password@host:8080/directory/file?query=pppppp#qwer=da');
let result = urlObject.toJSON();
```

## toString

```TypeScript
toString(): string
```

将解析过后的URL转化为字符串，返回值与URL的href属性值相同。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URL-toString(): string--><!--Device-URL-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | 解析后的URL序列化字符串。 |

## Examples

```TypeScript
const urlObject = url.URL.parseURL('https://username:password@host:8080/directory/file?query=pppppp#qwer=da');
let result = urlObject.toString(); // Output 'https://username:password@host:8080/directory/file?query=pppppp#qwer=da'
```

## hash

```TypeScript
hash: string
```

获取和设置URL的片段部分。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URL-hash: string--><!--Device-URL-hash: string-End-->

**System capability:** SystemCapability.Utils.Lang

## host

```TypeScript
host: string
```

获取和设置URL的主机部分。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URL-host: string--><!--Device-URL-host: string-End-->

**System capability:** SystemCapability.Utils.Lang

## hostname

```TypeScript
hostname: string
```

获取和设置URL的主机名部分，不带端口。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URL-hostname: string--><!--Device-URL-hostname: string-End-->

**System capability:** SystemCapability.Utils.Lang

## href

```TypeScript
href: string
```

获取和设置序列化的URL。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URL-href: string--><!--Device-URL-href: string-End-->

**System capability:** SystemCapability.Utils.Lang

## origin

```TypeScript
readonly origin: string
```

获取URL源的只读序列化。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URL-readonly origin: string--><!--Device-URL-readonly origin: string-End-->

**System capability:** SystemCapability.Utils.Lang

## params

```TypeScript
readonly params: URLParams
```

获取URLParams表示URL查询参数的对象。

**Type:** [URLParams](arkts-arkts-url-urlparams-c.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URL-readonly params: URLParams--><!--Device-URL-readonly params: URLParams-End-->

**System capability:** SystemCapability.Utils.Lang

## password

```TypeScript
password: string
```

获取和设置URL的密码部分。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URL-password: string--><!--Device-URL-password: string-End-->

**System capability:** SystemCapability.Utils.Lang

## pathname

```TypeScript
pathname: string
```

获取和设置URL的路径部分。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URL-pathname: string--><!--Device-URL-pathname: string-End-->

**System capability:** SystemCapability.Utils.Lang

## port

```TypeScript
port: string
```

获取和设置URL的端口部分。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URL-port: string--><!--Device-URL-port: string-End-->

**System capability:** SystemCapability.Utils.Lang

## protocol

```TypeScript
protocol: string
```

获取和设置URL的协议部分。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URL-protocol: string--><!--Device-URL-protocol: string-End-->

**System capability:** SystemCapability.Utils.Lang

## search

```TypeScript
search: string
```

获取和设置URL的序列化查询部分。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URL-search: string--><!--Device-URL-search: string-End-->

**System capability:** SystemCapability.Utils.Lang

## searchParams

```TypeScript
readonly searchParams: URLSearchParams
```

获取URLSearchParams表示URL查询参数的对象。

**Type:** [URLSearchParams](arkts-arkts-url-urlsearchparams-c.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.url.URLParams

<!--Device-URL-readonly searchParams: URLSearchParams--><!--Device-URL-readonly searchParams: URLSearchParams-End-->

**System capability:** SystemCapability.Utils.Lang

## username

```TypeScript
username: string
```

获取和设置URL的用户名部分。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URL-username: string--><!--Device-URL-username: string-End-->

**System capability:** SystemCapability.Utils.Lang

