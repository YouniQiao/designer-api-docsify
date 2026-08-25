# StarStyleOptions

评分组件选中、未选中以及部分选中的星级样式。

> **说明：**&gt;
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## backgroundUri

```TypeScript
backgroundUri: ResourceStr | undefined
```

未选中的星级的图片链接，可由用户自定义或使用系统默认图片。取值为undefined时，则使用系统默认图片。  
**卡片能力（仅ArkTS-Dyn）：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  
**原子化服务API（仅ArkTS-Dyn）：** 从API version 11开始，该接口支持在原子化服务中使用。从API version 20开始，该接口支持设置Resource资源。参考 示例3（通过Resource资源设置评分的样式） 代码。

**类型：** [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## foregroundUri

```TypeScript
foregroundUri: ResourceStr | undefined
```

选中的星级的图片路径，可由用户自定义或使用系统默认图片。取值为undefined时，则使用系统默认图片。  
**卡片能力（仅ArkTS-Dyn）：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  
**原子化服务API（仅ArkTS-Dyn）：** 从API version 11开始，该接口支持在原子化服务中使用。从API version 20开始，该接口支持设置Resource资源。参考 示例3（通过Resource资源设置评分的样式） 代码。

**类型：** [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## secondaryUri

```TypeScript
secondaryUri?: ResourceStr
```

部分选中的星级的图片路径，可由用户自定义或使用系统默认图片。  
**卡片能力（仅ArkTS-Dyn）：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  
**原子化服务API（仅ArkTS-Dyn）：** 从API version 11开始，该接口支持在原子化服务中使用。从API version 20开始，该接口支持设置Resource资源。参考 示例3（通过Resource资源设置评分的样式） 代码。

**类型：** [ResourceStr](arkts-arkui-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
