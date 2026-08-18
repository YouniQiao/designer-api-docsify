# WindowProxy

UIExtension窗口代理。

**起始版本：** 23

<!--Device-uiExtension-interface WindowProxy--><!--Device-uiExtension-interface WindowProxy-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## createSubWindowWithOptions

```TypeScript
createSubWindowWithOptions(name: string, subWindowOptions: window.SubWindowOptions): Promise<window.Window>
```

创建该WindowProxy实例下的子窗口，使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-WindowProxy-createSubWindowWithOptions(name: string, subWindowOptions: window.SubWindowOptions): Promise<window.Window>--><!--Device-WindowProxy-createSubWindowWithOptions(name: string, subWindowOptions: window.SubWindowOptions): Promise<window.Window>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| [subWindowOptions](arkts-arkui-window-extensionwindowconfig-i-sys.md) | window.SubWindowOptions | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;window.Window & gt; |

**错误码：**

| 错误码ID |
| --- |
| 1300035 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

**示例**

```TypeScript
// ExtensionProvider.ets
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    const subWindowOpts: window.SubWindowOptions = {
      title: 'This is a subwindow',
      decorEnabled: true
    };
    // 创建子窗口
    extensionWindow.createSubWindowWithOptions('subWindowForHost', subWindowOpts)
      .then((subWindow: window.Window) => {
        subWindow.setUIContent('pages/Index', (err, data) => {
          if (err && err.code) {
            return;
          }
          subWindow?.resize(300, 300, (err, data) => {
            if (err && err.code) {
              return;
            }
            subWindow?.moveWindowTo(100, 100, (err, data) => {
              if (err && err.code) {
                return;
              }
              subWindow?.showWindow((err, data) => {
                if (err && err.code) {
                  console.error(`Failed to show the subwindow. Code: ${err.code}, message: ${err.message}`);
                } else {
                  console.info(`The subwindow has been shown!`);
                }
              });
            });
          });
        });
      }).catch((error: BusinessError) => {
      console.error(`Create subwindow failed. Cause code: ${error.code}, message: ${error.message}`);
    });
  }
}
```

## createSubWindowWithOptions

```TypeScript
createSubWindowWithOptions(name: string, subWindowConfig: window.SubWindowOptions,
        followCreatorLifecycle: boolean): Promise<window.Window>
```

创建该WindowProxy实例下的子窗口，可通过设置followCreatorLifecycle，决定子窗是否跟随组件（EmbeddedComponent或UIExtensionComponent）的生命周期，使用 Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WindowProxy-createSubWindowWithOptions(name: string, subWindowConfig: window.SubWindowOptions,        followCreatorLifecycle: boolean): Promise<window.Window>--><!--Device-WindowProxy-createSubWindowWithOptions(name: string, subWindowConfig: window.SubWindowOptions,        followCreatorLifecycle: boolean): Promise<window.Window>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| subWindowConfig | window.SubWindowOptions | 是 |
| followCreatorLifecycle | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;window.Window & gt; |

**错误码：**

| 错误码ID |
| --- |
| 1300035 |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

**示例**

```TypeScript
// ExtensionProvider.ets
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    const subWindowConfig: window.SubWindowOptions = {
      title: 'This is a subwindow',
      decorEnabled: true
    };
    // 创建子窗口
    extensionWindow.createSubWindowWithOptions('subWindowForHost', subWindowConfig, true)
      .then((subWindow: window.Window) => {
        subWindow.setUIContent('pages/Index', (err, data) => {
          if (err && err.code) {
            return;
          }
          subWindow?.resize(300, 300, (err, data) => {
            if (err && err.code) {
              return;
            }
            subWindow?.moveWindowTo(100, 100, (err, data) => {
              if (err && err.code) {
                return;
              }
              subWindow?.showWindow((err, data) => {
                if (err && err.code) {
                  console.error(`Failed to show the subwindow. Code: ${err.code}, message: ${err.message}`);
                } else {
                  console.info(`The subwindow has been shown!`);
                }
              });
            });
          });
        });
      }).catch((error: BusinessError) => {
      console.error(`Create subwindow failed. Cause code: ${error.code}, message: ${error.message}`);
    });
  }
}
```

## getWindowAvoidArea

```TypeScript
getWindowAvoidArea(type: window.AvoidAreaType): window.AvoidArea
```

获取宿主应用窗口内容规避的区域；如系统栏区域、刘海屏区域、手势区域、软键盘区域等与宿主窗口内容重叠时，需要宿主窗口内容避让的区域。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-WindowProxy-getWindowAvoidArea(type: window.AvoidAreaType): window.AvoidArea--><!--Device-WindowProxy-getWindowAvoidArea(type: window.AvoidAreaType): window.AvoidArea-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | window.AvoidAreaType | 是 |

**返回值：**

