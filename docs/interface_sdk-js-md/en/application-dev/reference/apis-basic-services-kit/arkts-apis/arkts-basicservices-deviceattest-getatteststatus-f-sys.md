# getAttestStatus (System API)

## Modules to Import

```TypeScript
import { deviceAttest } from 'kits/@kit.BasicServicesKit';
```

## getAttestStatus

```TypeScript
function getAttestStatus(callback: AsyncCallback<AttestResultInfo>): void
```

Obtains the AttestResultInfo object.

**Since:** 9

**System capability:** SystemCapability.XTS.DeviceAttest

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[AttestResultInfo](arkts-basicservices-deviceattest-attestresultinfo-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [20000001](../errorcode-deviceAttest.md#20000001-system-service-abnormal) |


## getAttestStatus

```TypeScript
function getAttestStatus(): Promise<AttestResultInfo>
```

Obtains the AttestResultInfo object.

**Since:** 9

**System capability:** SystemCapability.XTS.DeviceAttest

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AttestResultInfo](arkts-basicservices-deviceattest-attestresultinfo-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [20000001](../errorcode-deviceAttest.md#20000001-system-service-abnormal) |
