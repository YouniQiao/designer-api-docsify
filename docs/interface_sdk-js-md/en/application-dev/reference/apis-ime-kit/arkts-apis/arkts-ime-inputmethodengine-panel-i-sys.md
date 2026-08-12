# Panel

In the following API examples, you must first use   
[createPanel](arkts-ime-inputmethodengine-inputmethodability-i.md#createPanel)to obtain a **Panel** instance, and then call the APIs using the obtained instance.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

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

**ArkTS mode:** ArkTS-Dyn only, since version 14.

<!--Device-Panel-off(type: 'sizeUpdate', callback?: SizeUpdateCallback): void--><!--Device-Panel-off(type: 'sizeUpdate', callback?: SizeUpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sizeUpdate' | Yes | Event type, which is **'sizeUpdate'**. |
| callback | [SizeUpdateCallback](arkts-ime-inputmethodengine-sizeupdatecallback-t-sys.md) | No | Callback used to return the size of the soft keyboard panel, including the width and height. |

## Examples

```TypeScript
import { window } from '@kit.ArkUI';

panel.off('sizeUpdate', (windowSize: window.Size, keyboardArea: inputMethodEngine.KeyboardArea) => {
  console.info(`panel size changed, width: ${windowSize.width}, height: ${windowSize.height}`);
});
```

## offSizeUpdate

```TypeScript
offSizeUpdate(callback?: SizeUpdateCallback): void
```

Unsubscribe 'sizeUpdate' event.

&lt;p&gt;It's only used for SOFT_KEYBOARD panel with FLG_FIXED and FLG_FLOATING.&lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Panel-offSizeUpdate(callback?: SizeUpdateCallback): void--><!--Device-Panel-offSizeUpdate(callback?: SizeUpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [SizeUpdateCallback](arkts-ime-inputmethodengine-sizeupdatecallback-t-sys.md) | No | optional, the callback called when the panel size updates. |

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

**ArkTS mode:** ArkTS-Dyn only, since version 14.

<!--Device-Panel-on(type: 'sizeUpdate', callback: SizeUpdateCallback): void--><!--Device-Panel-on(type: 'sizeUpdate', callback: SizeUpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sizeUpdate' | Yes | Event type, which is **'sizeUpdate'**. |
| callback | [SizeUpdateCallback](arkts-ime-inputmethodengine-sizeupdatecallback-t-sys.md) | Yes | Callback used to return the size of the soft keyboard panel, including the width and height. |

## Examples

```TypeScript
import { window } from '@kit.ArkUI';

panel.on('sizeUpdate', (windowSize: window.Size, keyboardArea: inputMethodEngine.KeyboardArea) => {
  console.info(`panel size changed, windowSize: ${windowSize.width}, ${windowSize.height}, ` +
    `keyboardArea: ${keyboardArea.top}, ${keyboardArea.bottom}, ${keyboardArea.left}, ${keyboardArea.right}`);
});
```

## onSizeUpdate

```TypeScript
onSizeUpdate(callback: SizeUpdateCallback): void
```

Subscribe 'sizeUpdate' event.

&lt;p&gt;It's only used for SOFT_KEYBOARD panel with FLG_FIXED and FLG_FLOATING.&lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Panel-onSizeUpdate(callback: SizeUpdateCallback): void--><!--Device-Panel-onSizeUpdate(callback: SizeUpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [SizeUpdateCallback](arkts-ime-inputmethodengine-sizeupdatecallback-t-sys.md) | Yes | the callback called when the panel size updates. |

## setShadow

ArkTS-Dyn:
```TypeScript
setShadow(radius: number, color: string, offsetX: number, offsetY: number): void
```

ArkTS-Sta:
```TypeScript
setShadow(radius: double, color: string, offsetX: double, offsetY: double): void
```

Sets the shadow effect of the input method window.

> **NOTE：**
> 
> Panels whose [PanelType](arkts-ime-inputmethodengine-paneltype-e.md#PanelType) is **SOFT_KEYBOARD** and
> [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md#PanelFlag) is **FLG_FIXED** are not supported.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-Panel-setShadow(radius: double, color: string, offsetX: double, offsetY: double): void--><!--Device-Panel-setShadow(radius: double, color: string, offsetX: double, offsetY: double): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radius | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Radius of the shadow. The value is a floating-point number greater than or equal to 0. 0, in px. The value **0.0** means that the shadow is disabled for the window borders. |
| color | string | Yes | Color of the shadow. The value is a hexadecimal RGB or ARGB color code and is case insensitive, for example, `#000000` or `#FF000000`. |
| offsetX | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Offset of the shadow along the x-axis, in pixels. The value is a floating-point number. |
| offsetY | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Offset of the shadow along the y-axis, in pixels. The value is a floating-point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800017](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800017-invalid-panel-type-or-panel-flag) | invalid panel type or panel flag. Possible causes: Panel's flag is FLG_FIXED. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |
| [12800013](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800013-window-manager-service-error) | window manager service error. |

## Examples

```TypeScript
panel.setShadow(20, '#000000', 20, 20);
```

