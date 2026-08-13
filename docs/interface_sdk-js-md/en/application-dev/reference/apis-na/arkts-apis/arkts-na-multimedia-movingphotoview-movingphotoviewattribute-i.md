# MovingPhotoViewAttribute

Defines the moving photo view attribute functions.

**Inheritance/Implementation:** MovingPhotoViewAttribute extends CommonMethod

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface MovingPhotoViewAttribute--><!--Device-unnamed-export declare interface MovingPhotoViewAttribute-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## autoPlay

```TypeScript
autoPlay(isAutoPlay: boolean): MovingPhotoViewAttribute
```

Sets whether to allow automatic play. If the value is true, the moving photo starts automatic after the resource is loaded.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MovingPhotoViewAttribute-autoPlay(isAutoPlay: boolean): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-autoPlay(isAutoPlay: boolean): MovingPhotoViewAttribute-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isAutoPlay | boolean | Yes | Whether to automatic play |

**Return value:**

| Type | Description |
| --- | --- |
| [MovingPhotoViewAttribute](arkts-na-multimedia-movingphotoview-movingphotoviewattribute-i.md) |  |

## autoPlayPeriod

```TypeScript
autoPlayPeriod(startTime: double, endTime: double): MovingPhotoViewAttribute
```

Sets automatic play period, If not set, the moving photo plays in the full video duration. If set, the moving photo plays in the automatic play period.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MovingPhotoViewAttribute-autoPlayPeriod(startTime: double, endTime: double): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-autoPlayPeriod(startTime: double, endTime: double): MovingPhotoViewAttribute-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startTime | double | Yes | video plays start time |
| endTime | double | Yes | video plays end time |

**Return value:**

| Type | Description |
| --- | --- |
| [MovingPhotoViewAttribute](arkts-na-multimedia-movingphotoview-movingphotoviewattribute-i.md) |  |

## enableAnalyzer

```TypeScript
enableAnalyzer(enabled: boolean): MovingPhotoViewAttribute
```

Sets whether to enable moving photo analyzer. If the value is true, the moving photo can be analyzed by AI.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MovingPhotoViewAttribute-enableAnalyzer(enabled: boolean): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-enableAnalyzer(enabled: boolean): MovingPhotoViewAttribute-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | whether to enable moving photo analyzer |

**Return value:**

| Type | Description |
| --- | --- |
| [MovingPhotoViewAttribute](arkts-na-multimedia-movingphotoview-movingphotoviewattribute-i.md) |  |

## muted

```TypeScript
muted(isMuted: boolean): MovingPhotoViewAttribute
```

Called when judging whether the video is muted.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MovingPhotoViewAttribute-muted(isMuted: boolean): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-muted(isMuted: boolean): MovingPhotoViewAttribute-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isMuted | boolean | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [MovingPhotoViewAttribute](arkts-na-multimedia-movingphotoview-movingphotoviewattribute-i.md) |  |

## objectFit

```TypeScript
objectFit(value: ImageFit): MovingPhotoViewAttribute
```

Called when determining the zoom type of the view.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MovingPhotoViewAttribute-objectFit(value: ImageFit): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-objectFit(value: ImageFit): MovingPhotoViewAttribute-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ImageFit | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [MovingPhotoViewAttribute](arkts-na-multimedia-movingphotoview-movingphotoviewattribute-i.md) |  |

## onComplete

```TypeScript
onComplete(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute
```

Called when the image load completed.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MovingPhotoViewAttribute-onComplete(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-onComplete(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [MovingPhotoViewEventCallback](arkts-na-movingphotovieweventcallback-t.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [MovingPhotoViewAttribute](arkts-na-multimedia-movingphotoview-movingphotoviewattribute-i.md) |  |

## onError

```TypeScript
onError(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute
```

Called when playback fails.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MovingPhotoViewAttribute-onError(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-onError(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [MovingPhotoViewEventCallback](arkts-na-movingphotovieweventcallback-t.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [MovingPhotoViewAttribute](arkts-na-multimedia-movingphotoview-movingphotoviewattribute-i.md) |  |

## onFinish

```TypeScript
onFinish(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute
```

Called when the video playback ends.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MovingPhotoViewAttribute-onFinish(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-onFinish(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [MovingPhotoViewEventCallback](arkts-na-movingphotovieweventcallback-t.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [MovingPhotoViewAttribute](arkts-na-multimedia-movingphotoview-movingphotoviewattribute-i.md) |  |

## onPause

```TypeScript
onPause(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute
```

Called when the video playback paused.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MovingPhotoViewAttribute-onPause(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-onPause(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [MovingPhotoViewEventCallback](arkts-na-movingphotovieweventcallback-t.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [MovingPhotoViewAttribute](arkts-na-multimedia-movingphotoview-movingphotoviewattribute-i.md) |  |

## onPrepared

```TypeScript
onPrepared(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute
```

Called when playback prepared.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MovingPhotoViewAttribute-onPrepared(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-onPrepared(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [MovingPhotoViewEventCallback](arkts-na-movingphotovieweventcallback-t.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [MovingPhotoViewAttribute](arkts-na-multimedia-movingphotoview-movingphotoviewattribute-i.md) |  |

## onStart

```TypeScript
onStart(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute
```

Called when the video is played.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MovingPhotoViewAttribute-onStart(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-onStart(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [MovingPhotoViewEventCallback](arkts-na-movingphotovieweventcallback-t.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [MovingPhotoViewAttribute](arkts-na-multimedia-movingphotoview-movingphotoviewattribute-i.md) |  |

## onStop

```TypeScript
onStop(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute
```

Called when the video playback stopped.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MovingPhotoViewAttribute-onStop(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-onStop(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [MovingPhotoViewEventCallback](arkts-na-movingphotovieweventcallback-t.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [MovingPhotoViewAttribute](arkts-na-multimedia-movingphotoview-movingphotoviewattribute-i.md) |  |

## repeatPlay

```TypeScript
repeatPlay(isRepeatPlay: boolean): MovingPhotoViewAttribute
```

Sets whether to allow repeat play. If the value is true, the moving photo plays repeat after the resource is loaded.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MovingPhotoViewAttribute-repeatPlay(isRepeatPlay: boolean): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-repeatPlay(isRepeatPlay: boolean): MovingPhotoViewAttribute-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isRepeatPlay | boolean | Yes | Whether to repeat play |

**Return value:**

| Type | Description |
| --- | --- |
| [MovingPhotoViewAttribute](arkts-na-multimedia-movingphotoview-movingphotoviewattribute-i.md) |  |

