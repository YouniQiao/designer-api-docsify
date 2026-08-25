# setWindowLayoutMode（系统接口）

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## setWindowLayoutMode

```TypeScript
function setWindowLayoutMode(mode: WindowLayoutMode, callback: AsyncCallback<void>): void
```

设置窗口布局模式，使用callback异步回调。

**起始版本：** 9

**废弃版本：** 26.0.0

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [WindowLayoutMode](arkts-arkui-window-windowlayoutmode-e-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |


## setWindowLayoutMode

```TypeScript
function setWindowLayoutMode(mode: WindowLayoutMode): Promise<void>
```

设置窗口布局模式，使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 26.0.0

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [WindowLayoutMode](arkts-arkui-window-windowlayoutmode-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
