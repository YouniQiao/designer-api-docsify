# Panel (System API)

Describes a **Panel** object, which is created using [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md). This method can be used to set, display, hide, and move the panel, as well as subscribe to events. It is applicable to scenarios where a custom operation UI needs to be displayed to users after word selection is complete.

**Since:** 24

<!--Device-selectionManager-interface Panel--><!--Device-selectionManager-interface Panel-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';
```

## moveToGlobalDisplay

```TypeScript
moveToGlobalDisplay(x: int, y: int): Promise<void>
```

Moves the word selection panel to the specified coordinates in the global coordinates system of the screen. The panel can be moved to an extended screen. This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md). This API uses a promise to return the result.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-moveToGlobalDisplay(x: int, y: int): Promise<void>--><!--Device-Panel-moveToGlobalDisplay(x: int, y: int): Promise<void>-End-->

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
| [33600001](../errorcode-selection.md#33600001-word-selection-service-invocation-error) | Selection service exception. |
| [33600002](../errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) | This selection window has been destroyed. |

**Examples**

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

## offDestroy

```TypeScript
offDestroy(callback?: Callback<void>): void
```

Unregisters the callback used to listen for the destroy event of the word selection panel. This API uses an asynchronous callback to return the result.  
**ArkTS mode:** This API applies only to ArkTS-Sta.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-offDestroy(callback?: Callback<void>): void--><!--Device-Panel-offDestroy(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | Callback function that returns no value. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Examples**

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

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-offHide(callback?: Callback<void>): void--><!--Device-Panel-offHide(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | Callback function that returns no value. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import selectionManager from '@ohos.selectionInput.selectionManager';

try {
  selectionPanel?.offHide();
} catch (err) {
  console.error(`Failed to unregister hide: ${err.code}, error message: ${err.message}`);
}
```

## onDestroy

```TypeScript
onDestroy(callback: Callback<void>): void
```

Registers a callback to listen for the destroy event of the word selection panel. This API uses an asynchronous callback to return the result.  
**ArkTS mode:** This API applies only to ArkTS-Sta.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-onDestroy(callback: Callback<void>): void--><!--Device-Panel-onDestroy(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Callback that returns no value. |

**Examples**

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

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-onHide(callback: Callback<void>): void--><!--Device-Panel-onHide(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Callback function that returns no value. |

**Examples**

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

