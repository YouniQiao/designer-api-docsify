# uptime

## 导入模块

```TypeScript
import { process } from '@kit.ArkTS';
```

## uptime

```TypeScript
function uptime(): number
```

获取当前系统已运行的时间（以秒为单位）。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| number |

**示例**

```TypeScript
let time = process.uptime();
```
