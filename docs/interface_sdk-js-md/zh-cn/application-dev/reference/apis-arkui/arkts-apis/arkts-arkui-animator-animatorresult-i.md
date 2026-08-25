# AnimatorResult

定义Animator结果接口。

**起始版本：** 6

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { Animator, AnimatorOptions, AnimatorResult, SimpleAnimatorOptions } from 'kits/@kit.ArkUI';
```

## cancel

```TypeScript
cancel(): void
```

取消动画，会触发[onCancel](../../../reference/apis-arkui/js-apis-animator.md#属性)回调。此接口和 [finish](#finish)接口功能上没有区别，仅触发的回调不同，建议使用finish接口结束动画。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## finish

```TypeScript
finish(): void
```

结束动画，会触发[onFinish](../../../reference/apis-arkui/js-apis-animator.md#属性)回调。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## oncancel

```TypeScript
oncancel: () => void
```

动画被取消时回调。  
**说明:** 从API version 6开始支持，从API version 12开始废弃，推荐使用onCancel。

**起始版本：** 6

**废弃版本：** 12

**替代接口：** onCancel

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onCancel

```TypeScript
onCancel: () => void
```

动画被取消时回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onfinish

```TypeScript
onfinish: () => void
```

动画完成时回调。  
**说明:** 从API version 6开始支持，从API version 12开始废弃，推荐使用onFinish。

**起始版本：** 6

**废弃版本：** 12

**替代接口：** onFinish

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onFinish

```TypeScript
onFinish: () => void
```

动画完成时回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onframe

```TypeScript
onframe: (progress: number) => void
```

接收到帧时回调。  
**说明:** 从API version 6开始支持，从API version 12开始废弃，推荐使用onFrame。

**起始版本：** 6

**废弃版本：** 12

**替代接口：** onFrame

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| progress | number | 是 |

## onFrame

```TypeScript
onFrame: (progress: number) => void
```

接收到帧时回调。progress表示动画的当前值。取值范围为[AnimatorOptions](arkts-arkui-animator-animatoroptions-i.md)定义的[begin, end]，默认取值范围为[0, 1]。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| progress | number | 是 |

## onrepeat

```TypeScript
onrepeat: () => void
```

动画重复时回调。  
**说明:** 从API version 6开始支持，从API version 12开始废弃，推荐使用onRepeat。

**起始版本：** 6

**废弃版本：** 12

**替代接口：** onRepeat

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onRepeat

```TypeScript
onRepeat: () => void
```

动画重复时回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## pause

```TypeScript
pause(): void
```

暂停动画。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## play

```TypeScript
play(): void
```

启动动画。动画会保留上一次的播放状态，比如播放状态设置reverse后，再次播放会保留reverse的播放状态。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## reset

```TypeScript
reset(options: AnimatorOptions): void
```

重置当前animator动画参数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [AnimatorOptions](arkts-arkui-animator-animatoroptions-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |

## reset

```TypeScript
reset(options: AnimatorOptions | SimpleAnimatorOptions): void
```

重置当前animator动画参数。与[reset](#reset)相比，新增对 [SimpleAnimatorOptions](arkts-arkui-animator-simpleanimatoroptions-c.md)类型入参的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [AnimatorOptions](arkts-arkui-animator-animatoroptions-i.md) \| [SimpleAnimatorOptions](arkts-arkui-animator-simpleanimatoroptions-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |

## reverse

```TypeScript
reverse(): void
```

以相反的顺序播放动画。使用interpolating-spring曲线时此接口无效。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## setExpectedFrameRateRange

```TypeScript
setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange): void
```

设置期望的帧率范围。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rateRange | [ExpectedFrameRateRange](../arkts-components/arkts-arkui-expectedframeraterange-i.md) | 是 |

## update

```TypeScript
update(options: AnimatorOptions): void
```

更新当前动画器。

> **说明：**&gt;
> 从API version 6开始支持，从API version 9开始废弃。建议使用[reset](#reset)替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [reset](#reset)(options: AnimatorOptions)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [AnimatorOptions](arkts-arkui-animator-animatoroptions-i.md) | 是 |
