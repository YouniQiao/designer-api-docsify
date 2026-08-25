# alloc

## 导入模块

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## alloc

```TypeScript
function alloc(size: number, fill?: string | Buffer | number | number | number, encoding?: BufferEncoding): Buffer
```

创建指定字节长度的Buffer对象，并使用指定值进行初始化填充（默认填充0）。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |
| fill | string \| Buffer \| number \| number \| number | 否 |
| encoding | BufferEncoding | 否 |

**返回值：**

| 类型 |
| --- |
| Buffer |
