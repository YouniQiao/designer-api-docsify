# WebMessageExt

The message received or sent from web message port.

**Since:** 10

<!--Device-webview-class WebMessageExt--><!--Device-webview-class WebMessageExt-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## getArray

```TypeScript
getArray(): Array<string | number | boolean>
```

Get the array value of the web message.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessageExt-getArray(): Array<string | number | boolean>--><!--Device-WebMessageExt-getArray(): Array<string | number | boolean>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string \ | number \| boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17100014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) |

## getArrayBuffer

```TypeScript
getArrayBuffer(): ArrayBuffer
```

Get the array buffer value of the web message.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessageExt-getArrayBuffer(): ArrayBuffer--><!--Device-WebMessageExt-getArrayBuffer(): ArrayBuffer-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| ArrayBuffer |

**Error codes:**

| Error Code ID |
| --- |
| [17100014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) |

## getBoolean

```TypeScript
getBoolean(): boolean
```

Get the boolean value of the web message.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessageExt-getBoolean(): boolean--><!--Device-WebMessageExt-getBoolean(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [17100014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) |

## getError

```TypeScript
getError(): Error
```

Get the error value of the web message.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessageExt-getError(): Error--><!--Device-WebMessageExt-getError(): Error-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Error |

**Error codes:**

| Error Code ID |
| --- |
| [17100014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) |

## getNumber

```TypeScript
getNumber(): number
```

Get the number value of the web message.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessageExt-getNumber(): number--><!--Device-WebMessageExt-getNumber(): number-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [17100014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) |

## getString

```TypeScript
getString(): string
```

Get the string value of the web message.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessageExt-getString(): string--><!--Device-WebMessageExt-getString(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [17100014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) |

## getType

```TypeScript
getType(): WebMessageType
```

Get the type of the web message.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessageExt-getType(): WebMessageType--><!--Device-WebMessageExt-getType(): WebMessageType-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WebMessageType](arkts-arkweb-webview-webmessagetype-e.md) |

## setArray

```TypeScript
setArray(message: Array<string | number | boolean>): void
```

Set the array value of the web message.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessageExt-setArray(message: Array<string | number | boolean>): void--><!--Device-WebMessageExt-setArray(message: Array<string | number | boolean>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | Array & lt;string \ | number \| boolean & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17100014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) |

## setArrayBuffer

```TypeScript
setArrayBuffer(message: ArrayBuffer): void
```

Set the array buffer value of the web message.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessageExt-setArrayBuffer(message: ArrayBuffer): void--><!--Device-WebMessageExt-setArrayBuffer(message: ArrayBuffer): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | ArrayBuffer | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17100014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) |

## setBoolean

```TypeScript
setBoolean(message: boolean): void
```

Set the boolean value of the web message.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessageExt-setBoolean(message: boolean): void--><!--Device-WebMessageExt-setBoolean(message: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17100014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) |

## setError

```TypeScript
setError(message: Error): void
```

Set the error value of the web message.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessageExt-setError(message: Error): void--><!--Device-WebMessageExt-setError(message: Error): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | Error | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17100014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) |

## setNumber

```TypeScript
setNumber(message: number): void
```

Set the number value of the web message.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessageExt-setNumber(message: number): void--><!--Device-WebMessageExt-setNumber(message: number): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17100014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) |

## setString

```TypeScript
setString(message: string): void
```

Set the string value of the web message.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessageExt-setString(message: string): void--><!--Device-WebMessageExt-setString(message: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17100014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) |

## setType

```TypeScript
setType(type: WebMessageType): void
```

Set the type of the web message.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessageExt-setType(type: WebMessageType): void--><!--Device-WebMessageExt-setType(type: WebMessageType): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [WebMessageType](arkts-arkweb-webview-webmessagetype-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17100014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) |
