# DataPanelShadowOptions

DataPanelShadowOptions继承自MultiShadowOptions，具有MultiShadowOptions的全部属性。

**继承/实现关系：** DataPanelShadowOptions extends MultiShadowOptions

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## colors

```TypeScript
colors?: Array<ResourceColor | LinearGradient>
```

各数据段投影的颜色。 默认值：与valueColors值相同 **说明：** 若设置的投影颜色的个数少于数据段个数时，则显示的投影颜色的个数和设置的投影颜色个数一致。

**类型：** Array&lt;[ResourceColor](arkts-arkui-resourcecolor-t.md) \| [LinearGradient](arkts-arkui-datapanel-lineargradient-c.md)&gt;

**默认值：** Consistent with valueColors

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
