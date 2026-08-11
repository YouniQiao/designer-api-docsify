# Panel

In the following API examples, you must first use   
[createPanel](arkts-ime-inputmethodengine-inputmethodability-i.md#createpanel)to obtain a **Panel** instance, and then call the APIs using the obtained instance.

**Since:** 10

<!--Device-inputMethodEngine-interface Panel--><!--Device-inputMethodEngine-interface Panel-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from 'kits/@kit.IMEKit';
```

## adjustPanelRect

```TypeScript
adjustPanelRect(flag: PanelFlag, rect: PanelRect): void
```

Adjusts the panel rectangle. After the API is called, the adjust request is submitted to the input method framework, but the execution is not complete.

> **NOTE：**
> 
> This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING**
> state.
> 
> This API returns the result synchronously. The return only indicates that the system receives the setting
> request, not that the setting is complete.
> 
> When the **PanelFlag** of a smartphone is **FLG_FLOATING** and the panel width is between 0 and 288 vp, the
> function buttons at the bottom of the panel will dynamically adjust their size according to the panel width. To
> ensure the optimal user experience, it is recommended that the panel width be no less than 90 vp.

**Since:** 12

<!--Device-Panel-adjustPanelRect(flag: PanelFlag, rect: PanelRect): void--><!--Device-Panel-adjustPanelRect(flag: PanelFlag, rect: PanelRect): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| flag | [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md) | Yes |
| rect | [PanelRect](arkts-ime-inputmethodengine-panelrect-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-window-manager-service-error) |

## Examples

```TypeScript
import { window } from '@kit.ArkUI';

let landscapeRect: window.Rect = {
  left: 100,
  top: 100,
  width: 400,
  height: 400
};

let portraitRect: window.Rect = {
  left: 200,
  top: 200,
  width: 300,
  height: 300
};

// Target panel status type.
let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG_FIXED;
// X-coordinate, Y-coordinate, width, and height of the target panel in both landscape and portrait orientations.
let panelRect: inputMethodEngine.PanelRect = {
  landscapeRect: landscapeRect,
  portraitRect: portraitRect
};
panel.adjustPanelRect(panelFlag, panelRect);
```

## adjustPanelRect

```TypeScript
adjustPanelRect(flag: PanelFlag, rect: EnhancedPanelRect): void
```

Adjusts the panel rectangle, and customizes the avoid area and touch area.

> **NOTE：**
> 
> This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING**
> state. This API is compatible with
> [adjustPanelRect](arkts-ime-inputmethodengine-panel-i.md#adjustpanelrect). If the
> input parameter **rect** contains only the **landscapeRect** and **portraitRect** attributes,
> [adjustPanelRect](arkts-ime-inputmethodengine-panel-i.md#adjustpanelrect) is called by
> default.
> 
> This API returns the result synchronously. The return only indicates that the system receives the setting
> request, not that the setting is complete.
> 
> When the **PanelFlag** of a smartphone is **FLG_FLOATING** and the panel width is between 0 and 288 vp, the
> function buttons at the bottom of the panel will dynamically adjust their size according to the panel width. To
> ensure the optimal user experience, it is recommended that the panel width be no less than 90 vp.

**Since:** 15

<!--Device-Panel-adjustPanelRect(flag: PanelFlag, rect: EnhancedPanelRect): void--><!--Device-Panel-adjustPanelRect(flag: PanelFlag, rect: EnhancedPanelRect): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| flag | [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md) | Yes |
| rect | [EnhancedPanelRect](arkts-ime-inputmethodengine-enhancedpanelrect-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800017](../errorcode-inputmethod-framework.md#12800017-invalid-panel-type-or-panel-flag) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-window-manager-service-error) |

## Examples

```TypeScript
import { window } from '@kit.ArkUI';

let landscapeRect1: window.Rect = {
  left: 300,
  top: 650,
  width: 2000,
  height: 500
};
let landscapeInputRegion: Array<window.Rect> = [landscapeRect1];

let portraitRect1: window.Rect = {
  left: 0,
  top: 1800,
  width: 1200,
  height: 800
}
let portraitInputRegion: Array<window.Rect> = [portraitRect1];
// Target panel status type.
let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG_FIXED;
// Location, size, avoid area, and hot zone of the target panel in both landscape and portrait orientations.
let panelRect: inputMethodEngine.EnhancedPanelRect = {
  landscapeAvoidY: 650,
  landscapeInputRegion: landscapeInputRegion,
  portraitAvoidY: 1800,
  portraitInputRegion: portraitInputRegion,
  fullScreenMode: true
};
panel.adjustPanelRect(panelFlag, panelRect);
```

## changeFlag

```TypeScript
changeFlag(flag: PanelFlag): void
```

Changes the state type ([PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md)) of this input method panel. This API only works for [SOFT_KEYBOARD](arkts-ime-inputmethodengine-paneltype-e.md) panels.

**Since:** 10

<!--Device-Panel-changeFlag(flag: PanelFlag): void--><!--Device-Panel-changeFlag(flag: PanelFlag): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| flag | [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG_FIXED;
panel.changeFlag(panelFlag);
```

## getDisplayId

```TypeScript
getDisplayId(): Promise<number>
```

Obtains the window ID. This API uses a promise to return the result.

**Since:** 15

<!--Device-Panel-getDisplayId(): Promise<long>--><!--Device-Panel-getDisplayId(): Promise<long>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-window-manager-service-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

panel.getDisplayId().then((result: number) => {
  console.info('get displayId:' + result);
}).catch((err: BusinessError) => {
  console.error(`Failed to get displayId. Code is ${err.code}, message is ${err.message}`);
});
```

## getImmersiveMode

```TypeScript
getImmersiveMode(): ImmersiveMode
```

Obtains the immersive mode of the input method application.

**Since:** 15

<!--Device-Panel-getImmersiveMode(): ImmersiveMode--><!--Device-Panel-getImmersiveMode(): ImmersiveMode-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImmersiveMode](../../apis-arkui/arkts-apis/arkts-arkui-immersivemode-t.md) |

## Examples

```TypeScript
let mode: inputMethodEngine.ImmersiveMode = panel.getImmersiveMode();
```

## getSystemPanelCurrentInsets

```TypeScript
getSystemPanelCurrentInsets(displayId: number): Promise<SystemPanelInsets>
```

Obtains the offset area of the soft keyboard relative to the system panel under the current state of the specified screen (for example, folded or unfolded) and the current state of the input method keyboard (for example, floating or fixed). This API uses a promise to return the result.

**Since:** 21

<!--Device-Panel-getSystemPanelCurrentInsets(displayId: number): Promise<SystemPanelInsets>--><!--Device-Panel-getSystemPanelCurrentInsets(displayId: number): Promise<SystemPanelInsets>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;SystemPanelInsets&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800017](../errorcode-inputmethod-framework.md#12800017-invalid-panel-type-or-panel-flag) |
| [12800022](../errorcode-inputmethod-framework.md#12800022-invalid-displayid) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-window-manager-service-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { inputMethodEngine } from '@kit.IMEKit';

let inputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
let panelConfig: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG_FIXED
}
// The following logic needs to be executed in InputMethodExtensionAbility. this.context is the context of InputMethodExtensionAbility.
inputMethodAbility.createPanel(this.context, panelConfig).then( (panel: inputMethodEngine.Panel) =>{
  panel.getDisplayId().then((displayId: number) => {
    panel.getSystemPanelCurrentInsets(displayId).then((insets: inputMethodEngine.SystemPanelInsets) => {
      console.info(`getSystemPanelCurrentInsets success, insets is { left: ${insets.left}, right: ${insets.right}, bottom: ${insets.bottom} }`);
    }).catch((error: BusinessError) => {
      console.error(`getSystemPanelCurrentInsets failed, code: ${error.code}, message: ${error.message}`);
    })
  });
})
```

## hide

```TypeScript
hide(callback: AsyncCallback<void>): void
```

Hides this panel. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-Panel-hide(callback: AsyncCallback<void>): void--><!--Device-Panel-hide(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

panel.hide((err: BusinessError) => {
  if (err) {
    console.error(`Failed to hide panel. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in hiding the panel.');
});
```

## hide

```TypeScript
hide(): Promise<void>
```

Hides this panel. This API uses a promise to return the result.

**Since:** 10

<!--Device-Panel-hide(): Promise<void>--><!--Device-Panel-hide(): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

panel.hide().then(() => {
  console.info('Succeeded in hiding the panel.');
}).catch((err: BusinessError) => {
  console.error(`Failed to hide panel. Code is ${err.code}, message is ${err.message}`);
});
```

## moveTo

```TypeScript
moveTo(x: number, y: number, callback: AsyncCallback<void>): void
```

Moves this input method panel to the specified position. This API uses an asynchronous callback to return the result. This API does not work on panels in the [FLG_FIXED](arkts-ime-inputmethodengine-panelflag-e.md) state.

**Since:** 10

<!--Device-Panel-moveTo(x: int, y: int, callback: AsyncCallback<void>): void--><!--Device-Panel-moveTo(x: int, y: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

panel.moveTo(300, 300, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to move panel. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in moving the panel.');
});
```

## moveTo

```TypeScript
moveTo(x: number, y: number): Promise<void>
```

Moves this input method panel to the specified position. This API uses a promise to return the result. This API does not work on panels in the [FLG_FIXED](arkts-ime-inputmethodengine-panelflag-e.md) state.

**Since:** 10

<!--Device-Panel-moveTo(x: int, y: int): Promise<void>--><!--Device-Panel-moveTo(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

panel.moveTo(300, 300).then(() => {
  console.info('Succeeded in moving the panel.');
}).catch((err: BusinessError) => {
  console.error(`Failed to move panel. Code is ${err.code}, message is ${err.message}`);
});
```

## off('show')

```TypeScript
off(type: 'show', callback?: () => void): void
```

Disables listening for the show event of this panel. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-Panel-off(type: 'show', callback?: () => void): void--><!--Device-Panel-off(type: 'show', callback?: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'show' | Yes |
| callback | () =&gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
panel.off('show');
```

## off('hide')

```TypeScript
off(type: 'hide', callback?: () => void): void
```

Disables listening for the hide event of this panel. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-Panel-off(type: 'hide', callback?: () => void): void--><!--Device-Panel-off(type: 'hide', callback?: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'hide' | Yes |
| callback | () =&gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
panel.off('hide');
```

## off('sizeChange')

```TypeScript
off(type: 'sizeChange', callback?: SizeChangeCallback): void
```

Disables listening for the panel size change. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING**
> state. When you call **adjustPanelRect** to adjust the panel size, the system calculates the final value based
> on certain rules (for example, whether the panel size exceeds the screen). This callback can be used to obtain
> the actual panel size to refresh the panel layout.
> 
> - This API is supported from API version 12 to 14. The callback function of this API contains only mandatory
> parameters of the [window.Size](../../apis-arkui/arkts-apis/arkts-arkui-window-size-i.md/arkts-arkui-window-size-i.md) type.
> 
> - Since API version 15, after the
> [adjustPanelRect](arkts-ime-inputmethodengine-panel-i.md#adjustpanelrect) API
> is called, an optional parameter of the [KeyboardArea](arkts-ime-inputmethodengine-keyboardarea-i.md) type is added to
> the callback function of this API.

**Since:** 12

<!--Device-Panel-off(type: 'sizeChange', callback?: SizeChangeCallback): void--><!--Device-Panel-off(type: 'sizeChange', callback?: SizeChangeCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'sizeChange' | Yes |
| callback | [SizeChangeCallback](../../apis-arkui/arkts-components/arkts-arkui-sizechangecallback-t.md) | No |

## Examples

```TypeScript
import { window } from '@kit.ArkUI';

panel.off('sizeChange', (windowSize: window.Size) => {
  console.info(`panel size changed, width: ${windowSize.width}, height: ${windowSize.height}`);
});
```

## on('show')

```TypeScript
on(type: 'show', callback: () => void): void
```

Enables listening for the show event of this panel. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-Panel-on(type: 'show', callback: () => void): void--><!--Device-Panel-on(type: 'show', callback: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'show' | Yes |
| callback | () =&gt; void | Yes |

## Examples

```TypeScript
panel.on('show', () => {
  console.info('Panel is showing.');
});
```

## on('hide')

```TypeScript
on(type: 'hide', callback: () => void): void
```

Enables listening for the hide event of this panel. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-Panel-on(type: 'hide', callback: () => void): void--><!--Device-Panel-on(type: 'hide', callback: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'hide' | Yes |
| callback | () =&gt; void | Yes |

## Examples

```TypeScript
panel.on('hide', () => {
  console.info('Panel is hiding.');
});
```

## on('sizeChange')

```TypeScript
on(type: 'sizeChange', callback: SizeChangeCallback): void
```

Enables listening for the panel size change. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING**
> state. When you call **adjustPanelRect** to adjust the panel size, the system calculates the final value based
> on certain rules (for example, whether the panel size exceeds the screen). This callback can be used to obtain
> the actual panel size to refresh the panel layout.
> 
> - This API is supported from API version 12 to 14. The callback function of this API contains only mandatory
> parameters of the [window.Size](../../apis-arkui/arkts-apis/arkts-arkui-window-size-i.md/arkts-arkui-window-size-i.md) type.
> 
> - Since API version 15, after the
> [adjustPanelRect](arkts-ime-inputmethodengine-panel-i.md#adjustpanelrect) API
> is called, an optional parameter of the [KeyboardArea](arkts-ime-inputmethodengine-keyboardarea-i.md) type is added to
> the callback function of this API.

**Since:** 12

<!--Device-Panel-on(type: 'sizeChange', callback: SizeChangeCallback): void--><!--Device-Panel-on(type: 'sizeChange', callback: SizeChangeCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'sizeChange' | Yes |
| callback | [SizeChangeCallback](../../apis-arkui/arkts-components/arkts-arkui-sizechangecallback-t.md) | Yes |

## Examples

```TypeScript
import { window } from '@kit.ArkUI';

panel.on('sizeChange', (windowSize: window.Size) => {
  console.info(`panel size changed, width: ${windowSize.width}, height: ${windowSize.height}`);
});

panel.on('sizeChange', (windowSize: window.Size, keyboardArea: inputMethodEngine.KeyboardArea) => {
  console.info(`panel size changed, windowSize: ${windowSize.width}, ${windowSize.height}, ` +
    `keyboardArea: ${keyboardArea.top}, ${keyboardArea.bottom}, ${keyboardArea.left}, ${keyboardArea.right}`);
});
```

## resize

```TypeScript
resize(width: number, height: number, callback: AsyncCallback<void>): void
```

Resizes this input method panel. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> The panel width cannot exceed the screen width, and the panel height cannot be 0.7 times higher than the screen
> height.
> 
> When the **PanelFlag** of a smartphone is **FLG_FLOATING** and the panel width is between 0 and 288 vp, the
> function buttons at the bottom of the panel will dynamically adjust their size according to the panel width. To
> ensure the optimal user experience, it is recommended that the panel width be no less than 90 vp.

**Since:** 10

<!--Device-Panel-resize(width: long, height: long, callback: AsyncCallback<void>): void--><!--Device-Panel-resize(width: long, height: long, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | number | Yes |
| height | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

panel.resize(500, 1000, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to resize panel. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in changing the panel size.');
});
```

## resize

```TypeScript
resize(width: number, height: number): Promise<void>
```

Resizes this input method panel. This API uses a promise to return the result.

> **NOTE：**
> 
> The panel width cannot exceed the screen width, and the panel height cannot be 0.7 times higher than the screen
> height.
> 
> When the **PanelFlag** of a smartphone is **FLG_FLOATING** and the panel width is between 0 and 288 vp, the
> function buttons at the bottom of the panel will dynamically adjust their size according to the panel width. To
> ensure the optimal user experience, it is recommended that the panel width be no less than 90 vp.

**Since:** 10

<!--Device-Panel-resize(width: long, height: long): Promise<void>--><!--Device-Panel-resize(width: long, height: long): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | number | Yes |
| height | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

panel.resize(500, 1000).then(() => {
  console.info('Succeeded in changing the panel size.');
}).catch((err: BusinessError) => {
  console.error(`Failed to resize panel. Code is ${err.code}, message is ${err.message}`);
});
```

## setImmersiveEffect

```TypeScript
setImmersiveEffect(effect: ImmersiveEffect): void
```

Sets the immersive effect of the input method application.

- Gradient mode and fluid light mode can be used only when the   
[immersive mode](arkts-ime-inputmethodengine-panel-i.md#setimmersivemode) is enabled.  
- The fluid light mode can be used only when the gradient mode is enabled.  
- If the gradient mode is disabled, the gradient height must be 0 px.  
- Only system applications can set the fluid light mode.  
- The current API can be called only after any of the following APIs is called:  
 - [adjustPanelRect](arkts-ime-inputmethodengine-panel-i.md#adjustpanelrect) (available   
since API version 12)  
 - [adjustPanelRect](arkts-ime-inputmethodengine-panel-i.md#adjustpanelrect) (  
available since API version 15)  
 - [resize](arkts-ime-inputmethodengine-panel-i.md#resize) (  
available since API version 10)

**Since:** 20

<!--Device-Panel-setImmersiveEffect(effect: ImmersiveEffect): void--><!--Device-Panel-setImmersiveEffect(effect: ImmersiveEffect): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| effect | [ImmersiveEffect](arkts-ime-inputmethodengine-immersiveeffect-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |
| [12800021](../errorcode-inputmethod-framework.md#12800021-unsupported-operation-by-default-input-method) |
| [12800020](../errorcode-inputmethod-framework.md#12800020-invalid-immersive-effect) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-window-manager-service-error) |

## Examples

```TypeScript
let effect: inputMethodEngine.ImmersiveEffect = {
  gradientHeight: 100,
  gradientMode: inputMethodEngine.GradientMode.LINEAR_GRADIENT
}
panel.setImmersiveEffect(effect);
```

## setImmersiveMode

```TypeScript
setImmersiveMode(mode: ImmersiveMode): void
```

Sets the immersive mode of the input method application. You can only set the immersion mode to   
**NONE_IMMERSIVE**, **LIGHT_IMMERSIVE**, or **DARK_IMMERSIVE**. **IMMERSIVE** cannot be set.

**Since:** 15

<!--Device-Panel-setImmersiveMode(mode: ImmersiveMode): void--><!--Device-Panel-setImmersiveMode(mode: ImmersiveMode): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [ImmersiveMode](../../apis-arkui/arkts-apis/arkts-arkui-immersivemode-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-window-manager-service-error) |

## Examples

```TypeScript
panel.setImmersiveMode(inputMethodEngine.ImmersiveMode.LIGHT_IMMERSIVE);
```

## setKeepScreenOn

```TypeScript
setKeepScreenOn(isKeepScreenOn: boolean): Promise<void>
```

Sets to keep the screen always on. This API uses a promise to return the result.

> **NOTE：**
> 
> - When the keyboard is displayed, the screen stays on. When the keyboard is hidden, the screen turns off.
> 
> - You need to use this API properly. Set the attribute to **true** in necessary scenarios (for example, voice
> input) and reset this attribute to **false** after exiting necessary scenarios. In other scenarios, do not use
> this API.

**Since:** 20

<!--Device-Panel-setKeepScreenOn(isKeepScreenOn: boolean): Promise<void>--><!--Device-Panel-setKeepScreenOn(isKeepScreenOn: boolean): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isKeepScreenOn | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800013](../errorcode-inputmethod-framework.md#12800013-window-manager-service-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

panel.setKeepScreenOn(true).then(() => {
  console.info(`setKeepScreenOn success.`);
}).catch((error: BusinessError) => {
  console.error(`setKeepScreenOn failed, code: ${error.code}, message: ${error.message}`);
})
```

## setPrivacyMode

```TypeScript
setPrivacyMode(isPrivacyMode: boolean): void
```

Sets the input method panel to privacy mode. In privacy mode, screenshot and screen recording are blocked.

**Since:** 11

**Required permissions:** ohos.permission.PRIVACY_WINDOW

<!--Device-Panel-setPrivacyMode(isPrivacyMode: boolean): void--><!--Device-Panel-setPrivacyMode(isPrivacyMode: boolean): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isPrivacyMode | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
let isPrivacyMode: boolean = true;
panel.setPrivacyMode(isPrivacyMode);
```

## setSystemPanelButtonColor

```TypeScript
setSystemPanelButtonColor(fillColor: string | undefined, backgroundColor: string | undefined): Promise<void>
```

Sets the color of the function buttons and their background color on the current panel. This API uses a promise to return the result.

**Since:** 22

<!--Device-Panel-setSystemPanelButtonColor(fillColor: string | undefined, backgroundColor: string | undefined): Promise<void>--><!--Device-Panel-setSystemPanelButtonColor(fillColor: string | undefined, backgroundColor: string | undefined): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fillColor | string \| undefined | Yes |
| backgroundColor | string \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let fillColor = "#FFFF00";
  let backgroundColor = "#0000FF";
  this.panel.setSystemPanelButtonColor(fillColor, backgroundColor).then(() => {
    console.info(`setSystemPanelButtonColor success.`);
  }).catch((error: BusinessError) => {
    console.error(`setSystemPanelButtonColor failed, code: ${error.code}, message: ${error.message}`);
  })
} catch (err) {
  let error = err as BusinessError;
  console.error(`setSystemPanelButtonColor failed, code: ${error.code}, message: ${error.message}`);
}
```

## setUiContent

```TypeScript
setUiContent(path: string, callback: AsyncCallback<void>): void
```

Loads content from a page to this input method panel. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-Panel-setUiContent(path: string, callback: AsyncCallback<void>): void--><!--Device-Panel-setUiContent(path: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

panel.setUiContent('pages/page2/page2', (err: BusinessError) => {
  if (err) {
    console.error(`Failed to setUiContent. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the content.');
});
```

## setUiContent

```TypeScript
setUiContent(path: string): Promise<void>
```

Loads content from a page to this input method panel. This API uses a promise to return the result.

**Since:** 10

<!--Device-Panel-setUiContent(path: string): Promise<void>--><!--Device-Panel-setUiContent(path: string): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

panel.setUiContent('pages/page2/page2').then(() => {
  console.info('Succeeded in setting the content.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setUiContent. Code is ${err.code}, message is ${err.message}`);
});
```

## setUiContent

```TypeScript
setUiContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void
```

Loads content from a page linked to LocalStorage to this input method panel. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-Panel-setUiContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void--><!--Device-Panel-setUiContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| storage | [LocalStorage](../../apis-arkui/arkts-apis/arkts-arkui-localstorage-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let storage: LocalStorage = new LocalStorage();
storage.setOrCreate('storageSimpleProp', 121);
panel.setUiContent('pages/page2/page2', storage, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to setUiContent. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the content.');
});
```

## setUiContent

```TypeScript
setUiContent(path: string, storage: LocalStorage): Promise<void>
```

Loads content from a page linked to LocalStorage to this panel. This API uses a promise to return the result.

**Since:** 10

<!--Device-Panel-setUiContent(path: string, storage: LocalStorage): Promise<void>--><!--Device-Panel-setUiContent(path: string, storage: LocalStorage): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| storage | [LocalStorage](../../apis-arkui/arkts-apis/arkts-arkui-localstorage-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let storage: LocalStorage = new LocalStorage();
storage.setOrCreate('storageSimpleProp', 121);
panel.setUiContent('pages/page2/page2', storage).then(() => {
  console.info('Succeeded in setting the content.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setUiContent. Code is ${err.code}, message is ${err.message}`);
});
```

## show

```TypeScript
show(callback: AsyncCallback<void>): void
```

Shows this input method panel. This API uses an asynchronous callback to return the result. It can be called when the input method is bound to the edit box.

**Since:** 10

<!--Device-Panel-show(callback: AsyncCallback<void>): void--><!--Device-Panel-show(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

panel.show((err: BusinessError) => {
  if (err) {
    console.error(`Failed to show panel. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in showing the panel.');
});
```

## show

```TypeScript
show(): Promise<void>
```

Shows this input method panel. This API uses a promise to return the result. It can be called when the input method is bound to the edit box.

**Since:** 10

<!--Device-Panel-show(): Promise<void>--><!--Device-Panel-show(): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

panel.show().then(() => {
  console.info('Succeeded in showing the panel.');
}).catch((err: BusinessError) => {
  console.error(`Failed to show panel. Code is ${err.code}, message is ${err.message}`);
});
```

## startMoving

```TypeScript
startMoving(): void
```

Sends a command to start moving the window. The window can be moved only when the mouse is clicked.

**Since:** 15

<!--Device-Panel-startMoving(): void--><!--Device-Panel-startMoving(): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Error codes:**

| Error Code ID |
| --- |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [12800017](../errorcode-inputmethod-framework.md#12800017-invalid-panel-type-or-panel-flag) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-window-manager-service-error) |

## Examples

```TypeScript
panel.startMoving();
```

## updatePanelRect

```TypeScript
updatePanelRect(flag: PanelFlag, rect: PanelRect): Promise<void>
```

Update the panel rectangle. This API uses a promise to return the result.  
> **NOTE：**
> 
> This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING**
> state.
> 
> When the **PanelFlag** of a smartphone is **FLG_FLOATING** and the panel width is between 0 and 288 vp, the
> function buttons at the bottom of the panel will dynamically update their size according to the panel width. To
> ensure the optimal user experience, it is recommended that the panel width be no less than 90 vp.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-updatePanelRect(flag: PanelFlag, rect: PanelRect): Promise<void>--><!--Device-Panel-updatePanelRect(flag: PanelFlag, rect: PanelRect): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| flag | [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md) | Yes |
| rect | [PanelRect](arkts-ime-inputmethodengine-panelrect-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800013](../errorcode-inputmethod-framework.md#12800013-window-manager-service-error) |

## updatePanelRect

```TypeScript
updatePanelRect(flag: PanelFlag, rect: EnhancedPanelRect): Promise<void>
```

Update the panel rectangle, and customizes the avoid area and touch area. This API uses a promise to return the result.  
> **NOTE：**
> 
> This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING**
> state. This API is compatible with
> [updatePanelRect](arkts-ime-inputmethodengine-panel-i.md#updatepanelrect).
> If the input parameter **rect** contains only the **landscapeRect** and **portraitRect** attributes,
> [updatePanelRect](arkts-ime-inputmethodengine-panel-i.md#updatepanelrect)
> is called by default.
> 
> When the **PanelFlag** of a smartphone is **FLG_FLOATING** and the panel width is between 0 and 288 vp, the
> function buttons at the bottom of the panel will dynamically update their size according to the panel width. To
> ensure the optimal user experience, it is recommended that the panel width be no less than 90 vp.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-updatePanelRect(flag: PanelFlag, rect: EnhancedPanelRect): Promise<void>--><!--Device-Panel-updatePanelRect(flag: PanelFlag, rect: EnhancedPanelRect): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| flag | [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md) | Yes |
| rect | [EnhancedPanelRect](arkts-ime-inputmethodengine-enhancedpanelrect-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800017](../errorcode-inputmethod-framework.md#12800017-invalid-panel-type-or-panel-flag) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-window-manager-service-error) |

## updatePanelRectSync

```TypeScript
updatePanelRectSync(flag: PanelFlag, rect: PanelRect): void
```

Update the panel rectangle.  
> **NOTE：**
> 
> This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING**
> state.
> 
> When the **PanelFlag** of a smartphone is **FLG_FLOATING** and the panel width is between 0 and 288 vp, the
> function buttons at the bottom of the panel will dynamically update their size according to the panel width. To
> ensure the optimal user experience, it is recommended that the panel width be no less than 90 vp.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-updatePanelRectSync(flag: PanelFlag, rect: PanelRect): void--><!--Device-Panel-updatePanelRectSync(flag: PanelFlag, rect: PanelRect): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| flag | [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md) | Yes |
| rect | [PanelRect](arkts-ime-inputmethodengine-panelrect-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800013](../errorcode-inputmethod-framework.md#12800013-window-manager-service-error) |

## updatePanelRectSync

```TypeScript
updatePanelRectSync(flag: PanelFlag, rect: EnhancedPanelRect): void
```

Update the panel rectangle, and customizes the avoid area and touch area.  
> **NOTE：**
> 
> This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING**
> state. This API is compatible with
> [updatePanelRectSync](arkts-ime-inputmethodengine-panel-i.md#updatepanelrectsync).
> If the input parameter **rect** contains only the **landscapeRect** and **portraitRect** attributes,
> [updatePanelRectSync](arkts-ime-inputmethodengine-panel-i.md#updatepanelrectsync)
> is called by default.
> 
> When the **PanelFlag** of a smartphone is **FLG_FLOATING** and the panel width is between 0 and 288 vp, the
> function buttons at the bottom of the panel will dynamically update their size according to the panel width. To
> ensure the optimal user experience, it is recommended that the panel width be no less than 90 vp.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-updatePanelRectSync(flag: PanelFlag, rect: EnhancedPanelRect): void--><!--Device-Panel-updatePanelRectSync(flag: PanelFlag, rect: EnhancedPanelRect): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| flag | [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md) | Yes |
| rect | [EnhancedPanelRect](arkts-ime-inputmethodengine-enhancedpanelrect-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800017](../errorcode-inputmethod-framework.md#12800017-invalid-panel-type-or-panel-flag) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-window-manager-service-error) |

## updateRegion

```TypeScript
updateRegion(inputRegion: Array<window.Rect>): void
```

Updates the hot zone on the input method panel in the current state.

> **NOTE：**
> 
> This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING**
> state.
> 
> This API returns the result synchronously. The return only indicates that the system has received the request
> for updating the hot zone, not that the hot zone has been updated.

**Since:** 15

<!--Device-Panel-updateRegion(inputRegion: Array<window.Rect>): void--><!--Device-Panel-updateRegion(inputRegion: Array<window.Rect>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inputRegion | Array&lt;window.Rect&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800017](../errorcode-inputmethod-framework.md#12800017-invalid-panel-type-or-panel-flag) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-window-manager-service-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let inputRegion: Array<window.Rect> = [{
  left: 300,
  top: 650,
  width: 2000,
  height: 500
}];
panel.updateRegion(inputRegion);
```
