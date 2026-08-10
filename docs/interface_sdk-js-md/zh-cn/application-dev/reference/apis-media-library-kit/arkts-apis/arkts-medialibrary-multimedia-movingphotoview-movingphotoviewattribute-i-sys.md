# MovingPhotoViewAttribute

Defines the moving photo view attribute functions.

**继承/实现关系：** MovingPhotoViewAttribute extends [CommonMethod](../../apis-arkui/arkts-apis/arkts-arkui-common-commonmethod-i.md/arkts-arkui-common-commonmethod-i.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export declare interface MovingPhotoViewAttribute extends CommonMethod--><!--Device-unnamed-export declare interface MovingPhotoViewAttribute extends CommonMethod-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## setPlaybackStrategy

```TypeScript
setPlaybackStrategy(strategy: media.PlaybackStrategy): MovingPhotoViewAttribute
```

Sets playback strategy.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MovingPhotoViewAttribute-setPlaybackStrategy(strategy: media.PlaybackStrategy): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-setPlaybackStrategy(strategy: media.PlaybackStrategy): MovingPhotoViewAttribute-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategy | media.PlaybackStrategy | 是 | playback strategy |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MovingPhotoViewAttribute](arkts-medialibrary-multimedia-movingphotoview-movingphotoviewattribute-i-sys.md) |  |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 202 | Non-system applications are not allowed to use system APIs. |

