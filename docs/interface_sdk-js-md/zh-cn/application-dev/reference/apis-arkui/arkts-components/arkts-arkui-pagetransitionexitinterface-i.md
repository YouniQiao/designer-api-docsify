# PageTransitionExitInterface

当前页面的自定义退场动效。继承自[CommonTransition](arkts-arkui-commontransition-c.md)。

**继承/实现关系：** PageTransitionExitInterface extends CommonTransition<PageTransitionExitInterface>

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## [[Call]]

```TypeScript
(value: PageTransitionOptions): PageTransitionExitInterface
```

设置当前页面的自定义退场动效。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [PageTransitionOptions](arkts-arkui-pagetransitionoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [PageTransitionExitInterface](arkts-arkui-pagetransitionexitinterface-i.md) |

## onExit

```TypeScript
onExit(event: PageTransitionCallback): PageTransitionExitInterface
```

逐帧回调，直到出场动画结束，progress从0变化到1。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [PageTransitionCallback](arkts-arkui-pagetransitioncallback-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [PageTransitionExitInterface](arkts-arkui-pagetransitionexitinterface-i.md) |
