# ContentSlot

## ContentSlot

```TypeScript
export declare function ContentSlot(
    content: Content
): ContentSlotAttribute
```

当内容添加到占位符组件时调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** 
- SystemCapability.ArkUI.ArkUI.Full
- SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [Content](../arkts-components/arkts-arkui-content-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ContentSlotAttribute](arkts-arkui-contentslot-contentslotattribute-i.md) |


## ContentSlot

```TypeScript
export declare function ContentSlot(
    style: CustomBuilderT<ContentSlotAttribute>
): ContentSlotAttribute
```

定义ContentSlot组件。需要在组件属性设置开始时调用setContentSlotOptions，并在组件属性设置结束时调用applyAttributeFinish。

**起始版本：** 26.1.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[ContentSlotAttribute](arkts-arkui-contentslot-contentslotattribute-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [ContentSlotAttribute](arkts-arkui-contentslot-contentslotattribute-i.md) |
