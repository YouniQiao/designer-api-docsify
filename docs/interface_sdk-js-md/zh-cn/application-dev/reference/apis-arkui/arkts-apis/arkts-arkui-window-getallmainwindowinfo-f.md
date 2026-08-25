# getAllMainWindowInfo

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## getAllMainWindowInfo

```TypeScript
function getAllMainWindowInfo(): Promise<Array<MainWindowInfo>>
```

获取全部主窗口信息，使用Promise异步回调。

**起始版本：** 21

**需要权限：** ohos.permission.CUSTOM_SCREEN_CAPTURE

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[MainWindowInfo](arkts-arkui-window-mainwindowinfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
