# Panel

Represents the word selection panel.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-selectionManager-interface Panel--><!--Device-selectionManager-interface Panel-End-->

**System capability:** SystemCapability.SelectionInput.Selection

## hide

```TypeScript
hide(): Promise<void>
```

Hides the word selection panel. This API uses a promise to return the result.

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

**Example**

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

Moves the word selection panel to the specified coordinates on the screen. This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** 24

**Substitutes:** [selectionManager.Panel.moveToGlobalDisplay](arkts-basicservices-selectionmanager-panel-i.md#movetoglobaldisplay)

<!--Device-Panel-moveTo(x: int, y: int): Promise<void>--><!--Device-Panel-moveTo(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | int | Yes | Value of the movement along the X axis, in px. |
| y | int | Yes | Value of the movement along the Y axis, in px. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [33600001](../../apis-basic-services-kit/errorcode-selection.md#33600001-word-selection-service-invocation-error) | Selection service exception. |
| [33600002](../../apis-basic-services-kit/errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) | This selection window has been destroyed. |

**Example**

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

Moves the word selection panel to the specified coordinates on the screen. This API uses a promise to return the result.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-moveToGlobalDisplay(x: int, y: int): Promise<void>--><!--Device-Panel-moveToGlobalDisplay(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Value of the movement along the X axis, in px. |
| y | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Value of the movement along the Y axis, in px. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [33600001](../../apis-basic-services-kit/errorcode-selection.md#33600001-word-selection-service-invocation-error) | Selection service exception. |
| [33600002](../../apis-basic-services-kit/errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) | This selection window has been destroyed. |

**Example**

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

Unregisters the callback used to listen for the destroy event of the word selection panel. This API uses an asynchronous callback to return the result.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-Panel-off(type: 'destroyed', callback?: Callback<void>): void--><!--Device-Panel-off(type: 'destroyed', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'destroyed' | Yes | Event type, which is **'destroyed'**. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | No | Callback function that returns no value. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Example**

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

Unregisters the callback used to listen for the hide event of the word selection panel. This API uses an asynchronous callback to return the result.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-Panel-off(type: 'hidden', callback?: Callback<void>): void--><!--Device-Panel-off(type: 'hidden', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'hidden' | Yes | Event type, which is **'hidden'**. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | No | Callback function that returns no value. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Example**

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

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-offDestroy(callback?: Callback<void>): void--><!--Device-Panel-offDestroy(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | No | Callback function that returns no value. If this parameter is notspecified,this API unregisters all callbacks for the specified type. |

**Example**

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

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-offHide(callback?: Callback<void>): void--><!--Device-Panel-offHide(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | No | Callback function that returns no value. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Example**

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

Registers a callback to listen for the destroy event of the word selection panel. This API uses an asynchronous callback to return the result.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-Panel-on(type: 'destroyed', callback: Callback<void>): void--><!--Device-Panel-on(type: 'destroyed', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'destroyed' | Yes | Event type, which is **'destroyed'**. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback function that returns no value. |

**Example**

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

Registers a callback to listen for the hide event of the word selection panel. This API uses an asynchronous callback to return the result.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-Panel-on(type: 'hidden', callback: Callback<void>): void--><!--Device-Panel-on(type: 'hidden', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'hidden' | Yes | Event type, which is **'hidden'**. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback function that returns no value. |

**Example**

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

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-onDestroy(callback: Callback<void>): void--><!--Device-Panel-onDestroy(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback function that returns no value. |

**Example**

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

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-onHide(callback: Callback<void>): void--><!--Device-Panel-onHide(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback function that returns no value. |

**Example**

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

Sets the page content for the word selection panel. This API uses a promise to return the result.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-setUiContent(path: string): Promise<void>--><!--Device-Panel-setUiContent(path: string): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Path of the page content to be set. This path is configured in the **resources/base/profile/main\_\_\_ESCAPED\_UNDERSCORE\_\_\_pages.json** file of the project in the stage model. The FA model is not supported. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [33600001](../../apis-basic-services-kit/errorcode-selection.md#33600001-word-selection-service-invocation-error) | Selection service exception. |
| [33600002](../../apis-basic-services-kit/errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) | This selection window has been destroyed. |

**Example**

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

Shows the word selection panel. This API uses a promise to return the result.

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

**Example**

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

Moves the word selection panel by dragging. This API uses a promise to return the result. This API must be written in the **onTouch** callback and the event type must be **TouchType.Down**.

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

**Example**

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

