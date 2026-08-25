# WebSocket

在调用WebSocket的方法前，需要先通过[webSocket.createWebSocket](arkts-network-websocket-createwebsocket-f.md)创建一个WebSocket。

**起始版本：** 6

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { webSocket } from 'kits/@kit.NetworkKit';
```

## close

```TypeScript
close(callback: AsyncCallback<boolean>): void
```

关闭WebSocket连接，使用callback异步回调。

**起始版本：** 6

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## close

```TypeScript
close(options: WebSocketCloseOptions, callback: AsyncCallback<boolean>): void
```

根据参数options，关闭WebSocket连接，使用callback异步回调。

**起始版本：** 6

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [WebSocketCloseOptions](arkts-network-websocket-websocketcloseoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## close

```TypeScript
close(options?: WebSocketCloseOptions): Promise<boolean>
```

根据可选参数code和reason，关闭WebSocket连接。使用Promise异步回调。

**起始版本：** 6

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [WebSocketCloseOptions](arkts-network-websocket-websocketcloseoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## connect

```TypeScript
connect(url: string, callback: AsyncCallback<boolean>): void
```

根据URL地址，建立一个WebSocket连接，使用callback异步回调。

> **说明：**&gt;
> callback中返回的boolean值仅表示连接请求创建是否成功。如需感知WebSocket是否连接成功，需要在调用该接口前调用
> on('open')订阅open事件。
> 
> **注意：**&gt;
> URL地址长度不能超过1024个字符，否则会连接失败。从API version 15开始，URL地址长度限制由1024修改为2048。从API version 26开始，URL地址长度限制由2048修改为8196。

**起始版本：** 6

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2302999](../errorcode-net-webSocket.md#2302999-内部错误) |
| [2302001](../errorcode-net-webSocket.md#2302001-websocket-url错误) |
| [2302002](../errorcode-net-webSocket.md#2302002-websocket-证书不存在) |
| [2302003](../errorcode-net-webSocket.md#2302003-websocket-连接已经存在) |
| [2302998](../errorcode-net-webSocket.md#2302998-不允许访问域名) |

## connect

```TypeScript
connect(url: string, options: WebSocketRequestOptions, callback: AsyncCallback<boolean>): void
```

根据URL地址，建立一个WebSocket连接，使用callback异步回调。

> **说明：**&gt;
> callback中返回的boolean值仅表示连接请求创建是否成功。如需感知WebSocket是否连接成功，需要在调用该接口前调用
> on('open')订阅open事件。
> 
> **注意：**&gt;
> URL地址长度不能超过1024个字符，否则会连接失败。从API version 15开始，URL地址长度限制由1024修改为2048。从API version 26开始，URL地址长度限制由2048修改为8196。

**起始版本：** 6

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| options | [WebSocketRequestOptions](arkts-network-websocket-websocketrequestoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2302999](../errorcode-net-webSocket.md#2302999-内部错误) |
| [2302001](../errorcode-net-webSocket.md#2302001-websocket-url错误) |
| [2302002](../errorcode-net-webSocket.md#2302002-websocket-证书不存在) |
| [2302003](../errorcode-net-webSocket.md#2302003-websocket-连接已经存在) |
| [2302998](../errorcode-net-webSocket.md#2302998-不允许访问域名) |

## connect

```TypeScript
connect(url: string, options?: WebSocketRequestOptions): Promise<boolean>
```

根据URL地址和header，建立一个WebSocket连接。使用Promise异步回调。

> **说明：**&gt;
> callback中返回的boolean值仅表示连接请求创建是否成功。如需感知WebSocket是否连接成功，需要在调用该接口前调用
> on('open')订阅open事件。
> 
> **注意：**&gt;
> URL地址长度不能超过1024个字符，否则会连接失败。从API version 15开始，URL地址长度限制由1024修改为2048。从API version 26开始，URL地址长度限制由2048修改为8196。

**起始版本：** 6

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| options | [WebSocketRequestOptions](arkts-network-websocket-websocketrequestoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2302999](../errorcode-net-webSocket.md#2302999-内部错误) |
| [2302001](../errorcode-net-webSocket.md#2302001-websocket-url错误) |
| [2302002](../errorcode-net-webSocket.md#2302002-websocket-证书不存在) |
| [2302003](../errorcode-net-webSocket.md#2302003-websocket-连接已经存在) |
| [2302998](../errorcode-net-webSocket.md#2302998-不允许访问域名) |

## off('open')

```TypeScript
off(type: 'open', callback?: AsyncCallback<Object>): void
```

取消订阅WebSocket的打开事件，使用callback异步回调。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'open' | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Object&gt; | 否 |

## off('openInfo')

```TypeScript
off(type: 'openInfo', callback?: AsyncCallback<WebSocketOpenInfo>): void
```

取消订阅WebSocket的打开信息事件，使用callback异步回调。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'openInfo' | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[WebSocketOpenInfo](arkts-network-websocket-websocketopeninfo-i.md)&gt; | 否 |

## off('message')

```TypeScript
off(type: 'message', callback?: AsyncCallback<string | ArrayBuffer>): void
```

取消订阅WebSocket的接收服务器消息事件，使用callback异步回调。

> **说明：**&gt;
> AsyncCallback中的数据可以是字符串(API 6)或ArrayBuffer(API 8)。&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'message' | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string \| ArrayBuffer & gt; | 否 |

## off('close')

```TypeScript
off(type: 'close', callback?: AsyncCallback<CloseResult>): void
```

取消订阅WebSocket的关闭事件，使用callback异步回调。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'close' | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CloseResult](arkts-network-websocket-closeresult-i.md)&gt; | 否 |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

取消订阅WebSocket的Error事件，使用callback异步回调。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

## off('dataEnd')

```TypeScript
off(type: 'dataEnd', callback?: Callback<void>): void
```

取消订阅WebSocket的数据接收结束事件，使用callback异步回调。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'dataEnd' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

## off('headerReceive')

```TypeScript
off(type: 'headerReceive', callback?: Callback<ResponseHeaders>): void
```

取消订阅HTTP Response Header事件，使用callback异步回调。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 12

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'headerReceive' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ResponseHeaders](arkts-network-websocket-responseheaders-t.md)&gt; | 否 |

## on('open')

```TypeScript
on(type: 'open', callback: AsyncCallback<Object>): void
```

订阅WebSocket的打开事件，使用callback异步回调。该事件用于指示WebSocket是否连接成功。该接口需要在调用 [connect](#connect)发起连接请求前调用。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'open' | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Object&gt; | 是 |

## on('message')

```TypeScript
on(type: 'message', callback: AsyncCallback<string | ArrayBuffer>): void
```

订阅WebSocket的接收服务器消息事件，使用callback异步回调。

> **说明：**&gt;
> AsyncCallback中的数据可以是字符串（API version 6开始支持）或ArrayBuffer（API version 8开始支持）。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'message' | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string \| ArrayBuffer & gt; | 是 |

## on('openInfo')

```TypeScript
on(type: 'openInfo', callback: AsyncCallback<WebSocketOpenInfo>): void
```

订阅WebSocket的打开信息事件，使用callback异步回调。该事件用于获取WebSocket连接成功后的详细信息。该接口需要在调用 [connect](#connect)发起连接请求前调用。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'openInfo' | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[WebSocketOpenInfo](arkts-network-websocket-websocketopeninfo-i.md)&gt; | 是 |

## on('close')

```TypeScript
on(type: 'close', callback: AsyncCallback<CloseResult>): void
```

订阅WebSocket的关闭事件，使用callback异步回调。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'close' | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CloseResult](arkts-network-websocket-closeresult-i.md)&gt; | 是 |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

订阅WebSocket的Error事件，使用callback异步回调。关于[error](#onerror)事件回调的错误码说明：WebSocket的本质是HTTP协议升级，若 服务器同意升级，服务器会返回101。状态码表示协议从HTTP切换为WebSocket协议（触发open回调），而如果服务器拒绝了升级或出现其他异常，则返回200，表示服务器只是将请求当作普通的HTTP请求来处理。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

## on('dataEnd')

```TypeScript
on(type: 'dataEnd', callback: Callback<void>): void
```

订阅WebSocket的数据接收结束事件，使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'dataEnd' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

## on('headerReceive')

```TypeScript
on(type: 'headerReceive', callback: Callback<ResponseHeaders>): void
```

订阅HTTP Response Header事件，使用callback异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'headerReceive' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ResponseHeaders](arkts-network-websocket-responseheaders-t.md)&gt; | 是 |

## send

```TypeScript
send(data: string | ArrayBuffer, callback: AsyncCallback<boolean>): void
```

通过WebSocket连接发送数据，使用callback异步回调。

**起始版本：** 6

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | string \| ArrayBuffer | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## send

```TypeScript
send(data: string | ArrayBuffer): Promise<boolean>
```

通过WebSocket连接发送数据。使用Promise异步回调。

**起始版本：** 6

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | string \| ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
