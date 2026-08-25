# transcode

## 导入模块

```TypeScript
import { fastbuffer } from 'kits/@kit.ArkTS';
```

## transcode

```TypeScript
function transcode(source: FastBuffer | Uint8Array, fromEnc: string, toEnc: string): FastBuffer
```

将FastBuffer或Uint8Array对象从fromEnc编码转换为toEnc编码。适用于需要在不同编码格式之间转换数据的场景。例如，将UTF-8编码的数据转换为Latin1编码，以便在仅支持ASCII的系统中处理。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) \| Uint8Array | 是 |
| fromEnc | string | 是 | 当前编码格式。支持的格式范围为'ascii' \| 'utf8' \| 'utf16le' \| 'ucs2' \| 'latin1' \|
| toEnc | string | 是 | 目标编码。支持的格式范围为'ascii' \| 'utf8' \| 'utf16le' \| 'ucs2' \| 'latin1' \|

**返回值：**

| 类型 |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |
