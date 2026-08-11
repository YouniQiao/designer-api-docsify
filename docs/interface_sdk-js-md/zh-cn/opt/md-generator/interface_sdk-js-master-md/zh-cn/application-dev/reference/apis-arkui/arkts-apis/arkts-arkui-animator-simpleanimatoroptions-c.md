# SimpleAnimatorOptions

animator简易动画参数对象。与AnimatorOptions相比，部分动画参数有默认值，可不设置。

**起始版本：** 18

<!--Device-unnamed-export declare class SimpleAnimatorOptions--><!--Device-unnamed-export declare class SimpleAnimatorOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(begin: number, end: number)
```

SimpleAnimatorOptions的构造函数。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-SimpleAnimatorOptions-constructor(begin: number, end: number)--><!--Device-SimpleAnimatorOptions-constructor(begin: number, end: number)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| begin | number | 是 |
| end | number | 是 |

## 示例

完整示例请参考[基于ArkTS扩展的声明式开发范式](#基于arkts扩展的声明式开发范式)。

```TypeScript
import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200); // 动画插值过程从100到200，其余动画参数使用默认值。

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}
```

## delay

```TypeScript
delay(delay: number): SimpleAnimatorOptions
```

设置animator动画播放时延。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-SimpleAnimatorOptions-delay(delay: number): SimpleAnimatorOptions--><!--Device-SimpleAnimatorOptions-delay(delay: number): SimpleAnimatorOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [delay](#delay) | number | 是 |

**返回值：**

| 类型 |
| --- |
| [SimpleAnimatorOptions](arkts-arkui-animator-simpleanimatoroptions-c.md) |

## 示例

完整示例请参考[基于ArkTS扩展的声明式开发范式](#基于arkts扩展的声明式开发范式)。

```TypeScript
import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).delay(500);

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}
```

## direction

```TypeScript
direction(direction: PlayMode): SimpleAnimatorOptions
```

设置animator动画播放方向。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-SimpleAnimatorOptions-direction(direction: PlayMode): SimpleAnimatorOptions--><!--Device-SimpleAnimatorOptions-direction(direction: PlayMode): SimpleAnimatorOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [direction](#direction) | [PlayMode](arkts-arkui-playmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SimpleAnimatorOptions](arkts-arkui-animator-simpleanimatoroptions-c.md) |

## 示例

完整示例请参考[基于ArkTS扩展的声明式开发范式](#基于arkts扩展的声明式开发范式)。

```TypeScript
import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).direction(PlayMode.Alternate);

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}
```

## duration

```TypeScript
duration(duration: number): SimpleAnimatorOptions
```

设置animator动画时长。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-SimpleAnimatorOptions-duration(duration: number): SimpleAnimatorOptions--><!--Device-SimpleAnimatorOptions-duration(duration: number): SimpleAnimatorOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [duration](#duration) | number | 是 |

**返回值：**

| 类型 |
| --- |
| [SimpleAnimatorOptions](arkts-arkui-animator-simpleanimatoroptions-c.md) |

## 示例

完整示例请参考[基于ArkTS扩展的声明式开发范式](#基于arkts扩展的声明式开发范式)。

```TypeScript
import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).duration(500);

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}
```

## easing

```TypeScript
easing(curve: string): SimpleAnimatorOptions
```

设置animator动画插值曲线。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-SimpleAnimatorOptions-easing(curve: string): SimpleAnimatorOptions--><!--Device-SimpleAnimatorOptions-easing(curve: string): SimpleAnimatorOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| curve | string | 是 |

**返回值：**

| 类型 |
| --- |
| [SimpleAnimatorOptions](arkts-arkui-animator-simpleanimatoroptions-c.md) |

## 示例

完整示例请参考[基于ArkTS扩展的声明式开发范式](#基于arkts扩展的声明式开发范式)。

```TypeScript
import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).easing("ease-in");

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}
```

## fill

```TypeScript
fill(fillMode: FillMode): SimpleAnimatorOptions
```

设置animator动画填充方式。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-SimpleAnimatorOptions-fill(fillMode: FillMode): SimpleAnimatorOptions--><!--Device-SimpleAnimatorOptions-fill(fillMode: FillMode): SimpleAnimatorOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fillMode | [FillMode](arkts-arkui-fillmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SimpleAnimatorOptions](arkts-arkui-animator-simpleanimatoroptions-c.md) |

## 示例

完整示例请参考[基于ArkTS扩展的声明式开发范式](#基于arkts扩展的声明式开发范式)。

```TypeScript
import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).fill(FillMode.Forwards);

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}
```

## iterations

```TypeScript
iterations(iterations: number): SimpleAnimatorOptions
```

设置animator动画播放次数。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-SimpleAnimatorOptions-iterations(iterations: number): SimpleAnimatorOptions--><!--Device-SimpleAnimatorOptions-iterations(iterations: number): SimpleAnimatorOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [iterations](#iterations) | number | 是 |

**返回值：**

| 类型 |
| --- |
| [SimpleAnimatorOptions](arkts-arkui-animator-simpleanimatoroptions-c.md) |

## 示例

完整示例请参考[基于ArkTS扩展的声明式开发范式](#基于arkts扩展的声明式开发范式)。

```TypeScript
import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).iterations(3);

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}
```
