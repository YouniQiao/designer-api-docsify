# DeviceManager

设备管理实例，是分布式设备管理方法的调用入口，提供设备发现、设备认证、状态监听和信息查询等能力。 在调用DeviceManager的方法前，需要先通过createDeviceManager构建一个DeviceManager实例dmInstance。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

## 导入模块

```TypeScript
import { distributedDeviceManager } from 'kits/@kit.DistributedServiceKit';
```

## bindTarget

```TypeScript
bindTarget(deviceId: string, bindParam: { [key: string]: Object; }, callback: AsyncCallback<{deviceId: string;}>): void
```

认证设备，将发现的不可信设备通过认证流程绑定为可信设备。认证过程中，系统会根据bindParam中指定的认证类型发起认证请求， 认证成功后设备将加入可信设备列表，可通过getAvailableDeviceListSync查询。当不再需要与目标设备进行分布式业务时， 可调用unbindTarget解除绑定。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| bindParam | { [key: string]: Object; } | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;{deviceId: string;}&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |
| [11600103](../errorcode-device-manager.md#11600103-认证业务不可用) |

## getAvailableDeviceList

```TypeScript
getAvailableDeviceList(callback: AsyncCallback<Array<DeviceBasicInfo>>): void
```

获取所有在线可信设备。调用前需先通过createDeviceManager创建DeviceManager实例。使用callback异步回调。 与getAvailableDeviceListSync的区别在于：本方法为异步调用，通过callback返回结果；getAvailableDeviceListSync为同步调用， 直接返回结果。建议在不希望阻塞线程的场景使用本方法，在需要阻塞等待结果的场景使用getAvailableDeviceListSync。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[DeviceBasicInfo](arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## getAvailableDeviceList

```TypeScript
getAvailableDeviceList(): Promise<Array<DeviceBasicInfo>>
```

获取所有在线可信设备。调用前需先通过createDeviceManager创建DeviceManager实例。使用Promise异步回调。 与getAvailableDeviceListSync的区别在于：本方法为异步调用，通过Promise返回结果；getAvailableDeviceListSync为同步调用， 直接返回结果。建议在不希望阻塞线程的场景使用本方法，在需要阻塞等待结果的场景使用getAvailableDeviceListSync。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[DeviceBasicInfo](arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## getAvailableDeviceListSync

```TypeScript
getAvailableDeviceListSync(): Array<DeviceBasicInfo>
```

同步获取所有在线可信设备。调用前需先通过createDeviceManager创建DeviceManager实例。 与getAvailableDeviceList的区别在于：本方法为同步调用，直接返回结果；getAvailableDeviceList为异步调用，通过callback 或Promise返回结果。建议在需要阻塞等待结果的场景使用本方法，在不希望阻塞线程的场景使用getAvailableDeviceList。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**返回值：**

| 类型 |
| --- |
| Array&lt;[DeviceBasicInfo](arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## getDeviceName

```TypeScript
getDeviceName(networkId: string): string
```

通过指定设备的网络标识获取该设备名称。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| networkId | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## getDeviceType

```TypeScript
getDeviceType(networkId: string): number
```

通过指定设备的网络标识获取该设备类型。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## getLocalDeviceId

```TypeScript
getLocalDeviceId(): string
```

获取本地设备id，实际值为udid-hash与appid和盐值基于sha256方式进行混淆后的值。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## getLocalDeviceName

```TypeScript
getLocalDeviceName(): string
```

获取本地设备名称。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## getLocalDeviceNetworkId

```TypeScript
getLocalDeviceNetworkId(): string
```

获取本地设备网络标识。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## getLocalDeviceType

```TypeScript
getLocalDeviceType(): number
```

获取本地设备类型。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## off('deviceStateChange')

```TypeScript
off(type: 'deviceStateChange', callback?: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>): void
```

取消注册设备状态回调。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deviceStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ action: DeviceStateChange; device: DeviceBasicInfo; }&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('discoverSuccess')

```TypeScript
off(type: 'discoverSuccess', callback?: Callback<{ device: DeviceBasicInfo; }>): void
```

取消注册设备发现成功回调。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'discoverSuccess' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ device: DeviceBasicInfo; }&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('deviceNameChange')

```TypeScript
off(type: 'deviceNameChange', callback?: Callback<{ deviceName: string; }>): void
```

取消注册设备名称变更回调监听。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deviceNameChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ deviceName: string; }&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('discoverFailure')

```TypeScript
off(type: 'discoverFailure', callback?: Callback<{ reason: number; }>): void
```

取消注册设备发现失败回调。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'discoverFailure' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ reason: number; }&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('serviceDie')

