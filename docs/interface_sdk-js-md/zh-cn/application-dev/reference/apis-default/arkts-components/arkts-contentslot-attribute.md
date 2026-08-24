# ContentSlotAttribute

定义ContentSlot属性，防止不当递归使用ContentSlot@interface ContentSlotAttribute

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface ContentSlotAttribute--><!--Device-unnamed-export declare interface ContentSlotAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## applyAttributesFinish

```TypeScript
applyAttributesFinish(): void
```

通知ContentSlot已经完成属性设置。

**起始版本：** 26.1.0

**ArkTS模式：** ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ContentSlotAttribute-applyAttributesFinish(): void--><!--Device-ContentSlotAttribute-applyAttributesFinish(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## debugLine

```TypeScript
debugLine(sourceLine: string, moduleName?: string): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ContentSlotAttribute-debugLine(sourceLine: string, moduleName?: string): this--><!--Device-ContentSlotAttribute-debugLine(sourceLine: string, moduleName?: string): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sourceLine | string | 是 |  |
| moduleName | string | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setContentSlotOptions

```TypeScript
setContentSlotOptions(content: Content): this
```

设置ContentSlot选项。

**起始版本：** 26.1.0

**ArkTS模式：** ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ContentSlotAttribute-setContentSlotOptions(content: Content): this--><!--Device-ContentSlotAttribute-setContentSlotOptions(content: Content): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | Content | 是 | 要显示的内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | ContentSlotAttribute实例 |

## default

```TypeScript
default
```

设置组件源码重定向信息。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ContentSlotAttribute-default--><!--Device-ContentSlotAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

