# allocUninitializedFromPool

## 导入模块

```TypeScript
import { fastbuffer } from 'kits/@kit.ArkTS';
```

## allocUninitializedFromPool

```TypeScript
function allocUninitializedFromPool(size: number): FastBuffer
```

从缓冲池中创建指定大小未初始化的FastBuffer对象。调用[fill](arkts-arkts-fastbuffer-fastbuffer-c.md#fill)函数初始化该对象。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |

**返回值：**

| 类型 |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |
