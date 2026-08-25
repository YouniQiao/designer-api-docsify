# getMainWindowSnapshot

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## getMainWindowSnapshot

```TypeScript
function getMainWindowSnapshot(windowId: Array<number>, config: WindowSnapshotConfiguration):
    Promise<Array<image.PixelMap | undefined>>
```

获取一个或多个指定windowId的主窗口截图，使用Promise异步回调。

**起始版本：** 21

**需要权限：** ohos.permission.CUSTOM_SCREEN_CAPTURE

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | Array & lt;number & gt; | 是 |
| config | [WindowSnapshotConfiguration](arkts-arkui-window-windowsnapshotconfiguration-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;image.PixelMap \ | undefined & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
