# Panel (System API)

Describes a **Panel** object, which is created using [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createPanel-(System-API)). This method can be used to set, display, hide, and move the panel, as well as subscribe to events. It is applicable to scenarios where a custom operation UI needs to be displayed to users after word selection is complete.

**Since:** 24

**Deprecated since:** -1

<!--Device-selectionManager-interface Panel--><!--Device-selectionManager-interface Panel-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';
```

## moveToGlobalDisplay

```TypeScript
moveToGlobalDisplay(x: number, y: number): Promise<void>
```

Moves the word selection panel to the specified coordinates in the global coordinates system of the screen. The panel can be moved to an extended screen. This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createPanel-(System-API)). This API uses a promise to return the result.

**Since:** 24

**Deprecated since:** -1

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
| Promise & lt;void & gt; |

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

## offDestroy

```TypeScript
offDestroy(callback?: Callback<void>): void
```

Unregisters the callback used to listen for the destroy event of the word selection panel. This API uses an asynchronous callback to return the result. **ArkTS mode:** This API applies only to ArkTS-Sta.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-offDestroy(callback?: Callback<void>): void--><!--Device-Panel-offDestroy(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

## offHide

```TypeScript
offHide(callback?: Callback<void>): void
```

Unregisters the callback used to listen for the hide event of the word selection panel. This API uses an asynchronous callback to return the result. **ArkTS mode:** This API applies only to ArkTS-Sta.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-offHide(callback?: Callback<void>): void--><!--Device-Panel-offHide(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

## onDestroy

```TypeScript
onDestroy(callback: Callback<void>): void
```

Registers a callback to listen for the destroy event of the word selection panel. This API uses an asynchronous callback to return the result. **ArkTS mode:** This API applies only to ArkTS-Sta.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-onDestroy(callback: Callback<void>): void--><!--Device-Panel-onDestroy(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

## onHide

```TypeScript
onHide(callback: Callback<void>): void
```

Registers a callback to listen for the hide event of the word selection panel. This API uses an asynchronous callback to return the result. **ArkTS mode:** This API applies only to ArkTS-Sta.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-onHide(callback: Callback<void>): void--><!--Device-Panel-onHide(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |
