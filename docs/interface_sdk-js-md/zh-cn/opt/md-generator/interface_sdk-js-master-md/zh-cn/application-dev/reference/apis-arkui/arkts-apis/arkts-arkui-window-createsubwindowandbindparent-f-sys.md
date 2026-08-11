# createSubWindowAndBindParent（系统接口）

## createSubWindowAndBindParent

```TypeScript
function createSubWindowAndBindParent(name: string, parentId: number, ctx: BaseContext,
    parentWindowEventListener: WindowEventListener): Promise<Window>
```

创建一个子窗，并绑定父窗。使用Promise异步回调。

子窗跟随父窗显示/隐藏，但并不跟随父窗销毁，子窗通过回调函数监听父窗生命周期变化。

建议在父窗销毁后主动销毁创建的子窗。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-window-function createSubWindowAndBindParent(name: string, parentId: int, ctx: BaseContext,    parentWindowEventListener: WindowEventListener): Promise<Window>--><!--Device-window-function createSubWindowAndBindParent(name: string, parentId: int, ctx: BaseContext,    parentWindowEventListener: WindowEventListener): Promise<Window>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| parentId | number | 是 |
| ctx | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| parentWindowEventListener | [WindowEventListener](arkts-arkui-windoweventlistener-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Window&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300001](../errorcode-window.md#1300001-重复操作) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1300009](../errorcode-window.md#1300009-父窗口无效) |

## 示例

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    let windowClass: window.Window | undefined = undefined;
    const parentWindowEventListener = (windowId: number, event: window.WindowEventType) => {
      // ...
    }
    try {
      let promise = window.createSubWindowAndBindParent('test', 100, this.context, parentWindowEventListener);
      promise.then((data) => {
        console.info('Succeeded in creating the window. Data:' + JSON.stringify(data));
        windowClass = data;
      }).catch((err: BusinessError) => {
        console.error(`Failed to create the Window. Cause code: ${err.code}, message: ${err.message}`);
      });
    } catch (exception) {
      console.error(`Failed to create the window. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  }
}
```
