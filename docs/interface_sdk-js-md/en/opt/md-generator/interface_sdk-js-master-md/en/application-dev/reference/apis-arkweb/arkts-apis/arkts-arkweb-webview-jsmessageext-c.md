# JsMessageExt

The message for indicating the of result of JavaScript code execution.

**Since:** 10

<!--Device-webview-class JsMessageExt--><!--Device-webview-class JsMessageExt-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## getArray

```TypeScript
getArray(): Array<string | number | boolean>
```

Get the array value of the the JavaScript code execution result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-JsMessageExt-getArray(): Array<string | number | boolean>--><!--Device-JsMessageExt-getArray(): Array<string | number | boolean>-End-->

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

Get the array buffer value of the JavaScript code execution result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-JsMessageExt-getArrayBuffer(): ArrayBuffer--><!--Device-JsMessageExt-getArrayBuffer(): ArrayBuffer-End-->

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

Get the boolean value of the JavaScript code execution result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-JsMessageExt-getBoolean(): boolean--><!--Device-JsMessageExt-getBoolean(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [17100014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) |

## getErrorDescription

```TypeScript
getErrorDescription(): string | null
```

Get the object or exception of the the JavaScript code execution result and serialize it into a string.

**Since:** 22

<!--Device-JsMessageExt-getErrorDescription(): string | null--><!--Device-JsMessageExt-getErrorDescription(): string | null-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string | If an exception occurs, or the returned type is object, return the serialized string in the format of "Not support type: & lt;{exception\ |

## getNumber

```TypeScript
getNumber(): number
```

Get the number value of the JavaScript code execution result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-JsMessageExt-getNumber(): number--><!--Device-JsMessageExt-getNumber(): number-End-->

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

Get the string value of the JavaScript code execution result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-JsMessageExt-getString(): string--><!--Device-JsMessageExt-getString(): string-End-->

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
getType(): JsMessageType
```

Get the type of the JavaScript code execution result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-JsMessageExt-getType(): JsMessageType--><!--Device-JsMessageExt-getType(): JsMessageType-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [JsMessageType](arkts-arkweb-webview-jsmessagetype-e.md) |
