# @ohos.enterprise.bluetoothManager

本模块提供设备蓝牙管理的能力，包括设置蓝牙开关状态、查询蓝牙信息，管理蓝牙设备可用名单、蓝牙设备禁用名单、蓝牙协议禁用名单等。通过本模块，企业可以统一管理设备蓝牙功能，实现对蓝牙设备连接的精细化管控，提升企业信息安全水平，适用于企业需 要对员工设备的蓝牙使用进行规范化管理的场景。 > **说明：** > > 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。 > > 全局通用限制类策略由restrictions统一提供，若要全局禁用蓝牙，请参考 > [@ohos.enterprise.restrictions（限制类策略）](arkts-enterprise-restrictions.md#ohosenterpriserestrictions)。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace bluetoothManager--><!--Device-unnamed-declare namespace bluetoothManager-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [addAllowedBluetoothDevices](arkts-mdm-bluetoothmanager-addallowedbluetoothdevices-f.md#addallowedbluetoothdevices) |
| [addDisallowedBluetoothDevices](arkts-mdm-bluetoothmanager-adddisallowedbluetoothdevices-f.md#adddisallowedbluetoothdevices) |
| [addDisallowedBluetoothProtocols](arkts-mdm-bluetoothmanager-adddisallowedbluetoothprotocols-f.md#adddisallowedbluetoothprotocols) |
| [addDisallowedBluetoothProtocols](arkts-mdm-bluetoothmanager-adddisallowedbluetoothprotocols-f.md#adddisallowedbluetoothprotocols) |
| [getAllowedBluetoothDevices](arkts-mdm-bluetoothmanager-getallowedbluetoothdevices-f.md#getallowedbluetoothdevices) |
| [getAllowedBluetoothDevices](arkts-mdm-bluetoothmanager-getallowedbluetoothdevices-f.md#getallowedbluetoothdevices) |
| [getBluetoothInfo](arkts-mdm-bluetoothmanager-getbluetoothinfo-f.md#getbluetoothinfo) |
| [getDisallowedBluetoothDevices](arkts-mdm-bluetoothmanager-getdisallowedbluetoothdevices-f.md#getdisallowedbluetoothdevices) |
| [getDisallowedBluetoothDevices](arkts-mdm-bluetoothmanager-getdisallowedbluetoothdevices-f.md#getdisallowedbluetoothdevices) |
| [getDisallowedBluetoothProtocols](arkts-mdm-bluetoothmanager-getdisallowedbluetoothprotocols-f.md#getdisallowedbluetoothprotocols) |
| [getDisallowedBluetoothProtocols](arkts-mdm-bluetoothmanager-getdisallowedbluetoothprotocols-f.md#getdisallowedbluetoothprotocols) |
| [removeAllowedBluetoothDevices](arkts-mdm-bluetoothmanager-removeallowedbluetoothdevices-f.md#removeallowedbluetoothdevices) |
| [removeDisallowedBluetoothDevices](arkts-mdm-bluetoothmanager-removedisallowedbluetoothdevices-f.md#removedisallowedbluetoothdevices) |
| [removeDisallowedBluetoothProtocols](arkts-mdm-bluetoothmanager-removedisallowedbluetoothprotocols-f.md#removedisallowedbluetoothprotocols) |
| [removeDisallowedBluetoothProtocols](arkts-mdm-bluetoothmanager-removedisallowedbluetoothprotocols-f.md#removedisallowedbluetoothprotocols) |
| [turnOffBluetooth](arkts-mdm-bluetoothmanager-turnoffbluetooth-f.md#turnoffbluetooth) |
| [turnOnBluetooth](arkts-mdm-bluetoothmanager-turnonbluetooth-f.md#turnonbluetooth) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [isBluetoothDisabled](arkts-mdm-bluetoothmanager-isbluetoothdisabled-f-sys.md#isbluetoothdisabled系统接口) |
| [setBluetoothDisabled](arkts-mdm-bluetoothmanager-setbluetoothdisabled-f-sys.md#setbluetoothdisabled系统接口) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [BluetoothInfo](arkts-mdm-bluetoothmanager-bluetoothinfo-i.md) |

### 枚举

| 名称 |
| --- |
| [Protocol](arkts-mdm-bluetoothmanager-protocol-e.md) |
| [TransferPolicy](arkts-mdm-bluetoothmanager-transferpolicy-e.md) |
