# revokeUriPermission (System API)

## Modules to Import

```TypeScript
import { uriPermissionManager } from 'kits/@kit.AbilityKit';
```

## revokeUriPermission

```TypeScript
function revokeUriPermission(uri: string, targetBundleName: string, callback: AsyncCallback<number>): void
```

Revokes the URI permission from an application. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> - This API can be used to revoke the URI permission of another application obtained by this application or URI
> permission granted by this application.&gt;
> - URI processing involves encoding and decoding. Therefore, the input URI must be obtained through the
> [getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md) API. For URIs combined by the application, the
> system cannot guarantee their functions.

**Since:** 10

**Required permissions:** 
- API version 10 - 11: ohos.permission.PROXY_AUTHORIZATION_URI

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| targetBundleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000059](../errorcode-ability.md#16000059-specified-uri-type-is-invalid) |
| [801](../../errorcode-universal.md#801-api-not-supported) |


## revokeUriPermission

```TypeScript
function revokeUriPermission(uri: string, targetBundleName: string): Promise<number>
```

Revokes the URI permission from an application. This API uses a promise to return the result.

> **NOTE：**&gt;
> - This API can be used to revoke the URI permission of another application obtained by this application or URI
> permission granted by this application.&gt;
> - URI processing involves encoding and decoding. Therefore, the input URI must be obtained through the
> [getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md) API. For URIs combined by the application, the
> system cannot guarantee their functions.

**Since:** 10

**Required permissions:** 
- API version 10 - 11: ohos.permission.PROXY_AUTHORIZATION_URI

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| targetBundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000059](../errorcode-ability.md#16000059-specified-uri-type-is-invalid) |
| [801](../../errorcode-universal.md#801-api-not-supported) |


## revokeUriPermission

```TypeScript
function revokeUriPermission(uri: string, targetBundleName: string, appCloneIndex: number): Promise<void>
```

Revokes the URI permission from an application. This API uses a promise to return the result.

> **NOTE：**&gt;
> - This API can be used to revoke the URI permission of another application obtained by this application or URI
> permission granted by this application.&gt;
> - This API can be used to revoke the URI permissions granted to a cloned application. You need to specify the
> application bundle name and index of the cloned application.&gt;
> - URI processing involves encoding and decoding. Therefore, the input URI must be obtained through the
> [getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md) API. For URIs combined by the application, the
> system cannot guarantee their functions.

**Since:** 14

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| targetBundleName | string | Yes |
| appCloneIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000059](../errorcode-ability.md#16000059-specified-uri-type-is-invalid) |
| [16000081](../errorcode-ability.md#16000081-failed-to-obtain-the-target-application-information) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
