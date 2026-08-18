# startPairOutOfBand (System API)

## Modules to Import

```TypeScript
```

## startPairOutOfBand

```TypeScript
function startPairOutOfBand(deviceId: string, transport: BluetoothTransport, p192Data?: OobData,
    p256Data?: OobData): Promise<void>
```

Starts pairing with the specific remote Bluetooth device using the Out Of Band mechanism. This function is asynchronous, and the pairing status is obtained by listening to the bondStateChange event. If both p192Data and p256Data are not used, the function call will fail. If both p192Data and p256Data are used simultaneously, p256Data takes effect.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function startPairOutOfBand(deviceId: string, transport: BluetoothTransport, p192Data?: OobData,    p256Data?: OobData): Promise<void>--><!--Device-connection-function startPairOutOfBand(deviceId: string, transport: BluetoothTransport, p192Data?: OobData,    p256Data?: OobData): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| [transport](arkts-connectivity-ble-gattsetting-i.md) | [BluetoothTransport](arkts-connectivity-ble-bluetoothtransport-t.md) | Yes |
| p192Data | [OobData](arkts-connectivity-connection-oobdata-i-sys.md) | No |
| p256Data | [OobData](arkts-connectivity-connection-oobdata-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 2900003 |
| 2900099 |
