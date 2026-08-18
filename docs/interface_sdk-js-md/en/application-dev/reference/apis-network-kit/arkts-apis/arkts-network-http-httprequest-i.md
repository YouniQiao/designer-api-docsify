# HttpRequest

&lt;p&gt;Defines an HTTP request task. Before invoking APIs provided by HttpRequest, you must call createHttp() to create an HttpRequestTask object.&lt;/p&gt;

**Since:** 23

<!--Device-http-export interface HttpRequest--><!--Device-http-export interface HttpRequest-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { http } from '@kit.NetworkKit';
```

## destroy

```TypeScript
destroy(): void
```

Destroys an HTTP request.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HttpRequest-destroy(): void--><!--Device-HttpRequest-destroy(): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';
let httpRequest = http.createHttp();

httpRequest.destroy();
```

```TypeScript
import { http } from '@kit.NetworkKit';
let httpRequest = http.createHttp();

httpRequest.destroy();
```

## enableAutoCookie

```TypeScript
enableAutoCookie(enable: boolean): void
```

Sets whether to automatically reply with cookies.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-HttpRequest-enableAutoCookie(enable: boolean): void--><!--Device-HttpRequest-enableAutoCookie(enable: boolean): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | whether to automatically reply with cookies, default is false. |

## offDataEnd

```TypeScript
offDataEnd(callback?: Callback<void>): void
```

Unregisters an observer for receiving HTTP Response data ends events.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-HttpRequest-offDataEnd(callback?: Callback<void>): void--><!--Device-HttpRequest-offDataEnd(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | the callback used to return the result. |

## offDataReceive

```TypeScript
offDataReceive(callback?: Callback<ArrayBuffer>): void
```

Unregisters an observer for receiving HTTP Response data events continuously.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-HttpRequest-offDataReceive(callback?: Callback<ArrayBuffer>): void--><!--Device-HttpRequest-offDataReceive(callback?: Callback<ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | No | the callback used to return the result. |

## offDataReceiveProgress

```TypeScript
offDataReceiveProgress(callback?: Callback<DataReceiveProgressInfo>): void
```

Unregisters an observer for progress of receiving HTTP Response data events.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-HttpRequest-offDataReceiveProgress(callback?: Callback<DataReceiveProgressInfo>): void--><!--Device-HttpRequest-offDataReceiveProgress(callback?: Callback<DataReceiveProgressInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataReceiveProgressInfo](arkts-network-http-datareceiveprogressinfo-i.md)&gt; | No | the callback used to return the result. |

## offDataSendProgress

```TypeScript
offDataSendProgress(callback?: Callback<DataSendProgressInfo>): void
```

Unregisters an observer for progress of sendSize HTTP Response data events.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-HttpRequest-offDataSendProgress(callback?: Callback<DataSendProgressInfo>): void--><!--Device-HttpRequest-offDataSendProgress(callback?: Callback<DataSendProgressInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataSendProgressInfo](arkts-network-http-datasendprogressinfo-i.md)&gt; | No | the callback of off. |

## offHeadersReceive

```TypeScript
offHeadersReceive(callback?: Callback<Record<string, string>>): void
```

Unregisters the observer for HTTP Response Header events.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-HttpRequest-offHeadersReceive(callback?: Callback<Record<string, string>>): void--><!--Device-HttpRequest-offHeadersReceive(callback?: Callback<Record<string, string>>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, string&gt;&gt; | No | the callback used to return the result. |

## off_dataEnd

```TypeScript
off(type: "dataEnd", callback?: Callback<void>): void
```

Unregisters an observer for receiving HTTP Response data ends events.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-HttpRequest-off(type: "dataEnd", callback?: Callback<void>): void--><!--Device-HttpRequest-off(type: "dataEnd", callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | "dataEnd" | Yes | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | the callback used to return the result. |

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataEnd", () => {
  console.info("Receive dataEnd !");
});
httpRequest.off("dataEnd");
```

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataEnd", () => {
  console.info("Receive dataEnd !");
});
httpRequest.off("dataEnd");
```

## off_dataReceive

```TypeScript
off(type: "dataReceive", callback?: Callback<ArrayBuffer>): void
```

Unregisters an observer for receiving HTTP Response data events continuously.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-HttpRequest-off(type: "dataReceive", callback?: Callback<ArrayBuffer>): void--><!--Device-HttpRequest-off(type: "dataReceive", callback?: Callback<ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | "dataReceive" | Yes | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | No | the callback used to return the result. |

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataReceive", (data: ArrayBuffer) => {
  console.info("dataReceive length: " + JSON.stringify(data.byteLength));
});
httpRequest.off("dataReceive");
```

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataReceive", (data: ArrayBuffer) => {
  console.info("dataReceive length: " + JSON.stringify(data.byteLength));
});
httpRequest.off("dataReceive");
```

## off_dataReceiveProgress

```TypeScript
off(type: 'dataReceiveProgress', callback?: Callback<DataReceiveProgressInfo>): void
```

Unregisters an observer for progress of receiving HTTP Response data events.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-HttpRequest-off(type: 'dataReceiveProgress', callback?: Callback<DataReceiveProgressInfo>): void--><!--Device-HttpRequest-off(type: 'dataReceiveProgress', callback?: Callback<DataReceiveProgressInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'dataReceiveProgress' | Yes | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataReceiveProgressInfo](arkts-network-http-datareceiveprogressinfo-i.md)&gt; | No | the callback used to return the result. |

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataReceiveProgress", (data: http.DataReceiveProgressInfo) => {
  console.info("dataReceiveProgress:" + JSON.stringify(data));
});
httpRequest.off("dataReceiveProgress");
```

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataReceiveProgress", (data: http.DataReceiveProgressInfo) => {
  console.info("dataReceiveProgress:" + JSON.stringify(data));
});
httpRequest.off("dataReceiveProgress");
```

## off_dataSendProgress

```TypeScript
off(type: 'dataSendProgress', callback?: Callback<DataSendProgressInfo>): void
```

Unregisters an observer for progress of sendSize HTTP Response data events.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-HttpRequest-off(type: 'dataSendProgress', callback?: Callback<DataSendProgressInfo>): void--><!--Device-HttpRequest-off(type: 'dataSendProgress', callback?: Callback<DataSendProgressInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'dataSendProgress' | Yes | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataSendProgressInfo](arkts-network-http-datasendprogressinfo-i.md)&gt; | No | the callback of off. |

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataSendProgress", (data: http.DataSendProgressInfo) => {
  console.info("dataSendProgress:" + JSON.stringify(data));
});
httpRequest.off("dataSendProgress");
```

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataSendProgress", (data: http.DataSendProgressInfo) => {
  console.info("dataSendProgress:" + JSON.stringify(data));
});
httpRequest.off("dataSendProgress");
```

## off_headerReceive

```TypeScript
off(type: "headerReceive", callback?: AsyncCallback<Object>): void
```

Unregisters the observer for HTTP Response Header events.

**Since:** 6

**Deprecated since:** 8

