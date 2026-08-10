# HideSensitiveType（系统接口）

Enumerates the types of data masking applied to media resources when accessed by an application.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-enum HideSensitiveType--><!--Device-photoAccessHelper-enum HideSensitiveType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## HIDE_LOCATION_AND_SHOOTING_PARAM

```TypeScript
HIDE_LOCATION_AND_SHOOTING_PARAM = 0
```

Masks geographic location and capture parameters.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-HideSensitiveType-HIDE_LOCATION_AND_SHOOTING_PARAM = 0--><!--Device-HideSensitiveType-HIDE_LOCATION_AND_SHOOTING_PARAM = 0-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## HIDE_LOCATION_ONLY

```TypeScript
HIDE_LOCATION_ONLY = 1
```

Masks geographic location information only.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-HideSensitiveType-HIDE_LOCATION_ONLY = 1--><!--Device-HideSensitiveType-HIDE_LOCATION_ONLY = 1-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## HIDE_SHOOTING_PARAM_ONLY

```TypeScript
HIDE_SHOOTING_PARAM_ONLY = 2
```

Masks capture parameters only.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-HideSensitiveType-HIDE_SHOOTING_PARAM_ONLY = 2--><!--Device-HideSensitiveType-HIDE_SHOOTING_PARAM_ONLY = 2-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## NO_HIDE_SENSITIVE_TYPE

```TypeScript
NO_HIDE_SENSITIVE_TYPE = 3
```

No data masking is applied.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-HideSensitiveType-NO_HIDE_SENSITIVE_TYPE = 3--><!--Device-HideSensitiveType-NO_HIDE_SENSITIVE_TYPE = 3-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## DEFAULT

```TypeScript
DEFAULT = 4
```

Applies data masking based on the   
[ohos.permission.MEDIA_LOCATION](../../../security/AccessToken/permissions-for-all-user.md#ohospermissionmedia_location)permission. The specifications are as follows:

- If this permission is available, no masking is applied.  
- If this permission is unavailable, geographic location is masked.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-HideSensitiveType-DEFAULT = 4--><!--Device-HideSensitiveType-DEFAULT = 4-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

