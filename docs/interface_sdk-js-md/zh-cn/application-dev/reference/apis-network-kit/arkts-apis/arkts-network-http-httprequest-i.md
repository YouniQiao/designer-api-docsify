# HttpRequest

&lt;p&gt;Defines an HTTP request task. Before invoking APIs provided by HttpRequest,you must call createHttp() to create an HttpRequestTask object.&lt;/p&gt;

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-http-export interface HttpRequest--><!--Device-http-export interface HttpRequest-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## destroy

```TypeScript
destroy(): void
```

Destroys an HTTP request.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-destroy(): void--><!--Device-HttpRequest-destroy(): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 示例

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

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HttpRequest-enableAutoCookie(enable: boolean): void--><!--Device-HttpRequest-enableAutoCookie(enable: boolean): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | whether to automatically reply with cookies, default is false. |

## 示例

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
let url = "EXAMPLE_URL"; // 访问url，需要开发者根据实际场景自行定义。

// 开启自动Cookie共享。
httpRequest.enableAutoCookie(true);

httpRequest.request(url, {
  method: http.RequestMethod.GET
}).then((data: http.HttpResponse) => {
  console.info('first request code:' + data.responseCode);
  // 后续请求将自动复用该实例保存的Cookie。
  return httpRequest.request(url, { method: http.RequestMethod.GET });
}).then((data: http.HttpResponse) => {
  console.info('second request code:' + data.responseCode);
}).catch((err: Error) => {
  console.error('error:' + JSON.stringify(err));
}).finally(() => {
  httpRequest.destroy();
});
```

## off("headerReceive")

```TypeScript
off(type: "headerReceive", callback?: AsyncCallback<Object>): void
```

Unregisters the observer for HTTP Response Header events.

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 8

**替代接口：** [off_headersReceive](arkts-network-http-httprequest-i.md#off)

<!--Device-HttpRequest-off(type: "headerReceive", callback?: AsyncCallback<Object>): void--><!--Device-HttpRequest-off(type: "headerReceive", callback?: AsyncCallback<Object>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | "headerReceive" | 是 | Indicates Event name. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Object&gt; | 否 | the callback used to return the result. |

## 示例

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.off("headerReceive");
```

## off("headersReceive")

```TypeScript
off(type: "headersReceive", callback?: Callback<Object>): void
```

Unregisters the observer for HTTP Response Header events.

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-off(type: "headersReceive", callback?: Callback<Object>): void--><!--Device-HttpRequest-off(type: "headersReceive", callback?: Callback<Object>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | "headersReceive" | 是 | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Object&gt; | 否 | the callback used to return the result. |

## 示例

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("headersReceive", (header: Object) => {
  console.info("header: " + JSON.stringify(header));
});
httpRequest.off("headersReceive");
```

## off("dataReceive")

```TypeScript
off(type: "dataReceive", callback?: Callback<ArrayBuffer>): void
```

Unregisters an observer for receiving HTTP Response data events continuously.

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-off(type: "dataReceive", callback?: Callback<ArrayBuffer>): void--><!--Device-HttpRequest-off(type: "dataReceive", callback?: Callback<ArrayBuffer>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | "dataReceive" | 是 | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | 否 | the callback used to return the result. |

## 示例

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataReceive", (data: ArrayBuffer) => {
  console.info("dataReceive length: " + JSON.stringify(data.byteLength));
});
httpRequest.off("dataReceive");
```

## off("dataEnd")

```TypeScript
off(type: "dataEnd", callback?: Callback<void>): void
```

Unregisters an observer for receiving HTTP Response data ends events.

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-off(type: "dataEnd", callback?: Callback<void>): void--><!--Device-HttpRequest-off(type: "dataEnd", callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | "dataEnd" | 是 | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 | the callback used to return the result. |

## 示例

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataEnd", () => {
  console.info("Receive dataEnd !");
});
httpRequest.off("dataEnd");
```

## off('dataReceiveProgress')

```TypeScript
off(type: 'dataReceiveProgress', callback?: Callback<DataReceiveProgressInfo>): void
```

Unregisters an observer for progress of receiving HTTP Response data events.

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-off(type: 'dataReceiveProgress', callback?: Callback<DataReceiveProgressInfo>): void--><!--Device-HttpRequest-off(type: 'dataReceiveProgress', callback?: Callback<DataReceiveProgressInfo>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'dataReceiveProgress' | 是 | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataReceiveProgressInfo&gt; | 否 | the callback used to return the result. |

## 示例

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataReceiveProgress", (data: http.DataReceiveProgressInfo) => {
  console.info("dataReceiveProgress:" + JSON.stringify(data));
});
httpRequest.off("dataReceiveProgress");
```

## off('dataSendProgress')

```TypeScript
off(type: 'dataSendProgress', callback?: Callback<DataSendProgressInfo>): void
```

