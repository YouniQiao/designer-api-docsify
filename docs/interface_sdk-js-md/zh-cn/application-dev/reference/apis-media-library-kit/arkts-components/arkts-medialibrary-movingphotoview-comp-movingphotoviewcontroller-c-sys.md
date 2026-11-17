# MovingPhotoViewController（系统接口）

```TypeScript
export class MovingPhotoViewController
```

定义MovePhotoView控制器。

**起始版本：** 12

<!--Device-unnamed-export class MovingPhotoViewController--><!--Device-unnamed-export class MovingPhotoViewController-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute, PixelMapFormat, DynamicRangeMode, DisplayMode } from '@kit.MediaLibraryKit';
```

## enableAutoPlay

```TypeScript
enableAutoPlay(enabled: boolean)
```

动态刷新autoplay属性，设置为true时将强制动态照片在初始化后进行播放

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewController-enableAutoPlay(enabled: boolean)--><!--Device-MovingPhotoViewController-enableAutoPlay(enabled: boolean)-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否自动播放 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-非系统应用调用系统-api) | Non-system applications are not allowed to use system APIs. |

## enableTransition

```TypeScript
enableTransition(enabled: boolean)
```

启用或禁用缩放过渡效果，可在初始化时设置

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewController-enableTransition(enabled: boolean)--><!--Device-MovingPhotoViewController-enableTransition(enabled: boolean)-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否启用过渡效果 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-非系统应用调用系统-api) | Non-system applications are not allowed to use system APIs. |

## notifyMovingPhotoTransition

```TypeScript
notifyMovingPhotoTransition(): void
```

通知组件执行图片转场动画。

**起始版本：** 23

<!--Device-MovingPhotoViewController-notifyMovingPhotoTransition(): void--><!--Device-MovingPhotoViewController-notifyMovingPhotoTransition(): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-非系统应用调用系统-api) | Non-system applications are not allowed to use system APIs. |

## pausePlayback

```TypeScript
pausePlayback()
```

暂停动态照片并显示当前帧，当从当前帧开始播放时再播放一次

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewController-pausePlayback()--><!--Device-MovingPhotoViewController-pausePlayback()-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-非系统应用调用系统-api) | Non-system applications are not allowed to use system APIs. |

## reset

```TypeScript
reset()
```

将动态照片播放选项重置为默认选项。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewController-reset()--><!--Device-MovingPhotoViewController-reset()-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-非系统应用调用系统-api) | Non-system applications are not allowed to use system APIs. |

## restart

```TypeScript
restart()
```

使用当前配置信息重新播放视频。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewController-restart()--><!--Device-MovingPhotoViewController-restart()-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-非系统应用调用系统-api) | Non-system applications are not allowed to use system APIs. |

## setDisplayMode

```TypeScript
setDisplayMode(mode: DisplayMode, callback: MovingPhotoViewEventCallback): void
```

设置动态照片显示模式，并在完成时触发回调。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MovingPhotoViewController-setDisplayMode(mode: DisplayMode, callback: MovingPhotoViewEventCallback): void--><!--Device-MovingPhotoViewController-setDisplayMode(mode: DisplayMode, callback: MovingPhotoViewEventCallback): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [DisplayMode](arkts-medialibrary-movingphotoview-comp-displaymode-e-sys.md) | 是 | 显示模式。 |
| callback | [MovingPhotoViewEventCallback](arkts-medialibrary-movingphotoview-comp-movingphotovieweventcallback-t.md) | 是 | Set display mode completion callback |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-非系统应用调用系统-api) | Permission verification failed. A non-system application calls a system API. |

## setPlaybackPeriod

```TypeScript
setPlaybackPeriod(startTime: number, endTime: number)
```

设置动态照片播放区间

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewController-setPlaybackPeriod(startTime: double, endTime: double)--><!--Device-MovingPhotoViewController-setPlaybackPeriod(startTime: double, endTime: double)-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startTime | number | 是 | 视频播放开始时间<br>取值范围:大于等于0，小于视频时长，非法值将不响应此次调用的操作。 |
| endTime | number | 是 | 视频播放结束时间<br>取值范围:大于等于0，小于视频时长，非法值将不响应此次调用的操作。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-非系统应用调用系统-api) | Non-system applications are not allowed to use system APIs. |

## startPlayback

```TypeScript
startPlayback(mode: DisplayMode): void
```

开始播放动态照片。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MovingPhotoViewController-startPlayback(mode: DisplayMode): void--><!--Device-MovingPhotoViewController-startPlayback(mode: DisplayMode): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [DisplayMode](arkts-medialibrary-movingphotoview-comp-displaymode-e-sys.md) | 是 | 显示模式。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-非系统应用调用系统-api) | Permission verification failed. A non-system application calls a system API. |
