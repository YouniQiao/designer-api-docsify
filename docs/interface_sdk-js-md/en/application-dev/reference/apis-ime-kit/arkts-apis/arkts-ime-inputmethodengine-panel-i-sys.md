# Panel

@brief You need to use [createPanel](arkts-ime-inputmethodengine-inputmethodability-i.md#createpanel) to obtain the panel instance and then call the following APIs through the instance.

**Since:** 23

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

@brief Disables listening for the panel size change. This API uses an asynchronous callback to return the result. <br> <br>   
> **NOTE：**&lt;br
&gt; 
> &lt;br
&gt; 
> This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING** state. When you call [adjustPanelRect](arkts-ime-inputmethodengine-panel-i.md#adjustpanelrect) to adjust the panel size, the system calculates the final value based on certain rules (for example, whether the panel size exceeds the screen). This callback can be used to obtain the actual panel size to refresh the panel layout.

**Since:** 14

<!--Device-Panel-off(type: 'sizeUpdate', callback?: SizeUpdateCallback): void--><!--Device-Panel-off(type: 'sizeUpdate', callback?: SizeUpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sizeUpdate' | Yes | Event type, which is **'sizeUpdate'**. |
| callback | [SizeUpdateCallback](arkts-ime-inputmethodengine-sizeupdatecallback-t-sys.md) | No | Callback used to return the size of the soft keyboard panel, including the width and height. |

**Examples**

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

@brief Unsubscribe 'sizeUpdate' event. <br> <br><p>It's only used for SOFT_KEYBOARD panel with FLG_FIXED and FLG_FLOATING.</p>

**Since:** 23

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

@brief Listens for the panel size change. This API uses an asynchronous callback to return the result. <br> <br>   
> **NOTE：**&lt;br
&gt; 
> &lt;br
&gt; 
> This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING** state. When you call [adjustPanelRect](arkts-ime-inputmethodengine-panel-i.md#adjustpanelrect) to adjust the panel size, the system calculates the final value based on certain rules (for example, whether the panel size exceeds the screen). This callback can be used to obtain the actual panel size to refresh the panel layout.

**Since:** 14

<!--Device-Panel-on(type: 'sizeUpdate', callback: SizeUpdateCallback): void--><!--Device-Panel-on(type: 'sizeUpdate', callback: SizeUpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sizeUpdate' | Yes | Event type, which is **'sizeUpdate'**. |
| callback | [SizeUpdateCallback](arkts-ime-inputmethodengine-sizeupdatecallback-t-sys.md) | Yes | Callback used to return the size of the soft keyboard panel, including the width and height. |

**Examples**

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

@brief Subscribe 'sizeUpdate' event. <br> <br><p>It's only used for SOFT_KEYBOARD panel with FLG_FIXED and FLG_FLOATING.</p>

**Since:** 23

<!--Device-Panel-onSizeUpdate(callback: SizeUpdateCallback): void--><!--Device-Panel-onSizeUpdate(callback: SizeUpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [SizeUpdateCallback](arkts-ime-inputmethodengine-sizeupdatecallback-t-sys.md) | Yes | the callback called when the panel size updates. |

## setShadow

```TypeScript
setShadow(radius: double, color: string, offsetX: double, offsetY: double): void
```

@brief Sets the shadow effect of the input method window. <br> <br>   
> **NOTE：**&lt;br
&gt; 
> <br>
> Panels whose [PanelType](arkts-ime-inputmethodengine-paneltype-e.md) is **SOFT_KEYBOARD** and [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md) is **FLG_FIXED** are not supported.

**Since:** 23

<!--Device-Panel-setShadow(radius: double, color: string, offsetX: double, offsetY: double): void--><!--Device-Panel-setShadow(radius: double, color: string, offsetX: double, offsetY: double): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radius | double | Yes | Radius of the shadow. The value is a floating-point number greater than or equal to 0. 0, in px. The value **0.0** means that the shadow is disabled for the window borders. |
| color | string | Yes | Color of the shadow. The value is a hexadecimal RGB or ARGB color code and is case insensitive, for example, `#000000` or `#FF000000`. |
| offsetX | double | Yes | Offset of the shadow along the x-axis, in pixels. The value is a floating-point number. |
| offsetY | double | Yes | Offset of the shadow along the y-axis, in pixels. The value is a floating-point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |
| [12800013](../errorcode-inputmethod-framework.md#12800013-window-manager-service-error) | window manager service error. |
| [12800017](../errorcode-inputmethod-framework.md#12800017-invalid-panel-type-or-panel-flag) | invalid panel type or panel flag. Possible causes: Panel's flag is FLG_FIXED. |

**Examples**

```TypeScript
panel.setShadow(20, '#000000', 20, 20);
```

