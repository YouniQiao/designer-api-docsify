# decompressFile

## Modules to Import

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## decompressFile

```TypeScript
function decompressFile(inFile: string, outFile: string, options: Options, callback: AsyncCallback<void>): void
```

Decompresses a file. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> To avoid path traversal, the input parameters of **inFile** and **outFile** cannot contain two consecutive
> periods and a slash (../) since API version 13. Otherwise, error codes 900001 and 900002 are returned.&gt;
> The name of the zipped file or zipped folder cannot contain two consecutive periods and a slash (../). Otherwise,
> the error code 900003 is returned.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inFile | string | Yes |
| outFile | string | Yes |
| options | [Options](arkts-basicservices-zlib-options-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [900001](../../apis-ability-kit/errorcode-zlib.md#900001-invalid-source-file) |
| [900002](../../apis-ability-kit/errorcode-zlib.md#900002-invalid-destination-file) |
| [900003](../../apis-ability-kit/errorcode-zlib.md#900003-source-file-in-incorrect-format-or-damaged) |


## decompressFile

```TypeScript
function decompressFile(inFile: string, outFile: string, callback: AsyncCallback<void>): void
```

Decompresses a file. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> To avoid path traversal, the input parameters of **inFile** and **outFile** cannot contain two consecutive
> periods and a slash (../) since API version 13. Otherwise, error codes 900001 and 900002 are returned.&gt;
> The name of the zipped file or zipped folder cannot contain two consecutive periods and a slash (../). Otherwise,
> the error code 900003 is returned.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inFile | string | Yes |
| outFile | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [900001](../../apis-ability-kit/errorcode-zlib.md#900001-invalid-source-file) |
| [900002](../../apis-ability-kit/errorcode-zlib.md#900002-invalid-destination-file) |
| [900003](../../apis-ability-kit/errorcode-zlib.md#900003-source-file-in-incorrect-format-or-damaged) |


## decompressFile

```TypeScript
function decompressFile(inFile: string, outFile: string, options?: Options): Promise<void>
```

Decompresses a file. This API uses a promise to return the result.

> **NOTE：**&gt;
> To avoid path traversal, the input parameters of **inFile** and **outFile** cannot contain two consecutive
> periods and a slash (../) since API version 13. Otherwise, error codes 900001 and 900002 are returned.&gt;
> The name of the zipped file or zipped folder cannot contain two consecutive periods and a slash (../). Otherwise,
> the error code 900003 is returned.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inFile | string | Yes |
| outFile | string | Yes |
| options | [Options](arkts-basicservices-zlib-options-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [900001](../../apis-ability-kit/errorcode-zlib.md#900001-invalid-source-file) |
| [900002](../../apis-ability-kit/errorcode-zlib.md#900002-invalid-destination-file) |
| [900003](../../apis-ability-kit/errorcode-zlib.md#900003-source-file-in-incorrect-format-or-damaged) |
