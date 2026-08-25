# PluginComponentAttribute（系统接口）

定义插件组件的属性方法。

**继承/实现关系：** PluginComponentAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<PluginComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置PluginComponent组件的属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[PluginComponentAttribute](arkts-arkui-plugincomponent-plugincomponentattribute-i-sys.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [PluginComponentAttribute](arkts-arkui-plugincomponent-plugincomponentattribute-i-sys.md) |

## onComplete

```TypeScript
onComplete(callback: VoidCallback | undefined): this
```

组件加载完成时触发回调。 AnonyMous Object Rectification

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [PluginComponentAttribute](arkts-arkui-plugincomponent-plugincomponentattribute-i-sys.md) |

## onError

```TypeScript
onError(callback: PluginErrorCallback | undefined): this
```

组件加载错误时触发回调。 AnonyMous Object Rectification

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [PluginErrorCallback](arkts-arkui-pluginerrorcallback-t-sys.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [PluginComponentAttribute](arkts-arkui-plugincomponent-plugincomponentattribute-i-sys.md) |

## setPluginComponentOptions

```TypeScript
setPluginComponentOptions(options: PluginComponentOptions): this
```

设置插件组件选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

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
| this |
