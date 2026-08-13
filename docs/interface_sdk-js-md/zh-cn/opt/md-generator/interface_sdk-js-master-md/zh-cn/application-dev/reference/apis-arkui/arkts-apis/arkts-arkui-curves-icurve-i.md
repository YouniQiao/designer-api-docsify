# ICurve

曲线对象，支持通过本模块中的[curves.cubicBezierCurve](arkts-arkui-curves-cubicbeziercurve-f.md#cubicBezierCurve)、 [curves.interpolatingSpring](arkts-arkui-curves-interpolatingspring-f.md#interpolatingSpring)等方法创建不同类型的曲线对象，并可通过曲线对象调用其 [interpolate](#interpolate)的成员方法。

**起始版本：** 9

**废弃版本：** -1

<!--Device-curves-interface ICurve--><!--Device-curves-interface ICurve-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## interpolate

```TypeScript
interpolate(fraction : number) : number
```

插值曲线的插值计算函数，可以通过传入的归一化时间参数返回当前的插值

**起始版本：** 9

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ICurve-interpolate(fraction : number) : number--><!--Device-ICurve-interpolate(fraction : number) : number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fraction | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
import { curves } from '@kit.ArkUI'
let curveValue = curves.initCurve(Curve.EaseIn); // 创建一个默认先慢后快插值曲线
let interpolatedValue: number = curveValue.interpolate(0.5); // 计算得到时间到一半时的插值
```
