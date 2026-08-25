# alloc

## 导入模块

```TypeScript
import { fastbuffer } from 'kits/@kit.ArkTS';
```

## alloc

```TypeScript
function alloc(size: number, fill?: string | FastBuffer | number, encoding?: BufferEncoding): FastBuffer
```

创建指定字节长度的FastBuffer对象并初始化。调用后，FastBuffer对象的每个字节将被填充为指定的fill值，未指定fill时默认填充为0。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |
| fill | string \| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) \| number | 否 |
| encoding | BufferEncoding | 否 |

**返回值：**

| 类型 |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |
