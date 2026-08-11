# Panel

Describes a **Panel** object, which is created using [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel). This method can be used to set, display, hide, and move the panel, as well as subscribe to events. It is applicable to scenarios where a custom operation UI needs to be displayed to users after word selection is complete.

**Since:** 24

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

<!--Device-Panel-hide(): Promise<void>--><!--Device-Panel-hide(): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [33600001](../../apis-basic-services-kit/errorcode-selection.md#33600001-word-selection-service-invocation-error) |
| [33600002](../../apis-basic-services-kit/errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Hide the word selection panel. selectionPanel is a Panel instance created by createPanel.
selectionPanel.hide().then(() => {
  console.info('Succeeded in hiding the panel.');
}).catch((err: BusinessError) => {
  console.error(`Failed to hide panel. Error code: ${err.code}, error message: ${err.message}`);
});
```

## moveTo

```TypeScript
moveTo(x: number, y: number): Promise<void>
```

Moves the word selection panel to the specified coordinates in the global coordinate system of the screen. The panel can be moved to an extended screen. This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel). This API uses a promise to return the result.

**Since:** 20

**Deprecated since:** 24

**Substitutes:** [selectionManager.Panel.moveToGlobalDisplay](arkts-basicservices-selectionmanager-panel-i.md#movetoglobaldisplay)

<!--Device-Panel-moveTo(x: int, y: int): Promise<void>--><!--Device-Panel-moveTo(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

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
| [33600001](../../apis-basic-services-kit/errorcode-selection.md#33600001-word-selection-service-invocation-error) |
| [33600002](../../apis-basic-services-kit/errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Move the word selection panel to the specified coordinates on the screen. selectionPanel is a Panel instance created by createPanel.
  selectionPanel.moveTo(200, 200).then(() => {
    console.info('Succeeded in moving the panel.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to move panel. Error code: ${err.code}, error message: ${err.message}`);
  });
} catch (err) {
  console.error(`Failed to move panel. Error code: ${err.code}, error message: ${err.message}`);
}
```

## moveToGlobalDisplay

```TypeScript
moveToGlobalDisplay(x: number, y: number): Promise<void>
```

Moves the word selection panel to the specified coordinates in the global coordinates system of the screen. The panel can be moved to an extended screen. This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel). This API uses a promise to return the result.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-moveToGlobalDisplay(x: int, y: int): Promise<void>--><!--Device-Panel-moveToGlobalDisplay(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

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
| [33600001](../../apis-basic-services-kit/errorcode-selection.md#33600001-word-selection-service-invocation-error) |
| [33600002](../../apis-basic-services-kit/errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Move the word selection panel to the specified coordinates on the screen. selectionPanel is a Panel instance created by createPanel.
  selectionPanel.moveToGlobalDisplay(200, 200).then(() => {
    console.info('Succeeded in moving the panel.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to move panel. Error code: ${err.code}, error message: ${err.message}`);
  });
} catch (err) {
  console.error(`Failed to move panel. Error code: ${err.code}, error message: ${err.message}`);
}
```

## off('destroyed')

```TypeScript
off(type: 'destroyed', callback?: Callback<void>): void
```

Unsubscribes from the word selection panel destruction event. This API is used together with   
[on('destroyed')](selectionManager.Panel.on(type: 'destroyed', callback: Callback&lt;void&gt;)). This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel).

**Since:** 24

<!--Device-Panel-off(type: 'destroyed', callback?: Callback<void>): void--><!--Device-Panel-off(type: 'destroyed', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'destroyed' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

## Examples

```TypeScript
try {
  // Unsubscribe from the word selection panel destruction event. selectionPanel is a Panel instance created by createPanel.
  selectionPanel.off('destroyed');
} catch (err) {
  console.error(`Failed to unregister destroyed. Error code: ${err.code}, error message: ${err.message}`);
}
```

## off('hidden')

```TypeScript
off(type: 'hidden', callback?: Callback<void>): void
```

Unsubscribes from the word selection panel hiding event. This API is used together with   
[on('hidden')](selectionManager.Panel.on(type: 'hidden', callback: Callback&lt;void&gt;)). This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel).

**Since:** 24

<!--Device-Panel-off(type: 'hidden', callback?: Callback<void>): void--><!--Device-Panel-off(type: 'hidden', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'hidden' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

## Examples

```TypeScript
try {
  // // Unsubscribe from the word selection panel hiding event. selectionPanel is a Panel instance created by createPanel.
  selectionPanel.off('hidden');
} catch (err) {
  console.error(`Failed to unregister hidden. Error code: ${err.code}, error message: ${err.message}`);
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

<!--Device-Panel-on(type: 'destroyed', callback: Callback<void>): void--><!--Device-Panel-on(type: 'destroyed', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'destroyed' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
try {
  // Subscribe to the word selection panel destruction event. selectionPanel is a Panel instance created by createPanel.
  selectionPanel.on('destroyed', () => {
    console.info('Panel has been destroyed.');
  });
} catch (err) {
  console.error(`Failed to register destroyed callback. Error code: ${err.code}, error message: ${err.message}`);
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

<!--Device-Panel-on(type: 'hidden', callback: Callback<void>): void--><!--Device-Panel-on(type: 'hidden', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'hidden' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
try {
  // Subscribe to the word selection panel hiding event. selectionPanel is a Panel instance created by createPanel.
  selectionPanel.on('hidden', () => {
    console.info('Panel has been hidden.');
  });
} catch (err) {
  console.error(`Failed to register hidden callback. Error code: ${err.code}, error message: ${err.message}`);
}
```

## setUiContent

```TypeScript
setUiContent(path: string): Promise<void>
```

Sets the UI content for the current word selection panel, for example, to display translation results, search suggestions, or custom action buttons. This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel). This API uses a promise to return the result.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-setUiContent(path: string): Promise<void>--><!--Device-Panel-setUiContent(path: string): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

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
| [33600001](../../apis-basic-services-kit/errorcode-selection.md#33600001-word-selection-service-invocation-error) |
| [33600002](../../apis-basic-services-kit/errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Load page content for the word selection panel. selectionPanel is a Panel instance created by createPanel.
  selectionPanel.setUiContent('pages/Index').then(() => {
    console.info('Succeeded in setting the content.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to setUiContent. Error code: ${err.code}, error message: ${err.message}`);
  });
} catch (err) {
  console.error(`Failed to setUiContent. Error code: ${err.code}, error message: ${err.message}`);
}
```

## show

```TypeScript
show(): Promise<void>
```

Shows the word selection panel. This API is used together with [hide](arkts-basicservices-selectionmanager-panel-i.md#hide). This API can be called only after a **Panel** instance is obtained by calling  
[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel). This API uses a promise to return the result.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-show(): Promise<void>--><!--Device-Panel-show(): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [33600001](../../apis-basic-services-kit/errorcode-selection.md#33600001-word-selection-service-invocation-error) |
| [33600002](../../apis-basic-services-kit/errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Show the word selection panel. selectionPanel is a Panel instance created by createPanel.
selectionPanel.show().then(() => {
  console.info('Succeeded in showing the panel.');
}).catch((err: BusinessError) => {
  console.error(`Failed to show panel. Error code: ${err.code}, error message: ${err.message}`);
});
```

## startMoving

```TypeScript
startMoving(): Promise<void>
```

Sets whether the word selection panel can be dragged along with the mouse, touchpad, or touchscreen. The panel automatically stops moving after the pointer is released. This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel). This API uses a promise to return the result. This API must be called in the **onTouch** callback, and the event type must be **TouchType.Down**.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-startMoving(): Promise<void>--><!--Device-Panel-startMoving(): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [33600001](../../apis-basic-services-kit/errorcode-selection.md#33600001-word-selection-service-invocation-error) |
| [33600002](../../apis-basic-services-kit/errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// This code must be placed in build() of the ArkUI page component. RelativeContainer is a built-in component of ArkUI. TouchEvent and TouchType are built-in types of ArkUI.
RelativeContainer() {
  /* 
   * Page layout content, which should be defined based on your actual needs.
   */
}
.onTouch((event: TouchEvent) => {
  if (event.type === TouchType.Down) {
    if (selectionPanel !== undefined) {
      // Enable the word selection panel to be dragged and moved with the mouse, touchpad, or touchscreen. selectionPanel is the panel instance created by createPanel.
      selectionPanel.startMoving().then(() => {
        console.info('Succeeded in startMoving the panel.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to startMoving panel. Error code: ${err.code}, error message: ${err.message}`);
      });
    }
  }
})
```
