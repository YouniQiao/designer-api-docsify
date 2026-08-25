# TransitionContext（系统接口）

属性转换的上下文信息。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## completeTransition

```TypeScript
completeTransition(isCompleted: boolean): void
```

设置属性转换的最终完成状态。该函数需要在动画函数animateTo()执行后设置。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isCompleted | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## toWindow

```TypeScript
toWindow: Window
```

动画的目标窗口。

**类型：** [Window](arkts-arkui-window-window-i.md)

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。
