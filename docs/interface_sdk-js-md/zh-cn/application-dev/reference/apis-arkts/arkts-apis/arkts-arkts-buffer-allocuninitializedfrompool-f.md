# allocUninitializedFromPool

## 导入模块

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## allocUninitializedFromPool

```TypeScript
function allocUninitializedFromPool(size: number): Buffer
```

创建指定大小未初始化的Buffer对象。内存从缓冲池分配，缓冲池为预分配的内存区域，适用于创建较小Buffer时减少频繁内存分配的开销，提升性能。对于需要独立内存的场景，建议使用[allocUninitialized](arkts-arkts-buffer-allocuninitialized-f.md)。 创建的Buffer内容未知，需要使用[fill](arkts-arkts-buffer-buffer-c.md#fill)函数来初始化Buffer对象。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |

**返回值：**

| 类型 |
| --- |
| Buffer |
