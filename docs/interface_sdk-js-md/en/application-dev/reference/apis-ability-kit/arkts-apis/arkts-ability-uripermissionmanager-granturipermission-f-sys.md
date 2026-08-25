# grantUriPermission (System API)

## Modules to Import

```TypeScript
import { uriPermissionManager } from 'kits/@kit.AbilityKit';
```

## grantUriPermission

```TypeScript
function grantUriPermission(
    uri: string,
    flag: wantConstant.Flags,
    targetBundleName: string,
    callback: AsyncCallback<number>
  ): void
```

Grants the URI permission to an application. If the call is successful, the application obtains the permission to access the file specified by the URI. Once the application exits, the permission will be automatically revoked. For details about how to access the file based on the URI, see [Sharing an Application File](../../../file-management/share-app-file.md). This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> - If an application has the ohos.permission.PROXY_AUTHORIZATION_URI permission, it can grant the accessible URIs
> of another application. If the application does not have this permission, it can grant only its own URI
> permissions.&gt;
> - URI processing involves encoding and decoding. Therefore, the input URI must be obtained through the
> [getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md) API. For URIs combined by the application, the
> system cannot guarantee their functions.

**Since:** 10

**Required permissions:** ohos.permission.PROXY_AUTHORIZATION_URI

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| flag | wantConstant.Flags | Yes |
| targetBundleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000058](../errorcode-ability.md#16000058-specified-uri-flag-is-invalid) |
| [16000059](../errorcode-ability.md#16000059-specified-uri-type-is-invalid) |
| [16000060](../errorcode-ability.md#16000060-sandbox-applications-cannot-grant-uri-permission) |
| [801](../../errorcode-universal.md#801-api-not-supported) |


## grantUriPermission

```TypeScript
function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string): Promise<number>
```

Grants the URI permission to an application. If the call is successful, the application obtains the permission to access the file specified by the URI. Once the application exits, the permission will be automatically revoked. For details about how to access the file based on the URI, see [Sharing an Application File](../../../file-management/share-app-file.md). This API uses a promise to return the result.

> **NOTE：**&gt;
> - If an application has the ohos.permission.PROXY_AUTHORIZATION_URI permission, it can grant the accessible URIs
> of another application. If the application does not have this permission, it can grant only its own URI
> permissions.&gt;
> - URI processing involves encoding and decoding. Therefore, the input URI must be obtained through the
> [getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md) API. For URIs combined by the application, the
> system cannot guarantee their functions.

**Since:** 10

**Required permissions:** ohos.permission.PROXY_AUTHORIZATION_URI

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| flag | wantConstant.Flags | Yes |
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
| [16000058](../errorcode-ability.md#16000058-specified-uri-flag-is-invalid) |
| [16000059](../errorcode-ability.md#16000059-specified-uri-type-is-invalid) |
| [16000060](../errorcode-ability.md#16000060-sandbox-applications-cannot-grant-uri-permission) |
| [801](../../errorcode-universal.md#801-api-not-supported) |


## grantUriPermission

```TypeScript
function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string, appCloneIndex: number): Promise<void>
```

Grants the URI permission to an application. If the call is successful, the application obtains the permission to access the file specified by the URI. Once the application exits, the permission will be automatically revoked. For details about how to access the file based on the URI, see [Sharing an Application File](../../../file-management/share-app-file.md). This API uses a promise to return the result.

> **NOTE：**&gt;
> - If an application has the ohos.permission.PROXY_AUTHORIZATION_URI permission, it can grant the accessible URIs
> of another application. If the application does not have this permission, it can grant only its own URI
> permissions.&gt;
> - This API can be used to grant URI access permission to a cloned application. You need to specify the
> application bundle name and index of the cloned application.&gt;
> - URI processing involves encoding and decoding. Therefore, the input URI must be obtained through the
> [getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md) API. For URIs combined by the application, the
> system cannot guarantee their functions.

**Since:** 14

**Required permissions:** ohos.permission.PROXY_AUTHORIZATION_URI

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| flag | wantConstant.Flags | Yes |
| targetBundleName | string | Yes |
| appCloneIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000058](../errorcode-ability.md#16000058-specified-uri-flag-is-invalid) |
| [16000059](../errorcode-ability.md#16000059-specified-uri-type-is-invalid) |
| [16000060](../errorcode-ability.md#16000060-sandbox-applications-cannot-grant-uri-permission) |
| [16000081](../errorcode-ability.md#16000081-failed-to-obtain-the-target-application-information) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
