# getStorageDataDir (System API)

## Modules to Import

```TypeScript
import { Environment } from 'kits/@kit.CoreFileKit';
```

## getStorageDataDir

```TypeScript
function getStorageDataDir(): Promise<string>
```

异步方法获取内存存储根目录，使用promise异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-Environment-function getStorageDataDir(): Promise<string>--><!--Device-Environment-function getStorageDataDir(): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.File.Environment

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | 返回存储根目录。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 202 | The caller is not a system application |
| 13900042 | Unknown error |


## getStorageDataDir

```TypeScript
function getStorageDataDir(callback: AsyncCallback<string>): void
```

异步方法获取内存存储根目录，使用callback异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-Environment-function getStorageDataDir(callback: AsyncCallback<string>): void--><!--Device-Environment-function getStorageDataDir(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.FileManagement.File.Environment

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 异步获取内存存储根目录之后的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 202 | The caller is not a system application |
| 13900042 | Unknown error |

