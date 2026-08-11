# @ohos.distributedHardware.deviceManager

The APIs of this module are deprecated. You are advised to use  
[@ohos.distributedDeviceManager](arkts-distributeddevicemanager.md).The **deviceManager** module provides APIs for distributed device management.System applications can call the APIs to do the following:

- Subscribe to or unsubscribe from device state changes.  
- Discover devices nearby.  
- Authenticate or deauthenticate a device.  
- Query the trusted device list.  
- Query local device information, including the device name, type, and ID.  
- Publishes device information for discovery purposes.

**Since:** 7

**Deprecated since:** 11

**Substitutes:** [@ohos.distributedDeviceManager:distributedDeviceManager](arkts-distributeddevicemanager.md)

<!--Device-unnamed-declare namespace deviceManager--><!--Device-unnamed-declare namespace deviceManager-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

## Modules to Import

```TypeScript
import { deviceManager } from 'kits/@kit.DistributedServiceKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createDeviceManager](arkts-distributedservice-devicemanager-createdevicemanager-f-sys.md#createdevicemanager) |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AuthInfo](arkts-distributedservice-devicemanager-authinfo-i-sys.md) |
| [AuthParam](arkts-distributedservice-devicemanager-authparam-i-sys.md) |
| [DeviceInfo](arkts-distributedservice-devicemanager-deviceinfo-i-sys.md) |
| [DeviceManager](arkts-distributedservice-devicemanager-devicemanager-i-sys.md) |
| [PublishInfo](arkts-distributedservice-devicemanager-publishinfo-i-sys.md) |
| [SubscribeInfo](arkts-distributedservice-devicemanager-subscribeinfo-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AuthForm](arkts-distributedservice-devicemanager-authform-e-sys.md) |
| [DeviceStateChangeAction](arkts-distributedservice-devicemanager-devicestatechangeaction-e-sys.md) |
| [DeviceType](arkts-distributedservice-devicemanager-devicetype-e-sys.md) |
| [DiscoverMode](arkts-distributedservice-devicemanager-discovermode-e-sys.md) |
| [ExchangeFreq](arkts-distributedservice-devicemanager-exchangefreq-e-sys.md) |
| [ExchangeMedium](arkts-distributedservice-devicemanager-exchangemedium-e-sys.md) |
| [SubscribeCap](arkts-distributedservice-devicemanager-subscribecap-e-sys.md) |
<!--DelEnd-->
