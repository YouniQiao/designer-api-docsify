# PhotoBrowserChangeStartCallback

```TypeScript
export type PhotoBrowserChangeStartCallback = (targetPhotoInfo: BaseItemInfo) => void
```

Callback to be invoked when a grid view switches to the photo browser page or the photo browser page is switched.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export type PhotoBrowserChangeStartCallback = (targetPhotoInfo: BaseItemInfo) => void--><!--Device-unnamed-export type PhotoBrowserChangeStartCallback = (targetPhotoInfo: BaseItemInfo) => void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetPhotoInfo | [BaseItemInfo](arkts-medialibrary-file-photopickercomponent-baseiteminfo-c.md) | 是 | Basic information about the selected items. |

