# SecurityUIExtensionProxy（系统接口）

用于在双方建立连接成功后，向被拉起的Ability发送数据，以及订阅和取消订阅事件回调。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## offAsyncReceiverRegister

```TypeScript
offAsyncReceiverRegister(callback?: Callback<SecurityUIExtensionProxy>): void
```

取消订阅被拉起的Ability发生异步注册的回调。使用callback异步回调。 AnonyMous Object Rectification

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityUIExtensionProxy](arkts-arkui-securityuiextensioncomponent-securityuiextensionproxy-i-sys.md)&gt; | 否 |

## offSyncReceiverRegister

```TypeScript
offSyncReceiverRegister(callback?: Callback<SecurityUIExtensionProxy>): void
```

取消订阅被拉起的Ability发生同步注册的回调。使用callback异步回调。 AnonyMous Object Rectification

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityUIExtensionProxy](arkts-arkui-securityuiextensioncomponent-securityuiextensionproxy-i-sys.md)&gt; | 否 |

## onAsyncReceiverRegister

```TypeScript
onAsyncReceiverRegister(callback: Callback<SecurityUIExtensionProxy>): void
```

订阅被拉起的Ability发生异步注册的回调。使用callback异步回调。 AnonyMous Object Rectification

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityUIExtensionProxy](arkts-arkui-securityuiextensioncomponent-securityuiextensionproxy-i-sys.md)&gt; | 是 |

## onSyncReceiverRegister

```TypeScript
onSyncReceiverRegister(callback: Callback<SecurityUIExtensionProxy>): void
```

订阅被拉起的Ability发生同步注册的回调。使用callback异步回调。 AnonyMous Object Rectification

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityUIExtensionProxy](arkts-arkui-securityuiextensioncomponent-securityuiextensionproxy-i-sys.md)&gt; | 是 |

## send

```TypeScript
send(data: Record<string, RecordData>): void
```

用于在双方建立连接成功后，向被拉起的Ability发送数据，提供异步发送能力。数据将被扩展Ability通过setReceiveDataCallback接收处理。 AnonyMous Object Rectification

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | Record&lt;string, [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt; | 是 |

## sendSync

```TypeScript
sendSync(data: Record<string, RecordData>): Record<string, RecordData>
```

用于在双方建立连接成功后，向被拉起的Ability同步发送数据，数据将被拉起的Ability通过setReceiveDataForResultCallback处理并返回结果。 AnonyMous Object Rectification

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | Record&lt;string, [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Record&lt;string, [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [100011](../errorcode-uiextension.md#100011-未注册同步回调) |
| [100012](../errorcode-uiextension.md#100012-数据发送失败) |
