# setIfaceConfig（系统接口）

## 导入模块

```TypeScript
import { ethernet } from 'kits/@kit.NetworkKit';
```

## setIfaceConfig

```TypeScript
function setIfaceConfig(iface: string, ic: InterfaceConfiguration, callback: AsyncCallback<void>): void
```

设置网络接口配置信息，使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.CONNECTIVITY_INTERNAL

**系统能力：** SystemCapability.Communication.NetManager.Ethernet

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| iface | string | 是 |
| ic | [InterfaceConfiguration](arkts-network-ethernet-interfaceconfiguration-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2200002](../errorcode-net-ethernet.md#2200002-连接服务失败) |
| [2200003](../errorcode-net-ethernet.md#2200003-系统内部错误) |
| 2201004 |
| [2201005](../errorcode-net-ethernet.md#2201005-设备信息不存在) |
| [2201006](../errorcode-net-ethernet.md#2201006-设备未连接) |
| [2201007](../errorcode-net-ethernet.md#2201007-用户配置写入失败) |


## setIfaceConfig

```TypeScript
function setIfaceConfig(iface: string, ic: InterfaceConfiguration): Promise<void>
```

设置网络接口配置信息，使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.CONNECTIVITY_INTERNAL

**系统能力：** SystemCapability.Communication.NetManager.Ethernet

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| iface | string | 是 |
| ic | [InterfaceConfiguration](arkts-network-ethernet-interfaceconfiguration-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2200002](../errorcode-net-ethernet.md#2200002-连接服务失败) |
| [2200003](../errorcode-net-ethernet.md#2200003-系统内部错误) |
| 2201004 |
| [2201005](../errorcode-net-ethernet.md#2201005-设备信息不存在) |
| [2201006](../errorcode-net-ethernet.md#2201006-设备未连接) |
| [2201007](../errorcode-net-ethernet.md#2201007-用户配置写入失败) |
