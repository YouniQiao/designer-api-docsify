# PhotoSelectResult

Defines information about the images or videos selected.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为26.0.0。

<!--Device-photoAccessHelper-class PhotoSelectResult--><!--Device-photoAccessHelper-class PhotoSelectResult-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## contextRecoveryInfo

```TypeScript
contextRecoveryInfo: ContextRecoveryInfo
```

Information about the context of exiting the PhotoPicker. This information is returned when the selection process is complete and is used by the application within **PhotoSelectOptions** during the subsequent launch of the PhotoPicker to restore the state from the previous exit.

**类型：** [ContextRecoveryInfo](arkts-medialibrary-photoaccesshelper-contextrecoveryinfo-c.md)

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSelectResult-contextRecoveryInfo: ContextRecoveryInfo--><!--Device-PhotoSelectResult-contextRecoveryInfo: ContextRecoveryInfo-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isOriginalPhoto

```TypeScript
isOriginalPhoto: boolean
```

Whether the selected media file is the original image. **true** if yes, **false** otherwise. The default value is  
**false**.

**类型：** boolean

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSelectResult-isOriginalPhoto: boolean--><!--Device-PhotoSelectResult-isOriginalPhoto: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## movingPhotoBadgeStates

```TypeScript
movingPhotoBadgeStates: Array<MovingPhotoBadgeStateType>
```

Array of moving photo badge states for the media files selected from Gallery.

If **isMovingPhotoBadgeShown** is set to **true**, this array contains the moving photo badge states. Otherwise, it is empty.

**类型：** Array&lt;MovingPhotoBadgeStateType&gt;

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSelectResult-movingPhotoBadgeStates: Array<MovingPhotoBadgeStateType>--><!--Device-PhotoSelectResult-movingPhotoBadgeStates: Array<MovingPhotoBadgeStateType>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## photoUris

```TypeScript
photoUris: Array<string>
```

URIs of the media files selected.

This URI array can be used only by calling the   
[photoAccessHelper.getAssets](arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#getassets)API through temporary authorization. For details, see   
[Using a Media File URI](../../../file-management/user-file-uri-intro.md#using-a-media-file-uri).

**类型：** Array&lt;string&gt;

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSelectResult-photoUris: Array<string>--><!--Device-PhotoSelectResult-photoUris: Array<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

