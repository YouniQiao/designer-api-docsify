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

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-deviceAttest-function getAttestStatusSync(): AttestResultInfo--><!--Device-deviceAttest-function getAttestStatusSync(): AttestResultInfo-End-->

**System capability:** SystemCapability.XTS.DeviceAttest

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [AttestResultInfo](arkts-basicservices-deviceattest-attestresultinfo-i-sys.md) | Obtains the AttestResultInfo object synchronously. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 20000001 | System service exception, please try again or reboot your device. |
| 401 | Input parameters wrong, the number of parameters is incorrect,or the type of parameters is incorrect. |
| 202 | This api is system api, Please use the system application to call this api. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let value: deviceAttest.AttestResultInfo = deviceAttest.getAttestStatusSync();
    console.info("auth:" + value.authResult + " software:" + value.softwareResult + " ticket:" + value.ticket);
    console.info("versionIdResult:" + value.softwareResultDetail[0],
    " patchLevelResult:" + value.softwareResultDetail[1],
    " rootHashResult:" + value.softwareResultDetail[2],
    " PCIDResult:" + value.softwareResultDetail[3],
    " reserved:" + value.softwareResultDetail[4]);
} catch (error) {
    let code: number = (error as BusinessError).code;
    let message: string = (error as BusinessError).message;
    console.error("error code:" + code + " message:" + message);
}
```

