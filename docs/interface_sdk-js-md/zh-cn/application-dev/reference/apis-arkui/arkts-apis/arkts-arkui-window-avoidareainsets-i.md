# AvoidAreaInsets

```TypeScript
interface AvoidAreaInsets
```

窗口的避让区边衬。

避让区边衬表示由于[避让区](arkts-arkui-window-avoidarea-i.md)的存在，窗口内容在上下左右四个方向上需要避让的距离。

> **说明：** 
> 
> 避让区边衬的计算不包括[TYPE_KEYBOARD](arkts-arkui-window-avoidareatype-e.md)类型的避让区。

**起始版本：** 26.1.0

<!--Device-window-interface AvoidAreaInsets--><!--Device-window-interface AvoidAreaInsets-End-->

**系统能力：** SystemCapability.Window.SessionManager

## 导入模块

```TypeScript
import { window } from '@kit.ArkUI';
```

## bottom

```TypeScript
bottom: number
```

窗口底部需要避让的距离。单位为像素，取值限定为整数。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AvoidAreaInsets-bottom: int--><!--Device-AvoidAreaInsets-bottom: int-End-->

**系统能力：** SystemCapability.Window.SessionManager

## left

```TypeScript
left: number
```

窗口左侧需要避让的距离。单位为像素，取值限定为整数。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AvoidAreaInsets-left: int--><!--Device-AvoidAreaInsets-left: int-End-->

**系统能力：** SystemCapability.Window.SessionManager

## right

```TypeScript
right: number
```

窗口右侧需要避让的距离。单位为像素，取值限定为整数。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AvoidAreaInsets-right: int--><!--Device-AvoidAreaInsets-right: int-End-->

**系统能力：** SystemCapability.Window.SessionManager

## top

```TypeScript
top: number
```

窗口顶部需要避让的距离。单位为像素，取值限定为整数。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AvoidAreaInsets-top: int--><!--Device-AvoidAreaInsets-top: int-End-->

**系统能力：** SystemCapability.Window.SessionManager
