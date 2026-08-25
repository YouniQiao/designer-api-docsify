# getOriginalSize

## 导入模块

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## getOriginalSize

```TypeScript
function getOriginalSize(compressedFile: string): Promise<number>
```

获取压缩文件的原始大小。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

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
| [900001](../../apis-ability-kit/errorcode-zlib.md#900001-传入的源文件错误) |
| [900003](../../apis-ability-kit/errorcode-zlib.md#900003-传入的源文件格式错误或者已损坏) |
