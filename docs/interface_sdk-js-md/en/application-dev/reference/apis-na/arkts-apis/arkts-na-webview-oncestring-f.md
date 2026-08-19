# once_string

## Modules to Import

```TypeScript
```

## once_string

```TypeScript
function once(type: string, callback: Callback<void>): void
```

Subscribe to a callback of a specified type of web event once.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-webview-function once(type: string, callback: Callback<void>): void--><!--Device-webview-function once(type: string, callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | Types of web event. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Indicate callback used to receive the web event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |

