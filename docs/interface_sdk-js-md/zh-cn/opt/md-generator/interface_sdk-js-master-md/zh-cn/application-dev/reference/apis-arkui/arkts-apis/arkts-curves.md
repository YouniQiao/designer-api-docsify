# @ohos.curves

/*
 Copyright (c) 2021-2023 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


**起始版本：** 7

<!--Device-unnamed-declare namespace curves--><!--Device-unnamed-declare namespace curves-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [cubicBezier](arkts-arkui-curves-cubicbezier-f.md#cubicbezier) |
| [cubicBezierCurve](arkts-arkui-curves-cubicbeziercurve-f.md#cubicbeziercurve) |
| [customCurve](arkts-arkui-curves-customcurve-f.md#customcurve) |
| [init](arkts-arkui-curves-init-f.md#init) |
| [initCurve](arkts-arkui-curves-initcurve-f.md#initcurve) |
| [interpolatingSpring](arkts-arkui-curves-interpolatingspring-f.md#interpolatingspring) |
| [responsiveSpringMotion](arkts-arkui-curves-responsivespringmotion-f.md#responsivespringmotion) |
| [spring](arkts-arkui-curves-spring-f.md#spring) |
| [springCurve](arkts-arkui-curves-springcurve-f.md#springcurve) |
| [springMotion](arkts-arkui-curves-springmotion-f.md#springmotion) |
| [steps](arkts-arkui-curves-steps-f.md#steps) |
| [stepsCurve](arkts-arkui-curves-stepscurve-f.md#stepscurve) |

### 接口

| 名称 |
| --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) |

### 枚举

| 名称 |
| --- |
| [Curve](arkts-arkui-curves-curve-e.md) | 插值曲线和动效请参考&lt;!--RP1--&gt;[贝塞尔曲线](../../../../design/ux-design/animation-attributes.md)&lt;!--RP1End--&gt;。 \| 名称 \| 值 \| 说明 \| \| ------------------- \| -- \| ------------------------------------------------------------ \| \| Linear \| 0 \| 表示动画从头到尾的速度都是相同的。 \| \| Ease \| 1 \| 表示动画以低速开始，然后加快，在结束前变慢，cubic-bezier(0.25, 0.1, 0.25, 1.0)。 \| \| EaseIn \| 2 \| 表示动画以低速开始，cubic-bezier(0.42, 0.0, 1.0, 1.0)。 \| \| EaseOut \| 3 \| 表示动画以低速结束，cubic-bezier(0.0, 0.0, 0.58, 1.0)。 \| \| EaseInOut \| 4 \| 表示动画以低速开始和结束，cubic-bezier(0.42, 0.0, 0.58, 1.0)。 \| \| FastOutSlowIn \| 5 \| 标准曲线，cubic-bezier(0.4, 0.0, 0.2, 1.0)。 \| \| LinearOutSlowIn \| 6 \| 减速曲线，cubic-bezier(0.0, 0.0, 0.2, 1.0)。 \| \| FastOutLinearIn \| 7 \| 加速曲线，cubic-bezier(0.4, 0.0, 1.0, 1.0)。 \| \| ExtremeDeceleration \| 8 \| 急缓曲线，cubic-bezier(0.0, 0.0, 0.0, 1.0)。 \| \| Sharp \| 9 \| 锐利曲线，cubic-bezier(0.33, 0.0, 0.67, 1.0)。 \| \| Rhythm \| 10 \| 节奏曲线，cubic-bezier(0.7, 0.0, 0.2, 1.0)。 \| \| Smooth \| 11 \| 平滑曲线，cubic-bezier(0.4, 0.0, 0.4, 1.0)。 \| \| Friction \| 12 \| 阻尼曲线，cubic-bezier(0.2, 0.0, 0.2, 1.0)。 \|
