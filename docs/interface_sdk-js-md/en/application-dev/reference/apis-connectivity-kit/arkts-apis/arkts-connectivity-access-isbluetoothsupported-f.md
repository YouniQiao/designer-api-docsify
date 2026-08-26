# isBluetoothSupported

## Modules to Import

```TypeScript
```

## isBluetoothSupported

```TypeScript
function isBluetoothSupported(): boolean
```

Check whether Bluetooth is available.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 2900099 | Operation failed. |

**Examples**

```TypeScript
try {
    let isSupported: boolean = access.isBluetoothSupported();
    console.info("isSupported: " + isSupported);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```
