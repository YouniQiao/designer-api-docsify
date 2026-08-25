# @ohos.enterprise.usbManager(USB管理)

本模块提供USB管理能力。

> **说明：**&gt;
> 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。&gt;
> 全局通用限制类策略由restrictions统一提供，若要全局禁用USB，请参考
> [@ohos.enterprise.restrictions（限制类策略）](arkts-enterprise-restrictions.md)。

**起始版本：** 12

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 导入模块

```TypeScript
import { usbManager } from 'kits/@kit.MDMKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [addAllowedUsbDevices(USB管理)](arkts-mdm-usbmanager-addallowedusbdevices-f.md) |
| [addDisallowedPermissiveUsbDevices(USB管理)](arkts-mdm-usbmanager-adddisallowedpermissiveusbdevices-f.md) |
| [addDisallowedUsbDevices(USB管理)](arkts-mdm-usbmanager-adddisallowedusbdevices-f.md) |
| [getAllowedUsbDevices(USB管理)](arkts-mdm-usbmanager-getallowedusbdevices-f.md) |
| [getAllowedUsbDevices(USB管理)](arkts-mdm-usbmanager-getallowedusbdevices-f.md) |
| [getDisallowedPermissiveUsbDevices(USB管理)](arkts-mdm-usbmanager-getdisallowedpermissiveusbdevices-f.md) |
| [getDisallowedUsbDevices(USB管理)](arkts-mdm-usbmanager-getdisallowedusbdevices-f.md) |
| [getDisallowedUsbDevices(USB管理)](arkts-mdm-usbmanager-getdisallowedusbdevices-f.md) |
| [getUsbStorageDeviceAccessPolicy(USB管理)](arkts-mdm-usbmanager-getusbstoragedeviceaccesspolicy-f.md) |
| [getUsbStorageDeviceAccessPolicy(USB管理)](arkts-mdm-usbmanager-getusbstoragedeviceaccesspolicy-f.md) |
| [removeAllowedUsbDevices(USB管理)](arkts-mdm-usbmanager-removeallowedusbdevices-f.md) |
| [removeDisallowedPermissiveUsbDevices(USB管理)](arkts-mdm-usbmanager-removedisallowedpermissiveusbdevices-f.md) |
| [removeDisallowedUsbDevices(USB管理)](arkts-mdm-usbmanager-removedisallowedusbdevices-f.md) |
| [setUsbStorageDeviceAccessPolicy(USB管理)](arkts-mdm-usbmanager-setusbstoragedeviceaccesspolicy-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [disableUsb(USB管理)](arkts-mdm-usbmanager-disableusb-f-sys.md) |
| [isUsbDisabled(USB管理)](arkts-mdm-usbmanager-isusbdisabled-f-sys.md) |
| [setUsbPolicy(USB管理)](arkts-mdm-usbmanager-setusbpolicy-f-sys.md) |
| [setUsbPolicy(USB管理)](arkts-mdm-usbmanager-setusbpolicy-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [PermissiveUsbDeviceType(USB管理)](arkts-mdm-usbmanager-permissiveusbdevicetype-i.md) |
| [UsbDeviceId(USB管理)](arkts-mdm-usbmanager-usbdeviceid-i.md) |
| [UsbDeviceType(USB管理)](arkts-mdm-usbmanager-usbdevicetype-i.md) |

### 枚举

| 名称 |
| --- |
| [Descriptor(USB管理)](arkts-mdm-usbmanager-descriptor-e.md) |
| [UsbPolicy(USB管理)](arkts-mdm-usbmanager-usbpolicy-e.md) |
