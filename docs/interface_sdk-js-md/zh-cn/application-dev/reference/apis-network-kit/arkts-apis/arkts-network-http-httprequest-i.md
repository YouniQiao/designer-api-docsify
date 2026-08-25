# HttpRequest

HTTP请求任务。在调用HttpRequest的方法前，需要先通过[createHttp()](arkts-network-http-createhttp-f.md)创建一个任务。

**起始版本：** 6

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## destroy

```TypeScript
destroy(): void
```

终止HTTP请求任务，同时释放系统资源。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

## enableAutoCookie

```TypeScript
enableAutoCookie(enable: boolean): void
```

设置是否自动携带和共享Cookie，用于在同一个HttpRequest实例的多次请求之间自动复用服务端下发的Cookie。

> **说明：**&gt;
> (1) 默认值为false，表示默认不自动携带Cookie。

> (2) 当配置由false切换为true后，会在后续调用request接口发起请求时生效，并自动共享Cookie。

> (3) 当配置由true切换为false时，会清空当前实例内保存的Cookie共享状态。

> (4) 关于重定向场景的Cookie处理：通过header字段手动配置的Cookie在发生重定向时不会自动发送给重定向后的目标主机，仅服务端通过Set-Cookie下发的Cookie会根据域名规则自动携带。

> (5) 关于跨域Cookie携带规则：Cookie的自动携带仅在相同域名或相同子域名之间生效，不同域名之间不支持Cookie的自动携带。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

## off("headerReceive")

```TypeScript
off(type: "headerReceive", callback?: AsyncCallback<Object>): void
```

取消订阅HTTP Response Header事件。

**起始版本：** 6

**废弃版本：** 8

**替代接口：** [off_headersReceive](#offheadersreceive)

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | "headerReceive" | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Object&gt; | 否 |

## off("headersReceive")

```TypeScript
off(type: "headersReceive", callback?: Callback<Object>): void
```

取消订阅HTTP Response Header 事件。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | "headersReceive" | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Object&gt; | 否 |

## off("dataReceive")

```TypeScript
off(type: "dataReceive", callback?: Callback<ArrayBuffer>): void
```

取消订阅HTTP流式响应数据接收事件。

**起始版本：** 10

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | "dataReceive" | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | 否 |

## off("dataEnd")

```TypeScript
off(type: "dataEnd", callback?: Callback<void>): void
```

取消订阅HTTP流式响应数据接收完毕事件。

**起始版本：** 10

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | "dataEnd" | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

## off('dataReceiveProgress')

```TypeScript
off(type: 'dataReceiveProgress', callback?: Callback<DataReceiveProgressInfo>): void
```

取消订阅HTTP流式响应数据接收进度事件。

**起始版本：** 10

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'dataReceiveProgress' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataReceiveProgressInfo](arkts-network-http-datareceiveprogressinfo-i.md)&gt; | 否 |

## off('dataSendProgress')

```TypeScript
off(type: 'dataSendProgress', callback?: Callback<DataSendProgressInfo>): void
```

取消订阅HTTP网络请求数据发送进度事件。

**起始版本：** 11

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'dataSendProgress' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataSendProgressInfo](arkts-network-http-datasendprogressinfo-i.md)&gt; | 否 |

## on("headerReceive")

```TypeScript
on(type: "headerReceive", callback: AsyncCallback<Object>): void
```

订阅HTTP Response Header 事件。

**起始版本：** 6

**废弃版本：** 8

**替代接口：** [on_headersReceive](#onheadersreceive)

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | "headerReceive" | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Object&gt; | 是 |

## on("headersReceive")

```TypeScript
on(type: "headersReceive", callback: Callback<Object>): void
```

订阅HTTP Response Header 事件。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | "headersReceive" | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Object&gt; | 是 |

## on("dataReceive")

```TypeScript
on(type: "dataReceive", callback: Callback<ArrayBuffer>): void
```

订阅HTTP流式响应数据接收事件。

**起始版本：** 10

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | "dataReceive" | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | 是 |

## on("dataEnd")

```TypeScript
on(type: "dataEnd", callback: Callback<void>): void
```

订阅HTTP流式响应数据接收完毕事件。

**起始版本：** 10

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | "dataEnd" | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

## on('dataReceiveProgress')

```TypeScript
on(type: 'dataReceiveProgress', callback: Callback<DataReceiveProgressInfo>): void
```

订阅HTTP流式响应数据接收进度事件。

**起始版本：** 10

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'dataReceiveProgress' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataReceiveProgressInfo](arkts-network-http-datareceiveprogressinfo-i.md)&gt; | 是 |

