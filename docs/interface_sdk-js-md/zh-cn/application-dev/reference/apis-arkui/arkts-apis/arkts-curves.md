# @ohos.curves

本模块提供设置动画插值曲线功能，用于构造阶梯曲线对象、三阶贝塞尔曲线对象和弹簧曲线对象。

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { curves } from '@kit.ArkUI';
```

## 汇总

### 函数

| 名称 |
| --- |
| [cubicBezier](arkts-arkui-curves-cubicbezier-f.md) |
| [cubicBezierCurve](arkts-arkui-curves-cubicbeziercurve-f.md) |
| [customCurve](arkts-arkui-curves-customcurve-f.md) |
| [init](arkts-arkui-curves-init-f.md) |
| [initCurve](arkts-arkui-curves-initcurve-f.md) |
| [interpolatingSpring](arkts-arkui-curves-interpolatingspring-f.md) |
| [responsiveSpringMotion](arkts-arkui-curves-responsivespringmotion-f.md) |
| [spring](arkts-arkui-curves-spring-f.md) |
| [springCurve](arkts-arkui-curves-springcurve-f.md) |
| [springMotion](arkts-arkui-curves-springmotion-f.md) |
| [steps](arkts-arkui-curves-steps-f.md) |
| [stepsCurve](arkts-arkui-curves-stepscurve-f.md) |

### 接口

| 名称 |
| --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) |

### 枚举

| 名称 |
| --- |
| [Curve](arkts-arkui-curves-curve-e.md) | 插值曲线和动效请参考<!--RP1-->[贝塞尔曲线](#ohoscurves)<!--RP1End-->。  \| 名称 \| 值 \| 说明 \| \| ------------------- \| -- \| ------------------------------------------------------------ \| \| Linear \| 0 \| 表示动画从头到尾的速度都是相同的。 \| \| Ease \| 1 \| 表示动画以低速开始，然后加快，在结束前变慢，cubic-bezier(0.25, 0.1, 0.25, 1.0)。 \| \| EaseIn \| 2 \| 表示动画以低速开始，cubic-bezier(0.42, 0.0, 1.0, 1.0)。 \| \| EaseOut \| 3 \| 表示动画以低速结束，cubic-bezier(0.0, 0.0, 0.58, 1.0)。 \| \| EaseInOut \| 4 \| 表示动画以低速开始和结束，cubic-bezier(0.42, 0.0, 0.58, 1.0)。 \| \| FastOutSlowIn \| 5 \| 标准曲线，cubic-bezier(0.4, 0.0, 0.2, 1.0)。 \| \| LinearOutSlowIn \| 6 \| 减速曲线，cubic-bezier(0.0, 0.0, 0.2, 1.0)。 \| \| FastOutLinearIn \| 7 \| 加速曲线，cubic-bezier(0.4, 0.0, 1.0, 1.0)。 \| \| ExtremeDeceleration \| 8 \| 急缓曲线，cubic-bezier(0.0, 0.0, 0.0, 1.0)。 \| \| Sharp \| 9 \| 锐利曲线，cubic-bezier(0.33, 0.0, 0.67, 1.0)。 \| \| Rhythm \| 10 \| 节奏曲线，cubic-bezier(0.7, 0.0, 0.2, 1.0)。 \| \| Smooth \| 11 \| 平滑曲线，cubic-bezier(0.4, 0.0, 0.4, 1.0)。 \| \| Friction \| 12 \| 阻尼曲线，cubic-bezier(0.2, 0.0, 0.2, 1.0)。 \|
