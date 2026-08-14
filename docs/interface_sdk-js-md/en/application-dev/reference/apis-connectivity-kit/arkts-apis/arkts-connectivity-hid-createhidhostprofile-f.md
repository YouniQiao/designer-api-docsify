# createHidHostProfile

## Modules to Import

```TypeScript
import { hid } from 'hid';
```

## createHidHostProfile

```TypeScript
function createHidHostProfile(): HidHostProfile
```

create the instance of hid profile.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-hid-function createHidHostProfile(): HidHostProfile--><!--Device-hid-function createHidHostProfile(): HidHostProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| HidHostProfile | Returns the instance of hid profile. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

## Examples

```TypeScript
try {
    let hidHostProfile = hid.createHidHostProfile();
    console.info('hidHost success');
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

