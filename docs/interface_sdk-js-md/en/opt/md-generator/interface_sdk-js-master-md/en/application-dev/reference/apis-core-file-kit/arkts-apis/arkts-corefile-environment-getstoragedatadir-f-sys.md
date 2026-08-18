# getStorageDataDir (System API)

## Modules to Import

```TypeScript
```

## getStorageDataDir

```TypeScript
function getStorageDataDir(): Promise<string>
```

Obtains the root directory of the memory. This API uses a promise to return the result.

**Since:** 23

<!--Device-Environment-function getStorageDataDir(): Promise<string>--><!--Device-Environment-function getStorageDataDir(): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.File.Environment

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900042 |


## getStorageDataDir

```TypeScript
function getStorageDataDir(callback: AsyncCallback<string>): void
```

Obtains the root directory of the memory. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-Environment-function getStorageDataDir(callback: AsyncCallback<string>): void--><!--Device-Environment-function getStorageDataDir(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.FileManagement.File.Environment

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900042 |
