# Animator

定义Animator类。

**起始版本：** 6

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { Animator, AnimatorOptions, AnimatorResult, SimpleAnimatorOptions } from 'kits/@kit.ArkUI';
```

## create

```TypeScript
static create(options: AnimatorOptions): AnimatorResult
```

创建animator动画结果对象（AnimatorResult）。

> **说明：**&gt;
> -&gt;
> - 从API version 10开始，可以通过使用[UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md)中的
> createAnimator来明确UI的执行上下文。

**起始版本：** 9

**废弃版本：** 18

**替代接口：** createAnimator

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [AnimatorOptions](arkts-arkui-animator-animatoroptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [AnimatorResult](arkts-arkui-animator-animatorresult-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## create

```TypeScript
static create(options: AnimatorOptions | SimpleAnimatorOptions): AnimatorResult
```

创建animator动画结果对象（AnimatorResult）。与[create](#create)相比，新增对 [SimpleAnimatorOptions](arkts-arkui-animator-simpleanimatoroptions-c.md)类型入参的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [AnimatorOptions](arkts-arkui-animator-animatoroptions-i.md) \| [SimpleAnimatorOptions](arkts-arkui-animator-simpleanimatoroptions-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [AnimatorResult](arkts-arkui-animator-animatorresult-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## createAnimator

```TypeScript
static createAnimator(options: AnimatorOptions): AnimatorResult
```

创建动画。

> **说明：**

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [create](#create)(options: AnimatorOptions)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [AnimatorOptions](arkts-arkui-animator-animatoroptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [AnimatorResult](arkts-arkui-animator-animatorresult-i.md) |
