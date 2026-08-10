# RequestReadPermissionResult

Request read permission result

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

<!--Device-photoAccessHelper-export class RequestReadPermissionResult--><!--Device-photoAccessHelper-export class RequestReadPermissionResult-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## authorizedUris

```TypeScript
authorizedUris?: Array<string>
```

URIs that have been created and granted the save permission.

**类型：** Array&lt;string&gt;

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-RequestReadPermissionResult-authorizedUris?: Array<string>--><!--Device-RequestReadPermissionResult-authorizedUris?: Array<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## invalidUris

```TypeScript
invalidUris?: Array<string>
```

URIs that may be deleted, hidden, or renamed.

**类型：** Array&lt;string&gt;

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-RequestReadPermissionResult-invalidUris?: Array<string>--><!--Device-RequestReadPermissionResult-invalidUris?: Array<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

