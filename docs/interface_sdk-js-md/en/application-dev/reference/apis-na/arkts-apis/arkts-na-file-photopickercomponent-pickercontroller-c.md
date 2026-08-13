# PickerController

The class for PickerController

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export declare class PickerController--><!--Device-unnamed-export declare class PickerController-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## addData

```TypeScript
public addData(dataType: DataType, data: Object): void
```

Add data to picker component

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerController-public addData(dataType: DataType, data: Object): void--><!--Device-PickerController-public addData(dataType: DataType, data: Object): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataType | [DataType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-datatype-e.md) | Yes | data type |
| data | Object | Yes | data |

## completed

```TypeScript
public completed(): Promise<CompletedResult>
```

Call this method to obtain the complete data after a selection operation has finished.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerController-public completed(): Promise<CompletedResult>--><!--Device-PickerController-public completed(): Promise<CompletedResult>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[CompletedResult](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-completedresult-c.md)&gt; | Promise&lt;CompletedResult&gt; |

## deleteData

```TypeScript
public deleteData(dataType: DataType, data: Object): void
```

Delete data to picker component

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerController-public deleteData(dataType: DataType, data: Object): void--><!--Device-PickerController-public deleteData(dataType: DataType, data: Object): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataType | [DataType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-datatype-e.md) | Yes | data type |
| data | Object | Yes | data |

## exitPhotoBrowser

```TypeScript
public exitPhotoBrowser(): void
```

Exit photo browser.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

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

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerController-public replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback<void>): void--><!--Device-PickerController-public replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| originalUri | string | Yes | Original uri |
| newUri | string | Yes | New uri after replacement |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Returns void |

## saveTrustedPhotoAssets

```TypeScript
public saveTrustedPhotoAssets(trustedUris: string[], callback: AsyncCallback<string[]>,
    configs?: photoAccessHelper.PhotoCreationConfig[], saveMode?: SaveMode): void
```

Save the photo assets of uris.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerController-public saveTrustedPhotoAssets(trustedUris: string[], callback: AsyncCallback<string[]>,    configs?: photoAccessHelper.PhotoCreationConfig[], saveMode?: SaveMode): void--><!--Device-PickerController-public saveTrustedPhotoAssets(trustedUris: string[], callback: AsyncCallback<string[]>,    configs?: photoAccessHelper.PhotoCreationConfig[], saveMode?: SaveMode): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| trustedUris | string[] | Yes | Uris need to be saved |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string[]&gt; | Yes | Returns the uri list |
| configs | photoAccessHelper.PhotoCreationConfig[] | No | Photo asset creation configs |
| saveMode | [SaveMode](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-savemode-e.md) | No | Mode of save |

## setData

```TypeScript
public setData(dataType: DataType, data: Object): void
```

Set data to picker component

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerController-public setData(dataType: DataType, data: Object): void--><!--Device-PickerController-public setData(dataType: DataType, data: Object): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataType | [DataType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-datatype-e.md) | Yes | data type |
| data | Object | Yes | data |

## setMaxSelected

```TypeScript
public setMaxSelected(maxSelected: MaxSelected): void
```

Set max select count to picker component, include max_total_count, max_photo_count and max_video_count.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerController-public setMaxSelected(maxSelected: MaxSelected): void--><!--Device-PickerController-public setMaxSelected(maxSelected: MaxSelected): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| maxSelected | [MaxSelected](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-maxselected-c.md) | Yes | max select count data |

## setPhotoBrowserItem

```TypeScript
public setPhotoBrowserItem(uri: string, photoBrowserRange?: PhotoBrowserRange): void
```

Set photo browser item to picker component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerController-public setPhotoBrowserItem(uri: string, photoBrowserRange?: PhotoBrowserRange): void--><!--Device-PickerController-public setPhotoBrowserItem(uri: string, photoBrowserRange?: PhotoBrowserRange): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | specify image uri for photo browsing |
| photoBrowserRange | [PhotoBrowserRange](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-photobrowserrange-e.md) | No | photo browser slide range |

## setPhotoBrowserUIElementVisibility

```TypeScript
public setPhotoBrowserUIElementVisibility(elements: PhotoBrowserUIElement[], isVisible: boolean): void
```

Sets whether other elements on the photo browser page are visible.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerController-public setPhotoBrowserUIElementVisibility(elements: PhotoBrowserUIElement[], isVisible: boolean): void--><!--Device-PickerController-public setPhotoBrowserUIElementVisibility(elements: PhotoBrowserUIElement[], isVisible: boolean): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elements | [PhotoBrowserUIElement](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-photobrowseruielement-e.md)[] | Yes | other elements on the photo browser page |
| isVisible | boolean | Yes | visible or not |

