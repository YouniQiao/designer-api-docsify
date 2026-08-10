# PhotoSelectOptions

Defines additional options for selecting media assets from Gallery. It inherits from **BaseSelectOptions**. It is used to start the picker of the corresponding user ID space.

**继承/实现关系：** PhotoSelectOptions extends [BaseSelectOptions](arkts-medialibrary-photoaccesshelper-baseselectoptions-c.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为26.0.0。

<!--Device-photoAccessHelper-class PhotoSelectOptions extends BaseSelectOptions--><!--Device-photoAccessHelper-class PhotoSelectOptions extends BaseSelectOptions-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## completeButtonText

```TypeScript
completeButtonText?: CompleteButtonText
```

Text displayed on the complete button.

The complete button is located in the lower-right corner of the page. It is used by users to signify that they have finished selecting images.

**类型：** [CompleteButtonText](arkts-medialibrary-photoaccesshelper-completebuttontext-e.md)

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSelectOptions-completeButtonText?: CompleteButtonText--><!--Device-PhotoSelectOptions-completeButtonText?: CompleteButtonText-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## contextRecoveryInfo

```TypeScript
contextRecoveryInfo?: ContextRecoveryInfo
```

Information for restoring the PhotoPicker's state from the last exit.

When the selection process is complete, the PhotoPicker returns **contextRecoveryInfo** to the application. The application can then use the information to restore the PhotoPicker's state and the last viewed grid interface the next time it starts the PhotoPicker.

**类型：** [ContextRecoveryInfo](arkts-medialibrary-photoaccesshelper-contextrecoveryinfo-c.md)

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSelectOptions-contextRecoveryInfo?: ContextRecoveryInfo--><!--Device-PhotoSelectOptions-contextRecoveryInfo?: ContextRecoveryInfo-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isDestroyedWithNavigation

```TypeScript
isDestroyedWithNavigation?: boolean
```

Whether destruction with   
[Navigation](../../apis-arkui/arkts-apis/arkts-arkui-navigation-navigation-f.md/arkts-arkui-navigation-navigation-f.md#navigation) is supported. **true** if supported, **false** otherwise. The default value is **false**.

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSelectOptions-isDestroyedWithNavigation?: boolean--><!--Device-PhotoSelectOptions-isDestroyedWithNavigation?: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isEditSupported

```TypeScript
isEditSupported?: boolean
```

Whether the image can be edited. **true** if editable, **false** otherwise.

**类型：** boolean

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSelectOptions-isEditSupported?: boolean--><!--Device-PhotoSelectOptions-isEditSupported?: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isOriginalSupported

```TypeScript
isOriginalSupported?: boolean
```

Whether to display the button for selecting the original image. **true** to display, **false** otherwise. The default value is **false**.

**类型：** boolean

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSelectOptions-isOriginalSupported?: boolean--><!--Device-PhotoSelectOptions-isOriginalSupported?: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isReturnToPhotoBrowserEnabled

```TypeScript
isReturnToPhotoBrowserEnabled?: boolean
```

Whether to automatically switch to the full image preview mode after a photo is taken in single-selection mode.   
**true** means to switch, and **false** means the opposite. The default value is **false**.

Note: This parameter takes effect only when   
[SingleSelectionMode](arkts-medialibrary-photoaccesshelper-singleselectionmode-e.md) is set to   
**BROWSER_MODE** or **BROWSER_AND_SELECT_MODE** and   
[BaseSelectOptions.isPreviewForSingleSelectionSupported](arkts-medialibrary-photoaccesshelper-baseselectoptions-c.md)is set to **true**.

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSelectOptions-isReturnToPhotoBrowserEnabled?: boolean--><!--Device-PhotoSelectOptions-isReturnToPhotoBrowserEnabled?: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isSelectionNumberVisible

```TypeScript
isSelectionNumberVisible?: boolean
```

Support displaying index numbers.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSelectOptions-isSelectionNumberVisible?: boolean--><!--Device-PhotoSelectOptions-isSelectionNumberVisible?: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isSelectionOrderAdjustable

```TypeScript
isSelectionOrderAdjustable?: boolean
```

Support selection order adjustment.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSelectOptions-isSelectionOrderAdjustable?: boolean--><!--Device-PhotoSelectOptions-isSelectionOrderAdjustable?: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## maxPhotoSelectNumber

```TypeScript
maxPhotoSelectNumber?: int
```

Maximum number of photos that can be selected. 

A maximum of 500 photos can be selected. The default value is **500**.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSelectOptions-maxPhotoSelectNumber?: int--><!--Device-PhotoSelectOptions-maxPhotoSelectNumber?: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## maxVideoSelectNumber

```TypeScript
maxVideoSelectNumber?: int
```

Maximum number of videos that can be selected. 

A maximum of 500 videos can be selected. The default value is **500**.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSelectOptions-maxVideoSelectNumber?: int--><!--Device-PhotoSelectOptions-maxVideoSelectNumber?: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## subWindowName

```TypeScript
subWindowName?: string
```

Name of the child window.

**类型：** string

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSelectOptions-subWindowName?: string--><!--Device-PhotoSelectOptions-subWindowName?: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

