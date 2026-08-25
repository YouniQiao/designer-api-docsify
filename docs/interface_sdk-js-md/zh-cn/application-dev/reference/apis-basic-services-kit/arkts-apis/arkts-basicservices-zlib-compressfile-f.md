# compressFile

## 导入模块

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## compressFile

```TypeScript
function compressFile(inFile: string, outFile: string, options: Options, callback: AsyncCallback<void>): void
```

压缩文件，压缩的结果。使用callback异步回调。

> **说明：**&gt;
> 为了避免路径穿越，从API version 13开始，inFile和outFile传入的参数不允许包含“../”，否则会返回900001、900002错误码。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [900001](../../apis-ability-kit/errorcode-zlib.md#900001-传入的源文件错误) |
| [900002](../../apis-ability-kit/errorcode-zlib.md#900002-传入的目标文件错误) |


## compressFile

```TypeScript
function compressFile(inFile: string, outFile: string, options: Options): Promise<void>
```

压缩文件，压缩的结果。使用Promise异步回调。

> **说明：**&gt;
> 为了避免路径穿越，从API version 13开始，inFile和outFile传入的参数不允许包含“../”，否则会返回900001、900002错误码。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [900001](../../apis-ability-kit/errorcode-zlib.md#900001-传入的源文件错误) |
| [900002](../../apis-ability-kit/errorcode-zlib.md#900002-传入的目标文件错误) |
