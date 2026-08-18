# decompressFile

## 导入模块

```TypeScript
```

## decompressFile

```TypeScript
function decompressFile(inFile: string, outFile: string, options: Options, callback: AsyncCallback<void>): void
```

解压文件，解压的结果。使用callback异步回调。 > **说明：** > > 为了避免路径穿越，从API version 13开始，inFile和outFile传入的参数不允许包含“../”，否则会返回900001、900002错误码。 > > 传入的压缩包内部文件或者文件夹名称不能包含“../”，否则会返回900003错误码。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-zlib-function decompressFile(inFile: string, outFile: string, options: Options, callback: AsyncCallback<void>): void--><!--Device-zlib-function decompressFile(inFile: string, outFile: string, options: Options, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inFile | string | 是 |
| outFile | string | 是 |
| options | [Options](arkts-basicservices-zlib-options-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [900001](../../apis-basic-services-kit/errorcode-zlib.md#900001-传入的源文件错误) |
| [900003](../../apis-basic-services-kit/errorcode-zlib.md#900003-传入的源文件格式错误或者已损坏) |
| [900002](../../apis-basic-services-kit/errorcode-zlib.md#900002-传入的目标文件错误) |

**示例**

```TypeScript
// 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp,也可以通过context获取。
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/xxx.zip';
let outFileDir = '/data/storage/el2/base/temp';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
  parallel: zlib.ParallelStrategy.PARALLEL_STRATEGY_PARALLEL_DECOMPRESSION
};

try {
  zlib.decompressFile(inFile, outFileDir, options, (errData: BusinessError) => {
    if (errData) {
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

解压文件，解压的结果。使用callback异步回调。 > **说明：** > > 为了避免路径穿越，从API version 13开始，inFile和outFile传入的参数不允许包含“../”，否则会返回900001、900002错误码。 > > 传入的压缩包内部文件或者文件夹名称不能包含“../”，否则会返回900003错误码。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-zlib-function decompressFile(inFile: string, outFile: string, callback: AsyncCallback<void>): void--><!--Device-zlib-function decompressFile(inFile: string, outFile: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inFile | string | 是 |
| outFile | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [900001](../../apis-basic-services-kit/errorcode-zlib.md#900001-传入的源文件错误) |
| [900003](../../apis-basic-services-kit/errorcode-zlib.md#900003-传入的源文件格式错误或者已损坏) |
| [900002](../../apis-basic-services-kit/errorcode-zlib.md#900002-传入的目标文件错误) |

**示例**

```TypeScript
// 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp,也可以通过context获取。
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/xxx.zip';
let outFileDir = '/data/storage/el2/base/temp';

try {
  zlib.decompressFile(inFile, outFileDir, (errData: BusinessError) => {
    if (errData) {
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

解压文件，解压的结果。使用Promise异步回调。 > **说明：** > > 为了避免路径穿越，从API version 13开始，inFile和outFile传入的参数不允许包含“../”，否则会返回900001、900002错误码。 > > 传入的压缩包内部文件或者文件夹名称不能包含“../”，否则会返回900003错误码。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-zlib-function decompressFile(inFile: string, outFile: string, options?: Options): Promise<void>--><!--Device-zlib-function decompressFile(inFile: string, outFile: string, options?: Options): Promise<void>-End-->

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inFile | string | 是 |
| outFile | string | 是 |
| options | [Options](arkts-basicservices-zlib-options-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [900001](../../apis-basic-services-kit/errorcode-zlib.md#900001-传入的源文件错误) |
| [900003](../../apis-basic-services-kit/errorcode-zlib.md#900003-传入的源文件格式错误或者已损坏) |
| [900002](../../apis-basic-services-kit/errorcode-zlib.md#900002-传入的目标文件错误) |

**示例**

```TypeScript
// 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp,也可以通过context获取。
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
