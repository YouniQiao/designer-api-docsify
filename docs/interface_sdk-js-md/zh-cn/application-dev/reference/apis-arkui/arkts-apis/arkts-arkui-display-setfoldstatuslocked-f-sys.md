# setFoldStatusLocked（系统接口）

## 导入模块

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## setFoldStatusLocked

```TypeScript
function setFoldStatusLocked(locked: boolean): void
```

设置可折叠设备当前折叠状态的锁定状态。

**起始版本：** 11

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locked | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |
