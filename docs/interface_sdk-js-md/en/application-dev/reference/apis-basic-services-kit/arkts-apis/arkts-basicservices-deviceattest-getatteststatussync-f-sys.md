# getAttestStatusSync (System API)

## Modules to Import

```TypeScript
import { deviceAttest } from 'kits/@kit.BasicServicesKit';
```

## getAttestStatusSync

```TypeScript
function getAttestStatusSync(): AttestResultInfo
```

Obtains the AttestResultInfo object.

**Since:** 9

**System capability:** SystemCapability.XTS.DeviceAttest

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AttestResultInfo](arkts-basicservices-deviceattest-attestresultinfo-i-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [20000001](../errorcode-deviceAttest.md#20000001-system-service-abnormal) |
