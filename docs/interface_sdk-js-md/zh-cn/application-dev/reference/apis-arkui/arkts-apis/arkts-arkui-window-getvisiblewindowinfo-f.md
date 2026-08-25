# getVisibleWindowInfo

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## getVisibleWindowInfo

```TypeScript
function getVisibleWindowInfo(): Promise<Array<WindowInfo>>
```

获取当前屏幕的可见主窗口（未退至后台的主窗口）信息。使用Promise异步回调。

**起始版本：** 18

**需要权限：** 
- API版本18+：ohos.permission.VISIBLE_WINDOW_INFO

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;WindowInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
