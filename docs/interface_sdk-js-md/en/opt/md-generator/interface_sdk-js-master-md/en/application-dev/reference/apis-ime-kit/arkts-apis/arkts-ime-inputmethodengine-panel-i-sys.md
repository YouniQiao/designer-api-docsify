# Panel

In the following API examples, you must first use   
[createPanel](arkts-ime-inputmethodengine-inputmethodability-i.md#createPanel)to obtain a **Panel** instance, and then call the APIs using the obtained instance.

**Since:** 10

<!--Device-inputMethodEngine-interface Panel--><!--Device-inputMethodEngine-interface Panel-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from '@kit.IMEKit';
```

## off('sizeUpdate')

```TypeScript
off(type: 'sizeUpdate', callback?: SizeUpdateCallback): void
```

Disables listening for the panel size change. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING**
> state. When you call
> [adjustPanelRect](arkts-ime-inputmethodengine-panel-i.md#adjustPanelRect-1)
> to adjust the panel size, the system calculates the final value based on certain rules (for example, whether
> the panel size exceeds the screen). This callback can be used to obtain the actual panel size to refresh the
> panel layout.

**Since:** 14

<!--Device-Panel-off(type: 'sizeUpdate', callback?: SizeUpdateCallback): void--><!--Device-Panel-off(type: 'sizeUpdate', callback?: SizeUpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'sizeUpdate' | Yes |
| callback | [SizeUpdateCallback](arkts-ime-inputmethodengine-sizeupdatecallback-t-sys.md) | No |

## Examples

```TypeScript
import { window } from '@kit.ArkUI';

panel.off('sizeUpdate', (windowSize: window.Size, keyboardArea: inputMethodEngine.KeyboardArea) => {
  console.info(`panel size changed, width: ${windowSize.width}, height: ${windowSize.height}`);
});
```

## on('sizeUpdate')

```TypeScript
on(type: 'sizeUpdate', callback: SizeUpdateCallback): void
```

Listens for the panel size change. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING**
> state. When you call
> [adjustPanelRect](arkts-ime-inputmethodengine-panel-i.md#adjustPanelRect-1)
> to adjust the panel size, the system calculates the final value based on certain rules (for example, whether
> the panel size exceeds the screen). This callback can be used to obtain the actual panel size to refresh the
> panel layout.

**Since:** 14

<!--Device-Panel-on(type: 'sizeUpdate', callback: SizeUpdateCallback): void--><!--Device-Panel-on(type: 'sizeUpdate', callback: SizeUpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'sizeUpdate' | Yes |
| callback | [SizeUpdateCallback](arkts-ime-inputmethodengine-sizeupdatecallback-t-sys.md) | Yes |

## Examples

```TypeScript
import { window } from '@kit.ArkUI';

panel.on('sizeUpdate', (windowSize: window.Size, keyboardArea: inputMethodEngine.KeyboardArea) => {
  console.info(`panel size changed, windowSize: ${windowSize.width}, ${windowSize.height}, ` +
    `keyboardArea: ${keyboardArea.top}, ${keyboardArea.bottom}, ${keyboardArea.left}, ${keyboardArea.right}`);
});
```

## setShadow

```TypeScript
setShadow(radius: number, color: string, offsetX: number, offsetY: number): void
```

Sets the shadow effect of the input method window.

> **NOTE：**
> 
> Panels whose [PanelType](arkts-ime-inputmethodengine-paneltype-e.md#PanelType) is **SOFT_KEYBOARD** and
> [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md#PanelFlag) is **FLG_FIXED** are not supported.

**Since:** 22

<!--Device-Panel-setShadow(radius: double, color: string, offsetX: double, offsetY: double): void--><!--Device-Panel-setShadow(radius: double, color: string, offsetX: double, offsetY: double): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| radius | number | Yes |
| color | string | Yes |
| offsetX | number | Yes |
| offsetY | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800017](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800017-invalid-panel-type-or-panel-flag) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12800013](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800013-window-manager-service-error) |

## Examples

```TypeScript
panel.setShadow(20, '#000000', 20, 20);
```