Unregisters an observer for progress of sendSize HTTP Response data events.

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-off(type: 'dataSendProgress', callback?: Callback<DataSendProgressInfo>): void--><!--Device-HttpRequest-off(type: 'dataSendProgress', callback?: Callback<DataSendProgressInfo>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'dataSendProgress' | 是 | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataSendProgressInfo&gt; | 否 | the callback of off. |

## 示例

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataSendProgress", (data: http.DataSendProgressInfo) => {
  console.info("dataSendProgress:" + JSON.stringify(data));
});
httpRequest.off("dataSendProgress");
```

## offDataEnd

```TypeScript
offDataEnd(callback?: Callback<void>): void
```

Unregisters an observer for receiving HTTP Response data ends events.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-offDataEnd(callback?: Callback<void>): void--><!--Device-HttpRequest-offDataEnd(callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 | the callback used to return the result. |

## offDataReceive

```TypeScript
offDataReceive(callback?: Callback<ArrayBuffer>): void
```

Unregisters an observer for receiving HTTP Response data events continuously.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-offDataReceive(callback?: Callback<ArrayBuffer>): void--><!--Device-HttpRequest-offDataReceive(callback?: Callback<ArrayBuffer>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | 否 | the callback used to return the result. |

## offDataReceiveProgress

```TypeScript
offDataReceiveProgress(callback?: Callback<DataReceiveProgressInfo>): void
```

Unregisters an observer for progress of receiving HTTP Response data events.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-offDataReceiveProgress(callback?: Callback<DataReceiveProgressInfo>): void--><!--Device-HttpRequest-offDataReceiveProgress(callback?: Callback<DataReceiveProgressInfo>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataReceiveProgressInfo&gt; | 否 | the callback used to return the result. |

## offDataSendProgress

```TypeScript
offDataSendProgress(callback?: Callback<DataSendProgressInfo>): void
```

Unregisters an observer for progress of sendSize HTTP Response data events.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-offDataSendProgress(callback?: Callback<DataSendProgressInfo>): void--><!--Device-HttpRequest-offDataSendProgress(callback?: Callback<DataSendProgressInfo>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataSendProgressInfo&gt; | 否 | the callback of off. |

## offHeadersReceive

```TypeScript
offHeadersReceive(callback?: Callback<Record<string, string>>): void
```

Unregisters the observer for HTTP Response Header events.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-offHeadersReceive(callback?: Callback<Record<string, string>>): void--><!--Device-HttpRequest-offHeadersReceive(callback?: Callback<Record<string, string>>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, string&gt;&gt; | 否 | the callback used to return the result. |

## on("headerReceive")

```TypeScript
on(type: "headerReceive", callback: AsyncCallback<Object>): void
```

Registers an observer for HTTP Response Header events.

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 8

**替代接口：** [on_headersReceive](arkts-network-http-httprequest-i.md#on)

<!--Device-HttpRequest-on(type: "headerReceive", callback: AsyncCallback<Object>): void--><!--Device-HttpRequest-on(type: "headerReceive", callback: AsyncCallback<Object>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | "headerReceive" | 是 | Indicates Event name. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Object&gt; | 是 | the callback used to return the result. |

## 示例

```TypeScript
import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let httpRequest = http.createHttp();
httpRequest.on("headerReceive", (data: BusinessError) => {
  console.error("error:" + JSON.stringify(data));
});
```

## on("headersReceive")

```TypeScript
on(type: "headersReceive", callback: Callback<Object>): void
```

Registers an observer for HTTP Response Header events.

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-on(type: "headersReceive", callback: Callback<Object>): void--><!--Device-HttpRequest-on(type: "headersReceive", callback: Callback<Object>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | "headersReceive" | 是 | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Object&gt; | 是 | the callback used to return the result. |

## 示例

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("headersReceive", (header: Object) => {
  console.info("header: " + JSON.stringify(header));
});
httpRequest.off("headersReceive");
```

## on("dataReceive")

```TypeScript
on(type: "dataReceive", callback: Callback<ArrayBuffer>): void
```

Registers an observer for receiving HTTP Response data events continuously.

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-on(type: "dataReceive", callback: Callback<ArrayBuffer>): void--><!--Device-HttpRequest-on(type: "dataReceive", callback: Callback<ArrayBuffer>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | "dataReceive" | 是 | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | 是 | the callback used to return the result. |

## 示例

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataReceive", (data: ArrayBuffer) => {
  console.info("dataReceive length: " + JSON.stringify(data.byteLength));
});
httpRequest.off("dataReceive");
```

## on("dataEnd")

```TypeScript
on(type: "dataEnd", callback: Callback<void>): void
```

Registers an observer for receiving HTTP Response data ends events.

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-on(type: "dataEnd", callback: Callback<void>): void--><!--Device-HttpRequest-on(type: "dataEnd", callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | "dataEnd" | 是 | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 | the callback used to return the result. |

## 示例

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataEnd", () => {
  console.info("Receive dataEnd !");
});
httpRequest.off("dataEnd");
```

