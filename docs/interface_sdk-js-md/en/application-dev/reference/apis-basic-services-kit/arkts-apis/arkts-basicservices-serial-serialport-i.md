# SerialPort

Serial port object, which provides information and communication capabilities of the serial port device.

**Since:** 26.0.0

**System capability:** SystemCapability.BusManager.Serial

## Modules to Import

```TypeScript
import { serial } from '@kit.BasicServicesKit';
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

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) | Service error. |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) | Port not open. |

**Examples**

```TypeScript
// Import BusinessError from @kit.BasicServicesKit.
// port is a serial port object, which needs to be obtained through serial.getSerialPortList().
// Close the serial port device.
port.close().then(() => {
  console.info('close success');
}).catch((error: BusinessError) => {
  console.error(`Failed to close serial port. Code: ${error.code}, message: ${error.message}`);
});
```

## drain

```TypeScript
drain(): Promise<void>
```

Waits until all write requests are complete. This API returns the result asynchronously through a promise.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) | Service error. |
| [35700003](../errorcode-busmanager-serial.md#35700003-virtual-serial-port-disconnected) | Virtual serial port disconnected. |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) | Port not open. |

**Examples**

```TypeScript
// Import BusinessError from @kit.BasicServicesKit.
// port is a serial port object, which needs to be obtained through serial.getSerialPortList().
// Wait until all write requests are complete.
port.drain().then(() => {
  console.info('drain success');
}).catch((error: BusinessError) => {
  console.error(`Failed to drain serial port. Code: ${error.code}, message: ${error.message}`);
});
```

## flush

```TypeScript
flush(): Promise<void>
```

Flushes the serial port buffer. This API returns the result asynchronously through a promise.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) | Service error. |
| [35700003](../errorcode-busmanager-serial.md#35700003-virtual-serial-port-disconnected) | Virtual serial port disconnected. |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) | Port not open. |

**Examples**

```TypeScript
// Import BusinessError from @kit.BasicServicesKit.
// port is a serial port object, which needs to be obtained through serial.getSerialPortList().
// Flush the serial port buffer.
port.flush().then(() => {
  console.info('flush success');
}).catch((error: BusinessError) => {
  console.error(`Failed to flush serial port. Code: ${error.code}, message: ${error.message}`);
});
```

## getCts

```TypeScript
getCts(): Promise<boolean>
```

Obtains the CTS signal status. This API returns the result asynchronously through a promise.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the CTS signal status, indicating whether data can be sent. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) | Service error. |
| [35700003](../errorcode-busmanager-serial.md#35700003-virtual-serial-port-disconnected) | Virtual serial port disconnected. |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) | Port not open. |

**Examples**

```TypeScript
// Import BusinessError from @kit.BasicServicesKit.
// port is a serial port object, which needs to be obtained through serial.getSerialPortList().
// Obtain the CTS signal status.
port.getCts().then((cts: boolean) => {
  console.info('getCts success, cts: ' + cts);
}).catch((error: BusinessError) => {
  console.error(`Failed to get CTS. Code: ${error.code}, message: ${error.message}`);
});
```

## getDsr

```TypeScript
getDsr(): Promise<boolean>
```

Obtains the DSR signal status. This API returns the result asynchronously through a promise.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** indicates the remote end is ready, and **false** indicates the remote end is not ready. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) | Service error. |
| [35700003](../errorcode-busmanager-serial.md#35700003-virtual-serial-port-disconnected) | Virtual serial port disconnected. |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) | Port not open. |

**Examples**

```TypeScript
// Import BusinessError from @kit.BasicServicesKit.
// port is a serial port object, which needs to be obtained through serial.getSerialPortList().
// Obtain the DSR signal status.
port.getDsr().then((dsr: boolean) => {
  console.info('getDsr success, dsr: ' + dsr);
}).catch((error: BusinessError) => {
  console.error(`Failed to get DSR. Code: ${error.code}, message: ${error.message}`);
});
```

## offDataRead

```TypeScript
offDataRead(callback?: Callback<Uint8Array>): void
```

Cancels listening for data receiving events on the serial port.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Uint8Array&gt; | No | Callback used to return the data received by the serial port. Default value: Clear all listeners for data receiving events on the serial port. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) | Service error. |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) | Port not open. |

**Examples**

```TypeScript
// port is a serial port object, which needs to be obtained through serial.getSerialPortList().
// Cancel listening for data receiving events on the serial port.
port.offDataRead();

