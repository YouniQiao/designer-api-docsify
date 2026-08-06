# OperationItem

Describes the settings for filtering media files.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 26.0.0.

<!--Device-photoAccessHelper-export class OperationItem--><!--Device-photoAccessHelper-export class OperationItem-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## field

```TypeScript
field?: PhotoKeys
```

Column name in the data table.

Currently, only the following key fields are supported: **URI**, **PHOTO\_TYPE**, **DISPLAY\_NAME**, **SIZE**,  
**DURATION**, **WIDTH**, **HEIGHT**, **ORIENTATION**, **FAVORITE**, **TITLE**, **POSITION**, **PHOTO\_SUBTYPE**,  
**DYNAMIC\_RANGE\_TYPE**, **COVER\_POSITION**, **BURST\_KEY**, **LCD\_SIZE**, **THM\_SIZE**, **DETAIL\_TIME**,  
**MEDIA\_SUFFIX**, **OWNER\_ALBUM\_ID**, **ASPECT\_RATIO** and **DATE\_TAKEN\_MS**.

When  
[select]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_is used to set this parameter, an invalid field results in error code 401. When  
[@ohos.file.PhotoPickerComponent (PhotoPickerComponent)]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ is used to set this parameter, an invalid field does not trigger the **onPickerControllerReady** callback.

This field is not involved in non-conditional predicates such as **and**, **or**, **beginWrap**, and **endWrap**.

**Type:** PhotoKeys

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-OperationItem-field?: PhotoKeys--><!--Device-OperationItem-field?: PhotoKeys-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## operationType

```TypeScript
operationType: OperationType
```

Predicates.

**Type:** OperationType

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-OperationItem-operationType: OperationType--><!--Device-OperationItem-operationType: OperationType-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## value

```TypeScript
value?: Array<OperationValueType>
```

Values needed for matching different predicates.

This field is not involved in non-conditional predicates such as **and**, **or**, **beginWrap**, and **endWrap**.

The maximum length is 10; if exceeded, only the first 10 values are considered.

**Type:** Array&lt;OperationValueType&gt;

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-OperationItem-value?: Array<OperationValueType>--><!--Device-OperationItem-value?: Array<OperationValueType>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

