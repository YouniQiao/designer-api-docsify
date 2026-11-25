# WindowCreateParams（系统接口）

```TypeScript
interface WindowCreateParams
```

应用启动时的窗口参数配置。

**起始版本：** 20

<!--Device-window-interface WindowCreateParams--><!--Device-window-interface WindowCreateParams-End-->

**系统能力：** SystemCapability.Window.SessionManager

## 导入模块

```TypeScript
import { window } from '@kit.ArkUI';
```

## isWindowLimitsForcible

```TypeScript
isWindowLimitsForcible?: boolean
```

应用主窗口尺寸限制是否可突破系统默认限制。仅当被启动应用为系统应用时生效，否则不生效也不报错。  
- true：运行突破系统默认限制。在窗口尺寸限制计算过程中，将忽略系统默认限制，最终生效结果仍按各来源取交集计算，且优先级保持不变。详细说明可参考[WindowLimits](arkts-arkui-window-windowlimits-i.md)  
- false：不允许突破系统默认限，窗口尺寸限制按照默认规则计算（包含系统默认限制）。

**类型：** boolean

**默认值：** false

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WindowCreateParams-isWindowLimitsForcible?: boolean--><!--Device-WindowCreateParams-isWindowLimitsForcible?: boolean-End-->

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

## systemAnimationParams

```TypeScript
systemAnimationParams?: StartAnimationSystemParams
```

启动动画配置，仅对全屏应用生效。

不同应用间跳转场景不生效，仍保持系统默认动效。

**类型：** [StartAnimationSystemParams](arkts-arkui-window-startanimationsystemparams-i-sys.md)

**起始版本：** 20

<!--Device-WindowCreateParams-systemAnimationParams?: StartAnimationSystemParams--><!--Device-WindowCreateParams-systemAnimationParams?: StartAnimationSystemParams-End-->

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。
