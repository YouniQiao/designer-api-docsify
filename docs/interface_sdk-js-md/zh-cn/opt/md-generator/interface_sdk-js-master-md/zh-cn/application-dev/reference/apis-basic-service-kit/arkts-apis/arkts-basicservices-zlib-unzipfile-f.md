# unzipFile

## 导入模块

```TypeScript
```

## unzipFile

```TypeScript
function unzipFile(inFile: string, outFile: string, options: Options): Promise<void>
```

解压文件，解压完成后返回执行结果。使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [zlib.decompressFile](arkts-basicservices-zlib-decompressfile-f.md#decompressfile) > 替代。 > > 传入的压缩包内部文件或者文件夹名称不能包含“../”，否则会返回-1错误码。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [decompressFile](arkts-basicservices-zlib-decompressfile-f.md#decompressfile)(inFile: string, outFile: string, options: Options, callback: AsyncCallback&lt;void&gt;)

<!--Device-zlib-function unzipFile(inFile: string, outFile: string, options: Options): Promise<void>--><!--Device-zlib-function unzipFile(inFile: string, outFile: string, options: Options): Promise<void>-End-->

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

**示例**

```TypeScript
// 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp,也可以通过context获取。
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/xxx.zip';
let outFile = '/data/storage/el2/base/temp/xxx';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
  memLevel: zlib.MemLevel.MEM_LEVEL_DEFAULT,
  strategy: zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY
};

zlib.unzipFile(inFile, outFile, options).then((data: void) => {
  console.info('unzipFile result is ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error('error is ' + JSON.stringify(err));
})
```
