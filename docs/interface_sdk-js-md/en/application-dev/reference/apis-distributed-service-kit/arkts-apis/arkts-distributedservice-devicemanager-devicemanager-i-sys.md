# DeviceManager

Provides APIs to obtain information about trusted devices and local devices. Before calling any API in **DeviceManager**, you must use **createDeviceManager** to create a **DeviceManager** instance, for example, **dmInstance**.

**Since:** 7

**Deprecated since:** 11

**Substitutes:** [DeviceManager](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md)

**System capability:** SystemCapability.DistributedHardware.DeviceManager

## Modules to Import

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

Authenticates a device.

**Since:** 7

**Deprecated since:** 11

**Substitutes:** [bindTarget](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#bindtarget)(deviceId: string, bindParam: { [key: string]: Object; }, callback: AsyncCallback&lt;{deviceId: string;}&gt;)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceInfo | [DeviceInfo](../../apis-avsession-kit/arkts-apis/arkts-avsession-avsession-deviceinfo-i.md) | Yes |
| [authParam](../../apis-user-authentication-kit/arkts-apis/arkts-userauthentication-useriam-userauthicon-userauthicon-s.md) | [AuthParam](../../apis-user-authentication-kit/arkts-apis/arkts-userauthentication-userauth-authparam-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;{ deviceId: string, pinToken?: number }&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## deleteCredential

```TypeScript
deleteCredential(queryInfo: string, callback: AsyncCallback<{ resultInfo: string }>): void
```

Deletes credential information.

**Since:** 10

**Deprecated since:** 11

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| queryInfo | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;{ resultInfo: string }&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getDeviceInfo

```TypeScript
getDeviceInfo(networkId: string, callback: AsyncCallback<DeviceInfo>): void
```

Obtains the information about a specific device based on the network ID. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [getDeviceName](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getdevicename)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| networkId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DeviceInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getDeviceInfo

```TypeScript
getDeviceInfo(networkId: string): Promise<DeviceInfo>
```

Obtains the information about a specific device based on the network ID. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [getDeviceName](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getdevicename)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| networkId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;DeviceInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getLocalDeviceInfo

```TypeScript
getLocalDeviceInfo(callback: AsyncCallback<DeviceInfo>): void
```

Obtains local device information. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 11

**Substitutes:** [getLocalDeviceNetworkId](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getlocaldevicenetworkid)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DeviceInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getLocalDeviceInfo

```TypeScript
getLocalDeviceInfo(): Promise<DeviceInfo>
```

Obtains local device information. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 11

**Substitutes:** [getLocalDeviceNetworkId](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getlocaldevicenetworkid)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;DeviceInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getLocalDeviceInfoSync

```TypeScript
getLocalDeviceInfoSync(): DeviceInfo
```

Obtains local device information synchronously.

**Since:** 8

**Deprecated since:** 11

**Substitutes:** [getLocalDeviceNetworkId](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getlocaldevicenetworkid)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DeviceInfo](../../apis-avsession-kit/arkts-apis/arkts-avsession-avsession-deviceinfo-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [11600101](../errorcode-device-manager.md#11600101-service-invoking-exception) |

## getTrustedDeviceList

```TypeScript
getTrustedDeviceList(callback: AsyncCallback<Array<DeviceInfo>>): void
```

Obtains all trusted devices. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 11

**Substitutes:** [getAvailableDeviceList](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelist)(callback: AsyncCallback&lt;Array&lt;DeviceBasicInfo&gt;&gt;)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;DeviceInfo&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getTrustedDeviceList

```TypeScript
getTrustedDeviceList(): Promise<Array<DeviceInfo>>
```

Obtains all trusted devices. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 11

**Substitutes:** [getAvailableDeviceList](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelist)()

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;DeviceInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getTrustedDeviceListSync

```TypeScript
getTrustedDeviceListSync(): Array<DeviceInfo>
```

Obtains all trusted devices synchronously.

**Since:** 7

**Deprecated since:** 11

**Substitutes:** [getAvailableDeviceListSync](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;DeviceInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [11600101](../errorcode-device-manager.md#11600101-service-invoking-exception) |

## getTrustedDeviceListSync

```TypeScript
getTrustedDeviceListSync(isRefresh: boolean): Array<DeviceInfo>
```

Enables the DSoftBus heartbeat mode to quickly bring offline trusted devices online and updates the list of online trusted devices.

**Since:** 10

**Deprecated since:** 11

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isRefresh | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;DeviceInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [11600101](../errorcode-device-manager.md#11600101-service-invoking-exception) |

## importCredential

```TypeScript
importCredential(credentialInfo: string, callback: AsyncCallback<{ resultInfo: string }>): void
```

Imports credential information.

**Since:** 10

**Deprecated since:** 11

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| credentialInfo | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;{ resultInfo: string }&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## off('uiStateChange')

```TypeScript
off(type: 'uiStateChange', callback?: Callback<{ param: string }>): void
```

Unsubscribes from UI status changes.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** off(type: 'replyResult', callback: Callback&lt;{ param: string; }&gt;)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'uiStateChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ param: string }&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## off('deviceStateChange')

```TypeScript
off(type: 'deviceStateChange', callback?: Callback<{ action: DeviceStateChangeAction, device: DeviceInfo }>): void
```

Unsubscribes from changes in the device state.

**Since:** 7

**Deprecated since:** 11

**Substitutes:** [off](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#offdevicestatechange)(type: 'deviceStateChange', callback?: Callback&lt;{ action: DeviceStateChange; device: DeviceBasicInfo; }&gt;)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'deviceStateChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ action: DeviceStateChangeAction, device: DeviceInfo }&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## off('deviceFound')

```TypeScript
off(type: 'deviceFound', callback?: Callback<{ subscribeId: number, device: DeviceInfo }>): void
```

Unsubscribes from device discovery events.

**Since:** 7

**Deprecated since:** 11

**Substitutes:** off(type: 'discoverSuccess', callback: Callback&lt;{ device: DeviceBasicInfo; }&gt;)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'deviceFound' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ subscribeId: number, device: DeviceInfo }&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## off('discoverFail')

```TypeScript
off(type: 'discoverFail', callback?: Callback<{ subscribeId: number, reason: number }>): void
```

Unsubscribes from device discovery failures.

**Since:** 7

**Deprecated since:** 11

**Substitutes:** off(type: 'discoverFailure', callback: Callback&lt;{ reason: int; }&gt;)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'discoverFail' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ subscribeId: number, reason: number }&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## off('publishSuccess')

```TypeScript
off(type: 'publishSuccess', callback?: Callback<{ publishId: number }>): void
```

Unsubscribes from device information publication success events.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'publishSuccess' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ publishId: number }&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## off('publishFail')

```TypeScript
off(type: 'publishFail', callback?: Callback<{ publishId: number, reason: number }>): void
```

Unsubscribes from device information publication failures.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'publishFail' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ publishId: number, reason: number }&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## off('serviceDie')

```TypeScript
off(type: 'serviceDie', callback?: () => void): void
```

Unsubscribes from dead events of the **DeviceManager** service.

**Since:** 7

**Deprecated since:** 11

**Substitutes:** [off](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#offservicedie)(type: 'serviceDie', callback?: Callback&lt;{}&gt;)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'serviceDie' | Yes |
| callback | () = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on('uiStateChange')

```TypeScript
on(type: 'uiStateChange', callback: Callback<{ param: string }>): void
```

Subscribes to UI status changes.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [on](arkts-distributedservice-distributeddevicemanager-devicemanager-i-sys.md#onreplyresult)(type: 'replyResult', callback: Callback&lt;{ param: string; }&gt;)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'uiStateChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ param: string }&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on('deviceStateChange')

```TypeScript
on(type: 'deviceStateChange', callback: Callback<{ action: DeviceStateChangeAction, device: DeviceInfo }>): void
```

Subscribes to changes in the device state.

**Since:** 7

**Deprecated since:** 11

**Substitutes:** [on](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#ondevicestatechange)(type: 'deviceStateChange', callback: Callback&lt;{ action: DeviceStateChange; device: DeviceBasicInfo; }&gt;)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'deviceStateChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ action: DeviceStateChangeAction, device: DeviceInfo }&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on('deviceFound')

```TypeScript
on(type: 'deviceFound', callback: Callback<{ subscribeId: number, device: DeviceInfo }>): void
```

Subscribes to device discovery events.

**Since:** 7

**Deprecated since:** 11

**Substitutes:** [on](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#ondiscoversuccess)(type: 'discoverSuccess', callback: Callback&lt;{ device: DeviceBasicInfo; }&gt;)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'deviceFound' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ subscribeId: number, device: DeviceInfo }&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on('discoverFail')

```TypeScript
on(type: 'discoverFail', callback: Callback<{ subscribeId: number, reason: number }>): void
```

Subscribes to device discovery failures.

**Since:** 7

**Deprecated since:** 11

**Substitutes:** [on](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#ondiscoverfailure)(type: 'discoverFailure', callback: Callback&lt;{ reason: int; }&gt;)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'discoverFail' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ subscribeId: number, reason: number }&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on('publishSuccess')

```TypeScript
on(type: 'publishSuccess', callback: Callback<{ publishId: number }>): void
```

Subscribes to device information publication success events.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'publishSuccess' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ publishId: number }&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on('publishFail')

```TypeScript
on(type: 'publishFail', callback: Callback<{ publishId: number, reason: number }>): void
```

Subscribes to device information publication failures.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'publishFail' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ publishId: number, reason: number }&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on('serviceDie')

```TypeScript
on(type: 'serviceDie', callback: () => void): void
```

Subscribes to dead events of the **DeviceManager** service.

**Since:** 7

**Deprecated since:** 11

**Substitutes:** [on](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#onservicedie)(type: 'serviceDie', callback?: Callback&lt;{}&gt;)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'serviceDie' | Yes |
| callback | () = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## publishDeviceDiscovery

```TypeScript
publishDeviceDiscovery(publishInfo: PublishInfo): void
```

Publishes device information for discovery purposes. The publish process lasts 2 minutes.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| publishInfo | [PublishInfo](arkts-distributedservice-devicemanager-publishinfo-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [11600105](../errorcode-device-manager.md#11600105-publish-unavailable) |
| [11600101](../errorcode-device-manager.md#11600101-service-invoking-exception) |

## release

```TypeScript
release(): void
```

Releases this **DeviceManager** instance when it is no longer used.

**Since:** 7

**Deprecated since:** 11

**Substitutes:** [releaseDeviceManager](arkts-distributedservice-distributeddevicemanager-releasedevicemanager-f.md)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [11600101](../errorcode-device-manager.md#11600101-service-invoking-exception) |

## requestCredentialRegisterInfo

```TypeScript
requestCredentialRegisterInfo(requestInfo: string, callback: AsyncCallback<{ registerInfo: string }>): void
```

Obtains the registration information of the credential.

**Since:** 10

**Deprecated since:** 11

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| requestInfo | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;{ registerInfo: string }&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setUserOperation

```TypeScript
setUserOperation(operateAction: number, params: string): void
```

Sets a user operation.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [replyUiAction](arkts-distributedservice-distributeddevicemanager-devicemanager-i-sys.md#replyuiaction)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| operateAction | number | Yes |
| params | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## startDeviceDiscovery

```TypeScript
startDeviceDiscovery(subscribeInfo: SubscribeInfo): void
```

Starts to discover peripheral devices. The discovery process lasts 2 minutes. A maximum of 99 devices can be discovered.

**Since:** 8

**Deprecated since:** 11

**Substitutes:** [startDiscovering](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#startdiscovering)(discoverParam: { [key: string]: Object; }, filterOptions?: { [key: string]: Object; })

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| subscribeInfo | [SubscribeInfo](arkts-distributedservice-devicemanager-subscribeinfo-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [11600104](../errorcode-device-manager.md#11600104-discovery-unavailable) |
| [11600101](../errorcode-device-manager.md#11600101-service-invoking-exception) |

## startDeviceDiscovery

```TypeScript
startDeviceDiscovery(subscribeInfo: SubscribeInfo, filterOptions?: string): void
```

Starts to discover peripheral devices. The discovery process lasts 2 minutes. A maximum of 99 devices can be discovered.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [startDiscovering](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#startdiscovering)(discoverParam: { [key: string]: Object; }, filterOptions?: { [key: string]: Object; })

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| subscribeInfo | [SubscribeInfo](arkts-distributedservice-devicemanager-subscribeinfo-i-sys.md) | Yes |
| [filterOptions](../../apis-audio-kit/arkts-apis/arkts-audio-audio-audioplaybackcaptureconfig-i.md) | string | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [11600104](../errorcode-device-manager.md#11600104-discovery-unavailable) |
| [11600101](../errorcode-device-manager.md#11600101-service-invoking-exception) |

## stopDeviceDiscovery

```TypeScript
stopDeviceDiscovery(subscribeId: number): void
```

Stops device discovery.

**Since:** 7

**Deprecated since:** 11

**Substitutes:** [stopDiscovering](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#stopdiscovering)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [subscribeId](arkts-distributedservice-devicemanager-subscribeinfo-i-sys.md) | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [11600101](../errorcode-device-manager.md#11600101-service-invoking-exception) |

## unAuthenticateDevice

```TypeScript
unAuthenticateDevice(deviceInfo: DeviceInfo): void
```

Deauthenticates a device.

**Since:** 8

**Deprecated since:** 11

**Substitutes:** [unbindTarget](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#unbindtarget)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceInfo | [DeviceInfo](../../apis-avsession-kit/arkts-apis/arkts-avsession-avsession-deviceinfo-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [11600101](../errorcode-device-manager.md#11600101-service-invoking-exception) |

## unPublishDeviceDiscovery

```TypeScript
unPublishDeviceDiscovery(publishId: number): void
```

Stops publishing device information.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [publishId](arkts-distributedservice-devicemanager-publishinfo-i-sys.md) | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [11600101](../errorcode-device-manager.md#11600101-service-invoking-exception) |

## verifyAuthInfo

```TypeScript
verifyAuthInfo(authInfo: AuthInfo, callback: AsyncCallback<{ deviceId: string, level: number }>): void
```

Verifies authentication information.

**Since:** 7

**Deprecated since:** 11

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| authInfo | [AuthInfo](arkts-distributedservice-devicemanager-authinfo-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;{ deviceId: string, level: number }&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
