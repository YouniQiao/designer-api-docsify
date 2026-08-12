# JsMessageExt

The message for indicating the of result of JavaScript code execution.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-webview-class JsMessageExt--><!--Device-webview-class JsMessageExt-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## getArray

```TypeScript
getArray(): Array<string | double | long | boolean>
```

Get the array value of the the JavaScript code execution result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-JsMessageExt-getArray(): Array<string | double | long | boolean>--><!--Device-JsMessageExt-getArray(): Array<string | double | long | boolean>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string \| double \| long \| boolean&gt; | Returns data of Array type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100014](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) | The type and value of the message do not match. |

## getArrayBuffer

```TypeScript
getArrayBuffer(): ArrayBuffer
```

Get the array buffer value of the JavaScript code execution result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-JsMessageExt-getArrayBuffer(): ArrayBuffer--><!--Device-JsMessageExt-getArrayBuffer(): ArrayBuffer-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArrayBuffer | Returns data of ArrayBuffer |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100014](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) | The type and value of the message do not match. |

## getBoolean

```TypeScript
getBoolean(): boolean
```

Get the boolean value of the JavaScript code execution result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-JsMessageExt-getBoolean(): boolean--><!--Device-JsMessageExt-getBoolean(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns data of Boolean type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100014](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) | The type and value of the message do not match. |

## getErrorDescription

```TypeScript
getErrorDescription(): string | null
```

Get the exception or object of the the JavaScript code execution result and serialize it into a string.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-JsMessageExt-getErrorDescription(): string | null--><!--Device-JsMessageExt-getErrorDescription(): string | null-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | if an exception occurs, or the returned type is object, return the serialized string in the format of "Not support type: &lt;{exception\|object}&gt;", Parts exceeding a length of 2048 will be truncated; otherwise, return null. |

## getNumber

```TypeScript
getNumber(): double | long
```

Get the number value of the JavaScript code execution result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-JsMessageExt-getNumber(): double | long--><!--Device-JsMessageExt-getNumber(): double | long-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| double | Returns data of number type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100014](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) | The type and value of the message do not match. |

## getString

```TypeScript
getString(): string
```

Get the string value of the JavaScript code execution result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-JsMessageExt-getString(): string--><!--Device-JsMessageExt-getString(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns data of string type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100014](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-type-and-value-mismatch) | The type and value of the message do not match. |

## getType

```TypeScript
getType(): JsMessageType
```

Get the type of the JavaScript code execution result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-JsMessageExt-getType(): JsMessageType--><!--Device-JsMessageExt-getType(): JsMessageType-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [JsMessageType](arkts-arkweb-webview-jsmessagetype-e.md) | Returns data of JsMessageType type |

