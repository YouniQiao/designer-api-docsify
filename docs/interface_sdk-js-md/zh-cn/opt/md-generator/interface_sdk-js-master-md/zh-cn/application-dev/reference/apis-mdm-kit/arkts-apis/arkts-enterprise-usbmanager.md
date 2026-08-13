# @ohos.enterprise.usbManager

本模块提供USB管理能力。 > **说明：** > > 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。 > > 全局通用限制类策略由restrictions统一提供，若要全局禁用USB，请参考 > [@ohos.enterprise.restrictions（限制类策略）](arkts-enterprise-restrictions.md#@ohos.enterprise.restrictions)。

**起始版本：** 10

**废弃版本：** -1

<!--Device-unnamed-declare namespace usbManager--><!--Device-unnamed-declare namespace usbManager-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

## 汇总

### 函数

| 名称 |
| --- |
| [addAllowedUsbDevices](arkts-mdm-usbmanager-addallowedusbdevices-f.md#addAllowedUsbDevices) |
| [addDisallowedPermissiveUsbDevices](arkts-mdm-usbmanager-adddisallowedpermissiveusbdevices-f.md#addDisallowedPermissiveUsbDevices) |
| [addDisallowedUsbDevices](arkts-mdm-usbmanager-adddisallowedusbdevices-f.md#addDisallowedUsbDevices) |
| [getAllowedUsbDevices](arkts-mdm-usbmanager-getallowedusbdevices-f.md#getAllowedUsbDevices) |
| [getAllowedUsbDevices](arkts-mdm-usbmanager-getallowedusbdevices-f.md#getAllowedUsbDevices) |
| [getDisallowedPermissiveUsbDevices](arkts-mdm-usbmanager-getdisallowedpermissiveusbdevices-f.md#getDisallowedPermissiveUsbDevices) |
| [getDisallowedUsbDevices](arkts-mdm-usbmanager-getdisallowedusbdevices-f.md#getDisallowedUsbDevices) |
| [getDisallowedUsbDevices](arkts-mdm-usbmanager-getdisallowedusbdevices-f.md#getDisallowedUsbDevices) |
| [getUsbStorageDeviceAccessPolicy](arkts-mdm-usbmanager-getusbstoragedeviceaccesspolicy-f.md#getUsbStorageDeviceAccessPolicy) |
| [getUsbStorageDeviceAccessPolicy](arkts-mdm-usbmanager-getusbstoragedeviceaccesspolicy-f.md#getUsbStorageDeviceAccessPolicy) |
| [removeAllowedUsbDevices](arkts-mdm-usbmanager-removeallowedusbdevices-f.md#removeAllowedUsbDevices) |
| [removeDisallowedPermissiveUsbDevices](arkts-mdm-usbmanager-removedisallowedpermissiveusbdevices-f.md#removeDisallowedPermissiveUsbDevices) |
| [removeDisallowedUsbDevices](arkts-mdm-usbmanager-removedisallowedusbdevices-f.md#removeDisallowedUsbDevices) |
| [setUsbStorageDeviceAccessPolicy](arkts-mdm-usbmanager-setusbstoragedeviceaccesspolicy-f.md#setUsbStorageDeviceAccessPolicy) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [disableUsb](arkts-mdm-usbmanager-disableusb-f-sys.md#disableUsb（系统接口）) |
| [isUsbDisabled](arkts-mdm-usbmanager-isusbdisabled-f-sys.md#isUsbDisabled（系统接口）) |
| [setUsbPolicy](arkts-mdm-usbmanager-setusbpolicy-f-sys.md#setUsbPolicy（系统接口）) |
| [setUsbPolicy](arkts-mdm-usbmanager-setusbpolicy-f-sys.md#setUsbPolicy（系统接口）) |
<!--DelEnd-->

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
