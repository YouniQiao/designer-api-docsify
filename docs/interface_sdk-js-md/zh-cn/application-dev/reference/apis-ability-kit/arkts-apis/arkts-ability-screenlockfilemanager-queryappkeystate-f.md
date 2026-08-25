# queryAppKeyState

## 导入模块

```TypeScript
import { screenLockFileManager } from 'kits/@kit.AbilityKit';
```

## queryAppKeyState

```TypeScript
function queryAppKeyState(): KeyStatus
```

以同步方法查询调用方应用锁屏下敏感数据密钥的状态。

**起始版本：** 18

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**返回值：**

| 类型 |
| --- |
| [KeyStatus](arkts-ability-screenlockfilemanager-keystatus-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [29300002](../errorcode-screenLockFileManager.md#29300002-系统服务工作异常) |
