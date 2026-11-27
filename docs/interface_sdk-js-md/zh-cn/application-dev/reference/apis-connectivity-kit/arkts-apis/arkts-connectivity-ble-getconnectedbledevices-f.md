# getConnectedBLEDevices

## 导入模块

```TypeScript
import { ble } from '@kit.ConnectivityKit';
```

## getConnectedBLEDevices

```TypeScript
function getConnectedBLEDevices(): Array<string>
```

获取和本机设备已连接GATT的BLE设备集合。

建议给server端使用，client端使用返回的设备地址集合为空。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ble-function getConnectedBLEDevices(): Array<string>--><!--Device-ble-function getConnectedBLEDevices(): Array<string>-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;string&gt; | 返回和本机设备已建立GATT连接的BLE设备地址集合。基于信息安全考虑，此处获取的设备地址为虚拟MAC地址。若和该设备地址配对成功后，该地址不会变更。若该设备重启蓝牙开关，重新获取到的虚拟地址会立即变更。若取消配对，蓝牙子系统会根据该地址的实际使用情况，决策后续变更时机；若其他应用正在使用该地址，则不会立刻变更。若要持久化保存该地址，可使用[access.addPersistentDeviceId](arkts-connectivity-access-addpersistentdeviceid-f.md)方法。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | Permission verification failed. The application does not have the permission required to call the API. |
| [801](../../errorcode-universal.md#801-api功能在部分设备不支持) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| [2900001](../errorcode-bluetoothManager.md#2900001-蓝牙服务停止) | Service stopped. |
| [2900003](../errorcode-bluetoothManager.md#2900003-蓝牙开关关闭) | Bluetooth disabled. |
| [2900099](../errorcode-bluetoothManager.md#2900099-操作失败) | Operation failed. |

**示例**

```TypeScript
try {
    let result: Array<string> = ble.getConnectedBLEDevices();
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```


## getConnectedBLEDevices

```TypeScript
function getConnectedBLEDevices(profile: BleProfile): Array<string>
```

根据指定的本机设备Profile协议类型，获取和本机设备已连接GATT的BLE设备集合。

若指定本机设备作为client端，则返回与本机设备连接的所有server端设备地址集合。若指定本机设备作为server端，则返回与本机设备连接的所有client端设备地址集合。若指定本机设备同时作为client端和server端，则返回与本机设备连接的所有client端和server端设备地址集合。

**起始版本：** 21

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ble-function getConnectedBLEDevices(profile: BleProfile): Array<string>--><!--Device-ble-function getConnectedBLEDevices(profile: BleProfile): Array<string>-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| profile | [BleProfile](arkts-connectivity-ble-bleprofile-e.md) | 是 | 当前设备的Profile协议类型，表明该设备在GATT链路中的通信角色。GATT_CLIENT表示指定本机设备为client端角色，与其建立GATT连接的所有对端设备为server端角色。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;string&gt; | 返回和本机设备已建立GATT连接的BLE设备地址集合。基于信息安全考虑，此处获取的设备地址为虚拟MAC地址。若和该设备地址配对成功后，该地址不会变更。取消配对该设备或蓝牙关闭后，若重新获取，该虚拟地址会变更。蓝牙子系统会根据该地址的实际使用情况决策后续变更时机；若其他应用正在使用该地址，则不会立刻变更。若要持久化保存该地址，可使用[access.addPersistentDeviceId](arkts-connectivity-access-addpersistentdeviceid-f.md)方法 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | Permission verification failed. The application does not have the permission required to call the API. |
| [801](../../errorcode-universal.md#801-api功能在部分设备不支持) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| [2900001](../errorcode-bluetoothManager.md#2900001-蓝牙服务停止) | Service stopped. |
| [2900003](../errorcode-bluetoothManager.md#2900003-蓝牙开关关闭) | Bluetooth disabled. |
| [2900099](../errorcode-bluetoothManager.md#2900099-操作失败) | Operation failed. |

**示例**

```TypeScript
try {
    let result: Array<string> = ble.getConnectedBLEDevices(ble.BleProfile.GATT_CLIENT);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```
