# getPhotoAccessHelper (System API)

## Modules to Import

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## getPhotoAccessHelper

```TypeScript
function getPhotoAccessHelper(context: Context, userId: int): PhotoAccessHelper
```

Obtains a PhotoAccessHelper instance for the specified user, letting you access and modify media files in an album.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-photoAccessHelper-function getPhotoAccessHelper(context: Context, userId: int): PhotoAccessHelper--><!--Device-photoAccessHelper-function getPhotoAccessHelper(context: Context, userId: int): PhotoAccessHelper-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c-sys.md) | Yes | Context of the ability instance. |
| userId | int | Yes | ID of the user. |

**Return value:**

| Type | Description |
| --- | --- |
| [PhotoAccessHelper](arkts-medialibrary-sendablephotoaccesshelper-photoaccesshelper-i-sys.md) | PhotoAccessHelper instance obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 201 | Permission denied |
| 202 | Called by non-system application |

## Examples

```TypeScript
// The phAccessHelper instance obtained is a global object. It is used by default in subsequent operations. If the code snippet is not added, an error will be reported indicating that phAccessHelper is not defined.
// Obtain the context from the component and ensure that the return value of this.getUiContext().getHostContext() is UIAbilityContext.
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Button("example").onClick(async () => {
        let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
        // 101 indicates the user ID of another user space.
        let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context, 101);
      }).width('100%')
    }
    .height('90%')
  }
}
```


## getPhotoAccessHelper

```TypeScript
function getPhotoAccessHelper(context: Context, userId: int): PhotoAccessHelper | null
```

Obtains a PhotoAccessHelper instance for accessing and modifying media files in the album.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-photoAccessHelper-function getPhotoAccessHelper(context: Context, userId: int): PhotoAccessHelper | null--><!--Device-photoAccessHelper-function getPhotoAccessHelper(context: Context, userId: int): PhotoAccessHelper | null-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c-sys.md) | Yes | Context of the ability instance. |
| userId | int | Yes | Target userId |

**Return value:**

| Type | Description |
| --- | --- |
| [PhotoAccessHelper](arkts-medialibrary-sendablephotoaccesshelper-photoaccesshelper-i-sys.md) | Instance of PhotoAccessHelper. if the operation fails, returns null. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied |
| 202 | Called by non-system application |
| 23800151 | Scene parameters validate failed, possible causes: &lt;br&gt;1. userId is invalid. |

