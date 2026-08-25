# DeviceManager

设备管理实例，用于获取可信设备和本地设备的相关信息。在调用DeviceManager的方法前，需要先通过createDeviceManager构建一个DeviceManager实例dmInstance。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** [DeviceManager](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md)

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

## 导入模块

```TypeScript
import { deviceManager } from 'kits/@kit.DistributedServiceKit';
```

## authenticateDevice

```TypeScript
authenticateDevice(
      deviceInfo: DeviceInfo,
      authParam: AuthParam,
      callback: AsyncCallback<{ deviceId: string, pinToken?: number }>
    ): void
```

认证设备。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** [bindTarget](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#bindtarget)(deviceId: string, bindParam: { [key: string]: Object; }, callback: AsyncCallback&lt;{deviceId: string;}&gt;)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceInfo | [DeviceInfo](../../apis-avsession-kit/arkts-apis/arkts-avsession-avsession-deviceinfo-i.md) | 是 |
| [authParam](../../apis-user-authentication-kit/arkts-apis/arkts-userauthentication-useriam-userauthicon-userauthicon-s.md) | [AuthParam](../../apis-user-authentication-kit/arkts-apis/arkts-userauthentication-userauth-authparam-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;{ deviceId: string, pinToken?: number }&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## deleteCredential

```TypeScript
deleteCredential(queryInfo: string, callback: AsyncCallback<{ resultInfo: string }>): void
```

删除凭据信息。

**起始版本：** 10

**废弃版本：** 11

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| queryInfo | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;{ resultInfo: string }&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getDeviceInfo

```TypeScript
getDeviceInfo(networkId: string, callback: AsyncCallback<DeviceInfo>): void
```

通过指定设备的网络标识获取该设备的信息。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getDeviceName](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getdevicename)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| networkId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DeviceInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getDeviceInfo

```TypeScript
getDeviceInfo(networkId: string): Promise<DeviceInfo>
```

通过指定设备的网络标识获取该设备的信息。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getDeviceName](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getdevicename)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| networkId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;DeviceInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getLocalDeviceInfo

```TypeScript
getLocalDeviceInfo(callback: AsyncCallback<DeviceInfo>): void
```

获取本地设备信息。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** [getLocalDeviceNetworkId](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getlocaldevicenetworkid)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DeviceInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getLocalDeviceInfo

```TypeScript
getLocalDeviceInfo(): Promise<DeviceInfo>
```

获取本地设备信息。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** [getLocalDeviceNetworkId](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getlocaldevicenetworkid)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;DeviceInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getLocalDeviceInfoSync

```TypeScript
getLocalDeviceInfoSync(): DeviceInfo
```

同步获取本地设备信息。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** [getLocalDeviceNetworkId](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getlocaldevicenetworkid)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [DeviceInfo](../../apis-avsession-kit/arkts-apis/arkts-avsession-avsession-deviceinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## getTrustedDeviceList

```TypeScript
getTrustedDeviceList(callback: AsyncCallback<Array<DeviceInfo>>): void
```

获取所有可信设备列表。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** [getAvailableDeviceList](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelist)(callback: AsyncCallback&lt;Array&lt;DeviceBasicInfo&gt;&gt;)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;DeviceInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getTrustedDeviceList

```TypeScript
getTrustedDeviceList(): Promise<Array<DeviceInfo>>
```

获取所有可信设备列表。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** [getAvailableDeviceList](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelist)()

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;DeviceInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getTrustedDeviceListSync

```TypeScript
getTrustedDeviceListSync(): Array<DeviceInfo>
```

同步获取所有可信设备列表。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** [getAvailableDeviceListSync](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Array & lt;DeviceInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## getTrustedDeviceListSync

```TypeScript
getTrustedDeviceListSync(isRefresh: boolean): Array<DeviceInfo>
```

打开软总线系统端的心跳模式，让周围处于下线状态的可信设备快速上线，同时刷新已上线的可信设备列表。

**起始版本：** 10

**废弃版本：** 11

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isRefresh | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;DeviceInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## importCredential

```TypeScript
importCredential(credentialInfo: string, callback: AsyncCallback<{ resultInfo: string }>): void
```

导入凭据信息。

**起始版本：** 10

**废弃版本：** 11

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| credentialInfo | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;{ resultInfo: string }&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## off('uiStateChange')

```TypeScript
off(type: 'uiStateChange', callback?: Callback<{ param: string }>): void
```

取消ui状态变更回调。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** off(type: 'replyResult', callback: Callback&lt;{ param: string; }&gt;)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'uiStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ param: string }&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## off('deviceStateChange')

```TypeScript
off(type: 'deviceStateChange', callback?: Callback<{ action: DeviceStateChangeAction, device: DeviceInfo }>): void
```

取消注册设备状态回调。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** [off](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#offdevicestatechange)(type: 'deviceStateChange', callback?: Callback&lt;{ action: DeviceStateChange; device: DeviceBasicInfo; }&gt;)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deviceStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ action: DeviceStateChangeAction, device: DeviceInfo }&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## off('deviceFound')

```TypeScript
off(type: 'deviceFound', callback?: Callback<{ subscribeId: number, device: DeviceInfo }>): void
```

取消注册设备发现回调。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** off(type: 'discoverSuccess', callback: Callback&lt;{ device: DeviceBasicInfo; }&gt;)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deviceFound' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ subscribeId: number, device: DeviceInfo }&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## off('discoverFail')

```TypeScript
off(type: 'discoverFail', callback?: Callback<{ subscribeId: number, reason: number }>): void
```

取消注册设备发现失败回调。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** off(type: 'discoverFailure', callback: Callback&lt;{ reason: int; }&gt;)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'discoverFail' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ subscribeId: number, reason: number }&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## off('publishSuccess')

```TypeScript
off(type: 'publishSuccess', callback?: Callback<{ publishId: number }>): void
```

取消注册设备发布成功回调。

**起始版本：** 9

**废弃版本：** 11

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'publishSuccess' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ publishId: number }&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## off('publishFail')

```TypeScript
off(type: 'publishFail', callback?: Callback<{ publishId: number, reason: number }>): void
```

取消注册设备发布失败回调。

**起始版本：** 9

**废弃版本：** 11

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'publishFail' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ publishId: number, reason: number }&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## off('serviceDie')

```TypeScript
off(type: 'serviceDie', callback?: () => void): void
```

取消注册设备管理服务死亡监听。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** [off](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#offservicedie)(type: 'serviceDie', callback?: Callback&lt;{}&gt;)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'serviceDie' | 是 |
| callback | () = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## on('uiStateChange')

```TypeScript
on(type: 'uiStateChange', callback: Callback<{ param: string }>): void
```

ui状态变更回调。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [on](arkts-distributedservice-distributeddevicemanager-devicemanager-i-sys.md#onreplyresult)(type: 'replyResult', callback: Callback&lt;{ param: string; }&gt;)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'uiStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ param: string }&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## on('deviceStateChange')

```TypeScript
on(type: 'deviceStateChange', callback: Callback<{ action: DeviceStateChangeAction, device: DeviceInfo }>): void
```

注册设备状态回调。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** [on](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#ondevicestatechange)(type: 'deviceStateChange', callback: Callback&lt;{ action: DeviceStateChange; device: DeviceBasicInfo; }&gt;)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deviceStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ action: DeviceStateChangeAction, device: DeviceInfo }&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## on('deviceFound')

```TypeScript
on(type: 'deviceFound', callback: Callback<{ subscribeId: number, device: DeviceInfo }>): void
```

注册发现设备回调监听。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** [on](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#ondiscoversuccess)(type: 'discoverSuccess', callback: Callback&lt;{ device: DeviceBasicInfo; }&gt;)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deviceFound' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ subscribeId: number, device: DeviceInfo }&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## on('discoverFail')

```TypeScript
on(type: 'discoverFail', callback: Callback<{ subscribeId: number, reason: number }>): void
```

注册设备发现失败回调监听。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** on(type: 'discoverFailure', callback: Callback&lt;{ reason: int; }&gt;)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'discoverFail' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ subscribeId: number, reason: number }&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## on('publishSuccess')

```TypeScript
on(type: 'publishSuccess', callback: Callback<{ publishId: number }>): void
```

注册发布设备发现回调监听。

**起始版本：** 9

**废弃版本：** 11

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'publishSuccess' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ publishId: number }&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## on('publishFail')

```TypeScript
on(type: 'publishFail', callback: Callback<{ publishId: number, reason: number }>): void
```

注册设备发布失败回调监听。

**起始版本：** 9

**废弃版本：** 11

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'publishFail' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ publishId: number, reason: number }&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## on('serviceDie')

```TypeScript
on(type: 'serviceDie', callback: () => void): void
```

注册设备管理服务死亡监听。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** [on](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#onservicedie)(type: 'serviceDie', callback?: Callback&lt;{}&gt;)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'serviceDie' | 是 |
| callback | () = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## publishDeviceDiscovery

```TypeScript
publishDeviceDiscovery(publishInfo: PublishInfo): void
```

发布设备发现。发布状态持续两分钟，超过两分钟会停止发布。

**起始版本：** 9

**废弃版本：** 11

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| publishInfo | [PublishInfo](arkts-distributedservice-devicemanager-publishinfo-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [11600105](../errorcode-device-manager.md#11600105-发布业务不可用) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## release

```TypeScript
release(): void
```

设备管理实例不再使用后，通过该方法释放DeviceManager实例。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** [releaseDeviceManager](arkts-distributedservice-distributeddevicemanager-releasedevicemanager-f.md)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## requestCredentialRegisterInfo

```TypeScript
requestCredentialRegisterInfo(requestInfo: string, callback: AsyncCallback<{ registerInfo: string }>): void
```

获取凭据的注册信息。

**起始版本：** 10

**废弃版本：** 11

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| requestInfo | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;{ registerInfo: string }&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setUserOperation

```TypeScript
setUserOperation(operateAction: number, params: string): void
```

设置用户ui操作行为。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [replyUiAction](arkts-distributedservice-distributeddevicemanager-devicemanager-i-sys.md#replyuiaction)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| operateAction | number | 是 |
| params | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## startDeviceDiscovery

```TypeScript
startDeviceDiscovery(subscribeInfo: SubscribeInfo): void
```

发现周边设备。发现状态持续两分钟，超过两分钟，会停止发现，最大发现数量99个。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** [startDiscovering](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#startdiscovering)(discoverParam: { [key: string]: Object; }, filterOptions?: { [key: string]: Object; })

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| subscribeInfo | [SubscribeInfo](arkts-distributedservice-devicemanager-subscribeinfo-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [11600104](../errorcode-device-manager.md#11600104-发现业务不可用) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## startDeviceDiscovery

```TypeScript
startDeviceDiscovery(subscribeInfo: SubscribeInfo, filterOptions?: string): void
```

发现周边设备。发现状态持续两分钟，超过两分钟，会停止发现，最大发现数量99个。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [startDiscovering](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#startdiscovering)(discoverParam: { [key: string]: Object; }, filterOptions?: { [key: string]: Object; })

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| subscribeInfo | [SubscribeInfo](arkts-distributedservice-devicemanager-subscribeinfo-i-sys.md) | 是 |
| [filterOptions](../../apis-audio-kit/arkts-apis/arkts-audio-audio-audioplaybackcaptureconfig-i.md) | string | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [11600104](../errorcode-device-manager.md#11600104-发现业务不可用) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## stopDeviceDiscovery

```TypeScript
stopDeviceDiscovery(subscribeId: number): void
```

停止发现周边设备。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** [stopDiscovering](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#stopdiscovering)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [subscribeId](arkts-distributedservice-devicemanager-subscribeinfo-i-sys.md) | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## unAuthenticateDevice

```TypeScript
unAuthenticateDevice(deviceInfo: DeviceInfo): void
```

解除认证设备。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** [unbindTarget](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#unbindtarget)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceInfo | [DeviceInfo](../../apis-avsession-kit/arkts-apis/arkts-avsession-avsession-deviceinfo-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## unPublishDeviceDiscovery

```TypeScript
unPublishDeviceDiscovery(publishId: number): void
```

停止发布设备发现。

**起始版本：** 9

**废弃版本：** 11

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [publishId](arkts-distributedservice-devicemanager-publishinfo-i-sys.md) | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

## verifyAuthInfo

```TypeScript
verifyAuthInfo(authInfo: AuthInfo, callback: AsyncCallback<{ deviceId: string, level: number }>): void
```

验证认证信息。

**起始版本：** 7

**废弃版本：** 11

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| authInfo | [AuthInfo](arkts-distributedservice-devicemanager-authinfo-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;{ deviceId: string, level: number }&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
