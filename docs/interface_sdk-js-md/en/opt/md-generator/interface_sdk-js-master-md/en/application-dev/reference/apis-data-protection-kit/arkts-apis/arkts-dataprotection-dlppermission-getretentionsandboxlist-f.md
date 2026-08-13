# getRetentionSandboxList

## Modules to Import

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
```

## getRetentionSandboxList

```TypeScript
function getRetentionSandboxList(bundleName?: string): Promise<Array<RetentionSandboxInfo>>
```

Obtains the sandbox applications in the retention state of an application. This API can be called only in non-DLP sandbox applications. This API uses a promise to return the result. This API is used to query the sandbox retention information of a specified application, so that the sandbox environment in the retention state can be checked or managed.

**Since:** 10

**Deprecated since:** -1

<!--Device-dlpPermission-function getRetentionSandboxList(bundleName?: string): Promise<Array<RetentionSandboxInfo>>--><!--Device-dlpPermission-function getRetentionSandboxList(bundleName?: string): Promise<Array<RetentionSandboxInfo>>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[RetentionSandboxInfo](arkts-dataprotection-dlppermission-retentionsandboxinfo-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100007](../errorcode-dlp.md#19100007-access-denied-for-a-dlp-sandbox-application) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.getRetentionSandboxList().then((sandboxList) => { // Obtain the sandbox retention information.
  console.info('sandboxList', JSON.stringify(sandboxList));
}).catch((error: BusinessError)=> {
  console.error(JSON.stringify(error));
});
```


## getRetentionSandboxList

```TypeScript
function getRetentionSandboxList(bundleName: string, callback: AsyncCallback<Array<RetentionSandboxInfo>>): void
```

Obtains the sandbox applications in the retention state of an application. This API uses an asynchronous callback to return the result. This API is used to query the sandbox retention information of a specified application, so that the sandbox environment in the retention state can be checked or managed.

**Since:** 10

**Deprecated since:** -1

<!--Device-dlpPermission-function getRetentionSandboxList(bundleName: string, callback: AsyncCallback<Array<RetentionSandboxInfo>>): void--><!--Device-dlpPermission-function getRetentionSandboxList(bundleName: string, callback: AsyncCallback<Array<RetentionSandboxInfo>>): void-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[RetentionSandboxInfo](arkts-dataprotection-dlppermission-retentionsandboxinfo-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100007](../errorcode-dlp.md#19100007-access-denied-for-a-dlp-sandbox-application) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.getRetentionSandboxList("bundleName", (err, sandboxList) => {
  if (err) {
    console.error(`Failed to get retention sandbox list. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('sandboxList', JSON.stringify(sandboxList));
  }
}); // Obtain the sandbox retention information.
```


## getRetentionSandboxList

```TypeScript
function getRetentionSandboxList(callback: AsyncCallback<Array<RetentionSandboxInfo>>): void
```

Obtains the sandbox applications in the retention state of an application. This API uses an asynchronous callback to return the result. This API is used to query the sandbox retention information of a specified application, so that the sandbox environment in the retention state can be checked or managed.This API can be called only in non-DLP sandbox applications.

**Since:** 10

**Deprecated since:** -1

<!--Device-dlpPermission-function getRetentionSandboxList(callback: AsyncCallback<Array<RetentionSandboxInfo>>): void--><!--Device-dlpPermission-function getRetentionSandboxList(callback: AsyncCallback<Array<RetentionSandboxInfo>>): void-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[RetentionSandboxInfo](arkts-dataprotection-dlppermission-retentionsandboxinfo-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100007](../errorcode-dlp.md#19100007-access-denied-for-a-dlp-sandbox-application) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.getRetentionSandboxList((err, retentionSandboxList) => {
  if (err) {
    console.error('getRetentionSandboxList error,', err.code, err.message);
  } else {
    console.info('retentionSandboxList', JSON.stringify(retentionSandboxList));
  }
}); // Obtain the sandbox retention information.
```
