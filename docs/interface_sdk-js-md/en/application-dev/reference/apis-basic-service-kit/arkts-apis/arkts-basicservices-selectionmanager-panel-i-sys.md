# Panel (System API)

Describes a **Panel** object, which is created using [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createPanel-(System-API)). This method can be used to set, display, hide, and move the panel, as well as subscribe to events. It is applicable to scenarios where a custom operation UI needs to be displayed to users after word selection is complete.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

<!--Device-selectionManager-interface Panel--><!--Device-selectionManager-interface Panel-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { selectionManager } from 'selectionManager';
```

## hide

```TypeScript
hide(): Promise<void>
```

Hides the word selection panel. This API is used together with [show](#show). This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createPanel-(System-API)). This API uses a promise to return the result. If this API is not called proactively, the panel is automatically hidden when it loses focus.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

<!--Device-Panel-hide(): Promise<void>--><!--Device-Panel-hide(): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [33600001](../../apis-basic-services-kit/errorcode-selection.md#33600001-word-selection-service-invocation-error) | Selection service exception. |
| [33600002](../../apis-basic-services-kit/errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) | This selection window has been destroyed. |

## Examples

ArkTS-Dyn example:

```TypeScript
import { selectionManager, BusinessError } from '@kit.BasicServicesKit';

selectionPanel.hide().then(() => {
  console.info('Succeeded in hiding the panel.');
}).catch((err: BusinessError) => {
  console.error(`Failed to hide panel: ${err.code}, error message: ${err.message}`);
});
```

ArkTS-Sta example:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import selectionManager from '@ohos.selectionInput.selectionManager';

selectionPanel?.hide().then(() => {
  console.info('Succeeded in hiding the panel.');
}).catch((err) => {
  console.error(`Failed to hide panel: ${err.code}, error message: ${err.message}`);
});
```

## moveTo

```TypeScript
moveTo(x: int, y: int): Promise<void>
```

Moves the word selection panel to the specified coordinates in the global coordinate system of the screen. The panel can be moved to an extended screen. This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createPanel-(System-API)). This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** 24

**Substitutes:** [moveToGlobalDisplay](arkts-basicservices-selectionmanager-panel-i.md#moveToGlobalDisplay)

<!--Device-Panel-moveTo(x: int, y: int): Promise<void>--><!--Device-Panel-moveTo(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | int | Yes | X-coordinate of the target position in the global coordinate system of the screen, in px. The upper left corner of the main screen is the origin of the global coordinate system, and the positive direction of the X axis is rightward. The x-coordinate of an extended screen may be negative, depending on the screen layout. |
| y | int | Yes | Y-coordinate of the target position in the global coordinate system of the screen, in px. The upper left corner of the main screen is the origin of the global coordinate system, and the positive direction of the Y axis is downward. The y-coordinate of an extended screen may be negative, depending on the screen layout. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [33600001](../../apis-basic-services-kit/errorcode-selection.md#33600001-word-selection-service-invocation-error) | Selection service exception. |
| [33600002](../../apis-basic-services-kit/errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) | This selection window has been destroyed. |

## Examples

```TypeScript
import { selectionManager, BusinessError } from '@kit.BasicServicesKit';

try {
  selectionPanel.moveTo(200, 200).then(() => {
    console.info('Succeeded in moving the panel.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to move panel: ${err.code}, error message: ${err.message}`);
  });
} catch (err) {
  console.error(`Failed to move panel: ${err.code}, error message: ${err.message}`);
}
```

## off_destroyed

```TypeScript
off(type: 'destroyed', callback?: Callback<void>): void
```

Unsubscribes from the word selection panel destruction event. This API is used together with [on('destroyed')](#on_destroyed). This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createPanel-(System-API)).

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

<!--Device-Panel-off(type: 'destroyed', callback?: Callback<void>): void--><!--Device-Panel-off(type: 'destroyed', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'destroyed' | Yes | Type of the event to unsubscribe from. The value is fixed to **'destroyed'**. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | Callback to be unregistered, which the callback instance registered using **on**. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

## Examples

```TypeScript
import { selectionManager, BusinessError } from '@kit.BasicServicesKit';

try {
  selectionPanel.off('destroyed');
} catch (err) {
  console.error(`Failed to unregister destroyed: ${err.code}, error message: ${err.message}`);
}
```

## off_hidden

```TypeScript
off(type: 'hidden', callback?: Callback<void>): void
```

Unsubscribes from the word selection panel hiding event. This API is used together with [on('hidden')](#on_destroyed). This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createPanel-(System-API)).

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

<!--Device-Panel-off(type: 'hidden', callback?: Callback<void>): void--><!--Device-Panel-off(type: 'hidden', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'hidden' | Yes | Type of the event to unsubscribe from. The value is fixed to **'hidden'**. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | Callback to be unregistered, which the callback instance registered using **on**. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

## Examples

```TypeScript
import { selectionManager, BusinessError } from '@kit.BasicServicesKit';

try {
  selectionPanel.off('hidden');
} catch (err) {
  console.error(`Failed to unregister hidden: ${err.code}, error message: ${err.message}`);
}
```

## on_destroyed

```TypeScript
on(type: 'destroyed', callback: Callback<void>): void
```

Subscribes to the word selection panel destruction event. This API is used together with [off('destroyed')](#off_destroyed). This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createPanel-(System-API)).

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

<!--Device-Panel-on(type: 'destroyed', callback: Callback<void>): void--><!--Device-Panel-on(type: 'destroyed', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'destroyed' | Yes | Event type, which is **'destroyed'**. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Callback used to return the result, which is triggered when [destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f-sys.md#destroyPanel-(System-API)) is called to destroy the panel. |

## Examples

```TypeScript
import { selectionManager, BusinessError } from '@kit.BasicServicesKit';

try {
  selectionPanel.on('destroyed', () => {
    console.info('Panel has been destroyed.');
  });
} catch (err) {
  console.error(`Failed to register destroyed callback: ${err.code}, error message: ${err.message}`);
}
```

## on_hidden

```TypeScript
on(type: 'hidden', callback: Callback<void>): void
```

Subscribes to the word selection panel hiding event. This API is used together with [off('hidden')](#off_destroyed). This event is triggered when the panel is hidden by calling [hide](#hide) or automatically hidden when it loses focus. This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createPanel-(System-API)).

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

<!--Device-Panel-on(type: 'hidden', callback: Callback<void>): void--><!--Device-Panel-on(type: 'hidden', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'hidden' | Yes | Event type, which is **'hidden'**. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Callback used to return the result, which is triggered when the panel is hidden. The panel can be hidden by calling [hide](#hide) or automatically hidden when it loses focus. |

## Examples

```TypeScript
import { selectionManager, BusinessError } from '@kit.BasicServicesKit';

try {
  selectionPanel.on('hidden', () => {
    console.info('Panel has been hidden.');
  });
} catch (err) {
  console.error(`Failed to register hidden callback: ${err.code}, error message: ${err.message}`);
}
```

## setUiContent

```TypeScript
setUiContent(path: string): Promise<void>
```

Sets the UI content for the current word selection panel, for example, to display translation results, search suggestions, or custom action buttons. This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createPanel-(System-API)). This API uses a promise to return the result.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-setUiContent(path: string): Promise<void>--><!--Device-Panel-setUiContent(path: string): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Path of the page content to be set. This path is configured in the **resources/base/profile/main_pages.json** file of the project in the stage model. The FA model is not supported. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [33600001](../../apis-basic-services-kit/errorcode-selection.md#33600001-word-selection-service-invocation-error) | Selection service exception. |
| [33600002](../../apis-basic-services-kit/errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) | This selection window has been destroyed. |

## Examples

ArkTS-Dyn example:

```TypeScript
import { selectionManager, BusinessError } from '@kit.BasicServicesKit';

try {
  selectionPanel.setUiContent('pages/Index').then(() => {
    console.info('Succeeded in setting the content.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to setUiContent: ${err.code}, error message: ${err.message}`);
  });
} catch (err) {
  console.error(`Failed to setUiContent: ${err.code}, error message: ${err.message}`);
}
```

ArkTS-Sta example:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import selectionManager from '@ohos.selectionInput.selectionManager';

try {
  selectionPanel?.setUiContent('pages/Index').then(() => {
    console.info('Succeeded in setting the content.');
  }).catch((err) => {
    console.error(`Failed to setUiContent: ${err.code}, error message: ${err.message}}`);
  });
} catch (err) {
  console.error(`Failed to setUiContent: ${err.code}, error message: ${err.message}}`);
}
```

## show

```TypeScript
show(): Promise<void>
```

Shows the word selection panel. This API is used together with [hide](#hide). This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createPanel-(System-API)). This API uses a promise to return the result.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-show(): Promise<void>--><!--Device-Panel-show(): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [33600001](../../apis-basic-services-kit/errorcode-selection.md#33600001-word-selection-service-invocation-error) | Selection service exception. |
| [33600002](../../apis-basic-services-kit/errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) | This selection window has been destroyed. |

## Examples

ArkTS-Dyn example:

```TypeScript
import { selectionManager, BusinessError } from '@kit.BasicServicesKit';

selectionPanel.show().then(() => {
  console.info('Succeeded in showing the panel.');
}).catch((err: BusinessError) => {
  console.error(`Failed to show panel: ${err.code}, error message: ${err.message}`);
});
```

ArkTS-Sta example:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import selectionManager from '@ohos.selectionInput.selectionManager';

selectionPanel?.show().then(() => {
  console.info('Succeeded in showing the panel.');
}).catch((err) => {
  console.error(`Failed to show panel: ${err.code}, error message: ${err.message}`);
});
```

## startMoving

```TypeScript
startMoving(): Promise<void>
```

Sets whether the word selection panel can be dragged along with the mouse, touchpad, or touchscreen. The panel automatically stops moving after the pointer is released. This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createPanel-(System-API)). This API uses a promise to return the result. This API must be called in the **onTouch** callback, and the event type must be **TouchType.Down**.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-startMoving(): Promise<void>--><!--Device-Panel-startMoving(): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [33600001](../../apis-basic-services-kit/errorcode-selection.md#33600001-word-selection-service-invocation-error) | Selection service exception. |
| [33600002](../../apis-basic-services-kit/errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) | This selection window has been destroyed. |

## Examples

ArkTS-Dyn example:

```TypeScript
import { selectionManager, BusinessError } from '@kit.BasicServicesKit';

RelativeContainer() {
  /* 
   * Page layout content, which should be defined based on your actual needs.
   */
}
.onTouch((event: TouchEvent) => {
  if (event.type === TouchType.Down) {
    if (selectionPanel !== undefined) {
      selectionPanel.startMoving().then(() => {   // selectionPanel is the panel instance created by createPanel.
        console.info('Succeeded in startMoving the panel.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to startMoving panel: ${err.code}, error message: ${err.message}`);
      });
    }
  }
})
```

ArkTS-Sta example:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import selectionManager from '@ohos.selectionInput.selectionManager';

RelativeContainer() {
  /* 
   * Page layout content, which should be defined based on your actual needs.
   */
}
.onTouch((event: TouchEvent) => {
  if (event.type === TouchType.Down) {
    if (selectionPanel !== undefined) {
      selectionPanel?.startMoving().then(() => {   // selectionPanel is the panel instance created by createPanel.
        console.info('Succeeded in startMoving the panel.');
      }).catch((err) => {
        console.error(`Failed to startMoving panel: ${err.code}, error message: ${err.message}`);
      });
    }
  }
})
```

