# SerialPort

Serial port object, which provides information and communication capabilities of the serial port device.

**Since:** 26.0.0

**System capability:** SystemCapability.BusManager.Serial

## Modules to Import

```TypeScript
import { serial } from 'kits/@kit.BasicServicesKit';
```

## close

```TypeScript
close(): Promise<void>
```

Closes the serial port device. This API returns the result asynchronously through a promise.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) |

## drain

```TypeScript
drain(): Promise<void>
```

Waits until all write requests are complete. This API returns the result asynchronously through a promise.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) |
| [35700003](../errorcode-busmanager-serial.md#35700003-virtual-serial-port-disconnected) |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) |

## flush

```TypeScript
flush(): Promise<void>
```

Flushes the serial port buffer. This API returns the result asynchronously through a promise.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) |
| [35700003](../errorcode-busmanager-serial.md#35700003-virtual-serial-port-disconnected) |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) |

## getCts

```TypeScript
getCts(): Promise<boolean>
```

Obtains the CTS signal status. This API returns the result asynchronously through a promise.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) |
| [35700003](../errorcode-busmanager-serial.md#35700003-virtual-serial-port-disconnected) |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) |

## getDsr

```TypeScript
getDsr(): Promise<boolean>
```

Obtains the DSR signal status. This API returns the result asynchronously through a promise.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) |
| [35700003](../errorcode-busmanager-serial.md#35700003-virtual-serial-port-disconnected) |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) |

## offDataRead

```TypeScript
offDataRead(callback?: Callback<Uint8Array>): void
```

Cancels listening for data receiving events on the serial port.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Uint8Array&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) |

## offDisconnect

```TypeScript
offDisconnect(callback?: Callback<void>): void
```

This command is used to cancel the monitoring of the USB virtual serial port disconnection event.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) |

## onDataRead

```TypeScript
onDataRead(callback: Callback<Uint8Array>): void
```

Listens for data received by the serial port. This API uses an asynchronous callback to return the result. When [close](#close) is called, all callbacks are cleared.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Uint8Array&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) |
| [35700003](../errorcode-busmanager-serial.md#35700003-virtual-serial-port-disconnected) |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) |

## onDisconnect

```TypeScript
onDisconnect(callback: Callback<void>): void
```

This interface is used to listen to the disconnection event of the USB virtual serial port. Use Callback asynchronous callback. When the [close](#close) interface is invoked, all callbacks are cleared.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) |

## open

```TypeScript
open(config?: SerialConfigs): Promise<void>
```

Enables the port. This API returns the result asynchronously through a promise.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [SerialConfigs](arkts-basicservices-serial-serialconfigs-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) |
| [35700002](../errorcode-busmanager-serial.md#35700002-parameter-error) |
| [35700003](../errorcode-busmanager-serial.md#35700003-virtual-serial-port-disconnected) |
| [35700004](../errorcode-busmanager-serial.md#35700004-port-in-use) |
| [35700007](../errorcode-busmanager-serial.md#35700007-user-authorization-rejected) |

## sendBrk

```TypeScript
sendBrk(): Promise<void>
```

Sends a BRK signal. This API returns the result asynchronously through a promise.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) |
| [35700003](../errorcode-busmanager-serial.md#35700003-virtual-serial-port-disconnected) |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) |

## setDtr

```TypeScript
setDtr(enable: boolean): Promise<void>
```

Sets the DTR signal status. Use Promise asynchronous callbacks.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) |
| [35700003](../errorcode-busmanager-serial.md#35700003-virtual-serial-port-disconnected) |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) |

## setRts

```TypeScript
setRts(enable: boolean): Promise<void>
```

Sets the RTS signal. This API returns the result asynchronously through a promise.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) |
| [35700003](../errorcode-busmanager-serial.md#35700003-virtual-serial-port-disconnected) |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) |

## write

```TypeScript
write(data: Uint8Array, timeout?: number): Promise<number>
```

Sends data. This API returns the result asynchronously through a promise.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | Uint8Array | Yes |
| timeout | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) |
| [35700002](../errorcode-busmanager-serial.md#35700002-parameter-error) |
| [35700003](../errorcode-busmanager-serial.md#35700003-virtual-serial-port-disconnected) |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) |
| [35700006](../errorcode-busmanager-serial.md#35700006-transmission-timeout) |

## portInfo

```TypeScript
readonly portInfo: SerialPortInfo
```

Serial port information.

**Type:** [SerialPortInfo](arkts-basicservices-serial-serialportinfo-i.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial
