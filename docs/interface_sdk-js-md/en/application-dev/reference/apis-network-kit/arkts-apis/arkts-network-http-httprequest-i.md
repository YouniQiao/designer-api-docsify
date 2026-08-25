# HttpRequest

Defines an HTTP request task. Before invoking APIs provided by **HttpRequest**, you must call [createHttp()](arkts-network-http-createhttp-f.md) to create an **HttpRequestTask** object.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { http } from '@kit.NetworkKit';
```

## destroy

```TypeScript
destroy(): void
```

Stops an HTTP request task and releases system resources.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

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

Sets whether to automatically carry and share cookies. That is, whether to automatically reuse the cookies delivered by the server among multiple requests of the same **HttpRequest** instance.

> **NOTE：**&gt;
> (1) The default value is **false**, indicating that cookies are not automatically carried.

> (2) If the value is changed from **false** to **true**, the setting takes effect when the **request** API is
> called to initiate a request, and cookies are automatically shared.

> (3) If the value is changed from **true** to **false**, the cookie sharing status stored in the current
> instance is cleared.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

## off("headerReceive")

```TypeScript
off(type: "headerReceive", callback?: AsyncCallback<Object>): void
```

Unregisters the observer for HTTP Response Header events.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 8

**Substitutes:** [off_headersReceive](#offheadersreceive)

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | "headerReceive" | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Object&gt; | No |

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

## off("headersReceive")

```TypeScript
off(type: "headersReceive", callback?: Callback<Object>): void
```

Unregisters the observer for HTTP Response Header events.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | "headersReceive" | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Object&gt; | No |

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

## off("dataReceive")

```TypeScript
off(type: "dataReceive", callback?: Callback<ArrayBuffer>): void
```

Unregisters the observer for events indicating receiving of HTTP streaming responses.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | "dataReceive" | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | No |

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

## off("dataEnd")

```TypeScript
off(type: "dataEnd", callback?: Callback<void>): void
```

Unregisters the observer for events indicating completion of receiving HTTP streaming responses.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | "dataEnd" | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

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

## off('dataReceiveProgress')

```TypeScript
off(type: 'dataReceiveProgress', callback?: Callback<DataReceiveProgressInfo>): void
```

Unregisters the observer for events indicating progress of receiving HTTP streaming responses.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'dataReceiveProgress' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataReceiveProgressInfo](arkts-network-http-datareceiveprogressinfo-i.md)&gt; | No |

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

## off('dataSendProgress')

```TypeScript
off(type: 'dataSendProgress', callback?: Callback<DataSendProgressInfo>): void
```

Unregisters the observer for events indicating progress of sending HTTP requests.

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'dataSendProgress' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataSendProgressInfo](arkts-network-http-datasendprogressinfo-i.md)&gt; | No |

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

## on("headerReceive")

```TypeScript
on(type: "headerReceive", callback: AsyncCallback<Object>): void
```

Registers an observer for HTTP Response Header events.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 8

**Substitutes:** [on_headersReceive](#onheadersreceive)

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | "headerReceive" | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Object&gt; | Yes |

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

## on("headersReceive")

```TypeScript
on(type: "headersReceive", callback: Callback<Object>): void
```

Registers an observer for HTTP Response Header events.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | "headersReceive" | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Object&gt; | Yes |

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

## on("dataReceive")

```TypeScript
on(type: "dataReceive", callback: Callback<ArrayBuffer>): void
```

Registers an observer for events indicating receiving of HTTP streaming responses.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | "dataReceive" | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | Yes |

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

## on("dataEnd")

```TypeScript
on(type: "dataEnd", callback: Callback<void>): void
```

Registers an observer for events indicating completion of receiving HTTP streaming responses.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | "dataEnd" | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

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

## on('dataReceiveProgress')

```TypeScript
on(type: 'dataReceiveProgress', callback: Callback<DataReceiveProgressInfo>): void
```

Registers an observer for events indicating progress of receiving HTTP streaming responses.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'dataReceiveProgress' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataReceiveProgressInfo](arkts-network-http-datareceiveprogressinfo-i.md)&gt; | Yes |

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

## on('dataSendProgress')

```TypeScript
on(type: 'dataSendProgress', callback: Callback<DataSendProgressInfo>): void
```

Registers an observer for events indicating progress of sending HTTP requests.

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'dataSendProgress' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataSendProgressInfo](arkts-network-http-datasendprogressinfo-i.md)&gt; | Yes |

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

## once("headersReceive")

```TypeScript
once(type: "headersReceive", callback: Callback<Object>): void
```

Registers a one-time observer for HTTP Response Header events. Once triggered, the observer will be removed. This API uses an asynchronous callback to return the result.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | "headersReceive" | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Object&gt; | Yes |

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

Initiates an HTTP request to a given URL. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> (1) This API can receive only data whose size is less than 5 MB. If the data size exceeds 5 MB, you need to set
> **maxLimit** to a larger value in [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) or call
> [requestInStream](#requestinstream) to
> initiate a streaming request. Since API version 23, this API can receive a maximum of 50 MB data. In versions
> earlier than API version 23, this API can receive a maximum of 5 MB data, and any data exceeding this threshold
> will fail to be received.

> (2) If you need to pass in cookies, add them to the **options** parameter.

> (3) If the URL contains non-English characters, call **encodeURL(url)** to encode the URL before initiating an
> HTTP request.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HttpResponse&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2300001](../errorcode-net-http.md#2300001-protocol-not-supported) |
| [2300003](../errorcode-net-http.md#2300003-incorrect-url-format) |
| [2300005](../errorcode-net-http.md#2300005-failed-to-resolve-the-domain-name-of-the-proxy-server) |
| [2300006](../errorcode-net-http.md#2300006-failed-to-resolve-the-domain-name-of-the-host) |
| [2300007](../errorcode-net-http.md#2300007-failed-to-connect-to-the-server) |
| [2300008](../errorcode-net-http.md#2300008-invalid-data-returned-by-the-server) |
| [2300009](../errorcode-net-http.md#2300009-access-to-remote-resources-denied) |
| [2300016](../errorcode-net-http.md#2300016-http2-framing-layer-error) |
| [2300018](../errorcode-net-http.md#2300018-incomplete-data-returned-by-the-server) |
| [2300023](../errorcode-net-http.md#2300023-failed-to-write-received-data-to-a-disk-or-application) |
| [2300025](../errorcode-net-http.md#2300025-failed-to-upload-data) |
| [2300026](../errorcode-net-http.md#2300026-failed-to-open-or-read-local-data-from-a-file-or-application) |
| [2300027](../errorcode-net-http.md#2300027-insufficient-memory) |
| [2300028](../errorcode-net-http.md#2300028-operation-timeout) |
| [2300047](../errorcode-net-http.md#2300047-maximum-redirections-reached) |
| [2300052](../errorcode-net-http.md#2300052-no-content-returned-by-the-server) |
| [2300055](../errorcode-net-http.md#2300055-failed-to-send-network-data) |
| [2300056](../errorcode-net-http.md#2300056-failed-to-receive-network-data) |
| [2300058](../errorcode-net-http.md#2300058-local-ssl-certificate-error) |
| [2300059](../errorcode-net-http.md#2300059-failed-to-use-the-specified-ssl-cipher-algorithm) |
| [2300060](../errorcode-net-http.md#2300060-incorrect-ssl-certificate-or-ssh-key-of-the-remote-server) |
| [2300061](../errorcode-net-http.md#2300061-unrecognized-or-incorrect-http-encoding-format) |
| [2300063](../errorcode-net-http.md#2300063-maximum-file-size-exceeded) |
| [2300070](../errorcode-net-http.md#2300070-insufficient-server-disk-space) |
| [2300073](../errorcode-net-http.md#2300073-uploaded-file-already-exists) |
| [2300077](../errorcode-net-http.md#2300077-no-ssl-ca-certificate-or-access-permission) |
| [2300078](../errorcode-net-http.md#2300078-url-requested-file-not-found) |
| [2300094](../errorcode-net-http.md#2300094-identity-verification-failed) |
| [2300999](../errorcode-net-http.md#2300999-internal-error) |
| [2300998](../errorcode-net-http.md#2300998-domain-access-denied) |
| [2300997](../errorcode-net-http.md#2300997-plaintext-http-access-intercepted) |
| 2300996 |

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

## request

```TypeScript
request(url: string, options: HttpRequestOptions, callback: AsyncCallback<HttpResponse>): void
```

Initiates an HTTP request containing specified options to a given URL. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> (1) This API can receive only data whose size is less than 5 MB. If the data size exceeds 5 MB, you need to set
> **maxLimit** to a larger value in [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) or call
> [requestInStream](#requestinstream) to
> initiate a streaming request. Since API version 23, this API can receive a maximum of 50 MB data. In versions
> earlier than API version 23, this API can receive a maximum of 5 MB data, and any data exceeding this threshold
> will fail to be received.

> (2) If you need to pass in cookies, add them to the **options** parameter.

> (3) If the URL contains non-English characters, call **encodeURL(url)** to encode the URL before initiating an
> HTTP request.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| options | [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HttpResponse&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2300001](../errorcode-net-http.md#2300001-protocol-not-supported) |
| [2300003](../errorcode-net-http.md#2300003-incorrect-url-format) |
| [2300005](../errorcode-net-http.md#2300005-failed-to-resolve-the-domain-name-of-the-proxy-server) |
| [2300006](../errorcode-net-http.md#2300006-failed-to-resolve-the-domain-name-of-the-host) |
| [2300007](../errorcode-net-http.md#2300007-failed-to-connect-to-the-server) |
| [2300008](../errorcode-net-http.md#2300008-invalid-data-returned-by-the-server) |
| [2300009](../errorcode-net-http.md#2300009-access-to-remote-resources-denied) |
| [2300016](../errorcode-net-http.md#2300016-http2-framing-layer-error) |
| [2300018](../errorcode-net-http.md#2300018-incomplete-data-returned-by-the-server) |
| [2300023](../errorcode-net-http.md#2300023-failed-to-write-received-data-to-a-disk-or-application) |
| [2300025](../errorcode-net-http.md#2300025-failed-to-upload-data) |
| [2300026](../errorcode-net-http.md#2300026-failed-to-open-or-read-local-data-from-a-file-or-application) |
| [2300027](../errorcode-net-http.md#2300027-insufficient-memory) |
| [2300028](../errorcode-net-http.md#2300028-operation-timeout) |
| [2300047](../errorcode-net-http.md#2300047-maximum-redirections-reached) |
| [2300052](../errorcode-net-http.md#2300052-no-content-returned-by-the-server) |
| [2300055](../errorcode-net-http.md#2300055-failed-to-send-network-data) |
| [2300056](../errorcode-net-http.md#2300056-failed-to-receive-network-data) |
| [2300058](../errorcode-net-http.md#2300058-local-ssl-certificate-error) |
| [2300059](../errorcode-net-http.md#2300059-failed-to-use-the-specified-ssl-cipher-algorithm) |
| [2300060](../errorcode-net-http.md#2300060-incorrect-ssl-certificate-or-ssh-key-of-the-remote-server) |
| [2300061](../errorcode-net-http.md#2300061-unrecognized-or-incorrect-http-encoding-format) |
| [2300063](../errorcode-net-http.md#2300063-maximum-file-size-exceeded) |
| [2300070](../errorcode-net-http.md#2300070-insufficient-server-disk-space) |
| [2300073](../errorcode-net-http.md#2300073-uploaded-file-already-exists) |
| [2300077](../errorcode-net-http.md#2300077-no-ssl-ca-certificate-or-access-permission) |
| [2300078](../errorcode-net-http.md#2300078-url-requested-file-not-found) |
| [2300094](../errorcode-net-http.md#2300094-identity-verification-failed) |
| [2300999](../errorcode-net-http.md#2300999-internal-error) |
| [2300998](../errorcode-net-http.md#2300998-domain-access-denied) |
| [2300997](../errorcode-net-http.md#2300997-plaintext-http-access-intercepted) |
| 2300996 |

**Examples**

See [request](#request)

## request

```TypeScript
request(url: string, options?: HttpRequestOptions): Promise<HttpResponse>
```

Initiates an HTTP request containing specified options to a given URL. This API uses a promise to return the result.

> **NOTE：**&gt;
> (1) This API can receive only data whose size is less than 5 MB. If the data size exceeds 5 MB, you need to set
> **maxLimit** to a larger value in [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) or call
> [requestInStream](#requestinstream) to
> initiate a streaming request. Since API version 23, this API can receive a maximum of 50 MB data. In versions
> earlier than API version 23, this API can receive a maximum of 5 MB data, and any data exceeding this threshold
> will fail to be received.

> (2) If you need to pass in cookies, add them to the **options** parameter.

> (3) If the URL contains non-English characters, call **encodeURL(url)** to encode the URL before initiating an
> HTTP request.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| options | [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;HttpResponse & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2300001](../errorcode-net-http.md#2300001-protocol-not-supported) |
| [2300003](../errorcode-net-http.md#2300003-incorrect-url-format) |
| [2300005](../errorcode-net-http.md#2300005-failed-to-resolve-the-domain-name-of-the-proxy-server) |
| [2300006](../errorcode-net-http.md#2300006-failed-to-resolve-the-domain-name-of-the-host) |
| [2300007](../errorcode-net-http.md#2300007-failed-to-connect-to-the-server) |
| [2300008](../errorcode-net-http.md#2300008-invalid-data-returned-by-the-server) |
| [2300009](../errorcode-net-http.md#2300009-access-to-remote-resources-denied) |
| [2300016](../errorcode-net-http.md#2300016-http2-framing-layer-error) |
| [2300018](../errorcode-net-http.md#2300018-incomplete-data-returned-by-the-server) |
| [2300023](../errorcode-net-http.md#2300023-failed-to-write-received-data-to-a-disk-or-application) |
| [2300025](../errorcode-net-http.md#2300025-failed-to-upload-data) |
| [2300026](../errorcode-net-http.md#2300026-failed-to-open-or-read-local-data-from-a-file-or-application) |
| [2300027](../errorcode-net-http.md#2300027-insufficient-memory) |
| [2300028](../errorcode-net-http.md#2300028-operation-timeout) |
| [2300047](../errorcode-net-http.md#2300047-maximum-redirections-reached) |
| [2300052](../errorcode-net-http.md#2300052-no-content-returned-by-the-server) |
| [2300055](../errorcode-net-http.md#2300055-failed-to-send-network-data) |
| [2300056](../errorcode-net-http.md#2300056-failed-to-receive-network-data) |
| [2300058](../errorcode-net-http.md#2300058-local-ssl-certificate-error) |
| [2300059](../errorcode-net-http.md#2300059-failed-to-use-the-specified-ssl-cipher-algorithm) |
| [2300060](../errorcode-net-http.md#2300060-incorrect-ssl-certificate-or-ssh-key-of-the-remote-server) |
| [2300061](../errorcode-net-http.md#2300061-unrecognized-or-incorrect-http-encoding-format) |
| [2300063](../errorcode-net-http.md#2300063-maximum-file-size-exceeded) |
| [2300070](../errorcode-net-http.md#2300070-insufficient-server-disk-space) |
| [2300073](../errorcode-net-http.md#2300073-uploaded-file-already-exists) |
| [2300077](../errorcode-net-http.md#2300077-no-ssl-ca-certificate-or-access-permission) |
| [2300078](../errorcode-net-http.md#2300078-url-requested-file-not-found) |
| [2300094](../errorcode-net-http.md#2300094-identity-verification-failed) |
| [2300999](../errorcode-net-http.md#2300999-internal-error) |
| [2300998](../errorcode-net-http.md#2300998-domain-access-denied) |
| [2300997](../errorcode-net-http.md#2300997-plaintext-http-access-intercepted) |
| 2300996 |

**Examples**

See [request](#request)

## requestInStream

```TypeScript
requestInStream(url: string, callback: AsyncCallback<int>): void
```

Initiates an HTTP request containing specified options to a given URL. This API uses an asynchronous callback to return the result, which is a streaming response.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2300001](../errorcode-net-http.md#2300001-protocol-not-supported) |
| [2300003](../errorcode-net-http.md#2300003-incorrect-url-format) |
| [2300005](../errorcode-net-http.md#2300005-failed-to-resolve-the-domain-name-of-the-proxy-server) |
| [2300006](../errorcode-net-http.md#2300006-failed-to-resolve-the-domain-name-of-the-host) |
| [2300007](../errorcode-net-http.md#2300007-failed-to-connect-to-the-server) |
| [2300008](../errorcode-net-http.md#2300008-invalid-data-returned-by-the-server) |
| [2300009](../errorcode-net-http.md#2300009-access-to-remote-resources-denied) |
| [2300016](../errorcode-net-http.md#2300016-http2-framing-layer-error) |
| [2300018](../errorcode-net-http.md#2300018-incomplete-data-returned-by-the-server) |
| [2300023](../errorcode-net-http.md#2300023-failed-to-write-received-data-to-a-disk-or-application) |
| [2300025](../errorcode-net-http.md#2300025-failed-to-upload-data) |
| [2300026](../errorcode-net-http.md#2300026-failed-to-open-or-read-local-data-from-a-file-or-application) |
| [2300027](../errorcode-net-http.md#2300027-insufficient-memory) |
| [2300028](../errorcode-net-http.md#2300028-operation-timeout) |
| [2300047](../errorcode-net-http.md#2300047-maximum-redirections-reached) |
| [2300052](../errorcode-net-http.md#2300052-no-content-returned-by-the-server) |
| [2300055](../errorcode-net-http.md#2300055-failed-to-send-network-data) |
| [2300056](../errorcode-net-http.md#2300056-failed-to-receive-network-data) |
| [2300058](../errorcode-net-http.md#2300058-local-ssl-certificate-error) |
| [2300059](../errorcode-net-http.md#2300059-failed-to-use-the-specified-ssl-cipher-algorithm) |
| [2300060](../errorcode-net-http.md#2300060-incorrect-ssl-certificate-or-ssh-key-of-the-remote-server) |
| [2300061](../errorcode-net-http.md#2300061-unrecognized-or-incorrect-http-encoding-format) |
| [2300063](../errorcode-net-http.md#2300063-maximum-file-size-exceeded) |
| [2300070](../errorcode-net-http.md#2300070-insufficient-server-disk-space) |
| [2300073](../errorcode-net-http.md#2300073-uploaded-file-already-exists) |
| [2300077](../errorcode-net-http.md#2300077-no-ssl-ca-certificate-or-access-permission) |
| [2300078](../errorcode-net-http.md#2300078-url-requested-file-not-found) |
| [2300094](../errorcode-net-http.md#2300094-identity-verification-failed) |
| [2300999](../errorcode-net-http.md#2300999-internal-error) |
| [2300998](../errorcode-net-http.md#2300998-domain-access-denied) |
| [2300997](../errorcode-net-http.md#2300997-plaintext-http-access-intercepted) |
| 2300996 |

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

## requestInStream

```TypeScript
requestInStream(url: string, options: HttpRequestOptions, callback: AsyncCallback<int>): void
```

Initiates an HTTP request containing specified options to a given URL. This API uses an asynchronous callback to return the result, which is a streaming response.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| options | [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2300001](../errorcode-net-http.md#2300001-protocol-not-supported) |
| [2300003](../errorcode-net-http.md#2300003-incorrect-url-format) |
| [2300005](../errorcode-net-http.md#2300005-failed-to-resolve-the-domain-name-of-the-proxy-server) |
| [2300006](../errorcode-net-http.md#2300006-failed-to-resolve-the-domain-name-of-the-host) |
| [2300007](../errorcode-net-http.md#2300007-failed-to-connect-to-the-server) |
| [2300008](../errorcode-net-http.md#2300008-invalid-data-returned-by-the-server) |
| [2300009](../errorcode-net-http.md#2300009-access-to-remote-resources-denied) |
| [2300016](../errorcode-net-http.md#2300016-http2-framing-layer-error) |
| [2300018](../errorcode-net-http.md#2300018-incomplete-data-returned-by-the-server) |
| [2300023](../errorcode-net-http.md#2300023-failed-to-write-received-data-to-a-disk-or-application) |
| [2300025](../errorcode-net-http.md#2300025-failed-to-upload-data) |
| [2300026](../errorcode-net-http.md#2300026-failed-to-open-or-read-local-data-from-a-file-or-application) |
| [2300027](../errorcode-net-http.md#2300027-insufficient-memory) |
| [2300028](../errorcode-net-http.md#2300028-operation-timeout) |
| [2300047](../errorcode-net-http.md#2300047-maximum-redirections-reached) |
| [2300052](../errorcode-net-http.md#2300052-no-content-returned-by-the-server) |
| [2300055](../errorcode-net-http.md#2300055-failed-to-send-network-data) |
| [2300056](../errorcode-net-http.md#2300056-failed-to-receive-network-data) |
| [2300058](../errorcode-net-http.md#2300058-local-ssl-certificate-error) |
| [2300059](../errorcode-net-http.md#2300059-failed-to-use-the-specified-ssl-cipher-algorithm) |
| [2300060](../errorcode-net-http.md#2300060-incorrect-ssl-certificate-or-ssh-key-of-the-remote-server) |
| [2300061](../errorcode-net-http.md#2300061-unrecognized-or-incorrect-http-encoding-format) |
| [2300063](../errorcode-net-http.md#2300063-maximum-file-size-exceeded) |
| [2300070](../errorcode-net-http.md#2300070-insufficient-server-disk-space) |
| [2300073](../errorcode-net-http.md#2300073-uploaded-file-already-exists) |
| [2300077](../errorcode-net-http.md#2300077-no-ssl-ca-certificate-or-access-permission) |
| [2300078](../errorcode-net-http.md#2300078-url-requested-file-not-found) |
| [2300094](../errorcode-net-http.md#2300094-identity-verification-failed) |
| [2300999](../errorcode-net-http.md#2300999-internal-error) |
| [2300998](../errorcode-net-http.md#2300998-domain-access-denied) |
| [2300997](../errorcode-net-http.md#2300997-plaintext-http-access-intercepted) |
| 2300996 |

**Examples**

See [requestInStream](#requestinstream)

## requestInStream

```TypeScript
requestInStream(url: string, options?: HttpRequestOptions): Promise<int>
```

Initiates an HTTP request containing specified options to a given URL. This API uses a promise to return the result, which is a streaming response.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| options | [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2300001](../errorcode-net-http.md#2300001-protocol-not-supported) |
| [2300003](../errorcode-net-http.md#2300003-incorrect-url-format) |
| [2300005](../errorcode-net-http.md#2300005-failed-to-resolve-the-domain-name-of-the-proxy-server) |
| [2300006](../errorcode-net-http.md#2300006-failed-to-resolve-the-domain-name-of-the-host) |
| [2300007](../errorcode-net-http.md#2300007-failed-to-connect-to-the-server) |
| [2300008](../errorcode-net-http.md#2300008-invalid-data-returned-by-the-server) |
| [2300009](../errorcode-net-http.md#2300009-access-to-remote-resources-denied) |
| [2300016](../errorcode-net-http.md#2300016-http2-framing-layer-error) |
| [2300018](../errorcode-net-http.md#2300018-incomplete-data-returned-by-the-server) |
| [2300023](../errorcode-net-http.md#2300023-failed-to-write-received-data-to-a-disk-or-application) |
| [2300025](../errorcode-net-http.md#2300025-failed-to-upload-data) |
| [2300026](../errorcode-net-http.md#2300026-failed-to-open-or-read-local-data-from-a-file-or-application) |
| [2300027](../errorcode-net-http.md#2300027-insufficient-memory) |
| [2300028](../errorcode-net-http.md#2300028-operation-timeout) |
| [2300047](../errorcode-net-http.md#2300047-maximum-redirections-reached) |
| [2300052](../errorcode-net-http.md#2300052-no-content-returned-by-the-server) |
| [2300055](../errorcode-net-http.md#2300055-failed-to-send-network-data) |
| [2300056](../errorcode-net-http.md#2300056-failed-to-receive-network-data) |
| [2300058](../errorcode-net-http.md#2300058-local-ssl-certificate-error) |
| [2300059](../errorcode-net-http.md#2300059-failed-to-use-the-specified-ssl-cipher-algorithm) |
| [2300060](../errorcode-net-http.md#2300060-incorrect-ssl-certificate-or-ssh-key-of-the-remote-server) |
| [2300061](../errorcode-net-http.md#2300061-unrecognized-or-incorrect-http-encoding-format) |
| [2300063](../errorcode-net-http.md#2300063-maximum-file-size-exceeded) |
| [2300070](../errorcode-net-http.md#2300070-insufficient-server-disk-space) |
| [2300073](../errorcode-net-http.md#2300073-uploaded-file-already-exists) |
| [2300077](../errorcode-net-http.md#2300077-no-ssl-ca-certificate-or-access-permission) |
| [2300078](../errorcode-net-http.md#2300078-url-requested-file-not-found) |
| [2300094](../errorcode-net-http.md#2300094-identity-verification-failed) |
| [2300999](../errorcode-net-http.md#2300999-internal-error) |
| [2300998](../errorcode-net-http.md#2300998-domain-access-denied) |
| [2300997](../errorcode-net-http.md#2300997-plaintext-http-access-intercepted) |
| 2300996 |

**Examples**

See [requestInStream](#requestinstream)

## requestSync

```TypeScript
requestSync(url: string, options?: HttpRequestOptions): HttpResponse
```

Initiates an HTTP network request based on the URL and related configuration options (optional). This API returns the response synchronously.

> **NOTE：**&gt;
> (1) This API can receive data of up to 50 MB. To receive more than 50 MB of data, set the **maxLimit**
> parameter in [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md).

> (2) If you need to pass in cookies, add them to the **options** parameter.

> (3) If the URL contains non-English characters, call **encodeURL(url)** to encode the URL before initiating an
> HTTP request.

> (4) This API is synchronous and blocks the current thread until an HTTP response or error code is returned.
**Required permission**: ohos.permission.INTERNET

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Required permissions:** ohos.permission.INTERNET

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| options | [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [HttpResponse](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-httpresponse-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2300001](../errorcode-net-http.md#2300001-protocol-not-supported) |
| [2300003](../errorcode-net-http.md#2300003-incorrect-url-format) |
| [2300005](../errorcode-net-http.md#2300005-failed-to-resolve-the-domain-name-of-the-proxy-server) |
| [2300006](../errorcode-net-http.md#2300006-failed-to-resolve-the-domain-name-of-the-host) |
| [2300007](../errorcode-net-http.md#2300007-failed-to-connect-to-the-server) |
| [2300008](../errorcode-net-http.md#2300008-invalid-data-returned-by-the-server) |
| [2300009](../errorcode-net-http.md#2300009-access-to-remote-resources-denied) |
| [2300016](../errorcode-net-http.md#2300016-http2-framing-layer-error) |
| [2300018](../errorcode-net-http.md#2300018-incomplete-data-returned-by-the-server) |
| [2300023](../errorcode-net-http.md#2300023-failed-to-write-received-data-to-a-disk-or-application) |
| [2300025](../errorcode-net-http.md#2300025-failed-to-upload-data) |
| [2300026](../errorcode-net-http.md#2300026-failed-to-open-or-read-local-data-from-a-file-or-application) |
| [2300027](../errorcode-net-http.md#2300027-insufficient-memory) |
| [2300028](../errorcode-net-http.md#2300028-operation-timeout) |
| [2300047](../errorcode-net-http.md#2300047-maximum-redirections-reached) |
| [2300052](../errorcode-net-http.md#2300052-no-content-returned-by-the-server) |
| [2300055](../errorcode-net-http.md#2300055-failed-to-send-network-data) |
| [2300056](../errorcode-net-http.md#2300056-failed-to-receive-network-data) |
| [2300058](../errorcode-net-http.md#2300058-local-ssl-certificate-error) |
| [2300059](../errorcode-net-http.md#2300059-failed-to-use-the-specified-ssl-cipher-algorithm) |
| [2300060](../errorcode-net-http.md#2300060-incorrect-ssl-certificate-or-ssh-key-of-the-remote-server) |
| [2300061](../errorcode-net-http.md#2300061-unrecognized-or-incorrect-http-encoding-format) |
| [2300063](../errorcode-net-http.md#2300063-maximum-file-size-exceeded) |
| [2300070](../errorcode-net-http.md#2300070-insufficient-server-disk-space) |
| [2300073](../errorcode-net-http.md#2300073-uploaded-file-already-exists) |
| [2300077](../errorcode-net-http.md#2300077-no-ssl-ca-certificate-or-access-permission) |
| [2300078](../errorcode-net-http.md#2300078-url-requested-file-not-found) |
| [2300094](../errorcode-net-http.md#2300094-identity-verification-failed) |
| 2300996 |
| [2300997](../errorcode-net-http.md#2300997-plaintext-http-access-intercepted) |
| [2300998](../errorcode-net-http.md#2300998-domain-access-denied) |
| [2300999](../errorcode-net-http.md#2300999-internal-error) |
