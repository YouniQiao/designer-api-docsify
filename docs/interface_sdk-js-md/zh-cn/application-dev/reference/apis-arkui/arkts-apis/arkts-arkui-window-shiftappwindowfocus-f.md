# shiftAppWindowFocus

## 导入模块

```TypeScript
import { window } from '@kit.ArkUI';
```

## shiftAppWindowFocus

```TypeScript
function shiftAppWindowFocus(sourceWindowId: int, targetWindowId: int): Promise<void>
```

在同应用内将窗口焦点从源窗口转移到目标窗口，仅支持应用主窗、子窗范围内的焦点转移。使用Promise异步回调。目标窗口需确保具有获得焦点的能力（可通过 [setWindowFocusable()](arkts-arkui-window-window-i.md#setwindowfocusable) 设置），并确保调用[showWindow()](arkts-arkui-window-window-i.md#showwindow)成功且执行完毕。

> **说明：**&gt;
> 在调用shiftAppWindowFocus()前，建议确保目标窗口已调用
> [loadContent()](arkts-arkui-window-window-i.md#loadcontent)
> 或[setUIContent()](arkts-arkui-window-window-i.md#setuicontent)并生效，
> 否则可能会导致不可见窗口获取焦点，造成功能异常或影响用户体验。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceWindowId | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| targetWindowId | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

**示例**

ArkTS-Dyn示例：

```TypeScript
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // ...
    console.info('onWindowStageCreate');
    let mainWindow: window.Window | undefined = undefined;
    let subWindow: window.Window | undefined = undefined;
    let mainWindowId: number = -1;
    let subWindowId: number = -1;

    try {
      windowStage.loadContent('pages/Index', (err) => {
        if (err.code) {
          console.error(`Failed to load content for main window. Cause code: ${err.code}, message: ${err.message}`);
        }
        // 获取应用主窗及ID
        windowStage.getMainWindow().then((data) => {
          if (data == null) {
            console.error('Failed to obtain the main window. Cause: The data is empty');
            return;
          }
          mainWindow = data;
          mainWindowId = mainWindow.getWindowProperties().id;
          console.info('Succeeded in obtaining the main window');
        }).catch((err: BusinessError) => {
          console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        });

        // 创建或获取子窗及ID，此时子窗口获焦
        windowStage.createSubWindow('testSubWindow').then((data) => {
          if (data == null) {
            console.error('Failed to obtain the sub window. Cause: The data is empty');
            return;
          }
          subWindow = data;
          subWindowId = subWindow.getWindowProperties().id;
          subWindow.resize(500, 500);
          subWindow.setUIContent('pages/Index');
          subWindow.showWindow();

          // 监听Window状态，确保已经就绪
          subWindow.on("windowEvent", (windowEvent) => {
            if (windowEvent == window.WindowEventType.WINDOW_ACTIVE) {
              // 切换焦点
              window.shiftAppWindowFocus(subWindowId, mainWindowId).then(() => {
                console.info('Succeeded in shifting app window focus');
              }).catch((err: BusinessError) => {
                console.error(`Failed to shift app window focus. Cause code: ${err.code}, message: ${err.message}`);
              });
            }
          });
        });
      });
    } catch (exception) {
      console.error(`Failed to shift app focus. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import common from '@ohos.app.ability.common';
import { LocalStorage } from '@ohos.arkui.stateManagement'

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
     windowStage.loadContent('pages/Index', (err) => {
        if (err?.code) {
          console.error(`Failed to load content for main window. Cause code: ${err?.code}, message: ${err?.message}`);
        }
      // 创建子窗
      windowStage.createSubWindow('testSubWindow').then((subWindow: window.Window) => {
        let storage: LocalStorage = new LocalStorage();
        subWindow.loadContent('pages/Index', storage, (err: BusinessError): void => {
          subWindow.showWindow().then(() => {
            let mainWindow = windowStage.getMainWindowSync();
            let mainWindowId = mainWindow.getWindowProperties().id;
            let subWindowId = subWindow.getWindowProperties().id;
            // 切换焦点
            window.shiftAppWindowFocus(subWindowId as int, mainWindowId as int).then((): void => {
              console.info('Succeeded in shifting app window focus');
            }).catch((err: BusinessError): void => {
              console.error(`Failed to shift app window focus. Cause code: ${err.code}, message: ${err.message}`);
            });
          });
        });
      });
    });
  }
}
```
