# RichEditorChangeValue

图文变化信息。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## changeReason

```TypeScript
changeReason?: TextChangeReason
```

组件内容变化的原因，用于标识触发内容变化的操作类型（如用户输入、粘贴、剪切等），需通过注册onWillChange回调获取。 开发者可根据changeReason的值在onWillChange回调中针对不同变化原因做出相应处理决策。 字段缺省值为undefined。<br/>**系统接口：** 此接口为系统接口。<br> **模型约束：** 此接口仅可在Stage模型下使用。

**类型：** [TextChangeReason](arkts-arkui-textcommon-textchangereason-e-sys.md)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。
