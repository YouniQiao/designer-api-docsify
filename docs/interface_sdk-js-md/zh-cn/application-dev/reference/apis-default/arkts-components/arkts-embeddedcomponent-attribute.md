# EmbeddedComponentAttribute

定义EmbeddedComponent的属性函数。

**继承/实现关系：** EmbeddedComponentAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface EmbeddedComponentAttribute--><!--Device-unnamed-export declare interface EmbeddedComponentAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<EmbeddedComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置EmbeddedComponent组件的属性修改器。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EmbeddedComponentAttribute-attributeModifier(modifier: AttributeModifier<EmbeddedComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-EmbeddedComponentAttribute-attributeModifier(modifier: AttributeModifier<EmbeddedComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[EmbeddedComponentAttribute](arkts-embeddedcomponent-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 | EmbeddedComponent组件的属性修改器。取值为undefined时，不使用attributeModifier。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [EmbeddedComponentAttribute](arkts-embeddedcomponent-attribute.md) |  |

## onDrawReady

```TypeScript
onDrawReady(callback: VoidCallback | undefined ): this
```

被拉起的EmbeddedUIExtensionAbility绘制第一帧时触发该回调。使用callback异步回调。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EmbeddedComponentAttribute-onDrawReady(callback: VoidCallback | undefined ): this--><!--Device-EmbeddedComponentAttribute-onDrawReady(callback: VoidCallback | undefined ): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | 是 | 回调函数，在EmbeddedUIExtensionAbility绘制第一帧时触发。取值为undefined时，不使用回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [EmbeddedComponentAttribute](arkts-embeddedcomponent-attribute.md) |  |

## onError

```TypeScript
onError(callback: ErrorCallback<BusinessError> | undefined ): this
```

被拉起的EmbeddedUIExtensionAbility在运行过程中发生异常时触发本回调。可通过回调参数中的code、name和message获取错误信息并做处理，业务错误码详细介绍请参见UIExtension错误码。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EmbeddedComponentAttribute-onError(callback: ErrorCallback<BusinessError> | undefined ): this--><!--Device-EmbeddedComponentAttribute-onError(callback: ErrorCallback<BusinessError> | undefined ): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-errorcallback-t.md)&lt;[BusinessError](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-businesserror-c.md)&gt; \| undefined | 是 | 回调函数，入参用于接收异常信息，类型为BusinessError，可通过参数中的code、 name和message获取错误信息并做处理。<br/>ArkTS-Sta模式下，可传入undefined，表示取消回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [EmbeddedComponentAttribute](arkts-embeddedcomponent-attribute.md) |  |

## onTerminated

```TypeScript
onTerminated(callback: Callback<TerminationInfo> | undefined ): this
```

被拉起的EmbeddedUIExtensionAbility通过调用terminateSelfWithResult或者terminateSelf正常退出时，触发本回调函数。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EmbeddedComponentAttribute-onTerminated(callback: Callback<TerminationInfo> | undefined ): this--><!--Device-EmbeddedComponentAttribute-onTerminated(callback: Callback<TerminationInfo> | undefined ): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;TerminationInfo&gt; \| undefined | 是 | 回调函数，入参用于接收EmbeddedUIExtensionAbility的返回结果， 类型为TerminationInfo。取值为undefined时，不使用回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [EmbeddedComponentAttribute](arkts-embeddedcomponent-attribute.md) |  |

## setEmbeddedComponentOptions

```TypeScript
setEmbeddedComponentOptions(loader: Want, type?: EmbeddedType, options?: EmbeddedOptions): this
```

设置嵌入式组件的选项。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EmbeddedComponentAttribute-setEmbeddedComponentOptions(loader: Want, type?: EmbeddedType, options?: EmbeddedOptions): this--><!--Device-EmbeddedComponentAttribute-setEmbeddedComponentOptions(loader: Want, type?: EmbeddedType, options?: EmbeddedOptions): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| loader | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 | 表示初始化参数。 |
| type | [EmbeddedType](../../apis-arkui/arkts-apis/arkts-arkui-embeddedtype-e.md) | 否 | 表示EmbeddedComponent的类型。 |
| options | [EmbeddedOptions](arkts-embeddedcomponent-embeddedoptions-i.md) | 否 | 表示EmbeddedComponent选项的类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | EmbeddedComponentAttribute实例 |

## setEmbeddedComponentOptions

```TypeScript
setEmbeddedComponentOptions(loader: Want, type?: EmbeddedType): this
```

设置嵌入式组件的选项。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EmbeddedComponentAttribute-setEmbeddedComponentOptions(loader: Want, type?: EmbeddedType): this--><!--Device-EmbeddedComponentAttribute-setEmbeddedComponentOptions(loader: Want, type?: EmbeddedType): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| loader | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 | 表示初始化参数。 |
| type | [EmbeddedType](../../apis-arkui/arkts-apis/arkts-arkui-embeddedtype-e.md) | 否 | 表示EmbeddedComponent的类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | EmbeddedComponentAttribute实例 |

