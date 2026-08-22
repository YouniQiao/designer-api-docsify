# WebMessageExt

The message received or sent from web message port.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-webview-class WebMessageExt--><!--Device-webview-class WebMessageExt-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## getArray

```TypeScript
getArray(): Array<string | double | long | boolean>
```

Get the array value of the web message.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebMessageExt-getArray(): Array<string | double | long | boolean>--><!--Device-WebMessageExt-getArray(): Array<string | double | long | boolean>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string \| double \| long \| boolean&gt; | Returns data of Array type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100014](../../apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) | The type and value of the message do not match. |

## getArrayBuffer

```TypeScript
getArrayBuffer(): ArrayBuffer
```

Get the array buffer value of the web message.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebMessageExt-getArrayBuffer(): ArrayBuffer--><!--Device-WebMessageExt-getArrayBuffer(): ArrayBuffer-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArrayBuffer | Returns data of ArrayBuffer type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100014](../../apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) | The type and value of the message do not match. |

## getBoolean

```TypeScript
getBoolean(): boolean
```

Get the boolean value of the web message.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebMessageExt-getBoolean(): boolean--><!--Device-WebMessageExt-getBoolean(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns data of Boolean type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100014](../../apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) | The type and value of the message do not match. |

## getError

```TypeScript
getError(): Error
```

Get the error value of the web message.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebMessageExt-getError(): Error--><!--Device-WebMessageExt-getError(): Error-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| Error | Returns data of Error type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100014](../../apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) | The type and value of the message do not match. |

## getNumber

```TypeScript
getNumber(): double | long
```

Get the number value of the web message.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebMessageExt-getNumber(): double | long--><!--Device-WebMessageExt-getNumber(): double | long-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| double \| long | Returns data of number type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100014](../../apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) | The type and value of the message do not match. |

## getString

```TypeScript
getString(): string
```

Get the string value of the web message.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebMessageExt-getString(): string--><!--Device-WebMessageExt-getString(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns data of string type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100014](../../apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) | The type and value of the message do not match. |

## getType

```TypeScript
getType(): WebMessageType
```

Get the type of the web message.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebMessageExt-getType(): WebMessageType--><!--Device-WebMessageExt-getType(): WebMessageType-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [WebMessageType](arkts-webview-webmessagetype-e.md) | Returns data of WebMessageType type |

## setArray

```TypeScript
setArray(message: Array<string | double | long | boolean>): void
```

Set the array value of the web message.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebMessageExt-setArray(message: Array<string | double | long | boolean>): void--><!--Device-WebMessageExt-setArray(message: Array<string | double | long | boolean>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | Array&lt;string \| double \| long \| boolean&gt; | Yes | set Array type data |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100014](../../apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) | The type and value of the message do not match. |

## setArrayBuffer

```TypeScript
setArrayBuffer(message: ArrayBuffer): void
```

Set the array buffer value of the web message.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebMessageExt-setArrayBuffer(message: ArrayBuffer): void--><!--Device-WebMessageExt-setArrayBuffer(message: ArrayBuffer): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | ArrayBuffer | Yes | set ArrayBuffer type data |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100014](../../apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) | The type and value of the message do not match. |

## setBoolean

```TypeScript
setBoolean(message: boolean): void
```

Set the boolean value of the web message.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebMessageExt-setBoolean(message: boolean): void--><!--Device-WebMessageExt-setBoolean(message: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | boolean | Yes | set boolean type data |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100014](../../apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) | The type and value of the message do not match. |

## setError

```TypeScript
setError(message: Error): void
```

Set the error value of the web message.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebMessageExt-setError(message: Error): void--><!--Device-WebMessageExt-setError(message: Error): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | Error | Yes | set Error type data |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100014](../../apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) | The type and value of the message do not match. |

## setNumber

```TypeScript
setNumber(message: double): void
```

Set the number value of the web message.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebMessageExt-setNumber(message: double): void--><!--Device-WebMessageExt-setNumber(message: double): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | double | Yes | set number type data |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100014](../../apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) | The type and value of the message do not match. |

## setString

```TypeScript
setString(message: string): void
```

Set the string value of the web message.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebMessageExt-setString(message: string): void--><!--Device-WebMessageExt-setString(message: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | Yes | set string type data |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100014](../../apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) | The type and value of the message do not match. |

## setType

```TypeScript
setType(type: WebMessageType): void
```

Set the type of the web message.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebMessageExt-setType(type: WebMessageType): void--><!--Device-WebMessageExt-setType(type: WebMessageType): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [WebMessageType](arkts-webview-webmessagetype-e.md) | Yes | set WebMessageType type data |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100014](../../apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) | The type and value of the message do not match. |

