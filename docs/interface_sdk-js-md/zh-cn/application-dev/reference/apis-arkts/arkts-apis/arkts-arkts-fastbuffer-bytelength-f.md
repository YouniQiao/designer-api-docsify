# byteLength

## 导入模块

```TypeScript
import { fastbuffer } from 'kits/@kit.ArkTS';
```

## byteLength

```TypeScript
function byteLength(value: string | FastBuffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer, encoding?: BufferEncoding): number
```

根据不同的编码格式，返回指定内容的字节数。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) \| TypedArray \| DataView \| ArrayBuffer \| SharedArrayBuffer | 是 |
| encoding | BufferEncoding | 否 |

**返回值：**

| 类型 |
| --- |
| number |
