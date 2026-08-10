# OperationItem

Describes the settings for filtering media files.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

<!--Device-photoAccessHelper-export class OperationItem--><!--Device-photoAccessHelper-export class OperationItem-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## field

```TypeScript
field?: PhotoKeys
```

Column name in the data table.

Currently, only the following key fields are supported: **URI**, **PHOTO_TYPE**, **DISPLAY_NAME**, **SIZE**,   
**DURATION**, **WIDTH**, **HEIGHT**, **ORIENTATION**, **FAVORITE**, **TITLE**, **POSITION**, **PHOTO_SUBTYPE**,   
**DYNAMIC_RANGE_TYPE**, **COVER_POSITION**, **BURST_KEY**, **LCD_SIZE**, **THM_SIZE**, **DETAIL_TIME**,   
**MEDIA_SUFFIX**, **OWNER_ALBUM_ID**, **ASPECT_RATIO** and **DATE_TAKEN_MS**.

When   
[select](arkts-medialibrary-photoaccesshelper-photoviewpicker-c.md#select)is used to set this parameter, an invalid field results in error code 401. When   
[@ohos.file.PhotoPickerComponent (PhotoPickerComponent)](arkts-file-photopickercomponent.md) is used to set this parameter, an invalid field does not trigger the **onPickerControllerReady** callback.

This field is not involved in non-conditional predicates such as **and**, **or**, **beginWrap**, and **endWrap**.

**类型：** [PhotoKeys](arkts-medialibrary-photoaccesshelper-photokeys-e.md)

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-OperationItem-field?: PhotoKeys--><!--Device-OperationItem-field?: PhotoKeys-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## operationType

```TypeScript
operationType: OperationType
```

Predicates.

**类型：** [OperationType](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-operationtype-e.md)

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-OperationItem-operationType: OperationType--><!--Device-OperationItem-operationType: OperationType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## value

```TypeScript
value?: Array<OperationValueType>
```

Values needed for matching different predicates.

This field is not involved in non-conditional predicates such as **and**, **or**, **beginWrap**, and **endWrap**.

The maximum length is 10; if exceeded, only the first 10 values are considered.

**类型：** Array&lt;OperationValueType&gt;

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-OperationItem-value?: Array<OperationValueType>--><!--Device-OperationItem-value?: Array<OperationValueType>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

