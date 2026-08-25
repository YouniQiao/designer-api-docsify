# getMainThreadStackTrace

## 导入模块

```TypeScript
import { util } from '@kit.ArkTS';
```

## getMainThreadStackTrace

```TypeScript
function getMainThreadStackTrace(): string
```

获取主线程的栈追踪信息，最多返回 64 层调用帧。 该接口可能对主线程性能产生影响，建议仅在必要时使用，如日志记录、错误分析或调试场景。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

**示例**

```TypeScript
let stack = util.getMainThreadStackTrace();
console.info(stack);
// 输出当前主线程的栈追踪信息。
```