## on('dataReceiveProgress')

```TypeScript
on(type: 'dataReceiveProgress', callback: Callback<DataReceiveProgressInfo>): void
```

Registers an observer for progress of receiving HTTP Response data events.

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-on(type: 'dataReceiveProgress', callback: Callback<DataReceiveProgressInfo>): void--><!--Device-HttpRequest-on(type: 'dataReceiveProgress', callback: Callback<DataReceiveProgressInfo>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'dataReceiveProgress' | 是 | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataReceiveProgressInfo&gt; | 是 | the callback used to return the result. |

## 示例

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataReceiveProgress", (data: http.DataReceiveProgressInfo) => {
  console.info("dataReceiveProgress:" + JSON.stringify(data));
});
httpRequest.off("dataReceiveProgress");
```

## on('dataSendProgress')

```TypeScript
on(type: 'dataSendProgress', callback: Callback<DataSendProgressInfo>): void
```

Registers an observer for progress of sendSize HTTP Response data events.

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-on(type: 'dataSendProgress', callback: Callback<DataSendProgressInfo>): void--><!--Device-HttpRequest-on(type: 'dataSendProgress', callback: Callback<DataSendProgressInfo>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'dataSendProgress' | 是 | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataSendProgressInfo&gt; | 是 | the callback of on. |

## 示例

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataSendProgress", (data: http.DataSendProgressInfo) => {
  console.info("dataSendProgress:" + JSON.stringify(data));
});
httpRequest.off("dataSendProgress");
```

## onDataEnd

```TypeScript
onDataEnd(callback: Callback<void>): void
```

