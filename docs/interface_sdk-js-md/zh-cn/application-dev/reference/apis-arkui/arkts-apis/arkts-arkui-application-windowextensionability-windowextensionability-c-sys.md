# WindowExtensionAbility（系统接口）

WindowExtensionAbility类。

**起始版本：** 9

**废弃版本：** 21

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { WindowExtensionAbility, WindowExtensionContext } from 'kits/@kit.ArkUI';
```

## onConnect

```TypeScript
onConnect(want: Want): void
```

当窗口扩展组件第一次连接ability时回调。

**起始版本：** 9

**废弃版本：** 21

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

## onDisconnect

```TypeScript
onDisconnect(want: Want): void
```

当所有连接到窗口扩展组件的ability断开连接时回调。

**起始版本：** 9

**废弃版本：** 21

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

## onWindowReady

```TypeScript
onWindowReady(window: window.Window): void
```

当窗口被创建时回调。

**起始版本：** 9

**废弃版本：** 21

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [window](arkts-arkui-window-n.md) | window.Window | 是 |

## context

```TypeScript
context: WindowExtensionContext
```

Indicates window extension ability context.

**类型：** [WindowExtensionContext](arkts-arkui-windowextensioncontext-t-sys.md)

**起始版本：** 9

**废弃版本：** 21

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。
