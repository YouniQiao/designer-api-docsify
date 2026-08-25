# apiAvailable

## 导入模块

```TypeScript
import { deviceInfo } from 'kits/@kit.BasicServicesKit';
```

## apiAvailable

```TypeScript
function apiAvailable(version: string | number): boolean
```

检查指定的API版本在当前设备上是否可用。 此方法提供OpenHarmony及其各发行版系统版本的兼容性检查。该方法会根据输入格式和API版本范围自动选择合适的版本检查方法。

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Startup.SystemInfo

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| version | string \| number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
