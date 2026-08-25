# DeviceManager

设备管理实例，是分布式设备管理方法的调用入口，提供设备发现、设备认证、状态监听和信息查询等能力。 在调用DeviceManager的方法前，需要先通过createDeviceManager构建一个DeviceManager实例dmInstance。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

## 导入模块

```TypeScript
import { distributedDeviceManager } from 'kits/@kit.DistributedServiceKit';
```

## getDeviceIconInfo

```TypeScript
getDeviceIconInfo(filterOptions: DeviceIconInfoFilterOptions): Promise<DeviceIconInfo>
```

获取设备图标，使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [filterOptions](../../apis-audio-kit/arkts-apis/arkts-audio-audio-audioplaybackcaptureconfig-i.md) | [DeviceIconInfoFilterOptions](arkts-distributedservice-distributeddevicemanager-deviceiconinfofilteroptions-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DeviceIconInfo](arkts-distributedservice-distributeddevicemanager-deviceiconinfo-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |
| [11600106](../errorcode-device-manager.md#11600106-从云端获取数据失败) |

## getDeviceNetworkIdList

```TypeScript
getDeviceNetworkIdList(filterOptions: NetworkIdQueryFilter): Promise<Array<string>>
```

获取符合条件的网络设备ID列表。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [filterOptions](../../apis-audio-kit/arkts-apis/arkts-audio-audio-audioplaybackcaptureconfig-i.md) | [NetworkIdQueryFilter](arkts-distributedservice-distributeddevicemanager-networkidqueryfilter-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |
| [11600107](../errorcode-device-manager.md#11600107-需要登录账号) |

## getDeviceProfileInfoList

```TypeScript
getDeviceProfileInfoList(filterOptions: DeviceProfileInfoFilterOptions): Promise<Array<DeviceProfileInfo>>
```

获取同账号下全部的设备列表，使用Promise异步回调。

**起始版本：** 15

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [filterOptions](../../apis-audio-kit/arkts-apis/arkts-audio-audio-audioplaybackcaptureconfig-i.md) | [DeviceProfileInfoFilterOptions](arkts-distributedservice-distributeddevicemanager-deviceprofileinfofilteroptions-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[DeviceProfileInfo](arkts-distributedservice-distributeddevicemanager-deviceprofileinfo-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |
| [11600106](../errorcode-device-manager.md#11600106-从云端获取数据失败) |
| [11600107](../errorcode-device-manager.md#11600107-需要登录账号) |

## getIdentificationByDeviceIds

```TypeScript
getIdentificationByDeviceIds(deviceIds: Array<string>): Array<DeviceIdentification>
```

根据设备ID查询设备标识。

**起始版本：** 24

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC and ohos.permission.ACCESS_SERVICE_DM and ohos.permission.sec.ACCESS_UDID

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceIds | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[DeviceIdentification](arkts-distributedservice-distributeddevicemanager-deviceidentification-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## getLocalDisplayDeviceName

```TypeScript
getLocalDisplayDeviceName(maxNameLength: number): Promise<string>
```

获取本机指定长度（字节数）的显示名，使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| maxNameLength | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |

## getOsTypeByNetworkId

```TypeScript
getOsTypeByNetworkId(networkId: string): number
```

通过设备网络ID查询设备操作系统类型。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC and ohos.permission.ACCESS_SERVICE_DM

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| networkId | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |
| [11600110](../errorcode-device-manager.md#11600110-无效的网络id) |

## off('replyResult')

```TypeScript
off(type: 'replyResult', callback?: Callback<{ param: string; }>): void
```

取消回复UI操作结果回调。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'replyResult' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ param: string; }&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## on('replyResult')

```TypeScript
on(type: 'replyResult', callback: Callback<{ param: string; }>): void
```

回复UI操作结果回调。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'replyResult' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ param: string; }&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## putDeviceProfileInfoList

```TypeScript
putDeviceProfileInfoList(deviceProfileInfoList: Array<DeviceProfileInfo>): Promise<number>
```

业务调用更新设备列表，使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceProfileInfoList | Array&lt;[DeviceProfileInfo](arkts-distributedservice-distributeddevicemanager-deviceprofileinfo-i-sys.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |

## replyUiAction

```TypeScript
replyUiAction(action: number, actionResult: string): void
```

回复用户UI操作行为。此接口只能被devicemanager的PIN码hap使用。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| action | number | 是 |
| actionResult | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## restoreLocalDeivceName

```TypeScript
restoreLocalDeivceName(): void
```

系统重置还原网络设置时，还原本机设备名。

**起始版本：** 18

**废弃版本：** 24

**替代接口：** [restoreLocalDeviceName](#restorelocaldevicename)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |

## restoreLocalDeviceName

```TypeScript
restoreLocalDeviceName(): void
```

系统重置还原网络设置时，还原本机设备名。

**起始版本：** 24

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |

## setHeartbeatPolicy

```TypeScript
setHeartbeatPolicy(policy: StrategyForHeartbeat, delayTime: number): void
```

设置心跳广播策略。

**起始版本：** 15

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| policy | [StrategyForHeartbeat](arkts-distributedservice-distributeddevicemanager-strategyforheartbeat-e-sys.md) | 是 |
| delayTime | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |

## setLocalDeviceName

```TypeScript
setLocalDeviceName(deviceName: string): Promise<number>
```

修改本机设备名称，使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |
| [11600106](../errorcode-device-manager.md#11600106-从云端获取数据失败) |
| [11600107](../errorcode-device-manager.md#11600107-需要登录账号) |
| [11600108](../errorcode-device-manager.md#11600108-设备名称含非法信息) |

## setRemoteDeviceName

```TypeScript
setRemoteDeviceName(deviceId: string, deviceName: string): Promise<number>
```

设置配件设备名称，使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| deviceName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |
| [11600106](../errorcode-device-manager.md#11600106-从云端获取数据失败) |
| [11600107](../errorcode-device-manager.md#11600107-需要登录账号) |
| [11600108](../errorcode-device-manager.md#11600108-设备名称含非法信息) |
