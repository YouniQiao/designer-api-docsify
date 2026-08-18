# UIExtensionHostWindowProxy (System API)

Transition Controller

**Since:** 23

<!--Device-uiExtensionHost-interface UIExtensionHostWindowProxy--><!--Device-uiExtensionHost-interface UIExtensionHostWindowProxy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## createSubWindowWithOptions

```TypeScript
createSubWindowWithOptions(name: string, subWindowOptions: window.SubWindowOptions): Promise<window.Window>
```

Creates a subwindow for this **UIExtensionHostWindowProxy** instance. This API uses a promise to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionHostWindowProxy-createSubWindowWithOptions(name: string, subWindowOptions: window.SubWindowOptions): Promise<window.Window>--><!--Device-UIExtensionHostWindowProxy-createSubWindowWithOptions(name: string, subWindowOptions: window.SubWindowOptions): Promise<window.Window>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| [subWindowOptions](arkts-arkui-window-extensionwindowconfig-i-sys.md) | window.SubWindowOptions | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;window.Window & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 1300035 |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

**Examples**

```TypeScript
// ExtensionProvider.ets
import { UIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionHostWindow = session.getUIExtensionHostWindowProxy();
    const subWindowOpts: window.SubWindowOptions = {
      title: 'This is a subwindow',
      decorEnabled: true
    };
    // Create a subwindow.
    extensionHostWindow.createSubWindowWithOptions('subWindowForHost', subWindowOpts)
      .then((subWindow: window.Window) => {
        subWindow.setUIContent('pages/Index', (err, data) =>{
          if (err && err.code != 0) {
            return;
          }
          subWindow?.resize(300, 300, (err, data)=>{
            if (err && err.code != 0) {
              return;
            }
            subWindow?.moveWindowTo(100, 100, (err, data)=>{
              if (err && err.code != 0) {
                return;
              }
              subWindow?.showWindow((err, data) => {
                if (err && err.code == 0) {
                  console.info(`The subwindow has been shown!`);
                } else {
                  console.error(`Failed to show the subwindow!`);
                }
              });
            });
          });
        });
      }).catch((error: BusinessError) => {
        console.error(`Create subwindow failed: ${JSON.stringify(error)}`);
      })
  }
}
```

## createSubWindowWithOptions

```TypeScript
createSubWindowWithOptions(name: string, subWindowConfig: window.SubWindowOptions,
        followCreatorLifecycle: boolean): Promise<window.Window>
```

Create subwindow.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionHostWindowProxy-createSubWindowWithOptions(name: string, subWindowConfig: window.SubWindowOptions,        followCreatorLifecycle: boolean): Promise<window.Window>--><!--Device-UIExtensionHostWindowProxy-createSubWindowWithOptions(name: string, subWindowConfig: window.SubWindowOptions,        followCreatorLifecycle: boolean): Promise<window.Window>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| subWindowConfig | window.SubWindowOptions | Yes |
| followCreatorLifecycle | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;window.Window & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 1300035 |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

**Examples**

```TypeScript
// ExtensionProvider.ets
import { UIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionHostWindow = session.getUIExtensionHostWindowProxy();
    const subWindowConfig: window.SubWindowOptions = {
      title: 'This is a subwindow',
      decorEnabled: true
    };
    // Create a subwindow.
    extensionHostWindow.createSubWindowWithOptions('subWindowForHost', subWindowConfig, true)
      .then((subWindow: window.Window) => {
        subWindow.setUIContent('pages/Index', (err, data) =>{
          if (err && err.code != 0) {
            return;
          }
          subWindow?.resize(300, 300, (err, data)=>{
            if (err && err.code != 0) {
              return;
            }
            subWindow?.moveWindowTo(100, 100, (err, data)=>{
              if (err && err.code != 0) {
                return;
              }
              subWindow?.showWindow((err, data) => {
                if (err && err.code == 0) {
                  console.info(`The subwindow has been shown!`);
                } else {
                  console.error(`Failed to show the subwindow!`);
                }
              });
            });
          });
        });
      }).catch((error: BusinessError) => {
        console.error(`Create subwindow failed: ${JSON.stringify(error)}`);
      })
  }
}
```

## getWindowAvoidArea

```TypeScript
getWindowAvoidArea(type: window.AvoidAreaType): window.AvoidArea
```

Obtains the area where this window cannot be displayed, for example, the system bar area, notch, gesture area, and soft keyboard area.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionHostWindowProxy-getWindowAvoidArea(type: window.AvoidAreaType): window.AvoidArea--><!--Device-UIExtensionHostWindowProxy-getWindowAvoidArea(type: window.AvoidAreaType): window.AvoidArea-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | window.AvoidAreaType | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| window.AvoidArea |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

**Examples**

```TypeScript
// ExtensionProvider.ets

import { UIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionHostWindow = session.getUIExtensionHostWindowProxy();
    // Obtain the information about the area where the window cannot be displayed.
    const avoidArea = extensionHostWindow.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM);
    console.info(`avoidArea: ${JSON.stringify(avoidArea)}`);
  }
}
```

## hideNonSecureWindows

```TypeScript
hideNonSecureWindows(shouldHide: boolean): Promise<void>
```

Sets whether to hide non-secure windows. This API uses a promise to return the result. > **NOTE：**> > - A non-secure window refers to any window that may obstruct the > EmbeddedComponent or > UIExtensionComponent, such as global floating windows > , host subwindows, and dialog box windows created by the host application (excluding windows of these types > created by system applications). > > - When using the **EmbeddedComponent** or **UIExtensionComponent** to display sensitive information, call this > API to hide non-secure windows and prevent information obstruction. Hidden non-secure windows will reappear > when the **EmbeddedComponent** or **UIExtensionComponent** is hidden or destroyed. > > - On PCs/2-in-1 devices, global floating windows within non-secure windows remain visible when > **hideNonSecureWindows(true)** is called.

**Since:** 23

**Required permissions:** 
- API version 12+: ohos.permission.ALLOW_SHOW_NON_SECURE_WINDOWS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionHostWindowProxy-hideNonSecureWindows(shouldHide: boolean): Promise<void>--><!--Device-UIExtensionHostWindowProxy-hideNonSecureWindows(shouldHide: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| shouldHide | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
// ExtensionProvider.ets

import { UIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionHostWindow = session.getUIExtensionHostWindowProxy();
    // Hide insecure windows.
    extensionHostWindow.hideNonSecureWindows(true).then(()=> {
      console.info(`Succeeded in hiding the non-secure windows.`);
    }).catch((err: BusinessError)=> {
      console.error(`Failed to hide the non-secure windows. Cause:${JSON.stringify(err)}`);
    })
  }
  onSessionDestroy(session: UIExtensionContentSession) {
    const extensionHostWindow = session.getUIExtensionHostWindowProxy();
    // Unhide insecure windows.
    extensionHostWindow.hideNonSecureWindows(false).then(()=> {
      console.info(`Succeeded in showing the non-secure windows.`);
    }).catch((err: BusinessError)=> {
      console.error(`Failed to show the non-secure windows. Cause:${JSON.stringify(err)}`);
    })
  }
}
```

## hidePrivacyContentForHost

```TypeScript
hidePrivacyContentForHost(shouldHide: boolean): Promise<void>
```

Sets whether to enable privacy protection for the UIExtension component during non-system screenshots. This API uses a promise to return the result. > **NOTE：**> > When privacy protection is enabled, neither > window.snapshot nor > [UIContext.getComponentSnapshot](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getcomponentsnapshot) > will capture the content of the current component (excluding subwindows created under this component).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionHostWindowProxy-hidePrivacyContentForHost(shouldHide: boolean): Promise<void>--><!--Device-UIExtensionHostWindowProxy-hidePrivacyContentForHost(shouldHide: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| shouldHide | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
// ExtensionProvider.ets
import { UIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionHostWindow = session.getUIExtensionHostWindowProxy();
    // Enable privacy protection for screenshots.
    extensionHostWindow.hidePrivacyContentForHost(true).then(() => {
      console.info(`Successfully enabled privacy protection for non-system screenshots.`);
    }).catch((err: BusinessError) => {
      console.error(`Failed enabled privacy protection for non-system screenshots. Cause:${JSON.stringify(err)}`);
    })
  }
}
```

## offAvoidAreaChange

```TypeScript
offAvoidAreaChange(callback?: Callback<uiExtension.AvoidAreaInfo>): void
```

Unregister the callback of avoidAreaChange

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionHostWindowProxy-offAvoidAreaChange(callback?: Callback<uiExtension.AvoidAreaInfo>): void--><!--Device-UIExtensionHostWindowProxy-offAvoidAreaChange(callback?: Callback<uiExtension.AvoidAreaInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;uiExtension.AvoidAreaInfo&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offWindowSizeChange

```TypeScript
offWindowSizeChange(callback?: Callback<window.Size>): void
```

Unsubscribes from the component (EmbeddedComponent or UIExtensionComponent) size change event.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionHostWindowProxy-offWindowSizeChange(callback?: Callback<window.Size>): void--><!--Device-UIExtensionHostWindowProxy-offWindowSizeChange(callback?: Callback<window.Size>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;window.Size&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## off_avoidAreaChange

```TypeScript
off(type: 'avoidAreaChange', callback?: Callback<{ type: window.AvoidAreaType, area: window.AvoidArea }>): void
```

Unsubscribes from events of system avoidance area changes.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionHostWindowProxy-off(type: 'avoidAreaChange', callback?: Callback<{ type: window.AvoidAreaType, area: window.AvoidArea }>): void--><!--Device-UIExtensionHostWindowProxy-off(type: 'avoidAreaChange', callback?: Callback<{ type: window.AvoidAreaType, area: window.AvoidArea }>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'avoidAreaChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ type: window.AvoidAreaType, area: window.AvoidArea }&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

**Examples**

```TypeScript
// ExtensionProvider.ets
import { UIExtensionAbility, UIExtensionContentSession} from '@kit.AbilityKit';

export default class EntryAbility extends UIExtensionAbility {
  onSessionDestroy(session: UIExtensionContentSession) {
    const extensionHostWindow = session.getUIExtensionHostWindowProxy();
    // Cancel all subscriptions to the event indicating changes to the area where the window cannot be displayed.
    extensionHostWindow.off('avoidAreaChange');
  }
}
```

## off_windowSizeChange

```TypeScript
off(type: 'windowSizeChange', callback?: Callback<window.Size>): void
```

Unsubscribes from size change events of the component (**EmbeddedComponent** or **UIExtensionComponent**).

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionHostWindowProxy-off(type: 'windowSizeChange', callback?: Callback<window.Size>): void--><!--Device-UIExtensionHostWindowProxy-off(type: 'windowSizeChange', callback?: Callback<window.Size>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowSizeChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;window.Size&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

**Examples**

```TypeScript
// ExtensionProvider.ets
import { UIExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';

export default class EntryAbility extends UIExtensionAbility {
  onSessionDestroy(session: UIExtensionContentSession) {
    const extensionHostWindow = session.getUIExtensionHostWindowProxy();
    // Unsubscribe from size change events of the component (EmbeddedComponent or UIExtensionComponent).
    extensionHostWindow.off('windowSizeChange');
  }
}
```

## onAvoidAreaChange

```TypeScript
onAvoidAreaChange(callback: Callback<uiExtension.AvoidAreaInfo>): void
```

Register the callback of avoidAreaChange

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionHostWindowProxy-onAvoidAreaChange(callback: Callback<uiExtension.AvoidAreaInfo>): void--><!--Device-UIExtensionHostWindowProxy-onAvoidAreaChange(callback: Callback<uiExtension.AvoidAreaInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;uiExtension.AvoidAreaInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## onWindowSizeChange

```TypeScript
onWindowSizeChange(callback: Callback<window.Size>): void
```

Subscribes to the component (EmbeddedComponent or UIExtensionComponent) size change event.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionHostWindowProxy-onWindowSizeChange(callback: Callback<window.Size>): void--><!--Device-UIExtensionHostWindowProxy-onWindowSizeChange(callback: Callback<window.Size>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;window.Size&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## on_avoidAreaChange

```TypeScript
on(type: 'avoidAreaChange', callback: Callback<{ type: window.AvoidAreaType, area: window.AvoidArea }>): void
```

Subscribes to events of system avoidance area changes.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionHostWindowProxy-on(type: 'avoidAreaChange', callback: Callback<{ type: window.AvoidAreaType, area: window.AvoidArea }>): void--><!--Device-UIExtensionHostWindowProxy-on(type: 'avoidAreaChange', callback: Callback<{ type: window.AvoidAreaType, area: window.AvoidArea }>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'avoidAreaChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ type: window.AvoidAreaType, area: window.AvoidArea }&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

**Examples**

```TypeScript
// ExtensionProvider.ets
import { UIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionHostWindow = session.getUIExtensionHostWindowProxy();
    // Subscribe to the event indicating changes to the area where the window cannot be displayed.
    extensionHostWindow.on('avoidAreaChange', (info) => {
      console.info(`The avoid area of the host window is: ${JSON.stringify(info.area)}.`);
    });
  }
}
```

## on_windowSizeChange

```TypeScript
on(type: 'windowSizeChange', callback: Callback<window.Size>): void
```

Subscribes to size change events of the component (**EmbeddedComponent** or **UIExtensionComponent**).

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionHostWindowProxy-on(type: 'windowSizeChange', callback: Callback<window.Size>): void--><!--Device-UIExtensionHostWindowProxy-on(type: 'windowSizeChange', callback: Callback<window.Size>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowSizeChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;window.Size&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

**Examples**

```TypeScript
// ExtensionProvider.ets
import { UIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionHostWindow = session.getUIExtensionHostWindowProxy();
    // Subscribe to size change events of the component (EmbeddedComponent or UIExtensionComponent).
    extensionHostWindow.on('windowSizeChange', (size) => {
      console.info(`The size of the component is: ${JSON.stringify(size)}.`);
    });
  }
}
```

## setWaterMarkFlag

```TypeScript
setWaterMarkFlag(enable: boolean): Promise<void>
```

Adds or deletes the watermark flag for this window. This API uses a promise to return the result. > **NOTE：**> > With the watermark flag added, the watermark is applied on the full screen when the window is in the foreground > , regardless of whether the window is displayed in full screen, floating, and split screen mode.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionHostWindowProxy-setWaterMarkFlag(enable: boolean): Promise<void>--><!--Device-UIExtensionHostWindowProxy-setWaterMarkFlag(enable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300008](../errorcode-window.md#1300008-display-device-exception) |

**Examples**

```TypeScript
// ExtensionProvider.ets
import { UIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionHostWindow = session.getUIExtensionHostWindowProxy();
    // Add the watermark flag.
    extensionHostWindow.setWaterMarkFlag(true).then(() => {
      console.info(`Succeeded in setting water mark flag of window.`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to setting water mark flag of window. Cause:${JSON.stringify(err)}`);
    })
  }
  onSessionDestroy(session: UIExtensionContentSession) {
    const extensionHostWindow = session.getUIExtensionHostWindowProxy();
    // Delete the watermark flag.
    extensionHostWindow.setWaterMarkFlag(false).then(() => {
      console.info(`Succeeded in deleting water mark flag of window.`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to deleting water mark flag of window. Cause:${JSON.stringify(err)}`);
    })
  }
}
```

## properties

```TypeScript
properties: UIExtensionHostWindowProxyProperties
```

Information about the host application window and the **UIExtensionComponent**. Note: Due to architecture restrictions, avoid obtaining the value in [onSessionCreate](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#onsessioncreate). Instead, when possible, obtain the value after receiving the [on('windowSizeChange')](#onavoidareachange) callback.

**Type:** [UIExtensionHostWindowProxyProperties](arkts-arkui-uiextensionhost-uiextensionhostwindowproxyproperties-i-sys.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionHostWindowProxy-properties: UIExtensionHostWindowProxyProperties--><!--Device-UIExtensionHostWindowProxy-properties: UIExtensionHostWindowProxyProperties-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.
