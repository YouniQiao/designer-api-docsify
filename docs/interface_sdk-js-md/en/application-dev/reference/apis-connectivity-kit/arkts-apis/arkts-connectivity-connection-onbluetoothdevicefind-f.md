# onBluetoothDeviceFind

## onBluetoothDeviceFind

```TypeScript
function onBluetoothDeviceFind(callback: Callback<Array<string>>): void
```

Subscribe the event reported when a remote Bluetooth device is discovered.On API 26.0.0 and above, if the application has ohos.permission.GET\_BLUETOOTH\_PEERS\_MAC,the type of the peer device address is real.Otherwise, the type of the peer device address is virtual.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** 
- API version 26.0.0+: ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC)
- API version 23 - 24: ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function onBluetoothDeviceFind(callback: Callback<Array<string>>): void--><!--Device-connection-function onBluetoothDeviceFind(callback: Callback<Array<string>>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;string&gt;&gt; | Yes | Callback used to listen for the discovering event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| 2900099 | Operation failed. |

