# EmbeddedComponentAttribute

定义EmbeddedComponent的属性函数。

**继承/实现关系：** EmbeddedComponentAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<EmbeddedComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置EmbeddedComponent组件的属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[EmbeddedComponentAttribute](arkts-arkui-embeddedcomponent-embeddedcomponentattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [EmbeddedComponentAttribute](arkts-arkui-embeddedcomponent-embeddedcomponentattribute-i.md) |

## onDrawReady

```TypeScript
onDrawReady(callback: VoidCallback | undefined ): this
```

被拉起的EmbeddedUIExtensionAbility绘制第一帧时触发该回调。使用callback异步回调。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [EmbeddedComponentAttribute](arkts-arkui-embeddedcomponent-embeddedcomponentattribute-i.md) |

## onError

```TypeScript
onError(callback: ErrorCallback<BusinessError> | undefined ): this
```

被拉起的EmbeddedUIExtensionAbility在运行过程中发生异常时触发本回调。可通过回调参数中的code、name和message获取错误信息并做处理，业务错误码详细介绍请参见UIExtension错误码。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md)&lt;[BusinessError](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-businesserror-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [EmbeddedComponentAttribute](arkts-arkui-embeddedcomponent-embeddedcomponentattribute-i.md) |

## onTerminated

```TypeScript
onTerminated(callback: Callback<TerminationInfo> | undefined ): this
```

被拉起的EmbeddedUIExtensionAbility通过调用terminateSelfWithResult或者terminateSelf正常退出时，触发本回调函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TerminationInfo&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [EmbeddedComponentAttribute](arkts-arkui-embeddedcomponent-embeddedcomponentattribute-i.md) |

## setEmbeddedComponentOptions

```TypeScript
setEmbeddedComponentOptions(loader: Want, type?: EmbeddedType, options?: EmbeddedOptions): this
```

设置嵌入式组件的选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| loader | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| type | [EmbeddedType](arkts-arkui-embeddedtype-e.md) | 否 |
| options | [EmbeddedOptions](arkts-arkui-embeddedcomponent-embeddedoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## setEmbeddedComponentOptions

```TypeScript
setEmbeddedComponentOptions(loader: Want, type?: EmbeddedType): this
```

设置嵌入式组件的选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| loader | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| type | [EmbeddedType](arkts-arkui-embeddedtype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |
