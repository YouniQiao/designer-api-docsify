# connectDevice（系统接口）

## 导入模块

```TypeScript
```

## connectDevice

```TypeScript
function connectDevice(addrInfo: AddressInfo, params: ConnectParam): Promise<AttachStateChangeInfo>
```

基于地址连接设备

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CONNECT_MECHANIC_HARDWARE

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-mechanicManager-function connectDevice(addrInfo: AddressInfo, params: ConnectParam): Promise<AttachStateChangeInfo>--><!--Device-mechanicManager-function connectDevice(addrInfo: AddressInfo, params: ConnectParam): Promise<AttachStateChangeInfo>-End-->

**系统能力：** SystemCapability.Mechanic.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| addrInfo | [AddressInfo](arkts-mechanic-mechanicmanager-addressinfo-i-sys.md) | 是 |
| params | [ConnectParam](arkts-mechanic-mechanicmanager-connectparam-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AttachStateChangeInfo](arkts-mechanic-mechanicmanager-attachstatechangeinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [33300001](../errorcode-mechanic.md#33300001-系统错误) |
