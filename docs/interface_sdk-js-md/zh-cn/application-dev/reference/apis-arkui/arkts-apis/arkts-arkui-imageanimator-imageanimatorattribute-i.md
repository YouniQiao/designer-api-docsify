# ImageAnimatorAttribute

除支持通用属性外，还支持以下属性：除支持通用事件外，还支持以下事件：@extends CommonMethod @interface ImageAnimatorAttribute

**继承/实现关系：** ImageAnimatorAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(
    modifier: AttributeModifier<ImageAnimatorAttribute> | AttributeModifier<CommonMethod> | undefined
  ): this
```

Set the attribute modifier

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ImageAnimatorAttribute](arkts-arkui-imageanimator-imageanimatorattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAnimatorAttribute](arkts-arkui-imageanimator-imageanimatorattribute-i.md) |

## duration

```TypeScript
default duration(value: int | undefined): this
```

设置播放时长。当Images中任意一帧图片设置了单独的duration后，该属性设置无效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAnimatorAttribute](arkts-arkui-imageanimator-imageanimatorattribute-i.md) |

## fillMode

```TypeScript
default fillMode(value: FillMode | undefined): this
```

设置当前播放方向下，动画开始前和结束后的状态。动画结束后的状态由fillMode和reverse属性共同决定。 例如，fillMode为Forwards表示停止时维持动画最后一个关键帧的状态，若reverse为false则维持正 播的最后一帧，即最后一张图，若reverse为true则维持逆播的最后一帧，即第一张图。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [FillMode](arkts-arkui-fillmode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAnimatorAttribute](arkts-arkui-imageanimator-imageanimatorattribute-i.md) |

## fixedSize

```TypeScript
default fixedSize(value: boolean | undefined): this
```

设置图片大小是否固定为组件大小。

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
| [ImageAnimatorAttribute](arkts-arkui-imageanimator-imageanimatorattribute-i.md) |

## images

```TypeScript
default images(value: Array<ImageFrameInfo> | undefined): this
```

设置图片帧信息集合。不支持动态更新，动态更新可能会导致不可预期的行为。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;[ImageFrameInfo](arkts-arkui-imageanimator-imageframeinfo-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAnimatorAttribute](arkts-arkui-imageanimator-imageanimatorattribute-i.md) |

## iterations

```TypeScript
default iterations(value: int | undefined): this
```

设置播放次数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAnimatorAttribute](arkts-arkui-imageanimator-imageanimatorattribute-i.md) |

## monitorInvisibleArea

```TypeScript
default monitorInvisibleArea(monitorInvisibleArea: boolean | undefined): this
```

设置组件是否通过系统onVisibleAreaChange的可见性判定， 控制组件的暂停和播放。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** 
- SystemCapability.ArkUI.ArkUI.Full
- SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [monitorInvisibleArea](#monitorinvisiblearea) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAnimatorAttribute](arkts-arkui-imageanimator-imageanimatorattribute-i.md) |

## onCancel

```TypeScript
default onCancel(event: (() => void) | undefined): this
```

状态回调，动画返回最初状态时触发。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAnimatorAttribute](arkts-arkui-imageanimator-imageanimatorattribute-i.md) |

## onFinish

```TypeScript
default onFinish(event: (() => void) | undefined): this
```

状态回调，动画播放完成时或者停止播放时触发。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAnimatorAttribute](arkts-arkui-imageanimator-imageanimatorattribute-i.md) |

## onPause

```TypeScript
default onPause(event: (() => void) | undefined): this
```

状态回调，动画暂停播放时触发。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAnimatorAttribute](arkts-arkui-imageanimator-imageanimatorattribute-i.md) |

## onRepeat

```TypeScript
default onRepeat(event: (() => void) | undefined): this
```

状态回调，动画重复播放时触发。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAnimatorAttribute](arkts-arkui-imageanimator-imageanimatorattribute-i.md) |

## onStart

```TypeScript
default onStart(event: (() => void) | undefined): this
```

状态回调，动画开始播放时触发。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAnimatorAttribute](arkts-arkui-imageanimator-imageanimatorattribute-i.md) |

## reverse

```TypeScript
default reverse(value: boolean | undefined): this
```

设置播放方向。

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
| [ImageAnimatorAttribute](arkts-arkui-imageanimator-imageanimatorattribute-i.md) |

## setImageAnimatorOptions

```TypeScript
default setImageAnimatorOptions(): this
```

设置图像帧信息。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [ImageAnimatorAttribute](arkts-arkui-imageanimator-imageanimatorattribute-i.md) |

## state

```TypeScript
default state(value: AnimationStatus | undefined): this
```

控制播放状态。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [AnimationStatus](arkts-arkui-animationstatus-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAnimatorAttribute](arkts-arkui-imageanimator-imageanimatorattribute-i.md) |
