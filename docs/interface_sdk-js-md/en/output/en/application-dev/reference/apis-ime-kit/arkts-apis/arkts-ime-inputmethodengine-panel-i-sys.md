# Panel

In the following API examples, you must first use [createPanel]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to obtain a **Panel** instance, and then call the APIs using the obtained instance.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-inputMethodEngine-interface Panel--><!--Device-inputMethodEngine-interface Panel-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## off('sizeUpdate')

```TypeScript
off(type: 'sizeUpdate', callback?: SizeUpdateCallback): void
```

Disables listening for the panel size change. This API uses an asynchronous callback to return the result. > **NOTE** > > This API applies only to the panels of the **SOFT\_KEYBOARD** type in the **FLG\_FIXED** or **FLG\_FLOATING** > state. When you call > [adjustPanelRect]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ > to adjust the panel size, the system calculates the final value based on certain rules (for example, whether > the panel size exceeds the screen). This callback can be used to obtain the actual panel size to refresh the > panel layout.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

<!--Device-Panel-off(type: 'sizeUpdate', callback?: SizeUpdateCallback): void--><!--Device-Panel-off(type: 'sizeUpdate', callback?: SizeUpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sizeUpdate' | Yes | Event type, which is **'sizeUpdate'**. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Callback used to return the size of the soft keyboard panel,including the width and height. |

**Example**

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

Unsubscribe 'sizeUpdate' event. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_It's only used for SOFT\_KEYBOARD panel with FLG\_FIXED and FLG\_FLOATING.\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Panel-offSizeUpdate(callback?: SizeUpdateCallback): void--><!--Device-Panel-offSizeUpdate(callback?: SizeUpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | optional, the callback called when the panel size updates. |

## on('sizeUpdate')

```TypeScript
on(type: 'sizeUpdate', callback: SizeUpdateCallback): void
```

Listens for the panel size change. This API uses an asynchronous callback to return the result. > **NOTE** > > This API applies only to the panels of the **SOFT\_KEYBOARD** type in the **FLG\_FIXED** or **FLG\_FLOATING** > state. When you call > [adjustPanelRect]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ > to adjust the panel size, the system calculates the final value based on certain rules (for example, whether > the panel size exceeds the screen). This callback can be used to obtain the actual panel size to refresh the > panel layout.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

<!--Device-Panel-on(type: 'sizeUpdate', callback: SizeUpdateCallback): void--><!--Device-Panel-on(type: 'sizeUpdate', callback: SizeUpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sizeUpdate' | Yes | Event type, which is **'sizeUpdate'**. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback used to return the size of the soft keyboard panel, including the width and height. |

**Example**

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

Subscribe 'sizeUpdate' event. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_It's only used for SOFT\_KEYBOARD panel with FLG\_FIXED and FLG\_FLOATING.\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Panel-onSizeUpdate(callback: SizeUpdateCallback): void--><!--Device-Panel-onSizeUpdate(callback: SizeUpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the callback called when the panel size updates. |

## setShadow

ArkTS-Dyn:
```TypeScript
setShadow(radius: number, color: string, offsetX: number, offsetY: number): void
```

ArkTS-Sta:
```TypeScript
setShadow(radius: double, color: string, offsetX: double, offsetY: double): void
```

Sets the shadow effect of the input method window. > **NOTE** > > Panels whose [PanelType]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is **SOFT\_KEYBOARD** and > [PanelFlag]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ is **FLG\_FIXED** are not supported.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-Panel-setShadow(radius: double, color: string, offsetX: double, offsetY: double): void--><!--Device-Panel-setShadow(radius: double, color: string, offsetX: double, offsetY: double): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radius | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Radius of the shadow. The value is a floating-point number greater than or equal to 0.0, in px. The value **0.0** means that the shadow is disabled for the window borders. |
| color | string | Yes | Color of the shadow. The value is a hexadecimal RGB or ARGB color code and is case insensitive, for example, \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ or \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| offsetX | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Offset of the shadow along the x-axis, in pixels. The value is a floating-point number. |
| offsetY | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Offset of the shadow along the y-axis, in pixels. The value is a floating-point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |
| [12800013](../errorcode-inputmethod-framework.md#12800013-window-manager-service-error) | window manager service error. |
| [12800017](../errorcode-inputmethod-framework.md#12800017-invalid-panel-type-or-panel-flag) | invalid panel type or panel flag.Possible causes: Panel's flag is FLG\_\_\_ESCAPED\_UNDERSCORE\_\_\_FIXED. |

**Example**

```TypeScript
panel.setShadow(20, '#000000', 20, 20);
```

