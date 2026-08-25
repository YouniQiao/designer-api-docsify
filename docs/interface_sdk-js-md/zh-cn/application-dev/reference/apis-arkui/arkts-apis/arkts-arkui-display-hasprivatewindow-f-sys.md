# hasPrivateWindow（系统接口）

## 导入模块

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## hasPrivateWindow

```TypeScript
function hasPrivateWindow(displayId: number): boolean
```

查询指定display对象上是否有可见的隐私窗口。可通过 [setWindowPrivacyMode()](../../../reference/apis-arkui/arkts-apis-window-Window.md#setwindowprivacymode9)接口设置隐私窗口。 隐私窗口内容将无法被截屏或录屏。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayId | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |
