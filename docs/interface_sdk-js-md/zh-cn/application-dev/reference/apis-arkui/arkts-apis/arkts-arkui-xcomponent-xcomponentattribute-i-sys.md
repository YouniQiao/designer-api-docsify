# XComponentAttribute

定义XComponent属性。

**继承/实现关系：** XComponentAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## enableTransparentLayer

```TypeScript
default enableTransparentLayer(enabled: boolean | undefined): this
```

当背景颜色设置半透明的XComponent需要开启独立图层（即将该组件的内容置于单独的合成图层上进行渲染， 以避免半透明区域与下方内容混合时出现渲染异常）时，使用本接口。使用本接口，并不代表一定会被设置为独立图层。出于硬件规格（如硬件不支持独立图层进行硬件合成）、 软件规格（如独立图层与带有模糊效果的UI组件相交）等原因，将导致半透明XComponent无法设置为独立图层。  
**说明：** 仅type为SURFACE时有效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [XComponentAttribute](arkts-arkui-xcomponent-xcomponentattribute-i.md) |
