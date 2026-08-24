# WebDataBase

Implements a **WebDataBase** object.

> **NOTE：**&gt;
> - The sample effect is subject to the actual device.&gt;
> - You must load the **Web** component before calling the APIs in **WebDataBase**.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-webview-class WebDataBase--><!--Device-webview-class WebDataBase-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## deleteHttpAuthCredentials

```TypeScript
static deleteHttpAuthCredentials(): void
```

Deletes all HTTP authentication credentials saved in the cache. This API returns the result synchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebDataBase-static deleteHttpAuthCredentials(): void--><!--Device-WebDataBase-static deleteHttpAuthCredentials(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## existHttpAuthCredentials

```TypeScript
static existHttpAuthCredentials(): boolean
```

Checks whether any saved HTTP authentication credentials exist. This API returns the result synchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebDataBase-static existHttpAuthCredentials(): boolean--><!--Device-WebDataBase-static existHttpAuthCredentials(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether any saved HTTP authentication credentials exist. <br>**true** is returned if any saved HTTP authentication credentials exist; otherwise, **false** is returned. |

## getHttpAuthCredentials

```TypeScript
static getHttpAuthCredentials(host: string, realm: string): Array<string>
```

Retrieves HTTP authentication credentials for a given host and realm. This API returns the result synchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebDataBase-static getHttpAuthCredentials(host: string, realm: string): Array<string>--><!--Device-WebDataBase-static getHttpAuthCredentials(host: string, realm: string): Array<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| host | string | Yes | Host to which the HTTP authentication credential is applied. |
| realm | string | Yes | Realm to which the HTTP authentication credential is applied. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | Array of the matching user names and passwords is returned if the operation is successful; otherwise, an empty array is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

## saveHttpAuthCredentials

```TypeScript
static saveHttpAuthCredentials(host: string, realm: string, username: string, password: string): void
```

Saves HTTP authentication credentials for a given host and realm. This API returns the result synchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebDataBase-static saveHttpAuthCredentials(host: string, realm: string, username: string, password: string): void--><!--Device-WebDataBase-static saveHttpAuthCredentials(host: string, realm: string, username: string, password: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| host | string | Yes | Host to which the HTTP authentication credential is applied. |
| realm | string | Yes | Realm to which the HTTP authentication credential is applied. |
| username | string | Yes | User name. |
| password | string | Yes | Password. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

