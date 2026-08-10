# TextClockOptions

用于构建TextClock组件的选项。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-declare interface TextClockOptions--><!--Device-unnamed-declare interface TextClockOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## controller

```TypeScript
controller?: TextClockController
```

绑定一个控制器，用来控制文本时钟的状态。当需要通过代码控制时钟的启动与停止时传入此参数；不传入时，时钟仍会正常运行显示，但无法通过代码控制启停。

**Type:** [TextClockController](arkts-arkui-textclockcontroller-c.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-TextClockOptions-controller?: TextClockController--><!--Device-TextClockOptions-controller?: TextClockController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## timeZoneOffset

```TypeScript
timeZoneOffset?: number
```

设置时区偏移量，单位：小时。

取值范围为[-14, 12]，表示东十二区到西十二区，其中负值表示东时区，正值表示西时区，比如东八区为-8。设置值为该取值范围内的浮点数时会进行取整，舍弃小数部分。

对横跨国际日界线的国家或地区，用-13（UTC+13）和-14（UTC+14）来保证整个国家或者区域处在相同的时间，当设置的值不在取值范围内时，将使用当前系统的时区偏移量。

默认值：当前系统的时区偏移量 

设置值为{ 9.5, 3.5, -3.5, -4.5, -5.5, -5.75, -6.5, -9.5, -10.5, -12.75 }集合中的浮点数时不进行取整。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-TextClockOptions-timeZoneOffset?: number--><!--Device-TextClockOptions-timeZoneOffset?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