| 类型 |
| --- |
| window.AvoidArea |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
// ExtensionProvider.ets
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // 获取宿主应用窗口的避让信息
    let avoidArea: window.AvoidArea | undefined = extensionWindow?.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM);
    console.info(`avoidArea: ${JSON.stringify(avoidArea)}`);
  }
}
```

## occupyEvents

```TypeScript
occupyEvents(eventFlags: number): Promise<void>
```

设置组件（EmbeddedComponent或UIExtensionComponent）占用事件，宿主将不响应组件区域内被占用的事件。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-WindowProxy-occupyEvents(eventFlags: int): Promise<void>--><!--Device-WindowProxy-occupyEvents(eventFlags: int): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventFlags | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

**示例**

```TypeScript
// ExtensionProvider.ets
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { uiExtension } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // 占用事件
    setTimeout(() => {
      try {
        extensionWindow.occupyEvents(uiExtension.EventFlag.EVENT_CLICK | uiExtension.EventFlag.EVENT_LONG_PRESS).then(() => {
          console.info(`Succeeded in occupying events`);
        }).catch((err: BusinessError) => {
          console.error(`Failed to occupy events. Cause code: ${err.code}, message: ${err.message}`);
        });
      } catch (err) {
        console.error(`Occupy events got exception code: ${err.code}, message: ${err.message}`);
      }
    }, 500);
  }
}
```

## offAvoidAreaChange

```TypeScript
offAvoidAreaChange(callback?: Callback<AvoidAreaInfo>): void
```

Unsubscribes from the event indicating changes to the area where the window cannot be displayed.

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WindowProxy-offAvoidAreaChange(callback?: Callback<AvoidAreaInfo>): void--><!--Device-WindowProxy-offAvoidAreaChange(callback?: Callback<AvoidAreaInfo>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AvoidAreaInfo](arkts-arkui-uiextension-avoidareainfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offRectChange

```TypeScript
offRectChange(callback?: Callback<RectChangeOptions>): void
```

Unsubscribes from changes in the position and size of the component (EmbeddedComponent or UIExtensionComponent). This API can be used only on 2-in-1 devices.

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WindowProxy-offRectChange(callback?: Callback<RectChangeOptions>): void--><!--Device-WindowProxy-offRectChange(callback?: Callback<RectChangeOptions>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;RectChangeOptions&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offWindowSizeChange

```TypeScript
offWindowSizeChange(callback?: Callback<window.Size>): void
```

Unsubscribes from the component (EmbeddedComponent or UIExtensionComponent) size change event.

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WindowProxy-offWindowSizeChange(callback?: Callback<window.Size>): void--><!--Device-WindowProxy-offWindowSizeChange(callback?: Callback<window.Size>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;window.Size&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## off_avoidAreaChange

```TypeScript
off(type: 'avoidAreaChange', callback?: Callback<AvoidAreaInfo>): void
```

注销系统避让区变化的监听。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WindowProxy-off(type: 'avoidAreaChange', callback?: Callback<AvoidAreaInfo>): void--><!--Device-WindowProxy-off(type: 'avoidAreaChange', callback?: Callback<AvoidAreaInfo>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'avoidAreaChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AvoidAreaInfo](arkts-arkui-uiextension-avoidareainfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

**示例**

```TypeScript
// ExtensionProvider.ets
import { EmbeddedUIExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionDestroy(session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // 注销所有避让区变化的监听
    extensionWindow.off('avoidAreaChange');
  }
}
```

## off_rectChange

```TypeScript
off(type: 'rectChange', callback?: Callback<RectChangeOptions>): void
```

注销组件（EmbeddedComponent或UIExtensionComponent）位置及尺寸变化的监听。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-WindowProxy-off(type: 'rectChange', callback?: Callback<RectChangeOptions>): void--><!--Device-WindowProxy-off(type: 'rectChange', callback?: Callback<RectChangeOptions>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'rectChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;RectChangeOptions&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

**示例**

```TypeScript
// ExtensionProvider.ets
import { EmbeddedUIExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionDestroy(session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // 注销组件（EmbeddedComponent或UIExtensionComponent）位置及尺寸变化的监听
    extensionWindow.off('rectChange');
  }
}
```

## off_windowSizeChange

```TypeScript
off(type: 'windowSizeChange', callback?: Callback<window.Size>): void
```

注销组件（EmbeddedComponent或UIExtensionComponent）尺寸变化的监听。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WindowProxy-off(type: 'windowSizeChange', callback?: Callback<window.Size>): void--><!--Device-WindowProxy-off(type: 'windowSizeChange', callback?: Callback<window.Size>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowSizeChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;window.Size&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

**示例**

```TypeScript
// ExtensionProvider.ets
import { EmbeddedUIExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionDestroy(session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // 注销组件（EmbeddedComponent或UIExtensionComponent）大小变化的监听
    extensionWindow.off('windowSizeChange');
  }
}
```

## onAvoidAreaChange

```TypeScript
onAvoidAreaChange(callback: Callback<AvoidAreaInfo>): void
```

Subscribes to the event indicating changes to the area where the window cannot be displayed.

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WindowProxy-onAvoidAreaChange(callback: Callback<AvoidAreaInfo>): void--><!--Device-WindowProxy-onAvoidAreaChange(callback: Callback<AvoidAreaInfo>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AvoidAreaInfo](arkts-arkui-uiextension-avoidareainfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onRectChange

```TypeScript
onRectChange(reasons: number, callback: Callback<RectChangeOptions>): void
```

Subscribes to changes in the position and size of the component (EmbeddedComponent or UIExtensionComponent). This API can be used only on 2-in-1 devices.

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WindowProxy-onRectChange(reasons: int, callback: Callback<RectChangeOptions>): void--><!--Device-WindowProxy-onRectChange(reasons: int, callback: Callback<RectChangeOptions>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reasons | number | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;RectChangeOptions&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onWindowSizeChange

```TypeScript
onWindowSizeChange(callback: Callback<window.Size>): void
```

Subscribes to the component (EmbeddedComponent or UIExtensionComponent) size change event.

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WindowProxy-onWindowSizeChange(callback: Callback<window.Size>): void--><!--Device-WindowProxy-onWindowSizeChange(callback: Callback<window.Size>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;window.Size&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## on_avoidAreaChange

```TypeScript
on(type: 'avoidAreaChange', callback: Callback<AvoidAreaInfo>): void
```

注册系统避让区变化的监听。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WindowProxy-on(type: 'avoidAreaChange', callback: Callback<AvoidAreaInfo>): void--><!--Device-WindowProxy-on(type: 'avoidAreaChange', callback: Callback<AvoidAreaInfo>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'avoidAreaChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AvoidAreaInfo](arkts-arkui-uiextension-avoidareainfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

**示例**

```TypeScript
// ExtensionProvider.ets
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { uiExtension } from '@kit.ArkUI';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // 注册避让区变化的监听
    extensionWindow.on('avoidAreaChange', (info: uiExtension.AvoidAreaInfo) => {
      console.info(`The avoid area of the host window is: ${JSON.stringify(info.area)}.`);
    });
  }
}
```

## on_rectChange

```TypeScript
on(type: 'rectChange', reasons: number, callback: Callback<RectChangeOptions>): void
```

注册组件（EmbeddedComponent或UIExtensionComponent）位置及尺寸变化的监听。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-WindowProxy-on(type: 'rectChange', reasons: number, callback: Callback<RectChangeOptions>): void--><!--Device-WindowProxy-on(type: 'rectChange', reasons: number, callback: Callback<RectChangeOptions>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'rectChange' | 是 |
| reasons | number | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;RectChangeOptions&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

**示例**

```TypeScript
// ExtensionProvider.ets
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { uiExtension } from '@kit.ArkUI';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // 注册组件（EmbeddedComponent或UIExtensionComponent）位置及尺寸变化的监听
    extensionWindow.on('rectChange', uiExtension.RectChangeReason.HOST_WINDOW_RECT_CHANGE, (data: uiExtension.RectChangeOptions) => {
        console.info('Succeeded window rect changes. Data: ' + JSON.stringify(data));
    });
  }
}
```

## on_windowSizeChange

```TypeScript
on(type: 'windowSizeChange', callback: Callback<window.Size>): void
```

注册组件（EmbeddedComponent或UIExtensionComponent）尺寸变化的监听。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WindowProxy-on(type: 'windowSizeChange', callback: Callback<window.Size>): void--><!--Device-WindowProxy-on(type: 'windowSizeChange', callback: Callback<window.Size>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowSizeChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;window.Size&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

**示例**

```TypeScript
// ExtensionProvider.ets
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // 注册组件（EmbeddedComponent或UIExtensionComponent）大小变化的监听
    extensionWindow.on('windowSizeChange', (size: window.Size) => {
      console.info(`The size of the component is: ${JSON.stringify(size)}.`);
    });
  }
}
```

## properties

```TypeScript
properties: WindowProxyProperties
```

组件（EmbeddedComponent或UIExtensionComponent）的信息。 **约束：** 由于架构约束，不建议在 [onSessionCreate](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#onsessioncreate)阶段同步获取该值，建议在收到 [on('windowSizeChange')](#onavoidareachange) 回调之后获取。

**类型：** [WindowProxyProperties](arkts-arkui-uiextension-windowproxyproperties-i.md)

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-WindowProxy-properties: WindowProxyProperties--><!--Device-WindowProxy-properties: WindowProxyProperties-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
