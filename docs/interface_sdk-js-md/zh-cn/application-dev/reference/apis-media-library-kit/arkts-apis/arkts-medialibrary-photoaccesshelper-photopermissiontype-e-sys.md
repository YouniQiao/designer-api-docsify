# PhotoPermissionType（系统接口）

Enumerates the types of permissions for accessing media assets.

The permissions include temporary read permission and persistent read permission. The temporary read permission will be removed when the application is dead, while the persistent read permission will not.

For the same media asset and application, the persistent read permission overwrites the temporary read permission. The temporary read permission does not overwrite the persistent read permission.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-enum PhotoPermissionType--><!--Device-photoAccessHelper-enum PhotoPermissionType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## TEMPORARY_READ_IMAGEVIDEO

```TypeScript
TEMPORARY_READ_IMAGEVIDEO = 0
```

Temporary read permission.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-PhotoPermissionType-TEMPORARY_READ_IMAGEVIDEO = 0--><!--Device-PhotoPermissionType-TEMPORARY_READ_IMAGEVIDEO = 0-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## PERSISTENT_READ_IMAGEVIDEO

```TypeScript
PERSISTENT_READ_IMAGEVIDEO = 1
```

Persistent read permission.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-PhotoPermissionType-PERSISTENT_READ_IMAGEVIDEO = 1--><!--Device-PhotoPermissionType-PERSISTENT_READ_IMAGEVIDEO = 1-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

