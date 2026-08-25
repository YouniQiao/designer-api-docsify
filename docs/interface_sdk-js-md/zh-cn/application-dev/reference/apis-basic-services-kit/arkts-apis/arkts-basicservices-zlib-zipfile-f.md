# zipFile

## 导入模块

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## zipFile

```TypeScript
function zipFile(inFile: string, outFile: string, options: Options): Promise<void>
```

压缩接口，压缩完成后返回执行结果。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [zlib.compressFile](arkts-basicservices-zlib-compressfile-f.md)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [compressFile](arkts-basicservices-zlib-compressfile-f.md)(inFile: string, outFile: string, options: Options, callback: AsyncCallback&lt;void&gt;)

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