## on('dataSendProgress')

```TypeScript
on(type: 'dataSendProgress', callback: Callback<DataSendProgressInfo>): void
```

订阅HTTP网络请求数据发送进度事件。

**起始版本：** 11

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'dataSendProgress' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataSendProgressInfo](arkts-network-http-datasendprogressinfo-i.md)&gt; | 是 |

## once("headersReceive")

```TypeScript
once(type: "headersReceive", callback: Callback<Object>): void
```

订阅HTTP Response Header 事件，只能触发一次。触发之后，订阅器就会被移除。使用callback方式作为异步方法。

**起始版本：** 8

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | "headersReceive" | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Object&gt; | 是 |

## request

```TypeScript
request(url: string, callback: AsyncCallback<HttpResponse>): void
```

根据URL地址，发起HTTP网络请求，使用callback方式作为异步方法。

> **说明：**&gt;
> (1) 此接口仅支持接收5MB以内的数据，如果需要接收超过5MB的数据，则需主动在[HttpRequestOptions](arkts-network-http-httprequestoptions-i.md)的maxLimit中进行设置，或者使用
> [requestInStream](#requestinstream)接口发起流式请求。自
> API version 23开始，本接口支持的最大接收数据量为50MB，API version 23之前仍为5MB，超过5MB会接收失败。

> (2) 如需传入cookies，请开发者自行在参数options中添加。

> (3) 若URL包含中文或其他语言，需先调用encodeURL(URL)编码，再发起请求。

**起始版本：** 6

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HttpResponse&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2300001](../errorcode-net-http.md#2300001-不支持的协议) |
| [2300003](../errorcode-net-http.md#2300003-url格式错误) |
| [2300005](../errorcode-net-http.md#2300005-代理服务器域名解析失败) |
| [2300006](../errorcode-net-http.md#2300006-域名解析失败) |
| [2300007](../errorcode-net-http.md#2300007-无法连接到服务器) |
| [2300008](../errorcode-net-http.md#2300008-服务器返回非法数据) |
| [2300009](../errorcode-net-http.md#2300009-拒绝对远程资源的访问) |
| [2300016](../errorcode-net-http.md#2300016-http2帧层错误) |
| [2300018](../errorcode-net-http.md#2300018-服务器返回数据不完整) |
| [2300023](../errorcode-net-http.md#2300023-向磁盘应用程序写入接收数据失败) |
| [2300025](../errorcode-net-http.md#2300025-上传失败) |
| [2300026](../errorcode-net-http.md#2300026-从文件应用程序中打开读取本地数据失败) |
| [2300027](../errorcode-net-http.md#2300027-内存不足) |
| [2300028](../errorcode-net-http.md#2300028-操作超时) |
| [2300047](../errorcode-net-http.md#2300047-重定向次数达到最大值) |
| [2300052](../errorcode-net-http.md#2300052-服务器没有返回内容) |
| [2300055](../errorcode-net-http.md#2300055-发送网络数据失败) |
| [2300056](../errorcode-net-http.md#2300056-接收网络数据失败) |
| [2300058](../errorcode-net-http.md#2300058-本地ssl证书错误) |
| [2300059](../errorcode-net-http.md#2300059-无法使用指定的加密算法) |
| [2300060](../errorcode-net-http.md#2300060-远程服务器ssl证书或ssh密钥不正确) |
| [2300061](../errorcode-net-http.md#2300061-无法识别或错误的http编码格式) |
| [2300063](../errorcode-net-http.md#2300063-超出最大文件大小) |
| [2300070](../errorcode-net-http.md#2300070-服务器磁盘空间不足) |
| [2300073](../errorcode-net-http.md#2300073-服务器返回文件已存在) |
| [2300077](../errorcode-net-http.md#2300077-ssl-ca证书不存在或没有访问权限) |
| [2300078](../errorcode-net-http.md#2300078-url请求的文件不存在) |
| [2300094](../errorcode-net-http.md#2300094-身份校验失败) |
| [2300999](../errorcode-net-http.md#2300999-内部错误) |
| [2300998](../errorcode-net-http.md#2300998-不允许访问域名) |
| [2300997](../errorcode-net-http.md#2300997-明文http被拦截) |
| 2300996 |

## request

```TypeScript
request(url: string, options: HttpRequestOptions, callback: AsyncCallback<HttpResponse>): void
```

根据URL地址和相关配置项，发起HTTP网络请求，使用callback方式作为异步方法。

> **说明：**&gt;
> (1) 此接口仅支持接收5MB以内的数据，如果需要接收超过5MB的数据，则需主动在[HttpRequestOptions](arkts-network-http-httprequestoptions-i.md)的maxLimit中进行设置，或者使用
> [requestInStream](#requestinstream)接口发起流式请求。自
> API version 23开始，本接口支持的最大接收数据量为50MB，API version 23之前仍为5MB，超过5MB会接收失败。

> (2) 如需传入cookies，请开发者自行在参数options中添加。

> (3) 若URL包含中文或其他语言，需先调用encodeURL(URL)编码，再发起请求。

**起始版本：** 6

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| options | [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HttpResponse&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2300001](../errorcode-net-http.md#2300001-不支持的协议) |
| [2300003](../errorcode-net-http.md#2300003-url格式错误) |
| [2300005](../errorcode-net-http.md#2300005-代理服务器域名解析失败) |
| [2300006](../errorcode-net-http.md#2300006-域名解析失败) |
| [2300007](../errorcode-net-http.md#2300007-无法连接到服务器) |
| [2300008](../errorcode-net-http.md#2300008-服务器返回非法数据) |
| [2300009](../errorcode-net-http.md#2300009-拒绝对远程资源的访问) |
| [2300016](../errorcode-net-http.md#2300016-http2帧层错误) |
| [2300018](../errorcode-net-http.md#2300018-服务器返回数据不完整) |
| [2300023](../errorcode-net-http.md#2300023-向磁盘应用程序写入接收数据失败) |
| [2300025](../errorcode-net-http.md#2300025-上传失败) |
| [2300026](../errorcode-net-http.md#2300026-从文件应用程序中打开读取本地数据失败) |
| [2300027](../errorcode-net-http.md#2300027-内存不足) |
| [2300028](../errorcode-net-http.md#2300028-操作超时) |
| [2300047](../errorcode-net-http.md#2300047-重定向次数达到最大值) |
| [2300052](../errorcode-net-http.md#2300052-服务器没有返回内容) |
| [2300055](../errorcode-net-http.md#2300055-发送网络数据失败) |
| [2300056](../errorcode-net-http.md#2300056-接收网络数据失败) |
| [2300058](../errorcode-net-http.md#2300058-本地ssl证书错误) |
| [2300059](../errorcode-net-http.md#2300059-无法使用指定的加密算法) |
| [2300060](../errorcode-net-http.md#2300060-远程服务器ssl证书或ssh密钥不正确) |
| [2300061](../errorcode-net-http.md#2300061-无法识别或错误的http编码格式) |
| [2300063](../errorcode-net-http.md#2300063-超出最大文件大小) |
| [2300070](../errorcode-net-http.md#2300070-服务器磁盘空间不足) |
| [2300073](../errorcode-net-http.md#2300073-服务器返回文件已存在) |
| [2300077](../errorcode-net-http.md#2300077-ssl-ca证书不存在或没有访问权限) |
| [2300078](../errorcode-net-http.md#2300078-url请求的文件不存在) |
| [2300094](../errorcode-net-http.md#2300094-身份校验失败) |
| [2300999](../errorcode-net-http.md#2300999-内部错误) |
| [2300998](../errorcode-net-http.md#2300998-不允许访问域名) |
| [2300997](../errorcode-net-http.md#2300997-明文http被拦截) |
| 2300996 |

## request

```TypeScript
request(url: string, options?: HttpRequestOptions): Promise<HttpResponse>
```

根据URL地址，发起HTTP网络请求，使用Promise方式作为异步方法。

> **说明：**&gt;
> (1) 此接口仅支持接收5MB以内的数据，如果需要接收超过5MB的数据，则需主动在[HttpRequestOptions](arkts-network-http-httprequestoptions-i.md)的maxLimit中进行设置，或者使用
> [requestInStream](#requestinstream)接口发起流式请求。自
> API version 23开始，本接口支持的最大接收数据量为50MB，API version 23之前仍为5MB，超过5MB会接收失败。

> (2) 如需传入cookies，请开发者自行在参数options中添加。

> (3) 若URL包含中文或其他语言，需先调用encodeURL(URL)编码，再发起请求。

**起始版本：** 6

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| options | [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;HttpResponse & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2300001](../errorcode-net-http.md#2300001-不支持的协议) |
| [2300003](../errorcode-net-http.md#2300003-url格式错误) |
| [2300005](../errorcode-net-http.md#2300005-代理服务器域名解析失败) |
| [2300006](../errorcode-net-http.md#2300006-域名解析失败) |
| [2300007](../errorcode-net-http.md#2300007-无法连接到服务器) |
| [2300008](../errorcode-net-http.md#2300008-服务器返回非法数据) |
| [2300009](../errorcode-net-http.md#2300009-拒绝对远程资源的访问) |
| [2300016](../errorcode-net-http.md#2300016-http2帧层错误) |
| [2300018](../errorcode-net-http.md#2300018-服务器返回数据不完整) |
| [2300023](../errorcode-net-http.md#2300023-向磁盘应用程序写入接收数据失败) |
| [2300025](../errorcode-net-http.md#2300025-上传失败) |
| [2300026](../errorcode-net-http.md#2300026-从文件应用程序中打开读取本地数据失败) |
| [2300027](../errorcode-net-http.md#2300027-内存不足) |
| [2300028](../errorcode-net-http.md#2300028-操作超时) |
| [2300047](../errorcode-net-http.md#2300047-重定向次数达到最大值) |
| [2300052](../errorcode-net-http.md#2300052-服务器没有返回内容) |
| [2300055](../errorcode-net-http.md#2300055-发送网络数据失败) |
| [2300056](../errorcode-net-http.md#2300056-接收网络数据失败) |
| [2300058](../errorcode-net-http.md#2300058-本地ssl证书错误) |
| [2300059](../errorcode-net-http.md#2300059-无法使用指定的加密算法) |
| [2300060](../errorcode-net-http.md#2300060-远程服务器ssl证书或ssh密钥不正确) |
| [2300061](../errorcode-net-http.md#2300061-无法识别或错误的http编码格式) |
| [2300063](../errorcode-net-http.md#2300063-超出最大文件大小) |
| [2300070](../errorcode-net-http.md#2300070-服务器磁盘空间不足) |
| [2300073](../errorcode-net-http.md#2300073-服务器返回文件已存在) |
| [2300077](../errorcode-net-http.md#2300077-ssl-ca证书不存在或没有访问权限) |
| [2300078](../errorcode-net-http.md#2300078-url请求的文件不存在) |
| [2300094](../errorcode-net-http.md#2300094-身份校验失败) |
| [2300999](../errorcode-net-http.md#2300999-内部错误) |
| [2300998](../errorcode-net-http.md#2300998-不允许访问域名) |
| [2300997](../errorcode-net-http.md#2300997-明文http被拦截) |
| 2300996 |

## requestInStream

```TypeScript
requestInStream(url: string, callback: AsyncCallback<number>): void
```

根据URL地址，发起HTTP网络请求并返回流式响应，使用callback方式作为异步方法。

**起始版本：** 10

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2300001](../errorcode-net-http.md#2300001-不支持的协议) |
| [2300003](../errorcode-net-http.md#2300003-url格式错误) |
| [2300005](../errorcode-net-http.md#2300005-代理服务器域名解析失败) |
| [2300006](../errorcode-net-http.md#2300006-域名解析失败) |
| [2300007](../errorcode-net-http.md#2300007-无法连接到服务器) |
| [2300008](../errorcode-net-http.md#2300008-服务器返回非法数据) |
| [2300009](../errorcode-net-http.md#2300009-拒绝对远程资源的访问) |
| [2300016](../errorcode-net-http.md#2300016-http2帧层错误) |
| [2300018](../errorcode-net-http.md#2300018-服务器返回数据不完整) |
| [2300023](../errorcode-net-http.md#2300023-向磁盘应用程序写入接收数据失败) |
| [2300025](../errorcode-net-http.md#2300025-上传失败) |
| [2300026](../errorcode-net-http.md#2300026-从文件应用程序中打开读取本地数据失败) |
| [2300027](../errorcode-net-http.md#2300027-内存不足) |
| [2300028](../errorcode-net-http.md#2300028-操作超时) |
| [2300047](../errorcode-net-http.md#2300047-重定向次数达到最大值) |
| [2300052](../errorcode-net-http.md#2300052-服务器没有返回内容) |
| [2300055](../errorcode-net-http.md#2300055-发送网络数据失败) |
| [2300056](../errorcode-net-http.md#2300056-接收网络数据失败) |
| [2300058](../errorcode-net-http.md#2300058-本地ssl证书错误) |
| [2300059](../errorcode-net-http.md#2300059-无法使用指定的加密算法) |
| [2300060](../errorcode-net-http.md#2300060-远程服务器ssl证书或ssh密钥不正确) |
| [2300061](../errorcode-net-http.md#2300061-无法识别或错误的http编码格式) |
| [2300063](../errorcode-net-http.md#2300063-超出最大文件大小) |
| [2300070](../errorcode-net-http.md#2300070-服务器磁盘空间不足) |
| [2300073](../errorcode-net-http.md#2300073-服务器返回文件已存在) |
| [2300077](../errorcode-net-http.md#2300077-ssl-ca证书不存在或没有访问权限) |
| [2300078](../errorcode-net-http.md#2300078-url请求的文件不存在) |
| [2300094](../errorcode-net-http.md#2300094-身份校验失败) |
| [2300999](../errorcode-net-http.md#2300999-内部错误) |
| [2300998](../errorcode-net-http.md#2300998-不允许访问域名) |
| [2300997](../errorcode-net-http.md#2300997-明文http被拦截) |
| 2300996 |

## requestInStream

```TypeScript
requestInStream(url: string, options: HttpRequestOptions, callback: AsyncCallback<number>): void
```

根据URL地址和相关配置项，发起HTTP网络请求并返回流式响应，使用callback方式作为异步方法。

**起始版本：** 10

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| options | [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2300001](../errorcode-net-http.md#2300001-不支持的协议) |
| [2300003](../errorcode-net-http.md#2300003-url格式错误) |
| [2300005](../errorcode-net-http.md#2300005-代理服务器域名解析失败) |
| [2300006](../errorcode-net-http.md#2300006-域名解析失败) |
| [2300007](../errorcode-net-http.md#2300007-无法连接到服务器) |
| [2300008](../errorcode-net-http.md#2300008-服务器返回非法数据) |
| [2300009](../errorcode-net-http.md#2300009-拒绝对远程资源的访问) |
| [2300016](../errorcode-net-http.md#2300016-http2帧层错误) |
| [2300018](../errorcode-net-http.md#2300018-服务器返回数据不完整) |
| [2300023](../errorcode-net-http.md#2300023-向磁盘应用程序写入接收数据失败) |
| [2300025](../errorcode-net-http.md#2300025-上传失败) |
| [2300026](../errorcode-net-http.md#2300026-从文件应用程序中打开读取本地数据失败) |
| [2300027](../errorcode-net-http.md#2300027-内存不足) |
| [2300028](../errorcode-net-http.md#2300028-操作超时) |
| [2300047](../errorcode-net-http.md#2300047-重定向次数达到最大值) |
| [2300052](../errorcode-net-http.md#2300052-服务器没有返回内容) |
| [2300055](../errorcode-net-http.md#2300055-发送网络数据失败) |
| [2300056](../errorcode-net-http.md#2300056-接收网络数据失败) |
| [2300058](../errorcode-net-http.md#2300058-本地ssl证书错误) |
| [2300059](../errorcode-net-http.md#2300059-无法使用指定的加密算法) |
| [2300060](../errorcode-net-http.md#2300060-远程服务器ssl证书或ssh密钥不正确) |
| [2300061](../errorcode-net-http.md#2300061-无法识别或错误的http编码格式) |
| [2300063](../errorcode-net-http.md#2300063-超出最大文件大小) |
| [2300070](../errorcode-net-http.md#2300070-服务器磁盘空间不足) |
| [2300073](../errorcode-net-http.md#2300073-服务器返回文件已存在) |
| [2300077](../errorcode-net-http.md#2300077-ssl-ca证书不存在或没有访问权限) |
| [2300078](../errorcode-net-http.md#2300078-url请求的文件不存在) |
| [2300094](../errorcode-net-http.md#2300094-身份校验失败) |
| [2300999](../errorcode-net-http.md#2300999-内部错误) |
| [2300998](../errorcode-net-http.md#2300998-不允许访问域名) |
| [2300997](../errorcode-net-http.md#2300997-明文http被拦截) |
| 2300996 |

## requestInStream

```TypeScript
requestInStream(url: string, options?: HttpRequestOptions): Promise<number>
```

根据URL地址，发起HTTP网络请求并返回流式响应，使用Promise方式作为异步方法。

**起始版本：** 10

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| options | [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2300001](../errorcode-net-http.md#2300001-不支持的协议) |
| [2300003](../errorcode-net-http.md#2300003-url格式错误) |
| [2300005](../errorcode-net-http.md#2300005-代理服务器域名解析失败) |
| [2300006](../errorcode-net-http.md#2300006-域名解析失败) |
| [2300007](../errorcode-net-http.md#2300007-无法连接到服务器) |
| [2300008](../errorcode-net-http.md#2300008-服务器返回非法数据) |
| [2300009](../errorcode-net-http.md#2300009-拒绝对远程资源的访问) |
| [2300016](../errorcode-net-http.md#2300016-http2帧层错误) |
| [2300018](../errorcode-net-http.md#2300018-服务器返回数据不完整) |
| [2300023](../errorcode-net-http.md#2300023-向磁盘应用程序写入接收数据失败) |
| [2300025](../errorcode-net-http.md#2300025-上传失败) |
| [2300026](../errorcode-net-http.md#2300026-从文件应用程序中打开读取本地数据失败) |
| [2300027](../errorcode-net-http.md#2300027-内存不足) |
| [2300028](../errorcode-net-http.md#2300028-操作超时) |
| [2300047](../errorcode-net-http.md#2300047-重定向次数达到最大值) |
| [2300052](../errorcode-net-http.md#2300052-服务器没有返回内容) |
| [2300055](../errorcode-net-http.md#2300055-发送网络数据失败) |
| [2300056](../errorcode-net-http.md#2300056-接收网络数据失败) |
| [2300058](../errorcode-net-http.md#2300058-本地ssl证书错误) |
| [2300059](../errorcode-net-http.md#2300059-无法使用指定的加密算法) |
| [2300060](../errorcode-net-http.md#2300060-远程服务器ssl证书或ssh密钥不正确) |
| [2300061](../errorcode-net-http.md#2300061-无法识别或错误的http编码格式) |
| [2300063](../errorcode-net-http.md#2300063-超出最大文件大小) |
| [2300070](../errorcode-net-http.md#2300070-服务器磁盘空间不足) |
| [2300073](../errorcode-net-http.md#2300073-服务器返回文件已存在) |
| [2300077](../errorcode-net-http.md#2300077-ssl-ca证书不存在或没有访问权限) |
| [2300078](../errorcode-net-http.md#2300078-url请求的文件不存在) |
| [2300094](../errorcode-net-http.md#2300094-身份校验失败) |
| [2300999](../errorcode-net-http.md#2300999-内部错误) |
| [2300998](../errorcode-net-http.md#2300998-不允许访问域名) |
| [2300997](../errorcode-net-http.md#2300997-明文http被拦截) |
| 2300996 |

## requestSync

```TypeScript
requestSync(url: string, options?: HttpRequestOptions): HttpResponse
```

根据URL地址、相关配置项（可选），发起HTTP网络请求，同步返回响应结果。

> **说明：**&gt;
> (1) 此接口仅支持接收50MB以内的数据，如果需要接收超过50MB的数据，则需主动在[HttpRequestOptions](arkts-network-http-httprequestoptions-i.md)的maxLimit中进行设置。

> (2) 如需传入cookies，请开发者自行在参数options中添加。

> (3) 若URL包含中文或其他语言，需先调用encodeURL(URL)编码，再发起请求。

> (4) 此接口为同步接口，会阻塞当前线程直到返回HTTP请求响应结果或错误码。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.INTERNET

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| options | [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [HttpResponse](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-httpresponse-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2300001](../errorcode-net-http.md#2300001-不支持的协议) |
| [2300003](../errorcode-net-http.md#2300003-url格式错误) |
| [2300005](../errorcode-net-http.md#2300005-代理服务器域名解析失败) |
| [2300006](../errorcode-net-http.md#2300006-域名解析失败) |
| [2300007](../errorcode-net-http.md#2300007-无法连接到服务器) |
| [2300008](../errorcode-net-http.md#2300008-服务器返回非法数据) |
| [2300009](../errorcode-net-http.md#2300009-拒绝对远程资源的访问) |
| [2300016](../errorcode-net-http.md#2300016-http2帧层错误) |
| [2300018](../errorcode-net-http.md#2300018-服务器返回数据不完整) |
| [2300023](../errorcode-net-http.md#2300023-向磁盘应用程序写入接收数据失败) |
| [2300025](../errorcode-net-http.md#2300025-上传失败) |
| [2300026](../errorcode-net-http.md#2300026-从文件应用程序中打开读取本地数据失败) |
| [2300027](../errorcode-net-http.md#2300027-内存不足) |
| [2300028](../errorcode-net-http.md#2300028-操作超时) |
| [2300047](../errorcode-net-http.md#2300047-重定向次数达到最大值) |
| [2300052](../errorcode-net-http.md#2300052-服务器没有返回内容) |
| [2300055](../errorcode-net-http.md#2300055-发送网络数据失败) |
| [2300056](../errorcode-net-http.md#2300056-接收网络数据失败) |
| [2300058](../errorcode-net-http.md#2300058-本地ssl证书错误) |
| [2300059](../errorcode-net-http.md#2300059-无法使用指定的加密算法) |
| [2300060](../errorcode-net-http.md#2300060-远程服务器ssl证书或ssh密钥不正确) |
| [2300061](../errorcode-net-http.md#2300061-无法识别或错误的http编码格式) |
| [2300063](../errorcode-net-http.md#2300063-超出最大文件大小) |
| [2300070](../errorcode-net-http.md#2300070-服务器磁盘空间不足) |
| [2300073](../errorcode-net-http.md#2300073-服务器返回文件已存在) |
| [2300077](../errorcode-net-http.md#2300077-ssl-ca证书不存在或没有访问权限) |
| [2300078](../errorcode-net-http.md#2300078-url请求的文件不存在) |
| [2300094](../errorcode-net-http.md#2300094-身份校验失败) |
| 2300996 |
| [2300997](../errorcode-net-http.md#2300997-明文http被拦截) |
| [2300998](../errorcode-net-http.md#2300998-不允许访问域名) |
| [2300999](../errorcode-net-http.md#2300999-内部错误) |
