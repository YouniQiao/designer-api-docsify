# PasteButtonAttribute

Declare interfaces for the attributes of the paste button.

**继承/实现关系：** PasteButtonAttribute extends [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface PasteButtonAttribute extends SecurityComponentMethod--><!--Device-unnamed-export declare interface PasteButtonAttribute extends SecurityComponentMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onClick

```TypeScript
onClick(event: PasteButtonCallback | undefined): this
```

Called when the paste button is clicked.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PasteButtonAttribute-onClick(event: PasteButtonCallback | undefined): this--><!--Device-PasteButtonAttribute-onClick(event: PasteButtonCallback | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [PasteButtonCallback](../arkts-components/arkts-arkui-pastebuttoncallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the paste button. |

