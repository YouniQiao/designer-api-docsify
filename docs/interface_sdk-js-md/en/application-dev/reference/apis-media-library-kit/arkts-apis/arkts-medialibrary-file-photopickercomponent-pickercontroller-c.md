# PickerController

The class for PickerController

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Observed

<!--Device-unnamed-export declare class PickerController--><!--Device-unnamed-export declare class PickerController-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## addData

```TypeScript
public addData(dataType: DataType, data: Object): void
```

Add data to picker component

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerController-public addData(dataType: DataType, data: Object): void--><!--Device-PickerController-public addData(dataType: DataType, data: Object): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataType | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | data type |
| data | Object | Yes | data |

## completed

```TypeScript
public completed(): Promise<CompletedResult>
```

Call this method to obtain the complete data after a selection operation has finished.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerController-public completed(): Promise<CompletedResult>--><!--Device-PickerController-public completed(): Promise<CompletedResult>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;CompletedResult&gt; | Promise\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ |

## deleteData

```TypeScript
public deleteData(dataType: DataType, data: Object): void
```

Delete data to picker component

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerController-public deleteData(dataType: DataType, data: Object): void--><!--Device-PickerController-public deleteData(dataType: DataType, data: Object): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataType | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | data type |
| data | Object | Yes | data |

## exitPhotoBrowser

```TypeScript
public exitPhotoBrowser(): void
```

Exit photo browser.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerController-public exitPhotoBrowser(): void--><!--Device-PickerController-public exitPhotoBrowser(): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## replacePhotoPickerPreview

```TypeScript
public replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback<void>): void
```

Display the photo after edit.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerController-public replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback<void>): void--><!--Device-PickerController-public replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| originalUri | string | Yes | Original uri |
| newUri | string | Yes | New uri after replacement |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Returns void |

## saveTrustedPhotoAssets

```TypeScript
public saveTrustedPhotoAssets(trustedUris: string[], callback: AsyncCallback<string[]>,
    configs?: photoAccessHelper.PhotoCreationConfig[], saveMode?: SaveMode): void
```

Save the photo assets of uris.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerController-public saveTrustedPhotoAssets(trustedUris: string[], callback: AsyncCallback<string[]>,    configs?: photoAccessHelper.PhotoCreationConfig[], saveMode?: SaveMode): void--><!--Device-PickerController-public saveTrustedPhotoAssets(trustedUris: string[], callback: AsyncCallback<string[]>,    configs?: photoAccessHelper.PhotoCreationConfig[], saveMode?: SaveMode): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| trustedUris | string[] | Yes | Uris need to be saved |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string[]&gt; | Yes | Returns the uri list |
| configs | photoAccessHelper.PhotoCreationConfig[] | No | Photo asset creation configs |
| saveMode | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Mode of save |

## setData

```TypeScript
public setData(dataType: DataType, data: Object): void
```

Set data to picker component

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerController-public setData(dataType: DataType, data: Object): void--><!--Device-PickerController-public setData(dataType: DataType, data: Object): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataType | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | data type |
| data | Object | Yes | data |

## setMaxSelected

```TypeScript
public setMaxSelected(maxSelected: MaxSelected): void
```

Set max select count to picker component, include max\_total\_count, max\_photo\_count and max\_video\_count.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerController-public setMaxSelected(maxSelected: MaxSelected): void--><!--Device-PickerController-public setMaxSelected(maxSelected: MaxSelected): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| maxSelected | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | max select count data |

## setPhotoBrowserItem

```TypeScript
public setPhotoBrowserItem(uri: string, photoBrowserRange?: PhotoBrowserRange): void
```

Set photo browser item to picker component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerController-public setPhotoBrowserItem(uri: string, photoBrowserRange?: PhotoBrowserRange): void--><!--Device-PickerController-public setPhotoBrowserItem(uri: string, photoBrowserRange?: PhotoBrowserRange): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | specify image uri for photo browsing |
| photoBrowserRange | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | photo browser slide range |

## setPhotoBrowserUIElementVisibility

```TypeScript
public setPhotoBrowserUIElementVisibility(elements: PhotoBrowserUIElement[], isVisible: boolean): void
```

Sets whether other elements on the photo browser page are visible.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerController-public setPhotoBrowserUIElementVisibility(elements: PhotoBrowserUIElement[], isVisible: boolean): void--><!--Device-PickerController-public setPhotoBrowserUIElementVisibility(elements: PhotoBrowserUIElement[], isVisible: boolean): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elements | \_\_\_MD\_LINK\_USD\_0\_\_\_[] | Yes | other elements on the photo browser page |
| isVisible | boolean | Yes | visible or not |

