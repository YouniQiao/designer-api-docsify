# PageTransitionExit

设置当前页面的自定义退场动效。继承自[CommonTransition](arkts-arkui-pagetransition-commontransition-c.md)。

**继承/实现关系：** PageTransitionExit extends [CommonTransition](arkts-arkui-pagetransition-commontransition-c.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare class PageTransitionExit--><!--Device-unnamed-export declare class PageTransitionExit-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## $_invoke

```TypeScript
static $_invoke(value: PageTransitionOptions): PageTransitionExit
```

设置当前页面的自定义退场动效。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PageTransitionExit-static $_invoke(value: PageTransitionOptions): PageTransitionExit--><!--Device-PageTransitionExit-static $_invoke(value: PageTransitionOptions): PageTransitionExit-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PageTransitionOptions](arkts-arkui-pagetransition-pagetransitionoptions-i.md) | 是 | 配置退场动效的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PageTransitionExit](arkts-arkui-pagetransition-pagetransitionexit-c.md) |  |

## onExit

```TypeScript
onExit(event: PageTransitionCallback): this
```

逐帧回调，直到出场动画结束，progress从0变化到1。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PageTransitionExit-onExit(event: PageTransitionCallback): this--><!--Device-PageTransitionExit-onExit(event: PageTransitionCallback): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [PageTransitionCallback](arkts-arkui-pagetransitioncallback-t.md) | 是 | 出场动画的逐帧回调直到出场动画结束，progress从0变化到1。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

