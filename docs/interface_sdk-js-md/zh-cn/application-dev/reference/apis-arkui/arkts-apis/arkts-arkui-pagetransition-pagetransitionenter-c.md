# PageTransitionEnter

设置当前页面的自定义入场动效。继承自[CommonTransition](arkts-arkui-pagetransition-commontransition-c.md)。

**继承/实现关系：** PageTransitionEnter extends [CommonTransition](arkts-arkui-pagetransition-commontransition-c.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare class PageTransitionEnter--><!--Device-unnamed-export declare class PageTransitionEnter-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## $_invoke

```TypeScript
static $_invoke(value: PageTransitionOptions): PageTransitionEnter
```

设置当前页面的自定义入场动效。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PageTransitionEnter-static $_invoke(value: PageTransitionOptions): PageTransitionEnter--><!--Device-PageTransitionEnter-static $_invoke(value: PageTransitionOptions): PageTransitionEnter-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PageTransitionOptions](arkts-arkui-pagetransition-pagetransitionoptions-i.md) | 是 | 配置入场动效的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PageTransitionEnter](arkts-arkui-pagetransition-pagetransitionenter-c.md) |  |

## onEnter

```TypeScript
onEnter(event: PageTransitionCallback): this
```

逐帧回调，直到入场动画结束，progress从0变化到1。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PageTransitionEnter-onEnter(event: PageTransitionCallback): this--><!--Device-PageTransitionEnter-onEnter(event: PageTransitionCallback): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [PageTransitionCallback](arkts-arkui-pagetransitioncallback-t.md) | 是 | 入场动画的逐帧回调直到入场动画结束，progress从0变化到1。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

