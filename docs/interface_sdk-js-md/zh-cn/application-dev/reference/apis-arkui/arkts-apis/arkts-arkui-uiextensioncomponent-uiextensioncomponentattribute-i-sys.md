# UIExtensionComponentAttribute（系统接口）

定义UIExtensionComponent的属性函数。

**继承/实现关系：** UIExtensionComponentAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<UIExtensionComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置UIExtensionComponent组件的属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[UIExtensionComponentAttribute](arkts-arkui-uiextensioncomponent-uiextensioncomponentattribute-i-sys.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [UIExtensionComponentAttribute](arkts-arkui-uiextensioncomponent-uiextensioncomponentattribute-i-sys.md) |

## onDrawReady

```TypeScript
onDrawReady(callback: VoidCallback | undefined): this
```

被拉起的UIExtensionAbility绘制第一帧时触发本回调。

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
| [UIExtensionComponentAttribute](arkts-arkui-uiextensioncomponent-uiextensioncomponentattribute-i-sys.md) |

## onError

```TypeScript
onError(callback: ErrorCallback<BusinessError> | undefined): this
```

被拉起的Ability扩展在运行过程中发生异常时触发本回调。可通过回调参数中的code、name和message获取错误信息并做处理，业务错误码详细介绍请参见UIExtension错误码。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md)&lt;[BusinessError](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-businesserror-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [UIExtensionComponentAttribute](arkts-arkui-uiextensioncomponent-uiextensioncomponentattribute-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## onReceive

```TypeScript
onReceive(callback: ReceiveCallback | undefined): this
```

收到被拉起的Ability发送的数据时触发的回调。使用callback异步回调。<br/>AnonyMous Object Rectification

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ReceiveCallback](arkts-arkui-receivecallback-t-sys.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [UIExtensionComponentAttribute](arkts-arkui-uiextensioncomponent-uiextensioncomponentattribute-i-sys.md) |

## onRemoteReady

```TypeScript
onRemoteReady(callback: Callback<UIExtensionProxy> | undefined): this
```

UIExtensionAbility连接完成时的回调，之后可使用proxy向被拉起的Ability发送数据。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UIExtensionProxy](arkts-arkui-uiextensioncomponent-uiextensionproxy-i-sys.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [UIExtensionComponentAttribute](arkts-arkui-uiextensioncomponent-uiextensioncomponentattribute-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## onTerminated

```TypeScript
onTerminated(callback: Callback<TerminationInfo> | undefined): this
```

被拉起的UIExtensionAbility通过调用terminateSelfWithResult或者terminateSelf正常退出时，触发本回调函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TerminationInfo&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [UIExtensionComponentAttribute](arkts-arkui-uiextensioncomponent-uiextensioncomponentattribute-i-sys.md) |

## setUIExtensionComponentOptions

```TypeScript
setUIExtensionComponentOptions(want: Want, options?: UIExtensionOptions): this
```

设置UIExtensionComponent的选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [UIExtensionOptions](arkts-arkui-uiextensioncomponent-uiextensionoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |
