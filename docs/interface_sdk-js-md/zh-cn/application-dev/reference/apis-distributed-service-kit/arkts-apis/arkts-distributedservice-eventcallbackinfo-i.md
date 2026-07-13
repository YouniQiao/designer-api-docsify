# EventCallbackInfo

回调方法的接收信息。

**起始版本：** 18

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

## data

```TypeScript
data?: ArrayBuffer
```

表示接收的字节流。

**类型：** ArrayBuffer

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

## msg

```TypeScript
msg?: string
```

表示接收的消息。

**类型：** string

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

## reason

```TypeScript
reason?: DisconnectReason
```

表示断连原因。

**类型：** DisconnectReason

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

## sessionId

```TypeScript
sessionId: number
```

表示当前事件对应的协同会话ID。

**类型：** number

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

