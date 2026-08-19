# WebSocket

Defines a **WebSocket** object. Before invoking WebSocket APIs, you need to call [webSocket.createWebSocket](arkts-network-websocket-createwebsocket-f.md) to create a **WebSocket** object.

**Since:** 23

<!--Device-webSocket-export interface WebSocket--><!--Device-webSocket-export interface WebSocket-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { webSocket } from '@kit.NetworkKit';
```

## close

```TypeScript
close(callback: AsyncCallback<boolean>): void
```

Closes the WebSocket connection. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebSocket-close(callback: AsyncCallback<boolean>): void--><!--Device-WebSocket-close(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
ws.close((err: BusinessError) => {
  if (!err) {
    console.info("close success")
  } else {
    console.error(`close fail. Code: ${err.code}, message: ${err.message}`)
  }
});
```

## close

```TypeScript
close(options: WebSocketCloseOptions, callback: AsyncCallback<boolean>): void
```

Closes the WebSocket connection based on the options parameter. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebSocket-close(options: WebSocketCloseOptions, callback: AsyncCallback<boolean>): void--><!--Device-WebSocket-close(options: WebSocketCloseOptions, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [WebSocketCloseOptions](arkts-network-websocket-websocketcloseoptions-i.md) | Yes | Request options. For details, see [WebSocketCloseOptions](arkts-network-websocket-websocketcloseoptions-i.md). |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();

let options: webSocket.WebSocketCloseOptions | undefined;
if (options != undefined) {
    options.code = 1000
    options.reason = "your reason"
}
ws.close(options, (err: BusinessError) => {
    if (!err) {
        console.info("close success")
    } else {
        console.error(`close fail. Code: ${err.code}, message: ${err.message}`)
    }
});
```

## close

```TypeScript
close(options?: WebSocketCloseOptions): Promise<boolean>
```

Closes a WebSocket connection based on the specified options. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebSocket-close(options?: WebSocketCloseOptions): Promise<boolean>--><!--Device-WebSocket-close(options?: WebSocketCloseOptions): Promise<boolean>-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [WebSocketCloseOptions](arkts-network-websocket-websocketcloseoptions-i.md) | No | Request options. For details, see [WebSocketCloseOptions](arkts-network-websocket-websocketcloseoptions-i.md). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
let options: webSocket.WebSocketCloseOptions | undefined;
if (options != undefined) {
    options.code = 1000
    options.reason = "your reason"
}
let promise = ws.close();
promise.then((value: boolean) => {
    console.info("close success")
}).catch((err:string) => {
    console.error("close fail, error:" + JSON.stringify(err))
});
```

## connect

```TypeScript
connect(url: string, callback: AsyncCallback<boolean>): void
```

Initiates a WebSocket request to establish a WebSocket connection to a given URL. This API uses an asynchronous callback to return the result. > **NOTE：**> > The boolean value returned in the callback indicates only whether the connection request is created > successfully. To detect whether the WebSocket connection is successful, you need to subscribe to the **open** > event via [on('open')](#on_openopen) before > calling this API. > > **NOTE：**> > The URL cannot contain more than 1024 characters. Otherwise, the connection fails. Since API version 15, the > maximum length of URLs is changed from 1024 characters to 2048 characters. Since API version 26, the maximum > length of URLs is changed from 2048 characters to 8196 characters.

**Since:** 23

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebSocket-connect(url: string, callback: AsyncCallback<boolean>): void--><!--Device-WebSocket-connect(url: string, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | URL for establishing a WebSocket connection. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2302003](../errorcode-net-webSocket.md#2302003-websocket-connection-already-exists) | Websocket connection already exists.<br>**Applicable version:** 12 and later |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2302002](../errorcode-net-webSocket.md#2302002-websocket-certificate-does-not-exist) | Websocket certificate file does not exist.<br>**Applicable version:** 12 and later |
| [2302001](../errorcode-net-webSocket.md#2302001-websocket-url-error) | Websocket url error.<br>**Applicable version:** 12 and later |
| [2302999](../errorcode-net-webSocket.md#2302999-internal-error) | Websocket other unknown error.<br>**Applicable version:** 10 and later |
| [2302998](../errorcode-net-webSocket.md#2302998-domain-access-denied) | It is not allowed to access this domain.<br>**Applicable version:** 12 and later |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
let url = "ws://";
ws.connect(url, (err: BusinessError, value: boolean) => {
  if (!err) {
    console.info("connect success")
  } else {
    console.error(`connect fail. Code: ${err.code}, message: ${err.message}`)
  }
});
```

## connect

```TypeScript
connect(url: string, options: WebSocketRequestOptions, callback: AsyncCallback<boolean>): void
```

Initiates a WebSocket request to establish a WebSocket connection to a given URL. This API uses an asynchronous callback to return the result. > **NOTE：**> > The boolean value returned in the callback indicates only whether the connection request is created > successfully. To detect whether the WebSocket connection is successful, you need to subscribe to the **open** > event via [on('open')](#on_openopen) before > calling this API. > > **NOTE：**> > The URL cannot contain more than 1024 characters. Otherwise, the connection fails. Since API version 15, the > maximum length of URLs is changed from 1024 characters to 2048 characters. Since API version 26, the maximum > length of URLs is changed from 2048 characters to 8196 characters.

**Since:** 23

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebSocket-connect(url: string, options: WebSocketRequestOptions, callback: AsyncCallback<boolean>): void--><!--Device-WebSocket-connect(url: string, options: WebSocketRequestOptions, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | URL for establishing a WebSocket connection. |
| options | [WebSocketRequestOptions](arkts-network-websocket-websocketrequestoptions-i.md) | Yes | Request options. For details, see [WebSocketRequestOptions](arkts-network-websocket-websocketrequestoptions-i.md). |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2302003](../errorcode-net-webSocket.md#2302003-websocket-connection-already-exists) | Websocket connection already exists.<br>**Applicable version:** 12 and later |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2302002](../errorcode-net-webSocket.md#2302002-websocket-certificate-does-not-exist) | Websocket certificate file does not exist.<br>**Applicable version:** 12 and later |
| [2302001](../errorcode-net-webSocket.md#2302001-websocket-url-error) | Websocket url error.<br>**Applicable version:** 12 and later |
| [2302999](../errorcode-net-webSocket.md#2302999-internal-error) | Websocket other unknown error.<br>**Applicable version:** 10 and later |
| [2302998](../errorcode-net-webSocket.md#2302998-domain-access-denied) | It is not allowed to access this domain.<br>**Applicable version:** 12 and later |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Example 1:
let ws = webSocket.createWebSocket();
let options: webSocket.WebSocketRequestOptions | undefined;
if (options !=undefined) {
  options.header = {
     name1: "value1",
     name2: "value2",
     name3: "value3"
  };
  options.caPath = "";
}
let url = "ws://"
ws.connect(url, options, (err: BusinessError, value: Object) => {
  if (!err) {
    console.info("connect success")
  } else {
    console.error(`connect fail. Code: ${err.code}, message: ${err.message}`)
  }
});

// Example 2:
let url = "ws://"
let ws = webSocket.createWebSocket();
let options: webSocket.WebSocketRequestOptions = {
  minSupportTlsProtocol: webSocket.TlsProtocol.TLS_V_1_1
};
ws.connect(url, options, (err: BusinessError, value: Object) => {
  if (!err) {
    console.info("connect success")
  } else {
    console.error(`connect fail. Code: ${err.code}, message: ${err.message}`)
  }
});
```

## connect

```TypeScript
connect(url: string, options?: WebSocketRequestOptions): Promise<boolean>
```

Establishes a WebSocket connection to a given URL. This API uses a promise to return the result. > **NOTE：**> > The boolean value returned in the callback indicates only whether the connection request is created > successfully. To detect whether the WebSocket connection is successful, you need to subscribe to the **open** > event via [on('open')](#on_openopen) before > calling this API. > > **NOTE：**> > The URL cannot contain more than 1024 characters. Otherwise, the connection fails. Since API version 15, the > maximum length of URLs is changed from 1024 characters to 2048 characters. Since API version 26, the maximum > length of URLs is changed from 2048 characters to 8196 characters.

**Since:** 23

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebSocket-connect(url: string, options?: WebSocketRequestOptions): Promise<boolean>--><!--Device-WebSocket-connect(url: string, options?: WebSocketRequestOptions): Promise<boolean>-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | URL for establishing a WebSocket connection. |
| options | [WebSocketRequestOptions](arkts-network-websocket-websocketrequestoptions-i.md) | No | Request options. For details, see [WebSocketRequestOptions](arkts-network-websocket-websocketrequestoptions-i.md). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Callback used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2302003](../errorcode-net-webSocket.md#2302003-websocket-connection-already-exists) | Websocket connection already exists.<br>**Applicable version:** 12 and later |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2302002](../errorcode-net-webSocket.md#2302002-websocket-certificate-does-not-exist) | Websocket certificate file does not exist.<br>**Applicable version:** 12 and later |
| [2302001](../errorcode-net-webSocket.md#2302001-websocket-url-error) | Websocket url error.<br>**Applicable version:** 12 and later |
| [2302999](../errorcode-net-webSocket.md#2302999-internal-error) | Websocket other unknown error.<br>**Applicable version:** 10 and later |
| [2302998](../errorcode-net-webSocket.md#2302998-domain-access-denied) | It is not allowed to access this domain.<br>**Applicable version:** 12 and later |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
let url = "ws://"
let promise = ws.connect(url);
promise.then((value: boolean) => {
  console.info("connect success")
}).catch((err:string) => {
  console.error("connect fail, error:" + JSON.stringify(err))
});
```

## offDataEnd

```TypeScript
offDataEnd(callback?: Callback<void>): void
```

Cancels listening for receiving data ends events of a WebSocket connection.

**Since:** 23

<!--Device-WebSocket-offDataEnd(callback?: Callback<void>): void--><!--Device-WebSocket-offDataEnd(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |  |

## offHeaderReceive

```TypeScript
offHeaderReceive(callback?: Callback<ResponseHeaders>): void
```

Unregisters the observer for HTTP Response Header events.

**Since:** 23

<!--Device-WebSocket-offHeaderReceive(callback?: Callback<ResponseHeaders>): void--><!--Device-WebSocket-offHeaderReceive(callback?: Callback<ResponseHeaders>): void-End-->

**System capability:** 
- API version 23 and later: SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ResponseHeaders](arkts-network-websocket-responseheaders-t.md)&gt; | No | the callback used to return the result.<br>**Since:** 23 |

## offMessage

```TypeScript
offMessage(callback?: AsyncCallback<string | ArrayBuffer>): void
```

Cancels listening for the message events of a WebSocket connection. data in AsyncCallback can be a string(API 6) or an ArrayBuffer(API 8).

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WebSocket-offMessage(callback?: AsyncCallback<string | ArrayBuffer>): void--><!--Device-WebSocket-offMessage(callback?: AsyncCallback<string | ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string \| ArrayBuffer&gt; | No | the callback used to return the result. |

## offOpen

```TypeScript
offOpen(callback?: Callback<OpenResult>): void
```

Cancels listening for the open events of a WebSocket connection.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WebSocket-offOpen(callback?: Callback<OpenResult>): void--><!--Device-WebSocket-offOpen(callback?: Callback<OpenResult>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OpenResult](arkts-network-websocket-openresult-i.md)&gt; | No | the callback used to return the result. |

## offWebSocketClose

```TypeScript
offWebSocketClose(callback?: AsyncCallback<CloseResult>): void
```

Cancels listening for the close events of a WebSocket connection.

**Since:** 23

<!--Device-WebSocket-offWebSocketClose(callback?: AsyncCallback<CloseResult>): void--><!--Device-WebSocket-offWebSocketClose(callback?: AsyncCallback<CloseResult>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CloseResult](arkts-network-websocket-closeresult-i.md)&gt; | No | the callback used to return the result. <br>close indicates the close error code and reason indicates the error code description. |

## offWebSocketError

```TypeScript
offWebSocketError(callback?: ErrorCallback): void
```

Cancels listening for the error events of a WebSocket connection.

**Since:** 23

<!--Device-WebSocket-offWebSocketError(callback?: ErrorCallback): void--><!--Device-WebSocket-offWebSocketError(callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | the callback used to return the result. |

## off_close('close')

```TypeScript
off(type: 'close', callback?: AsyncCallback<CloseResult>): void
```

Unsubscribes from WebSocket close events. This API uses an asynchronous callback to return the result. > **NOTE：**> > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. > If you do not pass the callback, you will cancel listening for all events.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebSocket-off(type: 'close', callback?: AsyncCallback<CloseResult>): void--><!--Device-WebSocket-off(type: 'close', callback?: AsyncCallback<CloseResult>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'close' | Yes | Event type.&lt;br /&gt; **close**: event indicating that a WebSocket connection has been closed. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CloseResult](arkts-network-websocket-closeresult-i.md)&gt; | No | Callback used to return the result. <br>**close** and **reason** indicate the error code and error cause for closing the connection, respectively. |

**Examples**

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.off('close');
```

## off_dataEnd('dataEnd')

```TypeScript
off(type: 'dataEnd', callback?: Callback<void>): void
```

Unsubscribes from WebSocket data receiving end events. This API uses an asynchronous callback to return the result. > **NOTE：**> > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. > If you do not pass the callback, you will cancel listening for all events.

**Since:** 11

<!--Device-WebSocket-off(type: 'dataEnd', callback?: Callback<void>): void--><!--Device-WebSocket-off(type: 'dataEnd', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'dataEnd' | Yes | Event type.&lt;br /&gt; **dataEnd**: event indicating the data receiving over the WebSocket connection has ended. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |  |

**Examples**

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.off('dataEnd');
```

## off_error('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

Unsubscribes from WebSocket error events. This API uses an asynchronous callback to return the result. > **NOTE：**> > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. > If you do not pass the callback, you will cancel listening for all events.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebSocket-off(type: 'error', callback?: ErrorCallback): void--><!--Device-WebSocket-off(type: 'error', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type.&lt;br /&gt; **error**: event indicating the WebSocket connection has encountered an error. |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | Callback used to return the result. |

**Examples**

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.off('error');
```

## off_headerReceive('headerReceive')

```TypeScript
off(type: 'headerReceive', callback?: Callback<ResponseHeaders>): void
```

Unsubscribes from HTTP response header events. This API uses an asynchronous callback to return the result. > **NOTE：**> > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. > If you do not pass the callback, you will cancel listening for all events.

**Since:** 12

<!--Device-WebSocket-off(type: 'headerReceive', callback?: Callback<ResponseHeaders>): void--><!--Device-WebSocket-off(type: 'headerReceive', callback?: Callback<ResponseHeaders>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'headerReceive' | Yes | Event type.&lt;br /&gt; Event type. The value is **headerReceive**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ResponseHeaders](arkts-network-websocket-responseheaders-t.md)&gt; | No | Callback used to return the result. |

**Examples**

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.off('headerReceive');
```

## off_message('message')

```TypeScript
off(type: 'message', callback?: AsyncCallback<string | ArrayBuffer>): void
```

Unsubscribes from WebSocket server message receiving events. This API uses an asynchronous callback to return the result. > **NOTE：**> > The data in **AsyncCallback** can be in the format of string (API version 6) or ArrayBuffer (API version 8). > > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. > If you do not pass the callback, you will cancel listening for all events.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebSocket-off(type: 'message', callback?: AsyncCallback<string | ArrayBuffer>): void--><!--Device-WebSocket-off(type: 'message', callback?: AsyncCallback<string | ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'message' | Yes | Event type.&lt;br /&gt; **message**: event indicating that a message has been received from the server. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string \| ArrayBuffer&gt; | No | Callback used to return the result. |

**Examples**

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.off('message');
```

## off_open('open')

```TypeScript
off(type: 'open', callback?: AsyncCallback<Object>): void
```

Unsubscribes from WebSocket open events. This API uses an asynchronous callback to return the result. > **NOTE：**> > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. > If you do not pass the callback, you will cancel listening for all events.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebSocket-off(type: 'open', callback?: AsyncCallback<Object>): void--><!--Device-WebSocket-off(type: 'open', callback?: AsyncCallback<Object>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'open' | Yes | Event type.&lt;br /&gt; **open**: event indicating that a WebSocket connection has been opened. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Object&gt; | No | Callback used to return the result. |

**Examples**

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
class OutValue {
  status: number = 0
  message: string = ""
}
let callback1 = (err: BusinessError, value: Object) => {
 console.info("on open, status:" + ((value as OutValue).status + ", message:" + (value as OutValue).message))
}
ws.on('open', callback1);
// You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
ws.off('open', callback1);
```

## off_openInfo('openInfo')

```TypeScript
off(type: 'openInfo', callback?: AsyncCallback<WebSocketOpenInfo>): void
```

Cancels listening for the open info events of a WebSocket connection.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebSocket-off(type: 'openInfo', callback?: AsyncCallback<WebSocketOpenInfo>): void--><!--Device-WebSocket-off(type: 'openInfo', callback?: AsyncCallback<WebSocketOpenInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'openInfo' | Yes | event indicating that the open info of a WebSocket connection is returned. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[WebSocketOpenInfo](arkts-network-websocket-websocketopeninfo-i.md)&gt; | No | the callback used to return the result. |

## onDataEnd

```TypeScript
onDataEnd(callback: Callback<void>): void
```

Enables listening for receiving data ends events of a WebSocket connection.

**Since:** 23

<!--Device-WebSocket-onDataEnd(callback: Callback<void>): void--><!--Device-WebSocket-onDataEnd(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | the callback used to return the result. |

## onHeaderReceive

```TypeScript
onHeaderReceive(callback: Callback<ResponseHeaders>): void
```

Registers an observer for HTTP Response Header events.

**Since:** 23

<!--Device-WebSocket-onHeaderReceive(callback: Callback<ResponseHeaders>): void--><!--Device-WebSocket-onHeaderReceive(callback: Callback<ResponseHeaders>): void-End-->

**System capability:** 
- API version 23 and later: SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ResponseHeaders](arkts-network-websocket-responseheaders-t.md)&gt; | Yes | the callback used to return the result.<br>**Since:** 23 |

## onMessage

```TypeScript
onMessage(callback: AsyncCallback<string | ArrayBuffer>): void
```

Enables listening for the message events of a WebSocket connection. data in AsyncCallback can be a string(API 6) or an ArrayBuffer(API 8).

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WebSocket-onMessage(callback: AsyncCallback<string | ArrayBuffer>): void--><!--Device-WebSocket-onMessage(callback: AsyncCallback<string | ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string \| ArrayBuffer&gt; | Yes | the callback used to return the result. |

## onOpen

```TypeScript
onOpen(callback: Callback<OpenResult>): void
```

Enables listening for the open events of a WebSocket connection.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WebSocket-onOpen(callback: Callback<OpenResult>): void--><!--Device-WebSocket-onOpen(callback: Callback<OpenResult>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OpenResult](arkts-network-websocket-openresult-i.md)&gt; | Yes | the callback used to return the result. |

## onWebSocketClose

```TypeScript
onWebSocketClose(callback: AsyncCallback<CloseResult>): void
```

Enables listening for the close events of a WebSocket connection.

**Since:** 23

<!--Device-WebSocket-onWebSocketClose(callback: AsyncCallback<CloseResult>): void--><!--Device-WebSocket-onWebSocketClose(callback: AsyncCallback<CloseResult>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CloseResult](arkts-network-websocket-closeresult-i.md)&gt; | Yes | the callback used to return the result. <br>close indicates the close error code and reason indicates the error code description. |

## onWebSocketError

```TypeScript
onWebSocketError(callback: ErrorCallback): void
```

Enables listening for the error events of a WebSocket connection.

**Since:** 23

<!--Device-WebSocket-onWebSocketError(callback: ErrorCallback): void--><!--Device-WebSocket-onWebSocketError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | the callback used to return the result. |

## on_close('close')

```TypeScript
on(type: 'close', callback: AsyncCallback<CloseResult>): void
```

Subscribes to WebSocket close events. This API uses an asynchronous callback to return the result.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebSocket-on(type: 'close', callback: AsyncCallback<CloseResult>): void--><!--Device-WebSocket-on(type: 'close', callback: AsyncCallback<CloseResult>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'close' | Yes | Event type.<br/> **close**: event indicating that a WebSocket connection has been closed. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CloseResult](arkts-network-websocket-closeresult-i.md)&gt; | Yes | Callback used to return the result. <br>**close** and **reason** indicate the error code and error cause for closing the connection, respectively. |

**Examples**

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
ws.on('close', (err: BusinessError, value: webSocket.CloseResult) => {
  console.info("on close, code is " + value.code + ", reason is " + value.reason)
});
```

## on_dataEnd('dataEnd')

```TypeScript
on(type: 'dataEnd', callback: Callback<void>): void
```

Subscribes to the WebSocket data receiving end event. This API uses an asynchronous callback to return the result.

**Since:** 11

<!--Device-WebSocket-on(type: 'dataEnd', callback: Callback<void>): void--><!--Device-WebSocket-on(type: 'dataEnd', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'dataEnd' | Yes | Event type.<br/> **dataEnd**: event indicating the data receiving over the WebSocket connection has ended. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Examples**

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.on('dataEnd', () => {
  console.info("on dataEnd")
});
```

## on_error('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to WebSocket error events. This API uses an asynchronous callback to return the result. The error code of the [error](#on_openopen) event callback is described as follows: WebSocket is essentially an HTTP protocol upgrade. If the server agrees to the upgrade, the server returns 101. The status code indicates that the protocol is switched from HTTP to WebSocket ( the **open** callback is triggered). If the server rejects the upgrade or other exceptions occur, the server returns 200, indicating that the server only processes the request as a common HTTP request.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebSocket-on(type: 'error', callback: ErrorCallback): void--><!--Device-WebSocket-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type.<br/> **error**: event indicating the WebSocket connection has encountered an error. |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | Callback used to return the result. |

**Examples**

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
ws.on('error', (err: BusinessError) => {
  console.error(`on error. Code: ${err.code}, message: ${err.message}`)
});
```

## on_headerReceive('headerReceive')

```TypeScript
on(type: 'headerReceive', callback: Callback<ResponseHeaders>): void
```

Subscribes to HTTP response header events. This API uses an asynchronous callback to return the result.

**Since:** 12

<!--Device-WebSocket-on(type: 'headerReceive', callback: Callback<ResponseHeaders>): void--><!--Device-WebSocket-on(type: 'headerReceive', callback: Callback<ResponseHeaders>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'headerReceive' | Yes | Event type.<br/> Event type. The value is **headerReceive**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ResponseHeaders](arkts-network-websocket-responseheaders-t.md)&gt; | Yes | Callback used to return the result. |

**Examples**

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.on('headerReceive', (data) => {
  console.info("on headerReceive " + JSON.stringify(data))
});
```

## on_message('message')

```TypeScript
on(type: 'message', callback: AsyncCallback<string | ArrayBuffer>): void
```

Subscribes to WebSocket server message receiving events. This API uses an asynchronous callback to return the result. > **NOTE：**> > The data in **AsyncCallback** can be in the format of string (API version 6) or ArrayBuffer (API version 8).

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebSocket-on(type: 'message', callback: AsyncCallback<string | ArrayBuffer>): void--><!--Device-WebSocket-on(type: 'message', callback: AsyncCallback<string | ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'message' | Yes | Event type.<br/> **message**: event indicating that a message has been received from the server. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string \| ArrayBuffer&gt; | Yes | Callback used to return the result. |

**Examples**

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
ws.on('message', (err: BusinessError<void>, value: string | ArrayBuffer) => {
  console.info("on message, message:" + value)
});
```

## on_open('open')

```TypeScript
on(type: 'open', callback: AsyncCallback<Object>): void
```

Subscribes to WebSocket open events. This API uses an asynchronous callback to return the result. This event indicates whether the WebSocket connection is successful. This API must be called before [connect](#connect) is called to initiate a connection request.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebSocket-on(type: 'open', callback: AsyncCallback<Object>): void--><!--Device-WebSocket-on(type: 'open', callback: AsyncCallback<Object>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'open' | Yes | Event type.<br/> **open**: event indicating that a WebSocket connection has been opened. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Object&gt; | Yes | Callback used to return the result. |

**Examples**

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let ws= webSocket.createWebSocket();
class OutValue {
  status: number = 0
  message: string = ""
}
ws.on('open', (err: BusinessError, value: Object) => {
  console.info("on open, status:" + (value as OutValue).status + ", message:" + (value as OutValue).message)
});
```

## on_openInfo('openInfo')

```TypeScript
on(type: 'openInfo', callback: AsyncCallback<WebSocketOpenInfo>): void
```

Enables listening for the open info events of a WebSocket connection.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebSocket-on(type: 'openInfo', callback: AsyncCallback<WebSocketOpenInfo>): void--><!--Device-WebSocket-on(type: 'openInfo', callback: AsyncCallback<WebSocketOpenInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'openInfo' | Yes | event indicating that the open info of a WebSocket connection is returned. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[WebSocketOpenInfo](arkts-network-websocket-websocketopeninfo-i.md)&gt; | Yes | the callback used to return the result. |

## send

```TypeScript
send(data: string | ArrayBuffer, callback: AsyncCallback<boolean>): void
```

Sends data through a WebSocket connection. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebSocket-send(data: string | ArrayBuffer, callback: AsyncCallback<boolean>): void--><!--Device-WebSocket-send(data: string | ArrayBuffer, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | string \| ArrayBuffer | Yes | Data to send. <br>Only the string type is supported for API version 6 or earlier. Both the string and ArrayBuffer types are supported for API version 8 or later. A maximum of 5,242,864 bytes (that is, 5 x 1024 x 1024 - 16) can be sent. If the data size exceeds the upper limit, error code 401 will be returned. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
let url = "ws://"
class OutValue {
  status: number = 0
  message: string = ""
}
ws.connect(url, (err: BusinessError, value: boolean) => {
    if (!err) {
      console.info("connect success")
    } else {
      console.error(`connect fail. Code: ${err.code}, message: ${err.message}`)
    }
});
ws.on('open', (err: BusinessError, value: Object) => {
  console.info("on open, status:" + (value as OutValue).status + ", message:" + (value as OutValue).message)
    ws.send("Hello, server!", (err: BusinessError, value: boolean) => {
    if (!err) {
      console.info("send success")
    } else {
      console.error(`send fail. Code: ${err.code}, message: ${err.message}`)
    }
  });
});
```

## send

```TypeScript
send(data: string | ArrayBuffer): Promise<boolean>
```

Sends data through the WebSocket connection. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebSocket-send(data: string | ArrayBuffer): Promise<boolean>--><!--Device-WebSocket-send(data: string | ArrayBuffer): Promise<boolean>-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | string \| ArrayBuffer | Yes | Data to send. <br>Only the string type is supported for API version 6 or earlier. Both the string and ArrayBuffer types are supported for API version 8 or later. A maximum of 5,242,864 bytes (that is, 5 x 1024 x 1024 - 16) can be sent. If the data size exceeds the upper limit, error code 401 will be returned. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
let url = "ws://"
class OutValue {
  status: number = 0
  message: string = ""
}
ws.connect(url, (err: BusinessError, value: boolean) => {
    if (!err) {
      console.info("connect success")
    } else {
      console.error("connect fail. Code: ${err.code}, message: ${err.message}")
    }
});

ws.on('open', (err: BusinessError, value: Object) => {
  console.info("on open, status:" + (value as OutValue).status + ", message:" + (value as OutValue).message)
  let promise = ws.send("Hello, server!");
  promise.then((value: boolean) => {
    console.info("send success")
  }).catch((err:string) => {
    console.error("send fail, error:" + JSON.stringify(err))
  });
});
```

