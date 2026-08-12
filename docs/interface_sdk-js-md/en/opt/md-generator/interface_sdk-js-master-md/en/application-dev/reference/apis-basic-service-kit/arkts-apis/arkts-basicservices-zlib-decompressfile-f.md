# decompressFile

## Modules to Import

```TypeScript
import { zlib } from '@kit.BasicServicesKit';
```

## decompressFile

```TypeScript
function decompressFile(inFile: string, outFile: string, options: Options, callback: AsyncCallback<void>): void
```

Decompresses a file. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> To avoid path traversal, the input parameters of **inFile** and **outFile** cannot contain two consecutive
> periods and a slash (../) since API version 13. Otherwise, error codes 900001 and 900002 are returned.
> 
> The name of the zipped file or zipped folder cannot contain two consecutive periods and a slash (../). Otherwise,
> the error code 900003 is returned.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-zlib-function decompressFile(inFile: string, outFile: string, options: Options, callback: AsyncCallback<void>): void--><!--Device-zlib-function decompressFile(inFile: string, outFile: string, options: Options, callback: AsyncCallback<void>): void-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [900001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-zlib.md#900001-invalid-source-file) |
| [900003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-zlib.md#900003-source-file-in-incorrect-format-or-damaged) |
| [900002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-zlib.md#900002-invalid-destination-file) |

## Examples

```TypeScript
// The path used in the code must be an application sandbox path, for example, /data/storage/el2/base/temp. You can obtain the path through the context.
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/xxx.zip';
let outFileDir = '/data/storage/el2/base/temp';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
  parallel: zlib.ParallelStrategy.PARALLEL_STRATEGY_PARALLEL_DECOMPRESSION
};

try {
  zlib.decompressFile(inFile, outFileDir, options, (errData: BusinessError) => {
    if (errData !== null) {
      console.error(`decompressFile errData is errCode:${errData.code}  message:${errData.message}`);
    } else {
      console.info(`decompressFile success.`);
    }
  })
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`decompressFile errData is errCode:${code}  message:${message}`);
}
```


## decompressFile

```TypeScript
function decompressFile(inFile: string, outFile: string, callback: AsyncCallback<void>): void
```

Decompresses a file. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> To avoid path traversal, the input parameters of **inFile** and **outFile** cannot contain two consecutive
> periods and a slash (../) since API version 13. Otherwise, error codes 900001 and 900002 are returned.
> 
> The name of the zipped file or zipped folder cannot contain two consecutive periods and a slash (../). Otherwise,
> the error code 900003 is returned.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-zlib-function decompressFile(inFile: string, outFile: string, callback: AsyncCallback<void>): void--><!--Device-zlib-function decompressFile(inFile: string, outFile: string, callback: AsyncCallback<void>): void-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [900001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-zlib.md#900001-invalid-source-file) |
| [900003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-zlib.md#900003-source-file-in-incorrect-format-or-damaged) |
| [900002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-zlib.md#900002-invalid-destination-file) |

## Examples

```TypeScript
// The path used in the code must be an application sandbox path, for example, /data/storage/el2/base/temp. You can obtain the path through the context.
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/xxx.zip';
let outFileDir = '/data/storage/el2/base/temp';

try {
  zlib.decompressFile(inFile, outFileDir, (errData: BusinessError) => {
    if (errData !== null) {
      console.error(`decompressFile failed. code is ${errData.code}, message is ${errData.message}`);
    } else {
      console.info(`decompressFile success.`);
    }
  })
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`decompressFile failed. code is ${code}, message is ${message}`);
}
```


## decompressFile

```TypeScript
function decompressFile(inFile: string, outFile: string, options?: Options): Promise<void>
```

Decompresses a file. This API uses a promise to return the result.

> **NOTE：**
> 
> To avoid path traversal, the input parameters of **inFile** and **outFile** cannot contain two consecutive
> periods and a slash (../) since API version 13. Otherwise, error codes 900001 and 900002 are returned.
> 
> The name of the zipped file or zipped folder cannot contain two consecutive periods and a slash (../). Otherwise,
> the error code 900003 is returned.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-zlib-function decompressFile(inFile: string, outFile: string, options?: Options): Promise<void>--><!--Device-zlib-function decompressFile(inFile: string, outFile: string, options?: Options): Promise<void>-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [900001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-zlib.md#900001-invalid-source-file) |
| [900003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-zlib.md#900003-source-file-in-incorrect-format-or-damaged) |
| [900002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-zlib.md#900002-invalid-destination-file) |

## Examples

```TypeScript
// The path used in the code must be an application sandbox path, for example, /data/storage/el2/base/temp. You can obtain the path through the context.
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/xxx.zip';
let outFileDir = '/data/storage/el2/base/temp';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION
};

try {
  zlib.decompressFile(inFile, outFileDir, options).then((data: void) => {
    console.info('decompressFile success. data: ' + JSON.stringify(data));
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`errData is errCode:${code}  message:${message}`);
}
```
