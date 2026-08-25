# isStandby

## 导入模块

```TypeScript
import { power } from 'kits/@kit.BasicServicesKit';
```

## isStandby

```TypeScript
function isStandby(): boolean
```

检测当前设备是否进入待机低功耗续航模式。待机模式下系统会采取降低功耗的策略，开发者应据此调整应用的后台任务和资源使用策略，避免在待机时执行高耗能操作。

**起始版本：** 10

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [4900101](../errorcode-power.md#4900101-连接服务失败) |
