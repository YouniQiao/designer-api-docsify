# Transform

一种特殊的双工流，支持数据转换和结果输出。**Transform**类继承自[Duplex](arkts-arkts-stream-duplex-c.md)，支持**Duplex**中的所有API。

**继承/实现关系：** Transform extends [Duplex](arkts-arkts-stream-duplex-c.md)

**起始版本：** 12

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { stream } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor()
```

创建**Transform**对象的构造函数。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## doFlush

```TypeScript
doFlush(callback: Function): void
```

在流结束时调用，用于处理剩余数据。使用异步回调返回结果。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Function | 是 |

## doTransform

```TypeScript
doTransform(chunk: string, encoding: string, callback: Function): void
```

转换或处理输入的数据块，并通过回调通知处理完成。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| chunk | string | 是 |
| encoding | string | 是 |
| callback | Function | 是 |
