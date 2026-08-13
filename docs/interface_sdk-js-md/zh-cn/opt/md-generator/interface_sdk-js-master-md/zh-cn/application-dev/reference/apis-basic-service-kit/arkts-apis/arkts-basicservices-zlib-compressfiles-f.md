# compressFiles

## compressFiles

```TypeScript
function compressFiles(inFiles: Array<string>, outFile: string, options: Options): Promise<void>
```

压缩指定的多个文件。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-zlib-function compressFiles(inFiles: Array<string>, outFile: string, options: Options): Promise<void>--><!--Device-zlib-function compressFiles(inFiles: Array<string>, outFile: string, options: Options): Promise<void>-End-->

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inFiles | Array & lt;string & gt; | 是 |
| outFile | string | 是 |
| options | [Options](arkts-basicservices-zlib-options-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [900001](../../apis-basic-services-kit/errorcode-zlib.md#900001-传入的源文件错误) |
| [900002](../../apis-basic-services-kit/errorcode-zlib.md#900002-传入的目标文件错误) |

## 示例

```TypeScript
// 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp，也可以通过context获取。
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/filename.xxx';
let pathDir = '/data/storage/el2/base/temp/xxx';
let outFile = '/data/storage/el2/base/temp/xxx.zip';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
  memLevel: zlib.MemLevel.MEM_LEVEL_DEFAULT,
  strategy: zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY
};

try {
  zlib.compressFiles([inFile, pathDir], outFile, options).then(() => {
    console.info('compressFiles success.');
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  });
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`errData is errCode:${code}  message:${message}`);
}
```
