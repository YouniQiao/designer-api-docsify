# @ohos.enterprise.usbManager(USB管理)

本模块提供USB管理能力。

> **说明：**
> 
> 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。
> 
> 全局通用限制类策略由restrictions统一提供，若要全局禁用USB，请参考
> [@ohos.enterprise.restrictions（限制类策略）](arkts-enterprise-restrictions.md#restrictions)。

**起始版本：** 12

<!--Device-unnamed-declare namespace usbManager--><!--Device-unnamed-declare namespace usbManager-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 汇总

### 函数

| 名称 |
| --- |
| [addAllowedUsbDevices](arkts-mdm-usbmanager-addallowedusbdevices-f.md#addallowedusbdevices) |
| [addDisallowedPermissiveUsbDevices](arkts-mdm-usbmanager-adddisallowedpermissiveusbdevices-f.md#adddisallowedpermissiveusbdevices) |
| [addDisallowedUsbDevices](arkts-mdm-usbmanager-adddisallowedusbdevices-f.md#adddisallowedusbdevices) |
| [disableUsb](arkts-mdm-usbmanager-disableusb-f.md#disableusb) |
| [getAllowedUsbDevices](arkts-mdm-usbmanager-getallowedusbdevices-f.md#getallowedusbdevices) |
| [getAllowedUsbDevices](arkts-mdm-usbmanager-getallowedusbdevices-f.md#getallowedusbdevices-1) |
| [getDisallowedPermissiveUsbDevices](arkts-mdm-usbmanager-getdisallowedpermissiveusbdevices-f.md#getdisallowedpermissiveusbdevices) |
| [getDisallowedUsbDevices](arkts-mdm-usbmanager-getdisallowedusbdevices-f.md#getdisallowedusbdevices) |
| [getDisallowedUsbDevices](arkts-mdm-usbmanager-getdisallowedusbdevices-f.md#getdisallowedusbdevices-1) |
| [getUsbStorageDeviceAccessPolicy](arkts-mdm-usbmanager-getusbstoragedeviceaccesspolicy-f.md#getusbstoragedeviceaccesspolicy) |
| [getUsbStorageDeviceAccessPolicy](arkts-mdm-usbmanager-getusbstoragedeviceaccesspolicy-f.md#getusbstoragedeviceaccesspolicy-1) |
| [isUsbDisabled](arkts-mdm-usbmanager-isusbdisabled-f.md#isusbdisabled) |
| [removeAllowedUsbDevices](arkts-mdm-usbmanager-removeallowedusbdevices-f.md#removeallowedusbdevices) |
| [removeDisallowedPermissiveUsbDevices](arkts-mdm-usbmanager-removedisallowedpermissiveusbdevices-f.md#removedisallowedpermissiveusbdevices) |
| [removeDisallowedUsbDevices](arkts-mdm-usbmanager-removedisallowedusbdevices-f.md#removedisallowedusbdevices) |
| [setUsbPolicy](arkts-mdm-usbmanager-setusbpolicy-f.md#setusbpolicy) |
| [setUsbPolicy](arkts-mdm-usbmanager-setusbpolicy-f.md#setusbpolicy-1) |
| [setUsbStorageDeviceAccessPolicy](arkts-mdm-usbmanager-setusbstoragedeviceaccesspolicy-f.md#setusbstoragedeviceaccesspolicy) |

### 接口

| 名称 |
| --- |
| [PermissiveUsbDeviceType](arkts-mdm-usbmanager-permissiveusbdevicetype-i.md) |
| [UsbDeviceId](arkts-mdm-usbmanager-usbdeviceid-i.md) |
| [UsbDeviceType](arkts-mdm-usbmanager-usbdevicetype-i.md) |

### 枚举

| 名称 |
| --- |
| [Descriptor](arkts-mdm-usbmanager-descriptor-e.md) |
| [UsbPolicy](arkts-mdm-usbmanager-usbpolicy-e.md) |
