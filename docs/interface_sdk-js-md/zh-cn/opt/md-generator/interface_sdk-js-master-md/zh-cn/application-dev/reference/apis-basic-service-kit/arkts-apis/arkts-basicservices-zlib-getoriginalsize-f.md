# getOriginalSize

## getOriginalSize

```TypeScript
function getOriginalSize(compressedFile: string): Promise<number>
```

获取压缩文件的原始大小。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-zlib-function getOriginalSize(compressedFile: string): Promise<long>--><!--Device-zlib-function getOriginalSize(compressedFile: string): Promise<long>-End-->

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| compressedFile | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [900001](../../apis-basic-services-kit/errorcode-zlib.md#900001-传入的源文件错误) |
| [900003](../../apis-basic-services-kit/errorcode-zlib.md#900003-传入的源文件格式错误或者已损坏) |

## 示例

```TypeScript
// 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp，也可以通过context获取。
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let compressedFile = '/data/storage/el2/base/temp/test.zip';

try {
  zlib.getOriginalSize(compressedFile).then((data: number) => {
    console.info(`getOriginalSize success. getOriginalSize: ${data}`);
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`errData is errCode:${code}  message:${message}`);
}
```