**Substitutes:** [off_headersReceive](#offheadersreceive)

<!--Device-HttpRequest-off(type: "headerReceive", callback?: AsyncCallback<Object>): void--><!--Device-HttpRequest-off(type: "headerReceive", callback?: AsyncCallback<Object>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | "headerReceive" | Yes | Indicates Event name. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Object&gt; | No | the callback used to return the result. |

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.off("headerReceive");
```

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.off("headerReceive");
```

## off_headersReceive

```TypeScript
off(type: "headersReceive", callback?: Callback<Object>): void
```

Unregisters the observer for HTTP Response Header events.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HttpRequest-off(type: "headersReceive", callback?: Callback<Object>): void--><!--Device-HttpRequest-off(type: "headersReceive", callback?: Callback<Object>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | "headersReceive" | Yes | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Object&gt; | No | the callback used to return the result. |

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("headersReceive", (header: Object) => {
  console.info("header: " + JSON.stringify(header));
});
httpRequest.off("headersReceive");
```

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("headersReceive", (header: Object) => {
  console.info("header: " + JSON.stringify(header));
});
httpRequest.off("headersReceive");
```

## onDataEnd

```TypeScript
onDataEnd(callback: Callback<void>): void
```

Registers an observer for receiving HTTP Response data ends events.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-HttpRequest-onDataEnd(callback: Callback<void>): void--><!--Device-HttpRequest-onDataEnd(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | the callback used to return the result. |

## onDataReceive

```TypeScript
onDataReceive(callback: Callback<ArrayBuffer>): void
```

Registers an observer for receiving HTTP Response data events continuously.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-HttpRequest-onDataReceive(callback: Callback<ArrayBuffer>): void--><!--Device-HttpRequest-onDataReceive(callback: Callback<ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | Yes | the callback used to return the result. |

## onDataReceiveProgress

```TypeScript
onDataReceiveProgress(callback: Callback<DataReceiveProgressInfo>): void
```

Registers an observer for progress of receiving HTTP Response data events.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-HttpRequest-onDataReceiveProgress(callback: Callback<DataReceiveProgressInfo>): void--><!--Device-HttpRequest-onDataReceiveProgress(callback: Callback<DataReceiveProgressInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataReceiveProgressInfo](arkts-network-http-datareceiveprogressinfo-i.md)&gt; | Yes | the callback used to return the result. |

## onDataSendProgress

```TypeScript
onDataSendProgress(callback: Callback<DataSendProgressInfo>): void
```

Registers an observer for progress of sendSize HTTP Response data events.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-HttpRequest-onDataSendProgress(callback: Callback<DataSendProgressInfo>): void--><!--Device-HttpRequest-onDataSendProgress(callback: Callback<DataSendProgressInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataSendProgressInfo](arkts-network-http-datasendprogressinfo-i.md)&gt; | Yes | the callback of on. |

## onHeadersReceive

```TypeScript
onHeadersReceive(callback: Callback<Record<string, string>>): void
```

Registers an observer for HTTP Response Header events.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-HttpRequest-onHeadersReceive(callback: Callback<Record<string, string>>): void--><!--Device-HttpRequest-onHeadersReceive(callback: Callback<Record<string, string>>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, string&gt;&gt; | Yes | the callback used to return the result. |

## on_dataEnd

```TypeScript
on(type: "dataEnd", callback: Callback<void>): void
```

Registers an observer for receiving HTTP Response data ends events.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-HttpRequest-on(type: "dataEnd", callback: Callback<void>): void--><!--Device-HttpRequest-on(type: "dataEnd", callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | "dataEnd" | Yes | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | the callback used to return the result. |

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataEnd", () => {
  console.info("Receive dataEnd !");
});
httpRequest.off("dataEnd");
```

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataEnd", () => {
  console.info("Receive dataEnd !");
});
httpRequest.off("dataEnd");
```

## on_dataReceive

```TypeScript
on(type: "dataReceive", callback: Callback<ArrayBuffer>): void
```

Registers an observer for receiving HTTP Response data events continuously.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-HttpRequest-on(type: "dataReceive", callback: Callback<ArrayBuffer>): void--><!--Device-HttpRequest-on(type: "dataReceive", callback: Callback<ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | "dataReceive" | Yes | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | Yes | the callback used to return the result. |

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataReceive", (data: ArrayBuffer) => {
  console.info("dataReceive length: " + JSON.stringify(data.byteLength));
});
httpRequest.off("dataReceive");
```

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataReceive", (data: ArrayBuffer) => {
  console.info("dataReceive length: " + JSON.stringify(data.byteLength));
});
httpRequest.off("dataReceive");
```

## on_dataReceiveProgress

```TypeScript
on(type: 'dataReceiveProgress', callback: Callback<DataReceiveProgressInfo>): void
```

Registers an observer for progress of receiving HTTP Response data events.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-HttpRequest-on(type: 'dataReceiveProgress', callback: Callback<DataReceiveProgressInfo>): void--><!--Device-HttpRequest-on(type: 'dataReceiveProgress', callback: Callback<DataReceiveProgressInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'dataReceiveProgress' | Yes | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataReceiveProgressInfo](arkts-network-http-datareceiveprogressinfo-i.md)&gt; | Yes | the callback used to return the result. |

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataReceiveProgress", (data: http.DataReceiveProgressInfo) => {
  console.info("dataReceiveProgress:" + JSON.stringify(data));
});
httpRequest.off("dataReceiveProgress");
```

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataReceiveProgress", (data: http.DataReceiveProgressInfo) => {
  console.info("dataReceiveProgress:" + JSON.stringify(data));
});
httpRequest.off("dataReceiveProgress");
```

## on_dataSendProgress

```TypeScript
on(type: 'dataSendProgress', callback: Callback<DataSendProgressInfo>): void
```

Registers an observer for progress of sendSize HTTP Response data events.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-HttpRequest-on(type: 'dataSendProgress', callback: Callback<DataSendProgressInfo>): void--><!--Device-HttpRequest-on(type: 'dataSendProgress', callback: Callback<DataSendProgressInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'dataSendProgress' | Yes | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataSendProgressInfo](arkts-network-http-datasendprogressinfo-i.md)&gt; | Yes | the callback of on. |

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataSendProgress", (data: http.DataSendProgressInfo) => {
  console.info("dataSendProgress:" + JSON.stringify(data));
});
httpRequest.off("dataSendProgress");
```

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataSendProgress", (data: http.DataSendProgressInfo) => {
  console.info("dataSendProgress:" + JSON.stringify(data));
});
httpRequest.off("dataSendProgress");
```

## on_headerReceive

```TypeScript
on(type: "headerReceive", callback: AsyncCallback<Object>): void
```

Registers an observer for HTTP Response Header events.

**Since:** 6

**Deprecated since:** 8

