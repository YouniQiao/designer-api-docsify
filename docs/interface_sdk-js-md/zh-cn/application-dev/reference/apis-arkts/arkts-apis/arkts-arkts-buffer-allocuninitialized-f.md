# allocUninitialized

## 导入模块

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## allocUninitialized

```TypeScript
function allocUninitialized(size: number): Buffer
```

创建指定大小未初始化的Buffer对象。内存不从缓冲池分配，适用于需要创建较大Buffer或希望精确控制内存分配的场景，如一次性分配较大内存区域（避免缓冲池可能导致的内存碎片累积和缓存性能损耗）。 创建的Buffer的内容未知，需要使用[fill](arkts-arkts-buffer-buffer-c.md#fill)函数来初始化Buffer对象。

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
