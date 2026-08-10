# ButtonConfiguration

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](arkts-arkui-common-commonconfiguration-i.md)。

**Inheritance/Implementation:** ButtonConfiguration extends [CommonConfiguration<ButtonConfiguration>](CommonConfiguration<ButtonConfiguration>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ButtonConfiguration extends CommonConfiguration<ButtonConfiguration>--><!--Device-unnamed-export declare interface ButtonConfiguration extends CommonConfiguration<ButtonConfiguration>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## triggerClick

```TypeScript
triggerClick: ButtonTriggerClickCallback
```

使用builder新构建出来组件的点击事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ButtonConfiguration-triggerClick: ButtonTriggerClickCallback--><!--Device-ButtonConfiguration-triggerClick: ButtonTriggerClickCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## label

```TypeScript
label: string
```

Button的文本标签。

**说明：**当文本字符的长度超过按钮本身的宽度时，文本将会被截断。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ButtonConfiguration-label: string--><!--Device-ButtonConfiguration-label: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pressed

```TypeScript
pressed: boolean
```

指示是否按下Button。

true：按下；false：未按下。

默认值：false 

**说明：**

此按压属性生效区域大小为原本Button组件的大小，而非build出来的新组件大小。若新build出来的组件超过原本组件的大小，那么超出部分按压不触发。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ButtonConfiguration-pressed: boolean--><!--Device-ButtonConfiguration-pressed: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