Registers an observer for receiving HTTP Response data ends events.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-onDataEnd(callback: Callback<void>): void--><!--Device-HttpRequest-onDataEnd(callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 | the callback used to return the result. |

## onDataReceive

```TypeScript
onDataReceive(callback: Callback<ArrayBuffer>): void
```

Registers an observer for receiving HTTP Response data events continuously.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-onDataReceive(callback: Callback<ArrayBuffer>): void--><!--Device-HttpRequest-onDataReceive(callback: Callback<ArrayBuffer>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | 是 | the callback used to return the result. |

## onDataReceiveProgress

```TypeScript
onDataReceiveProgress(callback: Callback<DataReceiveProgressInfo>): void
```

Registers an observer for progress of receiving HTTP Response data events.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-onDataReceiveProgress(callback: Callback<DataReceiveProgressInfo>): void--><!--Device-HttpRequest-onDataReceiveProgress(callback: Callback<DataReceiveProgressInfo>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataReceiveProgressInfo&gt; | 是 | the callback used to return the result. |

## onDataSendProgress

```TypeScript
onDataSendProgress(callback: Callback<DataSendProgressInfo>): void
```

Registers an observer for progress of sendSize HTTP Response data events.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-onDataSendProgress(callback: Callback<DataSendProgressInfo>): void--><!--Device-HttpRequest-onDataSendProgress(callback: Callback<DataSendProgressInfo>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataSendProgressInfo&gt; | 是 | the callback of on. |

## onHeadersReceive

```TypeScript
onHeadersReceive(callback: Callback<Record<string, string>>): void
```

Registers an observer for HTTP Response Header events.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-onHeadersReceive(callback: Callback<Record<string, string>>): void--><!--Device-HttpRequest-onHeadersReceive(callback: Callback<Record<string, string>>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, string&gt;&gt; | 是 | the callback used to return the result. |

## once("headersReceive")

```TypeScript
once(type: "headersReceive", callback: Callback<Object>): void
```

Registers a one-time observer for HTTP Response Header events.

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-once(type: "headersReceive", callback: Callback<Object>): void--><!--Device-HttpRequest-once(type: "headersReceive", callback: Callback<Object>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | "headersReceive" | 是 | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Object&gt; | 是 | the callback used to return the result. |

## 示例

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.once("headersReceive", (header: Object) => {
  console.info("header: " + JSON.stringify(header));
});
```

## onceHeadersReceive

```TypeScript
onceHeadersReceive(callback: Callback<Record<string, string>>): void
```

Registers a one-time observer for HTTP Response Header events.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-onceHeadersReceive(callback: Callback<Record<string, string>>): void--><!--Device-HttpRequest-onceHeadersReceive(callback: Callback<Record<string, string>>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, string&gt;&gt; | 是 | the callback used to return the result. |

## request

```TypeScript
request(url: string, callback: AsyncCallback<HttpResponse>): void
```

Initiates an HTTP request to a given URL. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> (1) This API can receive only data whose size is less than 5 MB. If the data size exceeds 5 MB, you need to set
> **maxLimit** to a larger value in [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) or call
> [requestInStream](arkts-network-http-httprequest-i.md#requestinstream) to
> initiate a streaming request. Since API version 23, this API can receive a maximum of 50 MB data. In versions
> earlier than API version 23, this API can receive a maximum of 5 MB data, and any data exceeding this threshold
> will fail to be received.

> (2) If you need to pass in cookies, add them to the **options** parameter.

> (3) If the URL contains non-English characters, call **encodeURL(url)** to encode the URL before initiating an
> HTTP request.

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-request(url: string, callback: AsyncCallback<HttpResponse>): void--><!--Device-HttpRequest-request(url: string, callback: AsyncCallback<HttpResponse>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | URL for initiating an HTTP request. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HttpResponse&gt; | 是 | Callback used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2300003 | Invalid URL format or missing URL. |
| 2300001 | Unsupported protocol. |
| 2300007 | Failed to connect to the server. |
| 2300006 | Failed to resolve the host name. |
| 2300070 | Remote disk full. |
| 2300005 | Failed to resolve the proxy name. |
| 201 | Permission denied. |
| 2300009 | Access to the remote resource denied. |
| 2300073 | Remote file already exists. |
| 2300008 | Invalid server response. |
| 2300078 | Remote file not found. |
| 2300077 | The SSL CA certificate does not exist or is inaccessible. |
| 401 | Parameter error. |
| 2300018 | Transferred a partial file. |
| 2300016 | Error in the HTTP2 framing layer. |
| 2300023 | Failed to write the received data to the disk or application. |
| 2300027 | Out of memory. |
| 2300026 | Failed to open or read local data from the file or application. |
| 2300025 | Upload failed. |
| 2300094 | Authentication error. |
| 2300028 | Operation timeout. |
| 2300999 | Internal error. |
| 2300998 | It is not allowed to access this domain.<br>**适用版本：** 12+ |
| 2300997 | Cleartext traffic not permitted.<br>**适用版本：** 18+ |
| 2300996 | The request was intercepted by the HTTP global interceptor.<br>**适用版本：** 26.0.0 dynamic&static+ |
| 2300047 | The number of redirections reaches the maximum allowed. |
| 2300055 | Failed to send data to the peer. |
| 2300052 | The server returned nothing (no header or data). |
| 2300059 | The specified SSL cipher cannot be used. |
| 2300058 | Local SSL certificate error. |
| 2300056 | Failed to receive data from the peer. |
| 2300063 | Maximum file size exceeded. |
| 2300061 | Invalid HTTP encoding format. |
| 2300060 | Invalid SSL peer certificate or SSH remote key. |

## 示例

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.request("EXAMPLE_URL", (err: Error, data: http.HttpResponse) => {
  if (!err) {
    console.info('Result:' + data.result);
    console.info('code:' + data.responseCode);
    console.info('type:' + JSON.stringify(data.resultType));
    console.info('header:' + JSON.stringify(data.header));
    console.info('cookies:' + data.cookies); // 自API version 8开始支持cookie。
  } else {
    console.error('error:' + JSON.stringify(err));
  }
});
```

## request

```TypeScript
request(url: string, options: HttpRequestOptions, callback: AsyncCallback<HttpResponse>): void
```

Initiates an HTTP request containing specified options to a given URL. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> (1) This API can receive only data whose size is less than 5 MB. If the data size exceeds 5 MB, you need to set
> **maxLimit** to a larger value in [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) or call
> [requestInStream](arkts-network-http-httprequest-i.md#requestinstream) to
> initiate a streaming request. Since API version 23, this API can receive a maximum of 50 MB data. In versions
> earlier than API version 23, this API can receive a maximum of 5 MB data, and any data exceeding this threshold
> will fail to be received.

> (2) If you need to pass in cookies, add them to the **options** parameter.

> (3) If the URL contains non-English characters, call **encodeURL(url)** to encode the URL before initiating an
> HTTP request.

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-request(url: string, options: HttpRequestOptions, callback: AsyncCallback<HttpResponse>): void--><!--Device-HttpRequest-request(url: string, options: HttpRequestOptions, callback: AsyncCallback<HttpResponse>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | URL for initiating an HTTP request. |
| options | [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) | 是 | Request options. For details, see [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md). |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HttpResponse&gt; | 是 | Callback used to return the result. If the operation is successful, the callback content is an [HttpResponse](arkts-network-http-httpresponse-i.md) object; otherwise, the callback content is undefined. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2300003 | Invalid URL format or missing URL. |
| 2300001 | Unsupported protocol. |
| 2300007 | Failed to connect to the server. |
| 2300006 | Failed to resolve the host name. |
| 2300070 | Remote disk full. |
| 2300005 | Failed to resolve the proxy name. |
| 201 | Permission denied. |
| 2300009 | Access to the remote resource denied. |
| 2300073 | Remote file already exists. |
| 2300008 | Invalid server response. |
| 2300078 | Remote file not found. |
| 2300077 | The SSL CA certificate does not exist or is inaccessible. |
| 401 | Parameter error. |
| 2300018 | Transferred a partial file. |
| 2300016 | Error in the HTTP2 framing layer. |
| 2300023 | Failed to write the received data to the disk or application. |
| 2300027 | Out of memory. |
| 2300026 | Failed to open or read local data from the file or application. |
| 2300025 | Upload failed. |
| 2300094 | Authentication error. |
| 2300028 | Operation timeout. |
| 2300999 | Internal error. |
| 2300998 | It is not allowed to access this domain.<br>**适用版本：** 12+ |
| 2300997 | Cleartext traffic not permitted.<br>**适用版本：** 18+ |
| 2300996 | The request was intercepted by the HTTP global interceptor.<br>**适用版本：** 26.0.0 dynamic&static+ |
| 2300047 | The number of redirections reaches the maximum allowed. |
| 2300055 | Failed to send data to the peer. |
| 2300052 | The server returned nothing (no header or data). |
| 2300059 | The specified SSL cipher cannot be used. |
| 2300058 | Local SSL certificate error. |
| 2300056 | Failed to receive data from the peer. |
| 2300063 | Maximum file size exceeded. |
| 2300061 | Invalid HTTP encoding format. |
| 2300060 | Invalid SSL peer certificate or SSH remote key. |

## 示例

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
    method: http.RequestMethod.POST, // 可选，默认为http.RequestMethod.GET。
  // 推荐使用body字段传递请求体内容，具体格式与服务端协商确定。
  body: 'data to send', // 自API 26开始支持。
  // 推荐使用queryParams字段传递URL参数。可传string或对象。
  queryParams: { scene: 'request-demo', page: 1 }, // 自API 26开始支持。
    expectDataType: http.HttpDataType.STRING, // 可选，指定返回数据的类型。
    usingCache: true, // 可选，默认为true。
    priority: 1, // 可选，默认为1。
    // 开发者根据自身业务需要添加header字段。
    header: new Header('application/json'),
    readTimeout: 60000, // 可选，默认为60000ms。
    connectTimeout: 60000, // 可选，默认为60000ms。
    usingProtocol: http.HttpProtocol.HTTP1_1, // 可选，协议类型默认值由系统自动指定。
    usingProxy: false, // 可选，默认使用系统代理，设置为false不使用代理，自API 10开始支持该属性。
};

httpRequest.request("EXAMPLE_URL", options, (err: Error, data: http.HttpResponse) => {
  if (!err) {
    console.info('Result:' + data.result);
    console.info('code:' + data.responseCode);
    console.info('type:' + JSON.stringify(data.resultType));
    console.info('header:' + JSON.stringify(data.header));
    console.info('cookies:' + data.cookies); // 自API version 8开始支持cookie。
  } else {
    console.error('error:' + JSON.stringify(err));
  }
});
```

## request

```TypeScript
request(url: string, options?: HttpRequestOptions): Promise<HttpResponse>
```

Initiates an HTTP request containing specified options to a given URL. This API uses a promise to return the result.

> **NOTE：**
> 
> (1) This API can receive only data whose size is less than 5 MB. If the data size exceeds 5 MB, you need to set
> **maxLimit** to a larger value in [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) or call
> [requestInStream](arkts-network-http-httprequest-i.md#requestinstream) to
> initiate a streaming request. Since API version 23, this API can receive a maximum of 50 MB data. In versions
> earlier than API version 23, this API can receive a maximum of 5 MB data, and any data exceeding this threshold
> will fail to be received.

> (2) If you need to pass in cookies, add them to the **options** parameter.

> (3) If the URL contains non-English characters, call **encodeURL(url)** to encode the URL before initiating an
> HTTP request.

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-request(url: string, options?: HttpRequestOptions): Promise<HttpResponse>--><!--Device-HttpRequest-request(url: string, options?: HttpRequestOptions): Promise<HttpResponse>-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | URL for initiating an HTTP request. |
| options | [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) | 否 | Request options. For details, see [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md). |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;HttpResponse&gt; | Promise used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2300003 | Invalid URL format or missing URL. |
| 2300001 | Unsupported protocol. |
| 2300007 | Failed to connect to the server. |
| 2300006 | Failed to resolve the host name. |
| 2300070 | Remote disk full. |
| 2300005 | Failed to resolve the proxy name. |
| 201 | Permission denied. |
| 2300009 | Access to the remote resource denied. |
| 2300073 | Remote file already exists. |
| 2300008 | Invalid server response. |
| 2300078 | Remote file not found. |
| 2300077 | The SSL CA certificate does not exist or is inaccessible. |
| 401 | Parameter error. |
| 2300018 | Transferred a partial file. |
| 2300016 | Error in the HTTP2 framing layer. |
| 2300023 | Failed to write the received data to the disk or application. |
| 2300027 | Out of memory. |
| 2300026 | Failed to open or read local data from the file or application. |
| 2300025 | Upload failed. |
| 2300094 | Authentication error. |
| 2300028 | Operation timeout. |
| 2300999 | Internal error. |
| 2300998 | It is not allowed to access this domain.<br>**适用版本：** 12+ |
| 2300997 | Cleartext traffic not permitted.<br>**适用版本：** 18+ |
| 2300996 | The request was intercepted by the HTTP global interceptor.<br>**适用版本：** 26.0.0 dynamic&static+ |
| 2300047 | The number of redirections reaches the maximum allowed. |
| 2300055 | Failed to send data to the peer. |
| 2300052 | The server returned nothing (no header or data). |
| 2300059 | The specified SSL cipher cannot be used. |
| 2300058 | Local SSL certificate error. |
| 2300056 | Failed to receive data from the peer. |
| 2300063 | Maximum file size exceeded. |
| 2300061 | Invalid HTTP encoding format. |
| 2300060 | Invalid SSL peer certificate or SSH remote key. |

## 示例

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
  console.info('cookies:' + data.cookies); // 自API version 8开始支持cookie。
  console.info('header.content-Type:' + data.header);
  console.info('header.Status-Line:' + data.header);
}).catch((err:Error) => {
  console.error('error:' + JSON.stringify(err));
});
```

## requestInStream

ArkTS-Dyn:
```TypeScript
requestInStream(url: string, callback: AsyncCallback<number>): void
```

ArkTS-Sta:
```TypeScript
requestInStream(url: string, callback: AsyncCallback<int>): void
```

Initiates an HTTP request containing specified options to a given URL. This API uses an asynchronous callback to return the result, which is a streaming response.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为26.1.0。

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-requestInStream(url: string, callback: AsyncCallback<int>): void--><!--Device-HttpRequest-requestInStream(url: string, callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | URL for initiating an HTTP request. |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | 是 | Callback used to return the result. If the request is successful, **err** is **undefined**, and the HTTP result code is returned. Otherwise, **err** is an error object. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2300003 | Invalid URL format or missing URL. |
| 2300001 | Unsupported protocol. |
| 2300007 | Failed to connect to the server. |
| 2300006 | Failed to resolve the host name. |
| 2300070 | Remote disk full. |
| 2300005 | Failed to resolve the proxy name. |
| 201 | Permission denied. |
| 2300009 | Access to the remote resource denied. |
| 2300073 | Remote file already exists. |
| 2300008 | Invalid server response. |
| 2300078 | Remote file not found. |
| 2300077 | The SSL CA certificate does not exist or is inaccessible. |
| 401 | Parameter error. |
| 2300018 | Transferred a partial file. |
| 2300016 | Error in the HTTP2 framing layer. |
| 2300023 | Failed to write the received data to the disk or application. |
| 2300027 | Out of memory. |
| 2300026 | Failed to open or read local data from the file or application. |
| 2300025 | Upload failed. |
| 2300094 | Authentication error. |
| 2300028 | Operation timeout. |
| 2300999 | Unknown error. |
| 2300998 | It is not allowed to access this domain.<br>**适用版本：** 12+ |
| 2300997 | Cleartext traffic not permitted.<br>**适用版本：** 18+ |
| 2300996 | The request was intercepted by the HTTP global interceptor.<br>**适用版本：** 26.0.0 dynamic, 26.1.0 static+ |
| 2300047 | The number of redirections reaches the maximum allowed. |
| 2300055 | Failed to send data to the peer. |
| 2300052 | The server returned nothing (no header or data). |
| 2300059 | The specified SSL cipher cannot be used. |
| 2300058 | Local SSL certificate error. |
| 2300056 | Failed to receive data from the peer. |
| 2300063 | Maximum file size exceeded. |
| 2300061 | Invalid HTTP encoding format. |
| 2300060 | Invalid SSL peer certificate or SSH remote key. |

## 示例

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

ArkTS-Dyn:
```TypeScript
requestInStream(url: string, options: HttpRequestOptions, callback: AsyncCallback<number>): void
```

ArkTS-Sta:
```TypeScript
requestInStream(url: string, options: HttpRequestOptions, callback: AsyncCallback<int>): void
```

Initiates an HTTP request containing specified options to a given URL. This API uses an asynchronous callback to return the result, which is a streaming response.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为26.1.0。

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-requestInStream(url: string, options: HttpRequestOptions, callback: AsyncCallback<int>): void--><!--Device-HttpRequest-requestInStream(url: string, options: HttpRequestOptions, callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | URL for initiating an HTTP request. |
| options | [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) | 是 | Request options. For details, see [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md). |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | 是 | Callback used to return the result. If the request is successful, **err** is **undefined**, and the [HTTP result code](arkts-network-http-responsecode-e.md) is returned. Otherwise, **err** is an error object. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2300003 | Invalid URL format or missing URL. |
| 2300001 | Unsupported protocol. |
| 2300007 | Failed to connect to the server. |
| 2300006 | Failed to resolve the host name. |
| 2300070 | Remote disk full. |
| 2300005 | Failed to resolve the proxy name. |
| 201 | Permission denied. |
| 2300009 | Access to the remote resource denied. |
| 2300073 | Remote file already exists. |
| 2300008 | Invalid server response. |
| 2300078 | Remote file not found. |
| 2300077 | The SSL CA certificate does not exist or is inaccessible. |
| 401 | Parameter error. |
| 2300018 | Transferred a partial file. |
| 2300016 | Error in the HTTP2 framing layer. |
| 2300023 | Failed to write the received data to the disk or application. |
| 2300027 | Out of memory. |
| 2300026 | Failed to open or read local data from the file or application. |
| 2300025 | Upload failed. |
| 2300094 | Authentication error. |
| 2300028 | Operation timeout. |
| 2300999 | Unknown error. |
| 2300998 | It is not allowed to access this domain.<br>**适用版本：** 12+ |
| 2300997 | Cleartext traffic not permitted.<br>**适用版本：** 18+ |
| 2300996 | The request was intercepted by the HTTP global interceptor.<br>**适用版本：** 26.0.0 dynamic, 26.1.0 static+ |
| 2300047 | The number of redirections reaches the maximum allowed. |
| 2300055 | Failed to send data to the peer. |
| 2300052 | The server returned nothing (no header or data). |
| 2300059 | The specified SSL cipher cannot be used. |
| 2300058 | Local SSL certificate error. |
| 2300056 | Failed to receive data from the peer. |
| 2300063 | Maximum file size exceeded. |
| 2300061 | Invalid HTTP encoding format. |
| 2300060 | Invalid SSL peer certificate or SSH remote key. |

## 示例

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
    method: http.RequestMethod.POST, // 可选，默认为http.RequestMethod.GET。
    // 当使用POST请求时此字段用于传递请求体内容，具体格式与服务端协商确定。
    extraData: 'data to send', // 自API version 26开始，推荐使用body字段传递请求体内容，具体格式与服务端协商确定。
    expectDataType: http.HttpDataType.STRING, // 可选，指定返回数据的类型。
    usingCache: true, // 可选，默认为true。
    priority: 1, // 可选，默认为1。
    // 开发者根据自身业务需要添加header字段。
    header: new Header('application/json'),
    readTimeout: 60000, // 可选，默认为60000ms。
    connectTimeout: 60000, // 可选，默认为60000ms。
    usingProtocol: http.HttpProtocol.HTTP1_1, // 可选，协议类型默认值由系统自动指定。
    usingProxy: false, // 可选，默认使用系统代理，设置为false不使用代理，自API 10开始支持该属性。
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

ArkTS-Dyn:
```TypeScript
requestInStream(url: string, options?: HttpRequestOptions): Promise<number>
```

ArkTS-Sta:
```TypeScript
requestInStream(url: string, options?: HttpRequestOptions): Promise<int>
```

Initiates an HTTP request containing specified options to a given URL. This API uses a promise to return the result, which is a streaming response.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为26.1.0。

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequest-requestInStream(url: string, options?: HttpRequestOptions): Promise<int>--><!--Device-HttpRequest-requestInStream(url: string, options?: HttpRequestOptions): Promise<int>-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | URL for initiating an HTTP request. |
| options | [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) | 否 | Request options. For details, see [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md). |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise used to return the [result]{ |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2300003 | Invalid URL format or missing URL. |
| 2300001 | Unsupported protocol. |
| 2300007 | Failed to connect to the server. |
| 2300006 | Failed to resolve the host name. |
| 2300070 | Remote disk full. |
| 2300005 | Failed to resolve the proxy name. |
| 201 | Permission denied. |
| 2300009 | Access to the remote resource denied. |
| 2300073 | Remote file already exists. |
| 2300008 | Invalid server response. |
| 2300078 | Remote file not found. |
| 2300077 | The SSL CA certificate does not exist or is inaccessible. |
| 401 | Parameter error. |
| 2300018 | Transferred a partial file. |
| 2300016 | Error in the HTTP2 framing layer. |
| 2300023 | Failed to write the received data to the disk or application. |
| 2300027 | Out of memory. |
| 2300026 | Failed to open or read local data from the file or application. |
| 2300025 | Upload failed. |
| 2300094 | Authentication error. |
| 2300028 | Operation timeout. |
| 2300999 | Unknown error. |
| 2300998 | It is not allowed to access this domain.<br>**适用版本：** 12+ |
| 2300997 | Cleartext traffic not permitted.<br>**适用版本：** 18+ |
| 2300996 | The request was intercepted by the HTTP global interceptor.<br>**适用版本：** 26.0.0 dynamic, 26.1.0 static+ |
| 2300047 | The number of redirections reaches the maximum allowed. |
| 2300055 | Failed to send data to the peer. |
| 2300052 | The server returned nothing (no header or data). |
| 2300059 | The specified SSL cipher cannot be used. |
| 2300058 | Local SSL certificate error. |
| 2300056 | Failed to receive data from the peer. |
| 2300063 | Maximum file size exceeded. |
| 2300061 | Invalid HTTP encoding format. |
| 2300060 | Invalid SSL peer certificate or SSH remote key. |

## 示例

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

Initiates an HTTP network request based on the URL and related configuration options (optional). This API returns the response synchronously.

> **NOTE：**
> 
> (1) This API can receive data of up to 50 MB. To receive more than 50 MB of data, set the **maxLimit**
> parameter in [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md).

> (2) If you need to pass in cookies, add them to the **options** parameter.

> (3) If the URL contains non-English characters, call **encodeURL(url)** to encode the URL before initiating an
> HTTP request.

> (4) This API is synchronous and blocks the current thread until an HTTP response or error code is returned.

**Required permission**: ohos.permission.INTERNET

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.INTERNET

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HttpRequest-requestSync(url: string, options?: HttpRequestOptions): HttpResponse--><!--Device-HttpRequest-requestSync(url: string, options?: HttpRequestOptions): HttpResponse-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | URL for initiating an HTTP request. |
| options | [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) | 否 | Request options. For details, see [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md). |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HttpResponse](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-httpresponse-i.md) | HTTP request response result that is returned synchronously. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2300003 | Invalid URL format or missing URL. |
| 2300001 | Unsupported protocol. |
| 2300007 | Failed to connect to the server. |
| 2300006 | Failed to resolve the host name. |
| 2300070 | Remote disk full. |
| 2300005 | Failed to resolve the proxy name. |
| 201 | Permission denied. |
| 2300009 | Access to the remote resource denied. |
| 2300073 | Remote file already exists. |
| 2300008 | Invalid server response. |
| 2300078 | Remote file not found. |
| 2300077 | The SSL CA certificate does not exist or is inaccessible. |
| 2300018 | Transferred a partial file. |
| 2300016 | Error in the HTTP2 framing layer. |
| 2300023 | Failed to write the received data to the disk or application. |
| 2300027 | Out of memory. |
| 2300026 | Failed to open or read local data from the file or application. |
| 2300025 | Upload failed. |
| 2300094 | Authentication error. |
| 2300028 | Operation timeout. |
| 2300999 | Internal error. |
| 2300998 | It is not allowed to access this domain. |
| 2300997 | Cleartext traffic not permitted. |
| 2300996 | The request was intercepted by the HTTP global interceptor. |
| 2300047 | The number of redirections reaches the maximum allowed. |
| 2300055 | Failed to send data to the peer. |
| 2300052 | The server returned nothing (no header or data). |
| 2300059 | The specified SSL cipher cannot be used. |
| 2300058 | Local SSL certificate error. |
| 2300056 | Failed to receive data from the peer. |
| 2300063 | Maximum file size exceeded. |
| 2300061 | Invalid HTTP encoding format. |
| 2300060 | Invalid SSL peer certificate or SSH remote key. |

## 示例

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
    method: http.RequestMethod.POST, // 可选，默认为http.RequestMethod.GET。
    // 当使用POST请求时此字段用于传递请求体内容，具体格式与服务端协商确定。
    extraData: 'data to send',
    expectDataType: http.HttpDataType.STRING, // 可选，指定返回数据的类型。
    usingCache: true, // 可选，默认为true。
    priority: 1, // 可选，默认为1。
    // 开发者根据自身业务需要添加header字段。
    header: new Header('application/json'),
    readTimeout: 60000, // 可选，默认为60000ms。
    connectTimeout: 60000, // 可选，默认为60000ms。
    usingProtocol: http.HttpProtocol.HTTP1_1, // 可选，协议类型默认值由系统自动指定。
    usingProxy: false, // 可选，默认使用系统代理，设置为false不使用代理，自API 10开始支持该属性。
};
let url = "EXAMPLE_URL"; // 访问url
try {
  let data: http.HttpResponse = httpRequest.requestSync(url, options);
  console.info('Result:' + data.result);
  console.info('code:' + data.responseCode);
  console.info('type:' + JSON.stringify(data.resultType));
  console.info('header:' + JSON.stringify(data.header));
  console.info('cookies:' + data.cookies); // 自API version 8开始支持cookie。
} catch (err) {
  console.error('error:' + JSON.stringify(err));
}
httpRequest.destroy();
```

