# PluginComponent（系统接口）

## PluginComponent

```TypeScript
export declare function PluginComponent(
    options: PluginComponentOptions
): PluginComponentAttribute
```

创建插件组件，用于显示外部应用提供的UI。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [PluginComponentOptions](arkts-arkui-plugincomponent-plugincomponentoptions-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [PluginComponentAttribute](arkts-arkui-plugincomponent-plugincomponentattribute-i-sys.md) |


## PluginComponent

```TypeScript
export declare function PluginComponent(
    style: CustomBuilderT<PluginComponentAttribute>
): PluginComponentAttribute
```

定义PluginComponent组件。它要求在组件属性设置开始时调用setPluginComponentOptions， 并在组件属性设置结束时调用applyAttributeFinish。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[PluginComponentAttribute](arkts-arkui-plugincomponent-plugincomponentattribute-i-sys.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [PluginComponentAttribute](arkts-arkui-plugincomponent-plugincomponentattribute-i-sys.md) |
