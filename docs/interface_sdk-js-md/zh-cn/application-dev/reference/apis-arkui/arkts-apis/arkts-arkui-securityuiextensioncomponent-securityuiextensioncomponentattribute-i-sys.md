# SecurityUIExtensionComponentAttribute（系统接口）

定义SecurityUIExtensionComponent的属性函数。

**继承/实现关系：** SecurityUIExtensionComponentAttribute extends CommonMethod

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<SecurityUIExtensionComponentAttribute> | undefined): this
```

设置SecurityUIExtensionComponent组件的属性修饰器。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[SecurityUIExtensionComponentAttribute](arkts-arkui-securityuiextensioncomponent-securityuiextensioncomponentattribute-i-sys.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SecurityUIExtensionComponentAttribute](arkts-arkui-securityuiextensioncomponent-securityuiextensioncomponentattribute-i-sys.md) |

## onError

```TypeScript
onError(callback: ErrorCallback<BusinessError> | undefined): this
```

被拉起的UIExtensionAbility在运行过程中发生异常时触发的回调，不包含与UIExtensionAbility断开连接场景。使用callback异步回调。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

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
| [SecurityUIExtensionComponentAttribute](arkts-arkui-securityuiextensioncomponent-securityuiextensioncomponentattribute-i-sys.md) |

## onReceive

```TypeScript
onReceive(callback: ReceiveCallback | undefined): this
```

收到被拉起的Ability发送的数据时触发的回调。使用callback异步回调。<br/>AnonyMous Object Rectification

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

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
| [SecurityUIExtensionComponentAttribute](arkts-arkui-securityuiextensioncomponent-securityuiextensioncomponentattribute-i-sys.md) |

## onRemoteReady

```TypeScript
onRemoteReady(callback: Callback<SecurityUIExtensionProxy> | undefined): this
```

UIExtensionAbility连接完成时触发的回调，使用callback异步回调。之后可通过返回的SecurityUIExtensionProxy向被拉起的Ability发送数据。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityUIExtensionProxy](arkts-arkui-securityuiextensioncomponent-securityuiextensionproxy-i-sys.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SecurityUIExtensionComponentAttribute](arkts-arkui-securityuiextensioncomponent-securityuiextensioncomponentattribute-i-sys.md) |

## onTerminated

```TypeScript
onTerminated(callback: Callback<TerminationInfo> | undefined): this
```

被拉起的UIExtensionAbility通过调用terminateSelfWithResult或terminateSelf正常退出时触发此回调。使用callback异步回调。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

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
| [SecurityUIExtensionComponentAttribute](arkts-arkui-securityuiextensioncomponent-securityuiextensioncomponentattribute-i-sys.md) |

## setSecurityUIExtensionComponentOptions

```TypeScript
default setSecurityUIExtensionComponentOptions(want: Want, options?: SecurityUIExtensionOptions): this
```

设置SecurityUIExtensionComponent的选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [SecurityUIExtensionOptions](arkts-arkui-securityuiextensioncomponent-securityuiextensionoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |
