# RemoteDevice

远程设备操作方法。

**起始版本：** 26.0.0

**废弃版本：** -1

<!--Device-remoteDevice-interface RemoteDevice--><!--Device-remoteDevice-interface RemoteDevice-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

## getAcbState

```TypeScript
getAcbState(): AcbState
```

获取ACB连接状态。

**起始版本：** 26.0.0

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RemoteDevice-getAcbState(): AcbState--><!--Device-RemoteDevice-getAcbState(): AcbState-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**返回值：**

| 类型 |
| --- |
| [AcbState](arkts-connectivity-nearlinkconstant-acbstate-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [36100003](../errorcode-nearlink-service.md#36100003-星闪关闭) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## getConnectionState

```TypeScript
getConnectionState(): ConnectionState
```

获取profile连接状态。

**起始版本：** 26.0.0

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RemoteDevice-getConnectionState(): ConnectionState--><!--Device-RemoteDevice-getConnectionState(): ConnectionState-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**返回值：**

| 类型 |
| --- |
| [ConnectionState](arkts-connectivity-remotedevice-connectionstate-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [36100003](../errorcode-nearlink-service.md#36100003-星闪关闭) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## getDeviceClass

```TypeScript
getDeviceClass(): DeviceClass
```

获取星闪设备的类型。

**起始版本：** 26.0.0

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RemoteDevice-getDeviceClass(): DeviceClass--><!--Device-RemoteDevice-getDeviceClass(): DeviceClass-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**返回值：**

| 类型 |
| --- |
| [DeviceClass](arkts-connectivity-nearlinkconstant-deviceclass-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [36100003](../errorcode-nearlink-service.md#36100003-星闪关闭) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## getDeviceInformation

```TypeScript
getDeviceInformation(): DeviceInformation
```

获取远端设备信息。

**起始版本：** 26.0.0

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RemoteDevice-getDeviceInformation(): DeviceInformation--><!--Device-RemoteDevice-getDeviceInformation(): DeviceInformation-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**返回值：**

| 类型 |
| --- |
| [DeviceInformation](arkts-connectivity-remotedevice-deviceinformation-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [36100003](../errorcode-nearlink-service.md#36100003-星闪关闭) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## getDeviceName

```TypeScript
getDeviceName(): string
```

获取星闪设备的名称。

**起始版本：** 26.0.0

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RemoteDevice-getDeviceName(): string--><!--Device-RemoteDevice-getDeviceName(): string-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [36100003](../errorcode-nearlink-service.md#36100003-星闪关闭) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## getPairingState

```TypeScript
getPairingState(): PairingState
```

获取配对状态。

**起始版本：** 26.0.0

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RemoteDevice-getPairingState(): PairingState--><!--Device-RemoteDevice-getPairingState(): PairingState-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**返回值：**

| 类型 |
| --- |
| [PairingState](arkts-connectivity-remotedevice-pairingstate-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [36100003](../errorcode-nearlink-service.md#36100003-星闪关闭) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## startPairing

```TypeScript
startPairing(): Promise<void>
```

启动与远端星闪设备的配对。

**起始版本：** 26.0.0

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RemoteDevice-startPairing(): Promise<void>--><!--Device-RemoteDevice-startPairing(): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [36100003](../errorcode-nearlink-service.md#36100003-星闪关闭) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
