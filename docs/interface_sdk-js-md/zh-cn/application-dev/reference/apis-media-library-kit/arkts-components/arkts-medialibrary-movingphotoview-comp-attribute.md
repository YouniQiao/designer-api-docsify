# MovingPhotoView属性/事件

```TypeScript
declare class MovingPhotoViewAttribute extends CommonMethod<MovingPhotoViewAttribute>
```

定义动态照片属性函数。

**继承/实现关系：** MovingPhotoViewAttribute extends CommonMethod&lt;MovingPhotoViewAttribute&gt;

**起始版本：** 12

<!--Device-unnamed-declare class MovingPhotoViewAttribute extends CommonMethod<MovingPhotoViewAttribute>--><!--Device-unnamed-declare class MovingPhotoViewAttribute extends CommonMethod<MovingPhotoViewAttribute>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute, PixelMapFormat, DynamicRangeMode, DisplayMode } from '@kit.MediaLibraryKit';
```

## autoPlay

```TypeScript
autoPlay(isAutoPlay: boolean)
```

设置是否允许自动播放。如果该值为true，则移动照片开始在资源加载完成后自动执行。

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewAttribute-autoPlay(isAutoPlay: boolean): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-autoPlay(isAutoPlay: boolean): MovingPhotoViewAttribute-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isAutoPlay | boolean | 是 | Whether to automatic play |

## autoPlayPeriod

```TypeScript
autoPlayPeriod(startTime: number, endTime: number)
```

设置自动播放时间，如果不设置，则在整个视频时间内播放动态图片。如果设置，则在自动播放时段内播放移动照片。

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewAttribute-autoPlayPeriod(startTime: double, endTime: double): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-autoPlayPeriod(startTime: double, endTime: double): MovingPhotoViewAttribute-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startTime | number | 是 | 视频播放开始时间 |
| endTime | number | 是 | 视频播放结束时间 |

## enableAnalyzer

```TypeScript
enableAnalyzer(enabled: boolean)
```

设置是否启用动态照片分析器。如果为true，则移动照片可以被AI分析。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewAttribute-enableAnalyzer(enabled: boolean): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-enableAnalyzer(enabled: boolean): MovingPhotoViewAttribute-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否启用动态照片分析器 |

## muted

```TypeScript
muted(isMuted: boolean)
```

判断视频是否静音时调用。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewAttribute-muted(isMuted: boolean): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-muted(isMuted: boolean): MovingPhotoViewAttribute-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isMuted | boolean | 是 |  |

## objectFit

```TypeScript
objectFit(value: ImageFit)
```

在确定视图的缩放类型时调用。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewAttribute-objectFit(value: ImageFit): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-objectFit(value: ImageFit): MovingPhotoViewAttribute-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageFit](../../apis-arkui/arkts-apis/arkts-arkui-imagefit-e.md) | 是 |  |

## onComplete

```TypeScript
onComplete(callback: MovingPhotoViewEventCallback)
```

在图像加载完成时调用。

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewAttribute-onComplete(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-onComplete(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [MovingPhotoViewEventCallback](arkts-medialibrary-movingphotoview-comp-movingphotovieweventcallback-t.md) | 是 |  |

## onError

```TypeScript
onError(callback: MovingPhotoViewEventCallback)
```

播放失败时调用。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewAttribute-onError(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-onError(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [MovingPhotoViewEventCallback](arkts-medialibrary-movingphotoview-comp-movingphotovieweventcallback-t.md) | 是 |  |

## onFinish

```TypeScript
onFinish(callback: MovingPhotoViewEventCallback)
```

当视频播放结束时调用。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewAttribute-onFinish(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-onFinish(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [MovingPhotoViewEventCallback](arkts-medialibrary-movingphotoview-comp-movingphotovieweventcallback-t.md) | 是 |  |

## onPause

```TypeScript
onPause(callback: MovingPhotoViewEventCallback)
```

当视频播放暂停时调用。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewAttribute-onPause(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-onPause(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [MovingPhotoViewEventCallback](arkts-medialibrary-movingphotoview-comp-movingphotovieweventcallback-t.md) | 是 |  |

## onPrepared

```TypeScript
onPrepared(callback: MovingPhotoViewEventCallback)
```

在播放准备时调用。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewAttribute-onPrepared(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-onPrepared(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [MovingPhotoViewEventCallback](arkts-medialibrary-movingphotoview-comp-movingphotovieweventcallback-t.md) | 是 |  |

## onStart

```TypeScript
onStart(callback: MovingPhotoViewEventCallback)
```

在播放视频时调用。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewAttribute-onStart(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-onStart(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [MovingPhotoViewEventCallback](arkts-medialibrary-movingphotoview-comp-movingphotovieweventcallback-t.md) | 是 |  |

## onStop

```TypeScript
onStop(callback: MovingPhotoViewEventCallback)
```

当视频播放停止时调用。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewAttribute-onStop(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-onStop(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [MovingPhotoViewEventCallback](arkts-medialibrary-movingphotoview-comp-movingphotovieweventcallback-t.md) | 是 |  |

## repeatPlay

```TypeScript
repeatPlay(isRepeatPlay: boolean)
```

设置是否允许重复播放。如果值为true，则播放动态图片资源加载完成后，重复执行。

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务中使用。

<!--Device-MovingPhotoViewAttribute-repeatPlay(isRepeatPlay: boolean): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-repeatPlay(isRepeatPlay: boolean): MovingPhotoViewAttribute-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isRepeatPlay | boolean | 是 | 是否重复播放 |
