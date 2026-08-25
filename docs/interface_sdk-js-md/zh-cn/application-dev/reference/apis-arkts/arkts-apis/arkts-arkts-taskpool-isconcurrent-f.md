# isConcurrent

## 导入模块

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## isConcurrent

```TypeScript
function isConcurrent(func: Function): boolean
```

检查函数是否为并发函数。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| func | Function | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
