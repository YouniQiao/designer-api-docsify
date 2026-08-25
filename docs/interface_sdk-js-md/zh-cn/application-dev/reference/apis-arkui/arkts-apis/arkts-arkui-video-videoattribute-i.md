# VideoAttribute

用于播放视频文件并控制其播放状态的组件。@extends CommonMethod @interface VideoAttribute

**继承/实现关系：** VideoAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## analyzerConfig

```TypeScript
default analyzerConfig(config: ImageAnalyzerConfig | undefined): this
```

设置AI分析识别类型，包括主体识别、文字识别和对象查找等功能。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [ImageAnalyzerConfig](arkts-arkui-imagecommon-imageanalyzerconfig-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<VideoAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[VideoAttribute](arkts-arkui-video-videoattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |

## autoPlay

```TypeScript
default autoPlay(value: boolean | undefined): this
```

设置视频是否自动播放。 true：开启自动播放；false：关闭自动播放。 默认值：false，取值为undefined时，按默认值处理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |

## controls

```TypeScript
default controls(value: boolean | undefined): this
```

设置控制视频播放的控制栏是否显示。 true：控制栏显示；false：控制栏不显示。 默认值：true，取值为undefined时，按默认值处理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |

## enableAnalyzer

```TypeScript
default enableAnalyzer(enable: boolean | undefined): this
```

设置组件支持AI分析，当前支持主体识别、文字识别和对象查找等功能。 使能后，视频播放暂停时自动进入分析状态，开始分析当前画面帧， 视频继续播放后自动退出分析状态。 不能和overlay属性同时使用，两者同时设置时overlay中CustomBuilder属性将失效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |

## enableShortcutKey

```TypeScript
default enableShortcutKey(enabled: boolean | undefined): this
```

设置组件支持快捷键响应。 目前支持在组件获焦后响应空格键播放/暂停、上下方向键调整视频音量、 左右方向键快进/快退。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |

## loop

```TypeScript
default loop(value: boolean | undefined): this
```

设置是否单个视频循环播放。 true：开启循环播放；false：关闭循环播放。 默认值：false，取值为undefined时，按默认值处理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |

## muted

```TypeScript
default muted(value: boolean | undefined): this
```

设置视频是否静音。 true：开启静音；false：关闭静音。 默认值：false，取值为undefined时，按默认值处理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |

## objectFit

```TypeScript
default objectFit(value: ImageFit | undefined): this
```

设置视频的填充模式。 默认值：Cover。 约束：不支持ImageFit类型中的枚举值MATRIX，若设置，则作用效果与Cover一致。 异常值：若设置异常值undefined、null，或不在ImageFit枚举范围内的值， 作用效果均与Cover一致。取值为undefined时，按默认值处理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ImageFit](arkts-arkui-imagefit-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |

## onError

```TypeScript
default onError(event: VoidCallback | ErrorCallback | undefined): this
```

播放失败时触发该事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |

## onFinish

```TypeScript
default onFinish(event: VoidCallback | undefined): this
```

播放结束时触发该事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |

## onFullscreenChange

```TypeScript
default onFullscreenChange(callback: Callback<FullscreenInfo> | undefined): this
```

在全屏播放与非全屏播放状态之间切换时触发该事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[FullscreenInfo](arkts-arkui-video-fullscreeninfo-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |

## onPause

```TypeScript
default onPause(event: VoidCallback | undefined): this
```

暂停时触发该事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |

## onPrepared

```TypeScript
default onPrepared(callback: Callback<PreparedInfo> | undefined): this
```

视频准备完成时触发该事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[PreparedInfo](arkts-arkui-video-preparedinfo-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |

## onSeeked

```TypeScript
default onSeeked(callback: Callback<PlaybackInfo> | undefined): this
```

操作进度条完成后，上报播放时间信息。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[PlaybackInfo](arkts-arkui-video-playbackinfo-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |

## onSeeking

```TypeScript
default onSeeking(callback: Callback<PlaybackInfo> | undefined): this
```

操作进度条过程时上报时间信息。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[PlaybackInfo](arkts-arkui-video-playbackinfo-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |

## onStart

```TypeScript
default onStart(event: VoidCallback | undefined): this
```

播放时触发该事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |

## onStop

```TypeScript
default onStop(event: VoidCallback | undefined): this
```

播放停止时触发该事件（当stop()方法被调用后触发）。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |

## onUpdate

```TypeScript
default onUpdate(callback: Callback<PlaybackInfo> | undefined): this
```

播放进度变化时触发该事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[PlaybackInfo](arkts-arkui-video-playbackinfo-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |

## setVideoOptions

```TypeScript
default setVideoOptions(value: VideoOptions): this
```

设置Video选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [VideoOptions](arkts-arkui-video-videooptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |
