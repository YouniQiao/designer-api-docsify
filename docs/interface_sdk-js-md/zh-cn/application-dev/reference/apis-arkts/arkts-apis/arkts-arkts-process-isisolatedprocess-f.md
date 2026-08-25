# isIsolatedProcess

## 导入模块

```TypeScript
import { process } from '@kit.ArkTS';
```

## isIsolatedProcess

```TypeScript
function isIsolatedProcess(): boolean
```

检查进程是否已被隔离。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
let result = process.isIsolatedProcess();
```
