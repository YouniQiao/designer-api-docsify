# CommonEventSubscribeInfo

用于表示公共事件订阅者的信息，支持配置订阅的公共事件类型、发布者权限、发布者设备ID、用户ID、订阅优先级等参数，适用于应用需要订阅系统公共事件或自定义公共事件并精细化控制事件来源的场景。

> **说明：**
> 
> 订阅自定义公共事件后，任意应用都可以向订阅者发送潜在的恶意公共事件。通过本模块的publisherPermission和publisherBundleName参数，可以限制公共事件发布者的范围。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface CommonEventSubscribeInfo--><!--Device-unnamed-export interface CommonEventSubscribeInfo-End-->

**System capability:** SystemCapability.Notification.CommonEvent

## events

```TypeScript
events: Array<string>
```

表示要订阅的公共事件列表。

**Type:** Array&lt;string&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscribeInfo-events: Array<string>--><!--Device-CommonEventSubscribeInfo-events: Array<string>-End-->

**System capability:** SystemCapability.Notification.CommonEvent

## priority

```TypeScript
priority?: int
```

表示订阅者的优先级，数值越大，订阅者优先级越高，越优先接收到有序公共事件。取值范围是-100到1000，超过上下限的优先级将被设置为对应的上下限值，默认优先级为0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscribeInfo-priority?: int--><!--Device-CommonEventSubscribeInfo-priority?: int-End-->

**System capability:** SystemCapability.Notification.CommonEvent

## publisherBundleName

```TypeScript
publisherBundleName?: string
```

表示要订阅的发布者的bundleName，用于限制订阅方只接收该bundleName的发布者发布的公共事件。不设置时，可接收所有应用发布的公共事件。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscribeInfo-publisherBundleName?: string--><!--Device-CommonEventSubscribeInfo-publisherBundleName?: string-End-->

**System capability:** SystemCapability.Notification.CommonEvent

## publisherDeviceId

```TypeScript
publisherDeviceId?: string
```

表示设备ID，用于限制订阅者只接收来自指定设备发布的公共事件。通过[@ohos.deviceInfo](arkts-deviceinfo.md)获取udid，作为发布者的设备ID。预留能力，暂不支持。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscribeInfo-publisherDeviceId?: string--><!--Device-CommonEventSubscribeInfo-publisherDeviceId?: string-End-->

**System capability:** SystemCapability.Notification.CommonEvent

## publisherPermission

```TypeScript
publisherPermission?: string
```

表示发布者的权限，取值为系统已定义的权限名。用于限制订阅方只接收具有该权限的发布方发布的公共事件。不设置时，可接收所有发布方发布的公共事件。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscribeInfo-publisherPermission?: string--><!--Device-CommonEventSubscribeInfo-publisherPermission?: string-End-->

**System capability:** SystemCapability.Notification.CommonEvent

## userId

```TypeScript
userId?: int
```

表示用户ID，用于限制订阅者只接收指定用户ID相关的公共事件。此参数是可选的，默认值为当前用户的ID。如果指定了此参数，则该值必须是系统中现有的用户ID。通过  
[getOsAccountLocalId](arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid)获取系统用户ID，作为发布者的用户ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscribeInfo-userId?: int--><!--Device-CommonEventSubscribeInfo-userId?: int-End-->

**System capability:** SystemCapability.Notification.CommonEvent