// Cancel the specified listener callback.
let callback = (data: Uint8Array) => {
  console.info(`received data length: ${data.length}`);
};
port.offDataRead(callback);
```

## offDisconnect

```TypeScript
offDisconnect(callback?: Callback<void>): void
```

This command is used to cancel the monitoring of the USB virtual serial port disconnection event.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | Callback of the USB virtual serial port disconnection event. Default value: Clears all callbacks for USB virtual serial port disconnection events. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) | Service error. |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) | Port not open. |

**Examples**

```TypeScript
// port is a serial port object, which needs to be obtained through serial.getSerialPortList().
// Unsubscribe from serial port disconnection events.
port.offDisconnect();

// Cancel the specified listener callback.
let disconnectedCallback = () => {
  console.info('serial port disconnected');
};
port.offDisconnect(disconnectedCallback);
```

## onDataRead

```TypeScript
onDataRead(callback: Callback<Uint8Array>): void
```

Listens for data received by the serial port. This API uses an asynchronous callback to return the result. When [close](#close) is called, all callbacks are cleared.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Uint8Array&gt; | Yes | Callback used to return the data received by the serial port. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) | Service error. |
| [35700003](../errorcode-busmanager-serial.md#35700003-virtual-serial-port-disconnected) | Virtual serial port disconnected. |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) | Port not open. |

**Examples**

```TypeScript
// port is a serial port object, which needs to be obtained through serial.getSerialPortList().
// Listen for data receiving events on the serial port.
port.onDataRead((data: Uint8Array) => {
  console.info(`onDataRead, length: ${data.length}`);
});
```

## onDisconnect

```TypeScript
onDisconnect(callback: Callback<void>): void
```

This interface is used to listen to the disconnection event of the USB virtual serial port. Use Callback asynchronous callback. When the [close](#close) interface is invoked, all callbacks are cleared.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Callback of the USB virtual serial port disconnection event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) | Service error. |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) | Port not open. |

**Examples**

```TypeScript
// port is a serial port object, which needs to be obtained through serial.getSerialPortList().
// Subscribe to serial port disconnection events.
port.onDisconnect(() => {
  console.info('serial port disconnected');
});
```

## open

```TypeScript
open(config?: SerialConfigs): Promise<void>
```

Enables the port. This API returns the result asynchronously through a promise.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [SerialConfigs](arkts-basicservices-serial-serialconfigs-i.md) | No | Serial port communication parameter. Default value: Refer to the default value of SerialConfigs. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) | Service error. |
| [35700002](../errorcode-busmanager-serial.md#35700002-parameter-error) | Invalid parameter. |
| [35700003](../errorcode-busmanager-serial.md#35700003-virtual-serial-port-disconnected) | Virtual serial port disconnected. |
| [35700004](../errorcode-busmanager-serial.md#35700004-port-in-use) | Port already in use. |
| [35700007](../errorcode-busmanager-serial.md#35700007-user-authorization-rejected) | User authorization required. |

**Examples**

```TypeScript
// Import BusinessError from @kit.BasicServicesKit.
// Obtain the serial port list and open the first serial port.
serial.getSerialPortList().then(async (portList: serial.SerialPort[]) => {
  if (portList.length === 0) {
    console.error('portList is empty');
    return;
  }
  let port: serial.SerialPort = portList[0];
  let config: serial.SerialConfigs = {
    baudRate: 115200,
    dataBits: serial.DataBits.EIGHT,
    stopBits: serial.StopBits.ONE,
    parity: serial.Parity.NONE
  };
  await port.open(config);
  console.info('open success');
  // Call port.close() to release resources after the serial port is used.
  await port.close();
}).catch((error: BusinessError) => {
  console.error(`Failed to open serial port. Code: ${error.code}, message: ${error.message}`);
});
```

## sendBrk

```TypeScript
sendBrk(): Promise<void>
```

Sends a BRK signal. This API returns the result asynchronously through a promise.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) | Service error. |
| [35700003](../errorcode-busmanager-serial.md#35700003-virtual-serial-port-disconnected) | Virtual serial port disconnected. |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) | Port not open. |

**Examples**

```TypeScript
// Import BusinessError from @kit.BasicServicesKit.
// port is a serial port object, which needs to be obtained through serial.getSerialPortList().
// Send a BRK signal.
port.sendBrk().then(() => {
  console.info('sendBrk success');
}).catch((error: BusinessError) => {
  console.error(`Failed to send BRK. Code: ${error.code}, message: ${error.message}`);
});
```

## setDtr

```TypeScript
setDtr(enable: boolean): Promise<void>
```

Sets the DTR signal status. Use Promise asynchronous callbacks.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | DTR signal status, indicating whether the local end is ready. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) | Service error. |
| [35700003](../errorcode-busmanager-serial.md#35700003-virtual-serial-port-disconnected) | Virtual serial port disconnected. |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) | Port not open. |

**Examples**

```TypeScript
// Import BusinessError from @kit.BasicServicesKit.
// port is a serial port object, which needs to be obtained through serial.getSerialPortList().
// Set the DTR signal.
port.setDtr(true).then(() => {
  console.info('setDtr success');
}).catch((error: BusinessError) => {
  console.error(`Failed to set DTR. Code: ${error.code}, message: ${error.message}`);
});
```

## setRts

```TypeScript
setRts(enable: boolean): Promise<void>
```

Sets the RTS signal. This API returns the result asynchronously through a promise.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | RTS signal status, indicating whether to request sending data. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) | Service error. |
| [35700003](../errorcode-busmanager-serial.md#35700003-virtual-serial-port-disconnected) | Virtual serial port disconnected. |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) | Port not open. |

**Examples**

```TypeScript
// Import BusinessError from @kit.BasicServicesKit.
// port is a serial port object, which needs to be obtained through serial.getSerialPortList().
// Set the RTS signal.
port.setRts(true).then(() => {
  console.info('setRts success');
}).catch((error: BusinessError) => {
  console.error(`Failed to set RTS. Code: ${error.code}, message: ${error.message}`);
});
```

## write

```TypeScript
write(data: Uint8Array, timeout?: number): Promise<number>
```

Sends data. This API returns the result asynchronously through a promise.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | Uint8Array | Yes | Data to be sent. Length range: (0, 4096] |
| timeout | number | No | Timeout interval. Length range: [0, 300000]. The value must be an integer, in milliseconds. The default value is 0, indicating that when data cannot be written to the port, the API does not wait and directly returns 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the length of the data written. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) | Service error. |
| [35700002](../errorcode-busmanager-serial.md#35700002-parameter-error) | Invalid parameter. |
| [35700003](../errorcode-busmanager-serial.md#35700003-virtual-serial-port-disconnected) | Virtual serial port disconnected. |
| [35700005](../errorcode-busmanager-serial.md#35700005-port-not-opened) | Port not open. |
| [35700006](../errorcode-busmanager-serial.md#35700006-transmission-timeout) | Transmission timeout. |

**Examples**

```TypeScript
// Import buffer from @kit.ArkTS.
// Import BusinessError from @kit.BasicServicesKit.
// port is a serial port object, which needs to be obtained through serial.getSerialPortList().
// Write data to a serial port device.
let writeData: Uint8Array = new Uint8Array(buffer.from('Hello World', 'utf-8').buffer);
port.write(writeData, 2000).then((size: number) => {
  console.info('write success, size: ' + size);
}).catch((error: BusinessError) => {
  console.error(`Failed to write to serial port. Code: ${error.code}, message: ${error.message}`);
});
```

## portInfo

```TypeScript
readonly portInfo: SerialPortInfo
```

Serial port information.

**Type:** [SerialPortInfo](arkts-basicservices-serial-serialportinfo-i.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial
