# Panel

Describes a **Panel** object, which is created using [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel). This method can be used to set, display, hide, and move the panel, as well as subscribe to events. It is applicable to scenarios where a custom operation UI needs to be displayed to users after word selection is complete.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-selectionManager-interface Panel--><!--Device-selectionManager-interface Panel-End-->

**System capability:** SystemCapability.SelectionInput.Selection

## Modules to Import

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## hide

```TypeScript
hide(): Promise<void>
```

Hides the word selection panel. This API is used together with [show](arkts-basicservices-selectionmanager-panel-i.md#show). This API can be called only after a **Panel** instance is obtained by calling   
[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel). This API uses a promise to return the result. If this API is not called proactively, the panel is automatically hidden when it loses focus.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-Panel-hide(): Promise<void>--><!--Device-Panel-hide(): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

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

Moves the word selection panel to the specified coordinates in the global coordinate system of the screen. The panel can be moved to an extended screen. This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel). This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** 24

**Substitutes:** [selectionManager.Panel.moveToGlobalDisplay](arkts-basicservices-selectionmanager-panel-i.md#movetoglobaldisplay)

<!--Device-Panel-moveTo(x: int, y: int): Promise<void>--><!--Device-Panel-moveTo(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

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

## moveToGlobalDisplay

ArkTS-Dyn:
```TypeScript
moveToGlobalDisplay(x: number, y: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
moveToGlobalDisplay(x: int, y: int): Promise<void>
```

Moves the word selection panel to the specified coordinates in the global coordinates system of the screen. The panel can be moved to an extended screen. This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel). This API uses a promise to return the result.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-moveToGlobalDisplay(x: int, y: int): Promise<void>--><!--Device-Panel-moveToGlobalDisplay(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | X-coordinate of the target position in the global coordinate system of the screen, in px. The upper left corner of the main screen is the origin of the global coordinate system, and the positive direction of the X axis is rightward. The x-coordinate of an extended screen may be negative, depending on the screen layout. |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Y-coordinate of the target position in the global coordinate system of the screen, in px. The upper left corner of the main screen is the origin of the global coordinate system, and the positive direction of the Y axis is downward. The y-coordinate of an extended screen may be negative, depending on the screen layout. |

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
  selectionPanel.moveToGlobalDisplay(200, 200).then(() => {
    console.info('Succeeded in moving the panel.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to move panel: ${err.code}, error message: ${err.message}`);
  });
} catch (err) {
  console.error(`Failed to move panel: ${err.code}, error message: ${err.message}`);
}
```

ArkTS-Sta example:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import selectionManager from '@ohos.selectionInput.selectionManager';

try {
  selectionPanel?.moveToGlobalDisplay(200, 200).then(() => {
    console.info('Succeeded in moving the panel.');
  }).catch((err) => {
    console.error(`Failed to move panel: ${err.code}, error message: ${err.message}`);
  });
} catch (err) {
  console.error(`Failed to move panel: ${err.code}, error message: ${err.message}`);
}
```

## off('destroyed')

```TypeScript
off(type: 'destroyed', callback?: Callback<void>): void
```

Unsubscribes from the word selection panel destruction event. This API is used together with   
[on('destroyed')](selectionManager.Panel.on(type: 'destroyed', callback: Callback&lt;void&gt;)). This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel).

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-Panel-off(type: 'destroyed', callback?: Callback<void>): void--><!--Device-Panel-off(type: 'destroyed', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

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

## off('hidden')

```TypeScript
off(type: 'hidden', callback?: Callback<void>): void
```

Unsubscribes from the word selection panel hiding event. This API is used together with   
[on('hidden')](selectionManager.Panel.on(type: 'hidden', callback: Callback&lt;void&gt;)). This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel).

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-Panel-off(type: 'hidden', callback?: Callback<void>): void--><!--Device-Panel-off(type: 'hidden', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

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

## offDestroy

```TypeScript
offDestroy(callback?: Callback<void>): void
```

Unregisters the callback used to listen for the destroy event of the word selection panel. This API uses an asynchronous callback to return the result.

**ArkTS mode:** This API applies only to ArkTS-Sta.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-offDestroy(callback?: Callback<void>): void--><!--Device-Panel-offDestroy(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | Callback function that returns no value. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import selectionManager from '@ohos.selectionInput.selectionManager';

try {
  selectionPanel?.offDestroy();
} catch (err) {
  console.error(`Failed to unregister destroyed: ${err.code}, error message: ${err.message}`);
}
```

## offHide

```TypeScript
offHide(callback?: Callback<void>): void
```

Unregisters the callback used to listen for the hide event of the word selection panel. This API uses an asynchronous callback to return the result.

**ArkTS mode:** This API applies only to ArkTS-Sta.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-offHide(callback?: Callback<void>): void--><!--Device-Panel-offHide(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | Callback function that returns no value. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import selectionManager from '@ohos.selectionInput.selectionManager';

try {
  selectionPanel?.offHide();
} catch (err) {
  console.error(`Failed to unregister hide: ${err.code}, error message: ${err.message}`);
}
```

## on('destroyed')

```TypeScript
on(type: 'destroyed', callback: Callback<void>): void
```

Subscribes to the word selection panel destruction event. This API is used together with   
[off('destroyed')](selectionManager.Panel.off(type: 'destroyed', callback?: Callback&lt;void&gt;)). This API can be called only after a **Panel** instance is obtained by calling   
[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel).

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-Panel-on(type: 'destroyed', callback: Callback<void>): void--><!--Device-Panel-on(type: 'destroyed', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'destroyed' | Yes | Event type, which is **'destroyed'**. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Callback used to return the result, which is triggered when [destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f.md#destroypanel) is called to destroy the panel. |

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

## on('hidden')

```TypeScript
on(type: 'hidden', callback: Callback<void>): void
```

Subscribes to the word selection panel hiding event. This API is used together with   
[off('hidden')](selectionManager.Panel.off(type: 'hidden', callback?: Callback&lt;void&gt;)). This event is triggered when the panel is hidden by calling [hide](arkts-basicservices-selectionmanager-panel-i.md#hide) or automatically hidden when it loses focus. This API can be called only after a **Panel** instance is obtained by calling   
[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel).

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-Panel-on(type: 'hidden', callback: Callback<void>): void--><!--Device-Panel-on(type: 'hidden', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'hidden' | Yes | Event type, which is **'hidden'**. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Callback used to return the result, which is triggered when the panel is hidden. The panel can be hidden by calling [hide](arkts-basicservices-selectionmanager-panel-i.md#hide) or automatically hidden when it loses focus. |

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

## onDestroy

```TypeScript
onDestroy(callback: Callback<void>): void
```

Registers a callback to listen for the destroy event of the word selection panel. This API uses an asynchronous callback to return the result.

**ArkTS mode:** This API applies only to ArkTS-Sta.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-onDestroy(callback: Callback<void>): void--><!--Device-Panel-onDestroy(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Callback that returns no value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import selectionManager from '@ohos.selectionInput.selectionManager';

try {
  selectionPanel?.onDestroy(() => {
    console.info('Panel has been destroyed.');
  });
} catch (err) {
  console.error(`Failed to register destroy callback: ${err.code}, error message: ${err.message}`);
}
```

## onHide

```TypeScript
onHide(callback: Callback<void>): void
```

Registers a callback to listen for the hide event of the word selection panel. This API uses an asynchronous callback to return the result.

**ArkTS mode:** This API applies only to ArkTS-Sta.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-onHide(callback: Callback<void>): void--><!--Device-Panel-onHide(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Callback function that returns no value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import selectionManager from '@ohos.selectionInput.selectionManager';

try {
  selectionPanel?.onHide(() => {
    console.info('Panel has been hidden.');
  });
} catch (err) {
  console.error(`Failed to register hide callback: ${err.code}, error message: ${err.message}`);
}
```

## setUiContent

```TypeScript
setUiContent(path: string): Promise<void>
```

Sets the UI content for the current word selection panel, for example, to display translation results, search suggestions, or custom action buttons. This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel). This API uses a promise to return the result.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-setUiContent(path: string): Promise<void>--><!--Device-Panel-setUiContent(path: string): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

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

Shows the word selection panel. This API is used together with [hide](arkts-basicservices-selectionmanager-panel-i.md#hide). This API can be called only after a **Panel** instance is obtained by calling  
[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel). This API uses a promise to return the result.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-show(): Promise<void>--><!--Device-Panel-show(): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

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

Sets whether the word selection panel can be dragged along with the mouse, touchpad, or touchscreen. The panel automatically stops moving after the pointer is released. This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel). This API uses a promise to return the result. This API must be called in the **onTouch** callback, and the event type must be **TouchType.Down**.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-startMoving(): Promise<void>--><!--Device-Panel-startMoving(): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

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

