# NotifyChangeType

Enumerates the types of changes that trigger the media asset or album change events.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-enum NotifyChangeType--><!--Device-photoAccessHelper-enum NotifyChangeType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## NOTIFY_CHANGE_YUV_READY

```TypeScript
NOTIFY_CHANGE_YUV_READY = 3
```

A high-quality image is ready in deferred photo delivery scenarios.

Image quality metrics such as sharpness and color accuracy can be checked in the   
[OnDataPrepared](arkts-medialibrary-photoaccesshelper-quickimagedatahandler-i.md#ondataprepared)callback.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-NotifyChangeType-NOTIFY_CHANGE_YUV_READY = 3--><!--Device-NotifyChangeType-NOTIFY_CHANGE_YUV_READY = 3-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## NOTIFY_CHANGE_ADD_ANALYSIS

```TypeScript
NOTIFY_CHANGE_ADD_ANALYSIS = 4
```

A media asset (image or video) is created in the smart analysis album.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NotifyChangeType-NOTIFY_CHANGE_ADD_ANALYSIS = 4--><!--Device-NotifyChangeType-NOTIFY_CHANGE_ADD_ANALYSIS = 4-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## NOTIFY_CHANGE_REMOVE_ANALYSIS

```TypeScript
NOTIFY_CHANGE_REMOVE_ANALYSIS = 5
```

A media asset (image or video) is deleted from the smart analysis album.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NotifyChangeType-NOTIFY_CHANGE_REMOVE_ANALYSIS = 5--><!--Device-NotifyChangeType-NOTIFY_CHANGE_REMOVE_ANALYSIS = 5-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

