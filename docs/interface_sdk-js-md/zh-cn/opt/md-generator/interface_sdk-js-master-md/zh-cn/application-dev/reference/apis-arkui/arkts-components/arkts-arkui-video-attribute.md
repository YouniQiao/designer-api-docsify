# Video属性/事件

除支持[通用属性](./common)外，还支持以下属性：

除支持[通用事件](./common)外，还支持以下事件：

**继承/实现关系：** VideoAttribute extends [CommonMethod<VideoAttribute>](CommonMethod<VideoAttribute>)

**起始版本：** 7

<!--Device-unnamed-declare class VideoAttribute extends CommonMethod<VideoAttribute>--><!--Device-unnamed-declare class VideoAttribute extends CommonMethod<VideoAttribute>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## analyzerConfig

```TypeScript
analyzerConfig(config: ImageAnalyzerConfig)
```

设置AI分析识别类型，包括主体识别、文字识别和对象查找等功能，支持[attributeModifier](CommonMethod#attributeModifier)动态设置属性方法。

> **说明：**
> 
> 从API version 20开始，该接口支持在[attributeModifier](CommonMethod#attributeModifier)中调用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-VideoAttribute-analyzerConfig(config: ImageAnalyzerConfig): VideoAttribute--><!--Device-VideoAttribute-analyzerConfig(config: ImageAnalyzerConfig): VideoAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [ImageAnalyzerConfig](../arkts-apis/arkts-arkui-imageanalyzerconfig-i.md) | 是 |

## autoPlay

```TypeScript
autoPlay(value: boolean)
```

设置视频是否自动播放，支持[attributeModifier](CommonMethod#attributeModifier)动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-VideoAttribute-autoPlay(value: boolean): VideoAttribute--><!--Device-VideoAttribute-autoPlay(value: boolean): VideoAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## controls

```TypeScript
controls(value: boolean)
```

设置控制视频播放的控制栏是否显示，支持[attributeModifier](CommonMethod#attributeModifier)动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-VideoAttribute-controls(value: boolean): VideoAttribute--><!--Device-VideoAttribute-controls(value: boolean): VideoAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## enableAnalyzer

```TypeScript
enableAnalyzer(enable: boolean)
```

设置组件支持AI分析，当前支持主体识别、文字识别和对象查找等功能，支持[attributeModifier](CommonMethod#attributeModifier)动态设置属性方法。

启用后，视频播放暂停时自动进入分析状态，开始分析当前画面帧，视频继续播放后自动退出分析状态。

不支持与[overlay](CommonMethod#overlay)属性同时使用，两者同时设置时[overlay](CommonMethod#overlay)中  
[CustomBuilder](../../../reference/apis-arkui/arkui-ts/ts-types.md#custombuilder8)属性会失效。

> **说明：**
> 
> 从API version 20开始，该接口支持在[attributeModifier](CommonMethod#attributeModifier)中调用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-VideoAttribute-enableAnalyzer(enable: boolean): VideoAttribute--><!--Device-VideoAttribute-enableAnalyzer(enable: boolean): VideoAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

## enableShortcutKey

```TypeScript
enableShortcutKey(enabled: boolean)
```

设置组件支持快捷键响应，支持[attributeModifier](CommonMethod#attributeModifier)动态设置属性方法。

目前支持在组件获焦后响应空格键播放/暂停、上下方向键调整视频音量、左右方向键快进/快退。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-VideoAttribute-enableShortcutKey(enabled: boolean): VideoAttribute--><!--Device-VideoAttribute-enableShortcutKey(enabled: boolean): VideoAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |

## loop

```TypeScript
loop(value: boolean)
```

设置是否单个视频循环播放，支持[attributeModifier](CommonMethod#attributeModifier)动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-VideoAttribute-loop(value: boolean): VideoAttribute--><!--Device-VideoAttribute-loop(value: boolean): VideoAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## muted

```TypeScript
muted(value: boolean)
```

设置视频是否静音，支持[attributeModifier](CommonMethod#attributeModifier)动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-VideoAttribute-muted(value: boolean): VideoAttribute--><!--Device-VideoAttribute-muted(value: boolean): VideoAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## objectFit

```TypeScript
objectFit(value: ImageFit)
```

设置视频的填充模式，支持[attributeModifier](CommonMethod#attributeModifier)动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-VideoAttribute-objectFit(value: ImageFit): VideoAttribute--><!--Device-VideoAttribute-objectFit(value: ImageFit): VideoAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ImageFit](../arkts-apis/arkts-arkui-imagefit-e.md) | 是 |

## onError

```TypeScript
onError(event: VoidCallback | import('../api/@ohos.base').ErrorCallback)
```

播放失败时触发该事件，支持[attributeModifier](CommonMethod#attributeModifier)动态设置属性方法。

> **说明：**
> 
> 从API version 20开始，该接口支持在[attributeModifier](CommonMethod#attributeModifier)中调用。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-VideoAttribute-onError(event: VoidCallback | import('../api/@ohos.base').ErrorCallback): VideoAttribute--><!--Device-VideoAttribute-onError(event: VoidCallback | import('../api/@ohos.base').ErrorCallback): VideoAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](../arkts-apis/arkts-arkui-voidcallback-t.md) \| import('../api/@ohos.base').ErrorCallback | 是 |

## onFinish

```TypeScript
onFinish(event: VoidCallback)
```

播放结束时触发该事件，支持[attributeModifier](CommonMethod#attributeModifier)动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-VideoAttribute-onFinish(event: VoidCallback): VideoAttribute--><!--Device-VideoAttribute-onFinish(event: VoidCallback): VideoAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](../arkts-apis/arkts-arkui-voidcallback-t.md) | 是 |

## onFullscreenChange

```TypeScript
onFullscreenChange(callback: Callback<FullscreenInfo>)
```

在全屏播放与非全屏播放状态之间切换时触发该事件，支持[attributeModifier](CommonMethod#attributeModifier)动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-VideoAttribute-onFullscreenChange(callback: Callback<FullscreenInfo>): VideoAttribute--><!--Device-VideoAttribute-onFullscreenChange(callback: Callback<FullscreenInfo>): VideoAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Callback&lt;[FullscreenInfo](arkts-arkui-fullscreeninfo-i.md)&gt; | 是 |

## onPause

```TypeScript
onPause(event: VoidCallback)
```

暂停时触发该事件，支持[attributeModifier](CommonMethod#attributeModifier)动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-VideoAttribute-onPause(event: VoidCallback): VideoAttribute--><!--Device-VideoAttribute-onPause(event: VoidCallback): VideoAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](../arkts-apis/arkts-arkui-voidcallback-t.md) | 是 |

## onPrepared

```TypeScript
onPrepared(callback: Callback<PreparedInfo>)
```

视频准备完成时触发该事件，支持[attributeModifier](CommonMethod#attributeModifier)动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-VideoAttribute-onPrepared(callback: Callback<PreparedInfo>): VideoAttribute--><!--Device-VideoAttribute-onPrepared(callback: Callback<PreparedInfo>): VideoAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Callback&lt;[PreparedInfo](arkts-arkui-preparedinfo-i.md)&gt; | 是 |

## onSeeked

```TypeScript
onSeeked(callback: Callback<PlaybackInfo>)
```

操作进度条完成后，上报播放时间信息，支持[attributeModifier](CommonMethod#attributeModifier)动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-VideoAttribute-onSeeked(callback: Callback<PlaybackInfo>): VideoAttribute--><!--Device-VideoAttribute-onSeeked(callback: Callback<PlaybackInfo>): VideoAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Callback&lt;[PlaybackInfo](arkts-arkui-playbackinfo-i.md)&gt; | 是 |

## onSeeking

```TypeScript
onSeeking(callback: Callback<PlaybackInfo>)
```

操作进度条过程时上报时间信息，支持[attributeModifier](CommonMethod#attributeModifier)动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-VideoAttribute-onSeeking(callback: Callback<PlaybackInfo>): VideoAttribute--><!--Device-VideoAttribute-onSeeking(callback: Callback<PlaybackInfo>): VideoAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Callback&lt;[PlaybackInfo](arkts-arkui-playbackinfo-i.md)&gt; | 是 |

## onStart

```TypeScript
onStart(event: VoidCallback)
```

开始播放时触发该事件，支持[attributeModifier](CommonMethod#attributeModifier)动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-VideoAttribute-onStart(event: VoidCallback): VideoAttribute--><!--Device-VideoAttribute-onStart(event: VoidCallback): VideoAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](../arkts-apis/arkts-arkui-voidcallback-t.md) | 是 |

## onStop

```TypeScript
onStop(event: Callback<void>)
```

播放停止时触发该事件(当stop()方法被调用后触发)，支持[attributeModifier](CommonMethod#attributeModifier)动态设置属性方法。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-VideoAttribute-onStop(event: Callback<void>): VideoAttribute--><!--Device-VideoAttribute-onStop(event: Callback<void>): VideoAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | Callback & lt;void & gt; | 是 |

## onUpdate

```TypeScript
onUpdate(callback: Callback<PlaybackInfo>)
```

播放进度变化时触发该事件，支持[attributeModifier](CommonMethod#attributeModifier)动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-VideoAttribute-onUpdate(callback: Callback<PlaybackInfo>): VideoAttribute--><!--Device-VideoAttribute-onUpdate(callback: Callback<PlaybackInfo>): VideoAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Callback&lt;[PlaybackInfo](arkts-arkui-playbackinfo-i.md)&gt; | 是 |
