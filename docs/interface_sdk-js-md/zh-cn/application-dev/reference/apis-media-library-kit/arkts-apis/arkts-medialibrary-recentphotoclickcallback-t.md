# RecentPhotoClickCallback

```TypeScript
export type RecentPhotoClickCallback = (recentPhotoInfo: BaseItemInfo) => boolean
```

The callback of onRecentPhotoClick event

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export type RecentPhotoClickCallback = (recentPhotoInfo: BaseItemInfo) => boolean--><!--Device-unnamed-export type RecentPhotoClickCallback = (recentPhotoInfo: BaseItemInfo) => boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recentPhotoInfo | [BaseItemInfo](arkts-medialibrary-file-photopickercomponent-baseiteminfo-c.md) | 是 | The item information of recent photo |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | - |

