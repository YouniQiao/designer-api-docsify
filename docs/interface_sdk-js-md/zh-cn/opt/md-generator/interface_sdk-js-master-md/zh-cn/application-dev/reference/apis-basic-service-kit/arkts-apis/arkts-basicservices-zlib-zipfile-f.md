# zipFile

## zipFile

```TypeScript
function zipFile(inFile: string, outFile: string, options: Options): Promise<void>
```

压缩接口，压缩完成后返回执行结果。使用Promise异步回调。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [zlib.compressFile](arkts-basicservices-zlib-compressfile-f.md#compressFile)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [compressFile](zlib.compressFile(inFile:)

<!--Device-zlib-function zipFile(inFile: string, outFile: string, options: Options): Promise<void>--><!--Device-zlib-function zipFile(inFile: string, outFile: string, options: Options): Promise<void>-End-->

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inFile | string | 是 |
| outFile | string | 是 |
| options | [Options](arkts-basicservices-zlib-options-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## 示例

```TypeScript
// 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp,也可以通过context获取。
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/filename.xxx';
let outFile = '/data/storage/el2/base/temp/xxx.zip';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
  memLevel: zlib.MemLevel.MEM_LEVEL_DEFAULT,
  strategy: zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY
};

zlib.zipFile(inFile, outFile, options).then((data: void) => {
  console.info('zipFile result is ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error('error is ' + JSON.stringify(err));
});
```
