# Options

Options

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

<!--Device-unnamed-export interface Options<T extends ViewModel, Data = DefaultData<T>>--><!--Device-unnamed-export interface Options<T extends ViewModel, Data = DefaultData<T>>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onActive

```TypeScript
onActive?(): void
```

Listens for page active. Called when the page is active.

**Since:** 5

**ArkTS mode:** ArkTS-Dyn only, since version 5.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Options-onActive?(): void--><!--Device-Options-onActive?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onBackPress

```TypeScript
onBackPress?(): boolean
```

Listens for the back button action. The back button is tapped:

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Options-onBackPress?(): boolean--><!--Device-Options-onBackPress?(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true means that the page processes the return logic. |

## onCompleteContinuation

```TypeScript
onCompleteContinuation?(code: number): void
```

The callback for the completion of the migration, which is triggered on the calling side, indicates the result of the application migration to the target device.

**Since:** 5

**ArkTS mode:** ArkTS-Dyn only, since version 5.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Options-onCompleteContinuation?(code: number): void--><!--Device-Options-onCompleteContinuation?(code: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | number | Yes |  |

## onConfigurationUpdated

```TypeScript
onConfigurationUpdated?(configuration: Configuration): void
```

This callback is triggered when the corresponding system configuration changes, such as system font size, language region, etc.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Options-onConfigurationUpdated?(configuration: Configuration): void--><!--Device-Options-onConfigurationUpdated?(configuration: Configuration): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| configuration | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |

## onCreate

```TypeScript
onCreate?(): void
```

Listens for application creation. Called when the application is created.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Options-onCreate?(): void--><!--Device-Options-onCreate?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDestroy

```TypeScript
onDestroy?(): void
```

Listens for page destruction. Called when the page is destroyed.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Options-onDestroy?(): void--><!--Device-Options-onDestroy?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onHide

```TypeScript
onHide?(): void
```

Listens for page hiding. Called when the page disappears.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Options-onHide?(): void--><!--Device-Options-onHide?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onInactive

```TypeScript
onInactive?(): void
```

Listens for page inactive. Called when the page is paused.

**Since:** 5

**ArkTS mode:** ArkTS-Dyn only, since version 5.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Options-onInactive?(): void--><!--Device-Options-onInactive?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onInit

```TypeScript
onInit?(): void
```

Listens for page initialization. Called when page initialization is complete. This function is called only once in a lifecycle.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Options-onInit?(): void--><!--Device-Options-onInit?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onNewRequest

```TypeScript
onNewRequest?(): void
```

This callback is triggered when a new request is received when the FA has started.

**Since:** 5

**ArkTS mode:** ArkTS-Dyn only, since version 5.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Options-onNewRequest?(): void--><!--Device-Options-onNewRequest?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onReady

```TypeScript
onReady?(): void
```

Listens for page creation. Called when a page is created. This function is called only once in a lifecycle.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Options-onReady?(): void--><!--Device-Options-onReady?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onRestoreData

```TypeScript
onRestoreData?(value: object): void
```

The callback to restore the data saved by the onSaveData method when the migration was initiated.

**Since:** 5

**ArkTS mode:** ArkTS-Dyn only, since version 5.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Options-onRestoreData?(value: object): void--><!--Device-Options-onRestoreData?(value: object): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | object | Yes |  |

## onSaveData

```TypeScript
onSaveData?(value: object): void
```

For the callback of saving state data, the developer needs to fill in the parameter object the data to be migrated to the target device.

**Since:** 5

**ArkTS mode:** ArkTS-Dyn only, since version 5.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Options-onSaveData?(value: object): void--><!--Device-Options-onSaveData?(value: object): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | object | Yes |  |

## onShow

```TypeScript
onShow?(): void
```

Listens for page display. Called when the page is displayed.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Options-onShow?(): void--><!--Device-Options-onShow?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onStartContinuation

```TypeScript
onStartContinuation?(): boolean
```

Callback when FA initiates a migration, in this callback, the application can decide whether to migrate according to the current state.

**Since:** 5

**ArkTS mode:** ArkTS-Dyn only, since version 5.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Options-onStartContinuation?(): boolean--><!--Device-Options-onStartContinuation?(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## data

```TypeScript
data?: Data
```

Data model of the page that can be converted into a JSON object. The attribute name cannot start with \$ or an underscore (\_) or contain the reserved words such as for, if, show, and tid. For a function, the return value must be an object. Set the value of data to the return value of the function during page initialization.

**Type:** Data

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Options-data?: Data--><!--Device-Options-data?: Data-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

