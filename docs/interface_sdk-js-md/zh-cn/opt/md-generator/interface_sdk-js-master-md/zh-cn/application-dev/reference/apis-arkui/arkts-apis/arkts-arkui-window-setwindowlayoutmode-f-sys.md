# setWindowLayoutMode（系统接口）

## setWindowLayoutMode

```TypeScript
function setWindowLayoutMode(mode: WindowLayoutMode, callback: AsyncCallback<void>): void
```

设置窗口布局模式，使用callback异步回调。

**起始版本：** 9

**废弃版本：** 26.0.0

<!--Device-window-function setWindowLayoutMode(mode: WindowLayoutMode, callback: AsyncCallback<void>): void--><!--Device-window-function setWindowLayoutMode(mode: WindowLayoutMode, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [WindowLayoutMode](arkts-arkui-window-windowlayoutmode-e-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  window.setWindowLayoutMode(window.WindowLayoutMode.WINDOW_LAYOUT_MODE_CASCADE, (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(`Failed to set window layout mode. Cause code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in setting window layout mode.');
  });
} catch (exception) {
  console.error(`Failed to set window layout mode. Cause code: ${exception.code}, message: ${exception.message}`);
}
```


## setWindowLayoutMode

```TypeScript
function setWindowLayoutMode(mode: WindowLayoutMode): Promise<void>
```

设置窗口布局模式，使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 26.0.0

<!--Device-window-function setWindowLayoutMode(mode: WindowLayoutMode): Promise<void>--><!--Device-window-function setWindowLayoutMode(mode: WindowLayoutMode): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [WindowLayoutMode](arkts-arkui-window-windowlayoutmode-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = window.setWindowLayoutMode(window.WindowLayoutMode.WINDOW_LAYOUT_MODE_CASCADE);
  promise.then(() => {
    console.info('Succeeded in setting window layout mode.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set window layout mode. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to set window layout mode. Cause code: ${exception.code}, message: ${exception.message}`);
}
```
