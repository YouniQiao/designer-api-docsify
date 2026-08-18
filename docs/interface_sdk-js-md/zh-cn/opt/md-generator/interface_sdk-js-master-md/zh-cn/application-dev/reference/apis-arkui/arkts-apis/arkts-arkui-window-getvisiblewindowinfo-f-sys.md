# getVisibleWindowInfo（系统接口）

## 导入模块

```TypeScript
```

## getVisibleWindowInfo

```TypeScript
function getVisibleWindowInfo(): Promise<Array<WindowInfo>>
```

获取当前屏幕的可见主窗口（未退至后台的主窗口）信息。使用Promise异步回调。

**起始版本：** 23

**需要权限：** 
- API版本18+：ohos.permission.VISIBLE_WINDOW_INFO

<!--Device-window-function getVisibleWindowInfo(): Promise<Array<WindowInfo>>--><!--Device-window-function getVisibleWindowInfo(): Promise<Array<WindowInfo>>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;WindowInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = window.getVisibleWindowInfo();
  promise.then((data) => {
    data.forEach((windowInfo) => {
      console.info(`left:${windowInfo.rect.left}`);
      console.info(`top:${windowInfo.rect.top}`);
      console.info(`width:${windowInfo.rect.width}`);
      console.info(`height:${windowInfo.rect.height}`);
      console.info(`windowId:${windowInfo.windowId}`);
      console.info(`windowStatusType:${windowInfo.windowStatusType}`);
      console.info(`abilityName:${windowInfo.abilityName}`);
      console.info(`bundleName:${windowInfo.bundleName}`);
      console.info(`isFocused:${windowInfo.isFocused}`);
      console.info(`displayId:${windowInfo.displayId}`);
      console.info(`globalDisplayRect:${JSON.stringify(windowInfo.globalDisplayRect)}`);
      console.info(`globalRect:${JSON.stringify(windowInfo.globalRect)}`);
    });
  }).catch((err: BusinessError) => {
    console.error(`Failed to getWindowInfo. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to get visible window info. Cause code: ${exception.code}, message: ${exception.message}`);
}
```