**Substitutes:** [on_headersReceive](#onheadersreceive)

<!--Device-HttpRequest-on(type: "headerReceive", callback: AsyncCallback<Object>): void--><!--Device-HttpRequest-on(type: "headerReceive", callback: AsyncCallback<Object>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | "headerReceive" | Yes | Indicates Event name. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Object&gt; | Yes | the callback used to return the result. |

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let httpRequest = http.createHttp();
httpRequest.on("headerReceive", (data: BusinessError) => {
  console.error("error:" + JSON.stringify(data));
});
```

```TypeScript
import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let httpRequest = http.createHttp();
httpRequest.on("headerReceive", (data: BusinessError) => {
  console.error("error:" + JSON.stringify(data));
});
```

## on_headersReceive

```TypeScript
on(type: "headersReceive", callback: Callback<Object>): void
```

Registers an observer for HTTP Response Header events.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HttpRequest-on(type: "headersReceive", callback: Callback<Object>): void--><!--Device-HttpRequest-on(type: "headersReceive", callback: Callback<Object>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | "headersReceive" | Yes | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Object&gt; | Yes | the callback used to return the result. |

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("headersReceive", (header: Object) => {
  console.info("header: " + JSON.stringify(header));
});
httpRequest.off("headersReceive");
```

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("headersReceive", (header: Object) => {
  console.info("header: " + JSON.stringify(header));
});
httpRequest.off("headersReceive");
```

## onceHeadersReceive

```TypeScript
onceHeadersReceive(callback: Callback<Record<string, string>>): void
```

Registers a one-time observer for HTTP Response Header events.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-HttpRequest-onceHeadersReceive(callback: Callback<Record<string, string>>): void--><!--Device-HttpRequest-onceHeadersReceive(callback: Callback<Record<string, string>>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, string&gt;&gt; | Yes | the callback used to return the result. |

## once_headersReceive

```TypeScript
once(type: "headersReceive", callback: Callback<Object>): void
```

Registers a one-time observer for HTTP Response Header events.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-HttpRequest-once(type: "headersReceive", callback: Callback<Object>): void--><!--Device-HttpRequest-once(type: "headersReceive", callback: Callback<Object>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | "headersReceive" | Yes | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Object&gt; | Yes | the callback used to return the result. |

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.once("headersReceive", (header: Object) => {
  console.info("header: " + JSON.stringify(header));
});
```

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.once("headersReceive", (header: Object) => {
  console.info("header: " + JSON.stringify(header));
});
```

## request

```TypeScript
request(url: string, callback: AsyncCallback<HttpResponse>): void
```

Initiates an HTTP request to a given URL. This API uses an asynchronous callback to return the result. > **NOTE：**> > (1) This API can receive only data whose size is less than 5 MB. If the data size exceeds 5 MB, you need to set > **maxLimit** to a larger value in [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md#httprequestoptions) or call > [requestInStream](#requestinstream) to > initiate a streaming request. Since API version 23, this API can receive a maximum of 50 MB data. In versions > earlier than API version 23, this API can receive a maximum of 5 MB data, and any data exceeding this threshold > will fail to be received. > (2) If you need to pass in cookies, add them to the **options** parameter. > (3) If the URL contains non-English characters, call **encodeURL(url)** to encode the URL before initiating an > HTTP request.

**Since:** 23

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HttpRequest-request(url: string, callback: AsyncCallback<HttpResponse>): void--><!--Device-HttpRequest-request(url: string, callback: AsyncCallback<HttpResponse>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | URL for initiating an HTTP request. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HttpResponse&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2300003](../errorcode-net-http.md#2300003-incorrect-url-format) | Invalid URL format or missing URL. |
| [2300001](../errorcode-net-http.md#2300001-protocol-not-supported) | Unsupported protocol. |
| [2300007](../errorcode-net-http.md#2300007-failed-to-connect-to-the-server) | Failed to connect to the server. |
| [2300006](../errorcode-net-http.md#2300006-failed-to-resolve-the-domain-name-of-the-host) | Failed to resolve the host name. |
| [2300070](../errorcode-net-http.md#2300070-insufficient-server-disk-space) | Remote disk full. |
| [2300005](../errorcode-net-http.md#2300005-failed-to-resolve-the-domain-name-of-the-proxy-server) | Failed to resolve the proxy name. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [2300009](../errorcode-net-http.md#2300009-access-to-remote-resources-denied) | Access to the remote resource denied. |
| [2300073](../errorcode-net-http.md#2300073-uploaded-file-already-exists) | Remote file already exists. |
| [2300008](../errorcode-net-http.md#2300008-invalid-data-returned-by-the-server) | Invalid server response. |
| [2300078](../errorcode-net-http.md#2300078-url-requested-file-not-found) | Remote file not found. |
| [2300077](../errorcode-net-http.md#2300077-no-ssl-ca-certificate-or-access-permission) | The SSL CA certificate does not exist or is inaccessible. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2300018](../errorcode-net-http.md#2300018-incomplete-data-returned-by-the-server) | Transferred a partial file. |
| [2300016](../errorcode-net-http.md#2300016-http2-framing-layer-error) | Error in the HTTP2 framing layer. |
| [2300023](../errorcode-net-http.md#2300023-failed-to-write-received-data-to-a-disk-or-application) | Failed to write the received data to the disk or application. |
| [2300027](../errorcode-net-http.md#2300027-insufficient-memory) | Out of memory. |
| [2300026](../errorcode-net-http.md#2300026-failed-to-open-or-read-local-data-from-a-file-or-application) | Failed to open or read local data from the file or application. |
| [2300025](../errorcode-net-http.md#2300025-failed-to-upload-data) | Upload failed. |
| [2300094](../errorcode-net-http.md#2300094-identity-verification-failed) | Authentication error. |
| [2300028](../errorcode-net-http.md#2300028-operation-timeout) | Operation timeout. |
| [2300999](../errorcode-net-http.md#2300999-internal-error) | Internal error. |
| [2300998](../errorcode-net-http.md#2300998-domain-access-denied) | It is not allowed to access this domain.<br>**Applicable version:** 12 and later |
| [2300997](../errorcode-net-http.md#2300997-plaintext-http-access-intercepted) | Cleartext traffic not permitted.<br>**Applicable version:** 18 and later |
| 2300996 | The request was intercepted by the HTTP global interceptor.<br>**Applicable version:** 26.0.0 dynamic&static and later |
| [2300047](../errorcode-net-http.md#2300047-maximum-redirections-reached) | The number of redirections reaches the maximum allowed. |
| [2300055](../errorcode-net-http.md#2300055-failed-to-send-network-data) | Failed to send data to the peer. |
| [2300052](../errorcode-net-http.md#2300052-no-content-returned-by-the-server) | The server returned nothing (no header or data). |
| [2300059](../errorcode-net-http.md#2300059-failed-to-use-the-specified-ssl-cipher-algorithm) | The specified SSL cipher cannot be used. |
| [2300058](../errorcode-net-http.md#2300058-local-ssl-certificate-error) | Local SSL certificate error. |
| [2300056](../errorcode-net-http.md#2300056-failed-to-receive-network-data) | Failed to receive data from the peer. |
| [2300063](../errorcode-net-http.md#2300063-maximum-file-size-exceeded) | Maximum file size exceeded. |
| [2300061](../errorcode-net-http.md#2300061-unrecognized-or-incorrect-http-encoding-format) | Invalid HTTP encoding format. |
| [2300060](../errorcode-net-http.md#2300060-incorrect-ssl-certificate-or-ssh-key-of-the-remote-server) | Invalid SSL peer certificate or SSH remote key. |

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.request("EXAMPLE_URL", (err: Error, data: http.HttpResponse) => {
  if (!err) {
    console.info('Result:' + data.result);
    console.info('code:' + data.responseCode);
    console.info('type:' + JSON.stringify(data.resultType));
    console.info('header:' + JSON.stringify(data.header));
    console.info('cookies:' + data.cookies); // Cookies are supported since API version 8.
  } else {
    console.error('error:' + JSON.stringify(err));
  }
});
```

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.request("EXAMPLE_URL", (err: Error, data: http.HttpResponse) => {
  if (!err) {
    console.info('Result:' + data.result);
    console.info('code:' + data.responseCode);
    console.info('type:' + JSON.stringify(data.resultType));
    console.info('header:' + JSON.stringify(data.header));
    console.info('cookies:' + data.cookies); // Cookies are supported since API version 8.
  } else {
    console.error('error:' + JSON.stringify(err));
  }
});
```

## request

```TypeScript
request(url: string, options: HttpRequestOptions, callback: AsyncCallback<HttpResponse>): void
```

Initiates an HTTP request containing specified options to a given URL. This API uses an asynchronous callback to return the result. > **NOTE：**> > (1) This API can receive only data whose size is less than 5 MB. If the data size exceeds 5 MB, you need to set > **maxLimit** to a larger value in [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md#httprequestoptions) or call > [requestInStream](#requestinstream) to > initiate a streaming request. Since API version 23, this API can receive a maximum of 50 MB data. In versions > earlier than API version 23, this API can receive a maximum of 5 MB data, and any data exceeding this threshold > will fail to be received. > (2) If you need to pass in cookies, add them to the **options** parameter. > (3) If the URL contains non-English characters, call **encodeURL(url)** to encode the URL before initiating an > HTTP request.

**Since:** 23

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HttpRequest-request(url: string, options: HttpRequestOptions, callback: AsyncCallback<HttpResponse>): void--><!--Device-HttpRequest-request(url: string, options: HttpRequestOptions, callback: AsyncCallback<HttpResponse>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | URL for initiating an HTTP request. |
| options | [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) | Yes | Request options. For details, see [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md#httprequestoptions). |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HttpResponse&gt; | Yes | Callback used to return the result. If the operation is successful, the callback content is an [HttpResponse](arkts-network-http-httpresponse-i.md#httpresponse) object; otherwise, the callback content is undefined. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2300003](../errorcode-net-http.md#2300003-incorrect-url-format) | Invalid URL format or missing URL. |
| [2300001](../errorcode-net-http.md#2300001-protocol-not-supported) | Unsupported protocol. |
| [2300007](../errorcode-net-http.md#2300007-failed-to-connect-to-the-server) | Failed to connect to the server. |
| [2300006](../errorcode-net-http.md#2300006-failed-to-resolve-the-domain-name-of-the-host) | Failed to resolve the host name. |
| [2300070](../errorcode-net-http.md#2300070-insufficient-server-disk-space) | Remote disk full. |
| [2300005](../errorcode-net-http.md#2300005-failed-to-resolve-the-domain-name-of-the-proxy-server) | Failed to resolve the proxy name. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [2300009](../errorcode-net-http.md#2300009-access-to-remote-resources-denied) | Access to the remote resource denied. |
| [2300073](../errorcode-net-http.md#2300073-uploaded-file-already-exists) | Remote file already exists. |
| [2300008](../errorcode-net-http.md#2300008-invalid-data-returned-by-the-server) | Invalid server response. |
| [2300078](../errorcode-net-http.md#2300078-url-requested-file-not-found) | Remote file not found. |
| [2300077](../errorcode-net-http.md#2300077-no-ssl-ca-certificate-or-access-permission) | The SSL CA certificate does not exist or is inaccessible. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2300018](../errorcode-net-http.md#2300018-incomplete-data-returned-by-the-server) | Transferred a partial file. |
| [2300016](../errorcode-net-http.md#2300016-http2-framing-layer-error) | Error in the HTTP2 framing layer. |
| [2300023](../errorcode-net-http.md#2300023-failed-to-write-received-data-to-a-disk-or-application) | Failed to write the received data to the disk or application. |
| [2300027](../errorcode-net-http.md#2300027-insufficient-memory) | Out of memory. |
| [2300026](../errorcode-net-http.md#2300026-failed-to-open-or-read-local-data-from-a-file-or-application) | Failed to open or read local data from the file or application. |
| [2300025](../errorcode-net-http.md#2300025-failed-to-upload-data) | Upload failed. |
| [2300094](../errorcode-net-http.md#2300094-identity-verification-failed) | Authentication error. |
| [2300028](../errorcode-net-http.md#2300028-operation-timeout) | Operation timeout. |
| [2300999](../errorcode-net-http.md#2300999-internal-error) | Internal error. |
| [2300998](../errorcode-net-http.md#2300998-domain-access-denied) | It is not allowed to access this domain.<br>**Applicable version:** 12 and later |
| [2300997](../errorcode-net-http.md#2300997-plaintext-http-access-intercepted) | Cleartext traffic not permitted.<br>**Applicable version:** 18 and later |
| 2300996 | The request was intercepted by the HTTP global interceptor.<br>**Applicable version:** 26.0.0 dynamic&static and later |
| [2300047](../errorcode-net-http.md#2300047-maximum-redirections-reached) | The number of redirections reaches the maximum allowed. |
| [2300055](../errorcode-net-http.md#2300055-failed-to-send-network-data) | Failed to send data to the peer. |
| [2300052](../errorcode-net-http.md#2300052-no-content-returned-by-the-server) | The server returned nothing (no header or data). |
| [2300059](../errorcode-net-http.md#2300059-failed-to-use-the-specified-ssl-cipher-algorithm) | The specified SSL cipher cannot be used. |
| [2300058](../errorcode-net-http.md#2300058-local-ssl-certificate-error) | Local SSL certificate error. |
| [2300056](../errorcode-net-http.md#2300056-failed-to-receive-network-data) | Failed to receive data from the peer. |
| [2300063](../errorcode-net-http.md#2300063-maximum-file-size-exceeded) | Maximum file size exceeded. |
| [2300061](../errorcode-net-http.md#2300061-unrecognized-or-incorrect-http-encoding-format) | Invalid HTTP encoding format. |
| [2300060](../errorcode-net-http.md#2300060-incorrect-ssl-certificate-or-ssh-key-of-the-remote-server) | Invalid SSL peer certificate or SSH remote key. |

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';

class Header {
  public contentType: string;

  constructor(contentType: string) {
    this.contentType = contentType;
  }
}

let httpRequest = http.createHttp();
let options: http.HttpRequestOptions = {
    method: http.RequestMethod.POST, // Optional. The default value is http.RequestMethod.GET.
    // This field is used to transfer the request body when a POST request is used. Its format needs to be negotiated with the server.
    extraData: 'data to send',
    expectDataType: http.HttpDataType.STRING, // Optional. This parameter specifies the type of the return data.
    usingCache: true, // Optional. The default value is true.
    priority: 1, // Optional. The default value is 1.
    // You can add header fields based on service requirements.
    header: new Header('application/json'),
    readTimeout: 60000, // Optional. The default value is 60000, in ms.
    connectTimeout: 60000 // Optional. The default value is 60000, in ms.
    usingProtocol: http.HttpProtocol.HTTP1_1, // Optional. The default protocol type is automatically specified by the system.
    usingProxy: false, // Optional. By default, network proxy is not used. This field is supported since API version 10.
};

httpRequest.request("EXAMPLE_URL", options, (err: Error, data: http.HttpResponse) => {
  if (!err) {
    console.info('Result:' + data.result);
    console.info('code:' + data.responseCode);
    console.info('type:' + JSON.stringify(data.resultType));
    console.info('header:' + JSON.stringify(data.header));
    console.info('cookies:' + data.cookies); // Cookies are supported since API version 8.
  } else {
    console.error('error:' + JSON.stringify(err));
  }
});
```

```TypeScript
import { http } from '@kit.NetworkKit';

class Header {
  public contentType: string;

  constructor(contentType: string) {
    this.contentType = contentType;
  }
}

let httpRequest = http.createHttp();
let options: http.HttpRequestOptions = {
    method: http.RequestMethod.POST, // Optional. The default value is http.RequestMethod.GET.
    // This field is used to transfer the request body when a POST request is used. Its format needs to be negotiated with the server.
    extraData: 'data to send',
    expectDataType: http.HttpDataType.STRING, // Optional. This parameter specifies the type of the return data.
    usingCache: true, // Optional. The default value is true.
    priority: 1, // Optional. The default value is 1.
    // You can add header fields based on service requirements.
    header: new Header('application/json'),
    readTimeout: 60000, // Optional. The default value is 60000, in ms.
    connectTimeout: 60000 // Optional. The default value is 60000, in ms.
    usingProtocol: http.HttpProtocol.HTTP1_1, // Optional. The default protocol type is automatically specified by the system.
    usingProxy: false, // Optional. By default, network proxy is not used. This field is supported since API version 10.
};

httpRequest.request("EXAMPLE_URL", options, (err: Error, data: http.HttpResponse) => {
  if (!err) {
    console.info('Result:' + data.result);
    console.info('code:' + data.responseCode);
    console.info('type:' + JSON.stringify(data.resultType));
    console.info('header:' + JSON.stringify(data.header));
    console.info('cookies:' + data.cookies); // Cookies are supported since API version 8.
  } else {
    console.error('error:' + JSON.stringify(err));
  }
});
```

## request

```TypeScript
request(url: string, options?: HttpRequestOptions): Promise<HttpResponse>
```

Initiates an HTTP request containing specified options to a given URL. This API uses a promise to return the result. > **NOTE：**> > (1) This API can receive only data whose size is less than 5 MB. If the data size exceeds 5 MB, you need to set > **maxLimit** to a larger value in [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md#httprequestoptions) or call > [requestInStream](#requestinstream) to > initiate a streaming request. Since API version 23, this API can receive a maximum of 50 MB data. In versions > earlier than API version 23, this API can receive a maximum of 5 MB data, and any data exceeding this threshold > will fail to be received. > (2) If you need to pass in cookies, add them to the **options** parameter. > (3) If the URL contains non-English characters, call **encodeURL(url)** to encode the URL before initiating an > HTTP request.

**Since:** 23

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HttpRequest-request(url: string, options?: HttpRequestOptions): Promise<HttpResponse>--><!--Device-HttpRequest-request(url: string, options?: HttpRequestOptions): Promise<HttpResponse>-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | URL for initiating an HTTP request. |
| options | [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) | No | Request options. For details, see [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md#httprequestoptions). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;HttpResponse&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2300003](../errorcode-net-http.md#2300003-incorrect-url-format) | Invalid URL format or missing URL. |
| [2300001](../errorcode-net-http.md#2300001-protocol-not-supported) | Unsupported protocol. |
| [2300007](../errorcode-net-http.md#2300007-failed-to-connect-to-the-server) | Failed to connect to the server. |
| [2300006](../errorcode-net-http.md#2300006-failed-to-resolve-the-domain-name-of-the-host) | Failed to resolve the host name. |
| [2300070](../errorcode-net-http.md#2300070-insufficient-server-disk-space) | Remote disk full. |
| [2300005](../errorcode-net-http.md#2300005-failed-to-resolve-the-domain-name-of-the-proxy-server) | Failed to resolve the proxy name. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [2300009](../errorcode-net-http.md#2300009-access-to-remote-resources-denied) | Access to the remote resource denied. |
| [2300073](../errorcode-net-http.md#2300073-uploaded-file-already-exists) | Remote file already exists. |
| [2300008](../errorcode-net-http.md#2300008-invalid-data-returned-by-the-server) | Invalid server response. |
| [2300078](../errorcode-net-http.md#2300078-url-requested-file-not-found) | Remote file not found. |
| [2300077](../errorcode-net-http.md#2300077-no-ssl-ca-certificate-or-access-permission) | The SSL CA certificate does not exist or is inaccessible. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2300018](../errorcode-net-http.md#2300018-incomplete-data-returned-by-the-server) | Transferred a partial file. |
| [2300016](../errorcode-net-http.md#2300016-http2-framing-layer-error) | Error in the HTTP2 framing layer. |
| [2300023](../errorcode-net-http.md#2300023-failed-to-write-received-data-to-a-disk-or-application) | Failed to write the received data to the disk or application. |
| [2300027](../errorcode-net-http.md#2300027-insufficient-memory) | Out of memory. |
| [2300026](../errorcode-net-http.md#2300026-failed-to-open-or-read-local-data-from-a-file-or-application) | Failed to open or read local data from the file or application. |
| [2300025](../errorcode-net-http.md#2300025-failed-to-upload-data) | Upload failed. |
| [2300094](../errorcode-net-http.md#2300094-identity-verification-failed) | Authentication error. |
| [2300028](../errorcode-net-http.md#2300028-operation-timeout) | Operation timeout. |
| [2300999](../errorcode-net-http.md#2300999-internal-error) | Internal error. |
| [2300998](../errorcode-net-http.md#2300998-domain-access-denied) | It is not allowed to access this domain.<br>**Applicable version:** 12 and later |
| [2300997](../errorcode-net-http.md#2300997-plaintext-http-access-intercepted) | Cleartext traffic not permitted.<br>**Applicable version:** 18 and later |
| 2300996 | The request was intercepted by the HTTP global interceptor.<br>**Applicable version:** 26.0.0 dynamic&static and later |
| [2300047](../errorcode-net-http.md#2300047-maximum-redirections-reached) | The number of redirections reaches the maximum allowed. |
| [2300055](../errorcode-net-http.md#2300055-failed-to-send-network-data) | Failed to send data to the peer. |
| [2300052](../errorcode-net-http.md#2300052-no-content-returned-by-the-server) | The server returned nothing (no header or data). |
| [2300059](../errorcode-net-http.md#2300059-failed-to-use-the-specified-ssl-cipher-algorithm) | The specified SSL cipher cannot be used. |
| [2300058](../errorcode-net-http.md#2300058-local-ssl-certificate-error) | Local SSL certificate error. |
| [2300056](../errorcode-net-http.md#2300056-failed-to-receive-network-data) | Failed to receive data from the peer. |
| [2300063](../errorcode-net-http.md#2300063-maximum-file-size-exceeded) | Maximum file size exceeded. |
| [2300061](../errorcode-net-http.md#2300061-unrecognized-or-incorrect-http-encoding-format) | Invalid HTTP encoding format. |
| [2300060](../errorcode-net-http.md#2300060-incorrect-ssl-certificate-or-ssh-key-of-the-remote-server) | Invalid SSL peer certificate or SSH remote key. |

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';

class Header {
  public contentType: string;

  constructor(contentType: string) {
    this.contentType = contentType;
  }
}

let httpRequest = http.createHttp();
let promise = httpRequest.request("EXAMPLE_URL", {
  method: http.RequestMethod.GET,
  connectTimeout: 60000,
  readTimeout: 60000,
  header: new Header('application/json')
});
promise.then((data:http.HttpResponse) => {
  console.info('Result:' + data.result);
  console.info('code:' + data.responseCode);
  console.info('type:' + JSON.stringify(data.resultType));
  console.info('header:' + JSON.stringify(data.header));
  console.info('cookies:' + data.cookies); // Cookies are supported since API version 8.
  console.info('header.content-Type:' + data.header);
  console.info('header.Status-Line:' + data.header);
}).catch((err:Error) => {
  console.error('error:' + JSON.stringify(err));
});
```

```TypeScript
import { http } from '@kit.NetworkKit';

class Header {
  public contentType: string;

  constructor(contentType: string) {
    this.contentType = contentType;
  }
}

let httpRequest = http.createHttp();
let promise = httpRequest.request("EXAMPLE_URL", {
  method: http.RequestMethod.GET,
  connectTimeout: 60000,
  readTimeout: 60000,
  header: new Header('application/json')
});
promise.then((data:http.HttpResponse) => {
  console.info('Result:' + data.result);
  console.info('code:' + data.responseCode);
  console.info('type:' + JSON.stringify(data.resultType));
  console.info('header:' + JSON.stringify(data.header));
  console.info('cookies:' + data.cookies); // Cookies are supported since API version 8.
  console.info('header.content-Type:' + data.header);
  console.info('header.Status-Line:' + data.header);
}).catch((err:Error) => {
  console.error('error:' + JSON.stringify(err));
});
```

## requestInStream

```TypeScript
requestInStream(url: string, callback: AsyncCallback<int>): void
```

Initiates an HTTP request containing specified options to a given URL. This API uses an asynchronous callback to return the result, which is a streaming response.

**Since:** 26.1.0

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-HttpRequest-requestInStream(url: string, callback: AsyncCallback<int>): void--><!--Device-HttpRequest-requestInStream(url: string, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | URL for initiating an HTTP request. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | Callback used to return the result. If the request is successful, **err** is **undefined**, and the HTTP result code is returned. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2300003](../errorcode-net-http.md#2300003-incorrect-url-format) | Invalid URL format or missing URL. |
| [2300001](../errorcode-net-http.md#2300001-protocol-not-supported) | Unsupported protocol. |
| [2300007](../errorcode-net-http.md#2300007-failed-to-connect-to-the-server) | Failed to connect to the server. |
| [2300006](../errorcode-net-http.md#2300006-failed-to-resolve-the-domain-name-of-the-host) | Failed to resolve the host name. |
| [2300070](../errorcode-net-http.md#2300070-insufficient-server-disk-space) | Remote disk full. |
| [2300005](../errorcode-net-http.md#2300005-failed-to-resolve-the-domain-name-of-the-proxy-server) | Failed to resolve the proxy name. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [2300009](../errorcode-net-http.md#2300009-access-to-remote-resources-denied) | Access to the remote resource denied. |
| [2300073](../errorcode-net-http.md#2300073-uploaded-file-already-exists) | Remote file already exists. |
| [2300008](../errorcode-net-http.md#2300008-invalid-data-returned-by-the-server) | Invalid server response. |
| [2300078](../errorcode-net-http.md#2300078-url-requested-file-not-found) | Remote file not found. |
| [2300077](../errorcode-net-http.md#2300077-no-ssl-ca-certificate-or-access-permission) | The SSL CA certificate does not exist or is inaccessible. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2300018](../errorcode-net-http.md#2300018-incomplete-data-returned-by-the-server) | Transferred a partial file. |
| [2300016](../errorcode-net-http.md#2300016-http2-framing-layer-error) | Error in the HTTP2 framing layer. |
| [2300023](../errorcode-net-http.md#2300023-failed-to-write-received-data-to-a-disk-or-application) | Failed to write the received data to the disk or application. |
| [2300027](../errorcode-net-http.md#2300027-insufficient-memory) | Out of memory. |
| [2300026](../errorcode-net-http.md#2300026-failed-to-open-or-read-local-data-from-a-file-or-application) | Failed to open or read local data from the file or application. |
| [2300025](../errorcode-net-http.md#2300025-failed-to-upload-data) | Upload failed. |
| [2300094](../errorcode-net-http.md#2300094-identity-verification-failed) | Authentication error. |
| [2300028](../errorcode-net-http.md#2300028-operation-timeout) | Operation timeout. |
| [2300999](../errorcode-net-http.md#2300999-internal-error) | Unknown error. |
| [2300998](../errorcode-net-http.md#2300998-domain-access-denied) | It is not allowed to access this domain.<br>**Applicable version:** 12 and later |
| [2300997](../errorcode-net-http.md#2300997-plaintext-http-access-intercepted) | Cleartext traffic not permitted.<br>**Applicable version:** 18 and later |
| 2300996 | The request was intercepted by the HTTP global interceptor.<br>**Applicable version:** 26.0.0 dynamic, 26.1.0 static and later |
| [2300047](../errorcode-net-http.md#2300047-maximum-redirections-reached) | The number of redirections reaches the maximum allowed. |
| [2300055](../errorcode-net-http.md#2300055-failed-to-send-network-data) | Failed to send data to the peer. |
| [2300052](../errorcode-net-http.md#2300052-no-content-returned-by-the-server) | The server returned nothing (no header or data). |
| [2300059](../errorcode-net-http.md#2300059-failed-to-use-the-specified-ssl-cipher-algorithm) | The specified SSL cipher cannot be used. |
| [2300058](../errorcode-net-http.md#2300058-local-ssl-certificate-error) | Local SSL certificate error. |
| [2300056](../errorcode-net-http.md#2300056-failed-to-receive-network-data) | Failed to receive data from the peer. |
| [2300063](../errorcode-net-http.md#2300063-maximum-file-size-exceeded) | Maximum file size exceeded. |
| [2300061](../errorcode-net-http.md#2300061-unrecognized-or-incorrect-http-encoding-format) | Invalid HTTP encoding format. |
| [2300060](../errorcode-net-http.md#2300060-incorrect-ssl-certificate-or-ssh-key-of-the-remote-server) | Invalid SSL peer certificate or SSH remote key. |

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let httpRequest = http.createHttp();
httpRequest.requestInStream("EXAMPLE_URL", (err: BusinessError, data: number) => {
  if (!err) {
    console.info("requestInStream OK! ResponseCode is " + JSON.stringify(data));
  } else {
    console.error("requestInStream ERROR : err = " + JSON.stringify(err));
  }
})
```

```TypeScript
import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let httpRequest = http.createHttp();
httpRequest.requestInStream("EXAMPLE_URL", (err: BusinessError, data: number) => {
  if (!err) {
    console.info("requestInStream OK! ResponseCode is " + JSON.stringify(data));
  } else {
    console.error("requestInStream ERROR : err = " + JSON.stringify(err));
  }
})
```

## requestInStream

```TypeScript
requestInStream(url: string, options: HttpRequestOptions, callback: AsyncCallback<int>): void
```

Initiates an HTTP request containing specified options to a given URL. This API uses an asynchronous callback to return the result, which is a streaming response.

**Since:** 26.1.0

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-HttpRequest-requestInStream(url: string, options: HttpRequestOptions, callback: AsyncCallback<int>): void--><!--Device-HttpRequest-requestInStream(url: string, options: HttpRequestOptions, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | URL for initiating an HTTP request. |
| options | [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) | Yes | Request options. For details, see [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md#httprequestoptions). |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | Callback used to return the result. If the request is successful, **err** is **undefined**, and the [HTTP result code](arkts-network-http-responsecode-e.md#responsecode) is returned. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2300003](../errorcode-net-http.md#2300003-incorrect-url-format) | Invalid URL format or missing URL. |
| [2300001](../errorcode-net-http.md#2300001-protocol-not-supported) | Unsupported protocol. |
| [2300007](../errorcode-net-http.md#2300007-failed-to-connect-to-the-server) | Failed to connect to the server. |
| [2300006](../errorcode-net-http.md#2300006-failed-to-resolve-the-domain-name-of-the-host) | Failed to resolve the host name. |
| [2300070](../errorcode-net-http.md#2300070-insufficient-server-disk-space) | Remote disk full. |
| [2300005](../errorcode-net-http.md#2300005-failed-to-resolve-the-domain-name-of-the-proxy-server) | Failed to resolve the proxy name. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [2300009](../errorcode-net-http.md#2300009-access-to-remote-resources-denied) | Access to the remote resource denied. |
| [2300073](../errorcode-net-http.md#2300073-uploaded-file-already-exists) | Remote file already exists. |
| [2300008](../errorcode-net-http.md#2300008-invalid-data-returned-by-the-server) | Invalid server response. |
| [2300078](../errorcode-net-http.md#2300078-url-requested-file-not-found) | Remote file not found. |
| [2300077](../errorcode-net-http.md#2300077-no-ssl-ca-certificate-or-access-permission) | The SSL CA certificate does not exist or is inaccessible. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2300018](../errorcode-net-http.md#2300018-incomplete-data-returned-by-the-server) | Transferred a partial file. |
| [2300016](../errorcode-net-http.md#2300016-http2-framing-layer-error) | Error in the HTTP2 framing layer. |
| [2300023](../errorcode-net-http.md#2300023-failed-to-write-received-data-to-a-disk-or-application) | Failed to write the received data to the disk or application. |
| [2300027](../errorcode-net-http.md#2300027-insufficient-memory) | Out of memory. |
| [2300026](../errorcode-net-http.md#2300026-failed-to-open-or-read-local-data-from-a-file-or-application) | Failed to open or read local data from the file or application. |
| [2300025](../errorcode-net-http.md#2300025-failed-to-upload-data) | Upload failed. |
| [2300094](../errorcode-net-http.md#2300094-identity-verification-failed) | Authentication error. |
| [2300028](../errorcode-net-http.md#2300028-operation-timeout) | Operation timeout. |
| [2300999](../errorcode-net-http.md#2300999-internal-error) | Unknown error. |
| [2300998](../errorcode-net-http.md#2300998-domain-access-denied) | It is not allowed to access this domain.<br>**Applicable version:** 12 and later |
| [2300997](../errorcode-net-http.md#2300997-plaintext-http-access-intercepted) | Cleartext traffic not permitted.<br>**Applicable version:** 18 and later |
| 2300996 | The request was intercepted by the HTTP global interceptor.<br>**Applicable version:** 26.0.0 dynamic, 26.1.0 static and later |
| [2300047](../errorcode-net-http.md#2300047-maximum-redirections-reached) | The number of redirections reaches the maximum allowed. |
| [2300055](../errorcode-net-http.md#2300055-failed-to-send-network-data) | Failed to send data to the peer. |
| [2300052](../errorcode-net-http.md#2300052-no-content-returned-by-the-server) | The server returned nothing (no header or data). |
| [2300059](../errorcode-net-http.md#2300059-failed-to-use-the-specified-ssl-cipher-algorithm) | The specified SSL cipher cannot be used. |
| [2300058](../errorcode-net-http.md#2300058-local-ssl-certificate-error) | Local SSL certificate error. |
| [2300056](../errorcode-net-http.md#2300056-failed-to-receive-network-data) | Failed to receive data from the peer. |
| [2300063](../errorcode-net-http.md#2300063-maximum-file-size-exceeded) | Maximum file size exceeded. |
| [2300061](../errorcode-net-http.md#2300061-unrecognized-or-incorrect-http-encoding-format) | Invalid HTTP encoding format. |
| [2300060](../errorcode-net-http.md#2300060-incorrect-ssl-certificate-or-ssh-key-of-the-remote-server) | Invalid SSL peer certificate or SSH remote key. |

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Header {
  public contentType: string;

  constructor(contentType: string) {
    this.contentType = contentType;
  }
}

let httpRequest = http.createHttp();
let options: http.HttpRequestOptions = {
    method: http.RequestMethod.POST, // Optional. The default value is http.RequestMethod.GET.
    // This field is used to transfer the request body when a POST request is used. Its format needs to be negotiated with the server.
    extraData: 'data to send',
    expectDataType: http.HttpDataType.STRING, // Optional. This parameter specifies the type of the return data.
    usingCache: true, // Optional. The default value is true.
    priority: 1, // Optional. The default value is 1.
    // You can add header fields based on service requirements.
    header: new Header('application/json'),
    readTimeout: 60000, // Optional. The default value is 60000, in ms.
    connectTimeout: 60000 // Optional. The default value is 60000, in ms.
    usingProtocol: http.HttpProtocol.HTTP1_1, // Optional. The default protocol type is automatically specified by the system.
    usingProxy: false, // Optional. By default, network proxy is not used. This field is supported since API version 10.
};
httpRequest.requestInStream("EXAMPLE_URL", options, (err: BusinessError<void> , data: number) => {
  if (!err) {
    console.info("requestInStream OK! ResponseCode is " + JSON.stringify(data));
  } else {
    console.error("requestInStream ERROR : err = " + JSON.stringify(err));
  }
})
```

```TypeScript
import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Header {
  public contentType: string;

  constructor(contentType: string) {
    this.contentType = contentType;
  }
}

let httpRequest = http.createHttp();
let options: http.HttpRequestOptions = {
    method: http.RequestMethod.POST, // Optional. The default value is http.RequestMethod.GET.
    // This field is used to transfer the request body when a POST request is used. Its format needs to be negotiated with the server.
    extraData: 'data to send',
    expectDataType: http.HttpDataType.STRING, // Optional. This parameter specifies the type of the return data.
    usingCache: true, // Optional. The default value is true.
    priority: 1, // Optional. The default value is 1.
    // You can add header fields based on service requirements.
    header: new Header('application/json'),
    readTimeout: 60000, // Optional. The default value is 60000, in ms.
    connectTimeout: 60000 // Optional. The default value is 60000, in ms.
    usingProtocol: http.HttpProtocol.HTTP1_1, // Optional. The default protocol type is automatically specified by the system.
    usingProxy: false, // Optional. By default, network proxy is not used. This field is supported since API version 10.
};
httpRequest.requestInStream("EXAMPLE_URL", options, (err: BusinessError<void> , data: number) => {
  if (!err) {
    console.info("requestInStream OK! ResponseCode is " + JSON.stringify(data));
  } else {
    console.error("requestInStream ERROR : err = " + JSON.stringify(err));
  }
})
```

## requestInStream

```TypeScript
requestInStream(url: string, options?: HttpRequestOptions): Promise<int>
```

Initiates an HTTP request containing specified options to a given URL. This API uses a promise to return the result, which is a streaming response.

**Since:** 26.1.0

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-HttpRequest-requestInStream(url: string, options?: HttpRequestOptions): Promise<int>--><!--Device-HttpRequest-requestInStream(url: string, options?: HttpRequestOptions): Promise<int>-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | URL for initiating an HTTP request. |
| options | [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) | No | Request options. For details, see [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md#httprequestoptions). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the [result]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2300003](../errorcode-net-http.md#2300003-incorrect-url-format) | Invalid URL format or missing URL. |
| [2300001](../errorcode-net-http.md#2300001-protocol-not-supported) | Unsupported protocol. |
| [2300007](../errorcode-net-http.md#2300007-failed-to-connect-to-the-server) | Failed to connect to the server. |
| [2300006](../errorcode-net-http.md#2300006-failed-to-resolve-the-domain-name-of-the-host) | Failed to resolve the host name. |
| [2300070](../errorcode-net-http.md#2300070-insufficient-server-disk-space) | Remote disk full. |
| [2300005](../errorcode-net-http.md#2300005-failed-to-resolve-the-domain-name-of-the-proxy-server) | Failed to resolve the proxy name. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [2300009](../errorcode-net-http.md#2300009-access-to-remote-resources-denied) | Access to the remote resource denied. |
| [2300073](../errorcode-net-http.md#2300073-uploaded-file-already-exists) | Remote file already exists. |
| [2300008](../errorcode-net-http.md#2300008-invalid-data-returned-by-the-server) | Invalid server response. |
| [2300078](../errorcode-net-http.md#2300078-url-requested-file-not-found) | Remote file not found. |
| [2300077](../errorcode-net-http.md#2300077-no-ssl-ca-certificate-or-access-permission) | The SSL CA certificate does not exist or is inaccessible. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2300018](../errorcode-net-http.md#2300018-incomplete-data-returned-by-the-server) | Transferred a partial file. |
| [2300016](../errorcode-net-http.md#2300016-http2-framing-layer-error) | Error in the HTTP2 framing layer. |
| [2300023](../errorcode-net-http.md#2300023-failed-to-write-received-data-to-a-disk-or-application) | Failed to write the received data to the disk or application. |
| [2300027](../errorcode-net-http.md#2300027-insufficient-memory) | Out of memory. |
| [2300026](../errorcode-net-http.md#2300026-failed-to-open-or-read-local-data-from-a-file-or-application) | Failed to open or read local data from the file or application. |
| [2300025](../errorcode-net-http.md#2300025-failed-to-upload-data) | Upload failed. |
| [2300094](../errorcode-net-http.md#2300094-identity-verification-failed) | Authentication error. |
| [2300028](../errorcode-net-http.md#2300028-operation-timeout) | Operation timeout. |
| [2300999](../errorcode-net-http.md#2300999-internal-error) | Unknown error. |
| [2300998](../errorcode-net-http.md#2300998-domain-access-denied) | It is not allowed to access this domain.<br>**Applicable version:** 12 and later |
| [2300997](../errorcode-net-http.md#2300997-plaintext-http-access-intercepted) | Cleartext traffic not permitted.<br>**Applicable version:** 18 and later |
| 2300996 | The request was intercepted by the HTTP global interceptor.<br>**Applicable version:** 26.0.0 dynamic, 26.1.0 static and later |
| [2300047](../errorcode-net-http.md#2300047-maximum-redirections-reached) | The number of redirections reaches the maximum allowed. |
| [2300055](../errorcode-net-http.md#2300055-failed-to-send-network-data) | Failed to send data to the peer. |
| [2300052](../errorcode-net-http.md#2300052-no-content-returned-by-the-server) | The server returned nothing (no header or data). |
| [2300059](../errorcode-net-http.md#2300059-failed-to-use-the-specified-ssl-cipher-algorithm) | The specified SSL cipher cannot be used. |
| [2300058](../errorcode-net-http.md#2300058-local-ssl-certificate-error) | Local SSL certificate error. |
| [2300056](../errorcode-net-http.md#2300056-failed-to-receive-network-data) | Failed to receive data from the peer. |
| [2300063](../errorcode-net-http.md#2300063-maximum-file-size-exceeded) | Maximum file size exceeded. |
| [2300061](../errorcode-net-http.md#2300061-unrecognized-or-incorrect-http-encoding-format) | Invalid HTTP encoding format. |
| [2300060](../errorcode-net-http.md#2300060-incorrect-ssl-certificate-or-ssh-key-of-the-remote-server) | Invalid SSL peer certificate or SSH remote key. |

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';

class Header {
  public contentType: string;

  constructor(contentType: string) {
    this.contentType = contentType;
  }
}

let httpRequest = http.createHttp();
let promise = httpRequest.requestInStream("EXAMPLE_URL", {
  method: http.RequestMethod.GET,
  connectTimeout: 60000,
  readTimeout: 60000,
  header: new Header('application/json')
});
promise.then((data: number) => {
  console.info("requestInStream OK!" + data);
}).catch((err: Error) => {
  console.error("requestInStream ERROR : err = " + JSON.stringify(err));
});
```

```TypeScript
import { http } from '@kit.NetworkKit';

class Header {
  public contentType: string;

  constructor(contentType: string) {
    this.contentType = contentType;
  }
}

let httpRequest = http.createHttp();
let promise = httpRequest.requestInStream("EXAMPLE_URL", {
  method: http.RequestMethod.GET,
  connectTimeout: 60000,
  readTimeout: 60000,
  header: new Header('application/json')
});
promise.then((data: number) => {
  console.info("requestInStream OK!" + data);
}).catch((err: Error) => {
  console.error("requestInStream ERROR : err = " + JSON.stringify(err));
});
```

## requestSync

```TypeScript
requestSync(url: string, options?: HttpRequestOptions): HttpResponse
```

Initiates an HTTP network request based on the URL and related configuration options (optional). This API returns the response synchronously. > **NOTE：**> > (1) This API can receive data of up to 50 MB. To receive more than 50 MB of data, set the **maxLimit** > parameter in [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md#httprequestoptions). > (2) If you need to pass in cookies, add them to the **options** parameter. > (3) If the URL contains non-English characters, call **encodeURL(url)** to encode the URL before initiating an > HTTP request. > (4) This API is synchronous and blocks the current thread until an HTTP response or error code is returned. **Required permission**: ohos.permission.INTERNET

**Since:** 26.0.0

**Required permissions:** ohos.permission.INTERNET

**Model restriction:** This API can be used only in the stage model.

<!--Device-HttpRequest-requestSync(url: string, options?: HttpRequestOptions): HttpResponse--><!--Device-HttpRequest-requestSync(url: string, options?: HttpRequestOptions): HttpResponse-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | URL for initiating an HTTP request. |
| options | [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) | No | Request options. For details, see [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md#httprequestoptions). |

**Return value:**

| Type | Description |
| --- | --- |
| HttpResponse | HTTP request response result that is returned synchronously. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2300003](../errorcode-net-http.md#2300003-incorrect-url-format) | Invalid URL format or missing URL. |
| [2300001](../errorcode-net-http.md#2300001-protocol-not-supported) | Unsupported protocol. |
| [2300007](../errorcode-net-http.md#2300007-failed-to-connect-to-the-server) | Failed to connect to the server. |
| [2300006](../errorcode-net-http.md#2300006-failed-to-resolve-the-domain-name-of-the-host) | Failed to resolve the host name. |
| [2300070](../errorcode-net-http.md#2300070-insufficient-server-disk-space) | Remote disk full. |
| [2300005](../errorcode-net-http.md#2300005-failed-to-resolve-the-domain-name-of-the-proxy-server) | Failed to resolve the proxy name. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [2300009](../errorcode-net-http.md#2300009-access-to-remote-resources-denied) | Access to the remote resource denied. |
| [2300073](../errorcode-net-http.md#2300073-uploaded-file-already-exists) | Remote file already exists. |
| [2300008](../errorcode-net-http.md#2300008-invalid-data-returned-by-the-server) | Invalid server response. |
| [2300078](../errorcode-net-http.md#2300078-url-requested-file-not-found) | Remote file not found. |
| [2300077](../errorcode-net-http.md#2300077-no-ssl-ca-certificate-or-access-permission) | The SSL CA certificate does not exist or is inaccessible. |
| [2300018](../errorcode-net-http.md#2300018-incomplete-data-returned-by-the-server) | Transferred a partial file. |
| [2300016](../errorcode-net-http.md#2300016-http2-framing-layer-error) | Error in the HTTP2 framing layer. |
| [2300023](../errorcode-net-http.md#2300023-failed-to-write-received-data-to-a-disk-or-application) | Failed to write the received data to the disk or application. |
| [2300027](../errorcode-net-http.md#2300027-insufficient-memory) | Out of memory. |
| [2300026](../errorcode-net-http.md#2300026-failed-to-open-or-read-local-data-from-a-file-or-application) | Failed to open or read local data from the file or application. |
| [2300025](../errorcode-net-http.md#2300025-failed-to-upload-data) | Upload failed. |
| [2300094](../errorcode-net-http.md#2300094-identity-verification-failed) | Authentication error. |
| [2300028](../errorcode-net-http.md#2300028-operation-timeout) | Operation timeout. |
| [2300999](../errorcode-net-http.md#2300999-internal-error) | Internal error. |
| [2300998](../errorcode-net-http.md#2300998-domain-access-denied) | It is not allowed to access this domain. |
| [2300997](../errorcode-net-http.md#2300997-plaintext-http-access-intercepted) | Cleartext traffic not permitted. |
| 2300996 | The request was intercepted by the HTTP global interceptor. |
| [2300047](../errorcode-net-http.md#2300047-maximum-redirections-reached) | The number of redirections reaches the maximum allowed. |
| [2300055](../errorcode-net-http.md#2300055-failed-to-send-network-data) | Failed to send data to the peer. |
| [2300052](../errorcode-net-http.md#2300052-no-content-returned-by-the-server) | The server returned nothing (no header or data). |
| [2300059](../errorcode-net-http.md#2300059-failed-to-use-the-specified-ssl-cipher-algorithm) | The specified SSL cipher cannot be used. |
| [2300058](../errorcode-net-http.md#2300058-local-ssl-certificate-error) | Local SSL certificate error. |
| [2300056](../errorcode-net-http.md#2300056-failed-to-receive-network-data) | Failed to receive data from the peer. |
| [2300063](../errorcode-net-http.md#2300063-maximum-file-size-exceeded) | Maximum file size exceeded. |
| [2300061](../errorcode-net-http.md#2300061-unrecognized-or-incorrect-http-encoding-format) | Invalid HTTP encoding format. |
| [2300060](../errorcode-net-http.md#2300060-incorrect-ssl-certificate-or-ssh-key-of-the-remote-server) | Invalid SSL peer certificate or SSH remote key. |

