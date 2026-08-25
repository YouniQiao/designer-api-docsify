# @ohos.enterprise.bluetoothManager(蓝牙管理)

本模块提供设备蓝牙管理的能力，包括设置蓝牙开关状态、查询蓝牙信息，管理蓝牙设备可用名单、蓝牙设备禁用名单、蓝牙协议禁用名单等。通过本模块，企业可以统一管理设备蓝牙功能，实现对蓝牙设备连接的精细化管控，提升企业信息安全水平，适用于企业需 要对员工设备的蓝牙使用进行规范化管理的场景。

> **说明：**&gt;
> 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。&gt;
> 全局通用限制类策略由restrictions统一提供，若要全局禁用蓝牙，请参考
> [@ohos.enterprise.restrictions（限制类策略）](arkts-enterprise-restrictions.md)。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 导入模块

```TypeScript
import { bluetoothManager } from 'kits/@kit.MDMKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [addAllowedBluetoothDevices(蓝牙管理)](arkts-mdm-bluetoothmanager-addallowedbluetoothdevices-f.md) |
| [addDisallowedBluetoothDevices(蓝牙管理)](arkts-mdm-bluetoothmanager-adddisallowedbluetoothdevices-f.md) |
| [addDisallowedBluetoothProtocols(蓝牙管理)](arkts-mdm-bluetoothmanager-adddisallowedbluetoothprotocols-f.md) |
| [addDisallowedBluetoothProtocols(蓝牙管理)](arkts-mdm-bluetoothmanager-adddisallowedbluetoothprotocols-f.md) |
| [getAllowedBluetoothDevices(蓝牙管理)](arkts-mdm-bluetoothmanager-getallowedbluetoothdevices-f.md) |
| [getAllowedBluetoothDevices(蓝牙管理)](arkts-mdm-bluetoothmanager-getallowedbluetoothdevices-f.md) |
| [getBluetoothInfo(蓝牙管理)](arkts-mdm-bluetoothmanager-getbluetoothinfo-f.md) |
| [getDisallowedBluetoothDevices(蓝牙管理)](arkts-mdm-bluetoothmanager-getdisallowedbluetoothdevices-f.md) |
| [getDisallowedBluetoothDevices(蓝牙管理)](arkts-mdm-bluetoothmanager-getdisallowedbluetoothdevices-f.md) |
| [getDisallowedBluetoothProtocols(蓝牙管理)](arkts-mdm-bluetoothmanager-getdisallowedbluetoothprotocols-f.md) |
| [getDisallowedBluetoothProtocols(蓝牙管理)](arkts-mdm-bluetoothmanager-getdisallowedbluetoothprotocols-f.md) |
| [removeAllowedBluetoothDevices(蓝牙管理)](arkts-mdm-bluetoothmanager-removeallowedbluetoothdevices-f.md) |
| [removeDisallowedBluetoothDevices(蓝牙管理)](arkts-mdm-bluetoothmanager-removedisallowedbluetoothdevices-f.md) |
| [removeDisallowedBluetoothProtocols(蓝牙管理)](arkts-mdm-bluetoothmanager-removedisallowedbluetoothprotocols-f.md) |
| [removeDisallowedBluetoothProtocols(蓝牙管理)](arkts-mdm-bluetoothmanager-removedisallowedbluetoothprotocols-f.md) |
| [turnOffBluetooth(蓝牙管理)](arkts-mdm-bluetoothmanager-turnoffbluetooth-f.md) |
| [turnOnBluetooth(蓝牙管理)](arkts-mdm-bluetoothmanager-turnonbluetooth-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [isBluetoothDisabled(蓝牙管理)](arkts-mdm-bluetoothmanager-isbluetoothdisabled-f-sys.md) |
| [setBluetoothDisabled(蓝牙管理)](arkts-mdm-bluetoothmanager-setbluetoothdisabled-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [BluetoothInfo(蓝牙管理)](arkts-mdm-bluetoothmanager-bluetoothinfo-i.md) |

### 枚举

| 名称 |
| --- |
| [Protocol(蓝牙管理)](arkts-mdm-bluetoothmanager-protocol-e.md) |
| [TransferPolicy(蓝牙管理)](arkts-mdm-bluetoothmanager-transferpolicy-e.md) |
