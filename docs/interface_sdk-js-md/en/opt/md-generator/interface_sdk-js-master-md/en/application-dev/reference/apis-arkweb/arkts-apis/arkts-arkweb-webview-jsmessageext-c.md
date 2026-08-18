# JsMessageExt

JsMessageExt is a data class in the ArkWeb framework used to encapsulate the result returned after executing a JavaScript script through the [runJavaScriptExt](arkts-arkweb-webview-webviewcontroller-c.md#runjavascriptext) API. Unlike the conventional runJavaScript API, runJavaScriptExt supports richer return value types, and JsMessageExt provides a type-safe way to access these diverse return results. Developers first obtain the data type through the getType method of JsMessageExt, and then call the corresponding get method to retrieve the specific value. JsMessageExt supports parsing of multiple JavaScript return value types: string (getString), number (getNumber), boolean (getBoolean), raw binary data (getArrayBuffer), array (getArray), and more. When the obtained data type does not match the actual stored type (for example, calling getString on a numeric type), error code 17100014 is thrown. Starting from API version 22, JsMessageExt also provides the getErrorDescription method for obtaining exception information during JavaScript execution. If the return value is of the object type, it is uniformly formatted into a description string.

**Since:** 10

<!--Device-webview-class JsMessageExt--><!--Device-webview-class JsMessageExt-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## getArray

```TypeScript
getArray(): Array<string | number | boolean>
```

Obtains array-type data of the data object. For details about the sample code, see [runJavaScriptExt](arkts-arkweb-webview-webviewcontroller-c.md#runjavascriptext).

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
| [17100014](../errorcode-webview.md#17100014-type-and-value-mismatch) |

## getArrayBuffer

```TypeScript
getArrayBuffer(): ArrayBuffer
```

Obtains raw binary data of the data object. For details about the sample code, see [runJavaScriptExt](arkts-arkweb-webview-webviewcontroller-c.md#runjavascriptext).

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
| [17100014](../errorcode-webview.md#17100014-type-and-value-mismatch) |

## getBoolean

```TypeScript
getBoolean(): boolean
```

Obtains Boolean-type data of the data object. For details about the sample code, see [runJavaScriptExt](arkts-arkweb-webview-webviewcontroller-c.md#runjavascriptext).

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
| [17100014](../errorcode-webview.md#17100014-type-and-value-mismatch) |

## getErrorDescription

```TypeScript
getErrorDescription(): string | null
```

Obtains the error information about the JavaScript execution. For details about the sample code, see [runJavaScriptExt](arkts-arkweb-webview-webviewcontroller-c.md#runjavascriptext).

**Since:** 22

<!--Device-JsMessageExt-getErrorDescription(): string | null--><!--Device-JsMessageExt-getErrorDescription(): string | null-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string | If an exception occurs during JavaScript script execution, or the return value is of the object type, the system formats the exception information or object into the string "Not support type: & lt;{ exception \ |

## getNumber

```TypeScript
getNumber(): number
```

Obtains number-type data of the data object. For details about the sample code, see [runJavaScriptExt](arkts-arkweb-webview-webviewcontroller-c.md#runjavascriptext).

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
| [17100014](../errorcode-webview.md#17100014-type-and-value-mismatch) |

## getString

```TypeScript
getString(): string
```

Obtains string-type data of the data object. For details about the sample code, see [runJavaScriptExt](arkts-arkweb-webview-webviewcontroller-c.md#runjavascriptext).

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
| [17100014](../errorcode-webview.md#17100014-type-and-value-mismatch) |

## getType

```TypeScript
getType(): JsMessageType
```

Obtains the type of the data object. For details about the sample code, see [runJavaScriptExt](arkts-arkweb-webview-webviewcontroller-c.md#runjavascriptext).

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-JsMessageExt-getType(): JsMessageType--><!--Device-JsMessageExt-getType(): JsMessageType-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [JsMessageType](arkts-arkweb-webview-jsmessagetype-e.md) |
