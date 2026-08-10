# getPhotoAccessHelper（系统接口）

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## getPhotoAccessHelper

```TypeScript
function getPhotoAccessHelper(context: Context, userId: int): PhotoAccessHelper
```

Obtains a PhotoAccessHelper instance for the specified user, letting you access and modify media files in an album.

**起始版本：** 19

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为19。

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-photoAccessHelper-function getPhotoAccessHelper(context: Context, userId: int): PhotoAccessHelper--><!--Device-photoAccessHelper-function getPhotoAccessHelper(context: Context, userId: int): PhotoAccessHelper-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c-sys.md) | 是 | Context of the ability instance. |
| userId | int | 是 | ID of the user. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PhotoAccessHelper](arkts-medialibrary-sendablephotoaccesshelper-photoaccesshelper-i-sys.md) | PhotoAccessHelper instance obtained. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument |
| 201 | Permission denied |
| 202 | Called by non-system application |

## 示例

```TypeScript
// 此处获取的phAccessHelper实例为全局对象，后续使用到phAccessHelper的地方默认为使用此处获取的对象，如未添加此段代码报phAccessHelper未定义的错误请自行添加。
// 请在组件内获取context，确保this.getUiContext().getHostContext()返回结果为UIAbilityContext
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Button("example").onClick(async () => {
        let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
        // 此处101表示其他用户空间的userid
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

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-photoAccessHelper-function getPhotoAccessHelper(context: Context, userId: int): PhotoAccessHelper | null--><!--Device-photoAccessHelper-function getPhotoAccessHelper(context: Context, userId: int): PhotoAccessHelper | null-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c-sys.md) | 是 | Context of the ability instance. |
| userId | int | 是 | Target userId |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PhotoAccessHelper](arkts-medialibrary-sendablephotoaccesshelper-photoaccesshelper-i-sys.md) | Instance of PhotoAccessHelper. if the operation fails, returns null. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 202 | Called by non-system application |
| 23800151 | Scene parameters validate failed, possible causes: &lt;br&gt;1. userId is invalid. |

