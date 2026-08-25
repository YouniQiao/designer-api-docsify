# TransitionController（系统接口）

属性转换控制器。使用其子接口之前得先创建系统窗口，参照示例代码。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## animationForHidden

```TypeScript
animationForHidden(context: TransitionContext): void
```

窗口隐藏时的自定义动画配置。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [TransitionContext](arkts-arkui-window-transitioncontext-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## animationForShown

```TypeScript
animationForShown(context: TransitionContext): void
```

窗口显示时的自定义动画配置。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [TransitionContext](arkts-arkui-window-transitioncontext-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
