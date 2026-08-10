# getVisibleWindowInfo

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## getVisibleWindowInfo

```TypeScript
function getVisibleWindowInfo(): Promise<Array<WindowInfo>>
```

获取当前屏幕的可见主窗口（未退至后台的主窗口）信息。使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 18+: ohos.permission.VISIBLE_WINDOW_INFO

<!--Device-window-function getVisibleWindowInfo(): Promise<Array<WindowInfo>>--><!--Device-window-function getVisibleWindowInfo(): Promise<Array<WindowInfo>>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;WindowInfo&gt;&gt; | Promise对象，返回当前可见窗口的相关信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300003 | This window manager service works abnormally. Possible cause: Internal task error. |
| 801 | Capability not supported. Function getVisibleWindowInfo can not work correctly due to limited device capabilities. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. Possible cause: Need ohos.permission.VISIBLE_WINDOW_INFO permission.<br>**Applicable version:** 18 and later |
| 202 | Permission verification failed, non-system application uses system API.<br>**Applicable version:** 12 - 17 |

## Examples

```TypeScript
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = window.getVisibleWindowInfo();
  promise.then((data) => {
    data.forEach(windowInfo=>{
      console.info(`left:${windowInfo.rect.left}`);
      console.info(`top:${windowInfo.rect.top}`);
      console.info(`width:${windowInfo.rect.width}`);
      console.info(`height:${windowInfo.rect.height}`);
      console.info(`windowId:${windowInfo.windowId}`);
      console.info(`windowStatusType:${windowInfo.windowStatusType}`);
      console.info(`abilityName:${windowInfo.abilityName}`);
      console.info(`bundleName:${windowInfo.bundleName}`);
      console.info(`isFocused:${windowInfo.isFocused}`);
    })
  }).catch((err: BusinessError) => {
    console.error('Failed to getWindowInfo. Cause: ' + JSON.stringify(err));
  });
} catch (exception) {
  console.error(`Failed to get visible window info. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

