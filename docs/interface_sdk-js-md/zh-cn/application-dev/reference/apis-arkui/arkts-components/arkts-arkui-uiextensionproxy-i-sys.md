# UIExtensionProxy（系统接口）

该接口用于向UIExtensionAbility发送数据。当UIExtensionAbility连接成功时，它从UIExtensionComponent的onRemoteReady回调中返回。

**起始版本：** 10

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
```

## off('asyncReceiverRegister')

```TypeScript
off(type: 'asyncReceiverRegister', callback?: Callback<UIExtensionProxy>): void
```

注销监听UIExtensionAbility注册异步数据接收回调的监听器。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'asyncReceiverRegister' | 是 |
| callback | Callback&lt;[UIExtensionProxy](arkts-arkui-uiextensionproxy-i-sys.md)&gt; | 否 |

## off('syncReceiverRegister')

```TypeScript
off(type: 'syncReceiverRegister', callback?: Callback<UIExtensionProxy>): void
```

注销监听UIExtensionAbility注册同步数据接收回调的监听器。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'syncReceiverRegister' | 是 |
| callback | Callback&lt;[UIExtensionProxy](arkts-arkui-uiextensionproxy-i-sys.md)&gt; | 否 |

## on('asyncReceiverRegister')

```TypeScript
on(type: 'asyncReceiverRegister', callback: Callback<UIExtensionProxy>): void
```

注册监听器，用于监听UIExtensionAbility注册异步数据接收回调。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'asyncReceiverRegister' | 是 |
| callback | Callback&lt;[UIExtensionProxy](arkts-arkui-uiextensionproxy-i-sys.md)&gt; | 是 |

## on('syncReceiverRegister')

```TypeScript
on(type: 'syncReceiverRegister', callback: Callback<UIExtensionProxy>): void
```

注册监听器，用于监听UIExtensionAbility注册同步数据接收回调。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'syncReceiverRegister' | 是 |
| callback | Callback&lt;[UIExtensionProxy](arkts-arkui-uiextensionproxy-i-sys.md)&gt; | 是 |

## send

```TypeScript
send(data: Record<string, Object>): void
```

该接口用于向UIExtensionAbility发送数据。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | Record & lt;string, Object & gt; | 是 |

## sendSync

```TypeScript
sendSync(data: Record<string, Object>): Record<string, Object>
```

该接口用于向UIExtensionAbility发送数据，并以阻塞方式等待结果。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | Record & lt;string, Object & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| object |
| Record & lt;string, Object & gt; |

**错误码：**

| 错误码ID |
| --- |
| [100011](../errorcode-uiextension.md#100011-未注册同步回调) |
| [100012](../errorcode-uiextension.md#100012-数据发送失败) |
