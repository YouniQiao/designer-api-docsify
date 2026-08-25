# Display

屏幕实例。描述Display对象的属性和方法。下列API示例中都需先使用[getAllDisplays()](arkts-arkui-display-getalldisplays-f.md)、 [getDefaultDisplaySync()](arkts-arkui-display-getdefaultdisplaysync-f.md)中的任一方法获取到Display实例，再通过此实例调用对应方法。

**起始版本：** 7

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

## 导入模块

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## hasImmersiveWindow

```TypeScript
hasImmersiveWindow(callback: AsyncCallback<boolean>): void
```

判断当前屏幕是否包含沉浸式窗口，使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## hasImmersiveWindow

```TypeScript
hasImmersiveWindow(): Promise<boolean>
```

判断当前屏幕是否包含沉浸式窗口，使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |
