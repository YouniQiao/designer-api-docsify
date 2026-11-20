# MainWindowInfo

```TypeScript
interface MainWindowInfo
```

主窗口信息。

**起始版本：** 21

<!--Device-window-interface MainWindowInfo--><!--Device-window-interface MainWindowInfo-End-->

**系统能力：** SystemCapability.Window.SessionManager

## 导入模块

```TypeScript
import { window } from '@kit.ArkUI';
```

## displayId

```TypeScript
displayId: number
```

主窗口所在的屏幕ID。

**类型：** number

**起始版本：** 21

<!--Device-MainWindowInfo-displayId: long--><!--Device-MainWindowInfo-displayId: long-End-->

**系统能力：** SystemCapability.Window.SessionManager

## label

```TypeScript
label: string
```

主窗口的任务名称。

**类型：** string

**起始版本：** 21

<!--Device-MainWindowInfo-label: string--><!--Device-MainWindowInfo-label: string-End-->

**系统能力：** SystemCapability.Window.SessionManager

## showing

```TypeScript
showing: boolean
```

主窗口的前后台状态。true表示主窗口在前台，false表示主窗口不在前台。

**类型：** boolean

**起始版本：** 21

<!--Device-MainWindowInfo-showing: boolean--><!--Device-MainWindowInfo-showing: boolean-End-->

**系统能力：** SystemCapability.Window.SessionManager

## windowId

```TypeScript
windowId: number
```

主窗口ID。

**类型：** number

**起始版本：** 21

<!--Device-MainWindowInfo-windowId: int--><!--Device-MainWindowInfo-windowId: int-End-->

**系统能力：** SystemCapability.Window.SessionManager
