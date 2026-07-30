# Panel

Represents the word selection panel.

**Since:** 24

<!--Device-selectionManager-interface Panel--><!--Device-selectionManager-interface Panel-End-->

**System capability:** SystemCapability.SelectionInput.Selection

## Modules to Import

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';
```

## moveTo

```TypeScript
moveTo(x: number, y: number): Promise<void>
```

Moves the word selection panel to the specified coordinates on the screen. This API uses a promise to return the result.

**Since:** 20

**Deprecated since:** 24

**Substitutes:** [moveToGlobalDisplay](arkts-basicservices-selectionmanager-panel-i.md#movetoglobaldisplay)

<!--Device-Panel-moveTo(x: int, y: int): Promise<void>--><!--Device-Panel-moveTo(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | number | Yes | Value of the movement along the X axis, in px. |
| y | number | Yes | Value of the movement along the Y axis, in px. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [33600001](../../apis-basic-services-kit/errorcode-selection.md#33600001-word-selection-service-error) | Selection service exception. |
| [33600002](../../apis-basic-services-kit/errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) | This selection window has been destroyed. |

**Example**

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

