# getAttestStatus (System API)

## Modules to Import

```TypeScript
import { deviceAttest } from '@kit.BasicServicesKit';
```

## getAttestStatus

```TypeScript
function getAttestStatus(callback: AsyncCallback<AttestResultInfo>): void
```

Obtains the AttestResultInfo object.

**Since:** 9

<!--Device-deviceAttest-function getAttestStatus(callback: AsyncCallback<AttestResultInfo>): void--><!--Device-deviceAttest-function getAttestStatus(callback: AsyncCallback<AttestResultInfo>): void-End-->

**System capability:** SystemCapability.XTS.DeviceAttest

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[AttestResultInfo](arkts-basicservices-deviceattest-attestresultinfo-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [20000001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-deviceAttest.md#20000001-system-service-abnormal) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    deviceAttest.getAttestStatus((error: BusinessError, value: deviceAttest.AttestResultInfo) => {
    if (typeof error != 'undefined') {
        console.error("error code:" + error.code + " message:" + error.message);
    } else {
        console.info("auth:" + value.authResult + " software:" + value.softwareResult + " ticket:" + value.ticket);
        console.info("versionIdResult:" + value.softwareResultDetail[0],
        " patchLevelResult:" + value.softwareResultDetail[1],
        " rootHashResult:" + value.softwareResultDetail[2],
        " PCIDResult:" + value.softwareResultDetail[3],
        " reserved:" + value.softwareResultDetail[4]);
    }
    })
} catch (error) {
    let code: number = (error as BusinessError).code;
    let message: string = (error as BusinessError).message;
    console.error("error code:" + code + " message:" + message);
}
```


## getAttestStatus

```TypeScript
function getAttestStatus(): Promise<AttestResultInfo>
```

Obtains the AttestResultInfo object.

**Since:** 9

<!--Device-deviceAttest-function getAttestStatus(): Promise<AttestResultInfo>--><!--Device-deviceAttest-function getAttestStatus(): Promise<AttestResultInfo>-End-->

**System capability:** SystemCapability.XTS.DeviceAttest

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AttestResultInfo](arkts-basicservices-deviceattest-attestresultinfo-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [20000001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-deviceAttest.md#20000001-system-service-abnormal) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    deviceAttest.getAttestStatus().then((value: deviceAttest.AttestResultInfo) => {
    console.info("auth:" + value.authResult + " software:" + value.softwareResult + " ticket:" + value.ticket);
    console.info("versionIdResult:" + value.softwareResultDetail[0],
        " patchLevelResult:" + value.softwareResultDetail[1],
        " rootHashResult:" + value.softwareResultDetail[2],
        " PCIDResult:" + value.softwareResultDetail[3],
        " reserved:" + value.softwareResultDetail[4]);
    }).catch((error: BusinessError) => {
        console.error("error code:" + error.code + " message:" + error.message);
    });
} catch (error) {
    let code: number = (error as BusinessError).code;
    let message: string = (error as BusinessError).message;
    console.error("error code:" + code + " message:" + message);
}
```
