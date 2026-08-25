# PageTransitionEnter

设置当前页面的自定义入场动效。继承自[CommonTransition](arkts-arkui-pagetransition-commontransition-c.md)。

**继承/实现关系：** PageTransitionEnter extends [CommonTransition](arkts-arkui-pagetransition-commontransition-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## $_invoke

```TypeScript
static $_invoke(value: PageTransitionOptions): PageTransitionEnter
```

设置当前页面的自定义入场动效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [PageTransitionOptions](arkts-arkui-pagetransition-pagetransitionoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [PageTransitionEnter](arkts-arkui-pagetransition-pagetransitionenter-c.md) |

## onEnter

```TypeScript
onEnter(event: PageTransitionCallback): this
```

逐帧回调，直到入场动画结束，progress从0变化到1。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [PageTransitionCallback](arkts-arkui-pagetransitioncallback-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| this |