```TypeScript
off(type: 'serviceDie', callback?: Callback<{}>): void
```

取消注册设备管理服务死亡回调。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'serviceDie' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{}&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('deviceStateChange')

```TypeScript
on(type: 'deviceStateChange', callback: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>): void
```

注册设备状态回调，以便在设备状态发生变化时通知应用。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deviceStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ action: DeviceStateChange; device: DeviceBasicInfo; }&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('discoverSuccess')

```TypeScript
on(type: 'discoverSuccess', callback: Callback<{ device: DeviceBasicInfo; }>): void
```

注册发现设备成功回调。使用callback异步回调。此回调在调用startDiscovering发现到周边设备时触发， 返回发现的设备信息（DeviceBasicInfo）。需在调用startDiscovering之前注册此回调。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'discoverSuccess' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ device: DeviceBasicInfo; }&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('deviceNameChange')

```TypeScript
on(type: 'deviceNameChange', callback: Callback<{ deviceName: string; }>): void
```

注册设备名称变更回调，以便在设备名称改变时通知应用。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deviceNameChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ deviceName: string; }&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('discoverFailure')

```TypeScript
on(type: 'discoverFailure', callback: Callback<{ reason: number; }>): void
```

注册设备发现失败回调。使用callback异步回调。此回调在调用startDiscovering发现设备失败时触发， 返回失败原因。需在调用startDiscovering之前注册此回调。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'discoverFailure' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ reason: number; }&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('serviceDie')

```TypeScript
on(type: 'serviceDie', callback?: Callback<{}>): void
```

注册设备管理服务死亡回调，以便在服务死亡时通知应用。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'serviceDie' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{}&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## startDiscovering

```TypeScript
startDiscovering(discoverParam: { [key: string]: Object; }, filterOptions?: { [key: string]: Object; }): void
```

发现周边设备，用于在需要建立分布式连接前搜索可用设备。发现状态持续两分钟，超时后自动停止，最大发现数量为99个。使用WiFi进行 设备发现时，要求发现方与被发现方处于同一局域网内。调用本方法前，需先通过on('discoverSuccess')注册设备发现成功回调以接收 发现的设备信息，并通过on('discoverFailure')注册设备发现失败回调以接收失败通知。发现完成后可调用stopDiscovering停止发现。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| discoverParam | { [key: string]: Object; } | 是 |
| [filterOptions](../../apis-audio-kit/arkts-apis/arkts-audio-audio-audioplaybackcaptureconfig-i.md) | { [key: string]: Object; } | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [11600104](../errorcode-device-manager.md#11600104-发现业务不可用) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## stopDiscovering

```TypeScript
stopDiscovering(): void
```

停止发现周边设备。与startDiscovering方法配合使用，用于在发现超时（两分钟）前手动停止设备发现。 需在调用startDiscovering之后调用。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## unbindTarget

```TypeScript
unbindTarget(deviceId: string): void
```

解除认证设备，用于在不再需要与目标设备进行分布式业务时，解除与该设备的认证关系。与bindTarget方法配合使用， 仅能解除已通过bindTarget认证绑定的可信设备。解除后设备将从可信设备列表中移除， 可通过getAvailableDeviceListSync或getAvailableDeviceList查询确认。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |
