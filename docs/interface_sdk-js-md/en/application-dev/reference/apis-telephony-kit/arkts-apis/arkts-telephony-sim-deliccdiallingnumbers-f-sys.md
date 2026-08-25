# delIccDiallingNumbers (System API)

## Modules to Import

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## delIccDiallingNumbers

```TypeScript
function delIccDiallingNumbers(slotId: number, type: ContactType, diallingNumbers: DiallingNumbersInfo, callback: AsyncCallback<void>): void
```

Delete dialing number information on SIM card.

**Since:** 8

**Required permissions:** ohos.permission.WRITE_CONTACTS

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| type | [ContactType](arkts-telephony-sim-contacttype-e-sys.md) | Yes |
| diallingNumbers | [DiallingNumbersInfo](arkts-telephony-sim-diallingnumbersinfo-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8301002](../errorcode-telephony.md#8301002-failed-to-read-or-update-sim-card-data) |


## delIccDiallingNumbers

```TypeScript
function delIccDiallingNumbers(slotId: number, type: ContactType, diallingNumbers: DiallingNumbersInfo): Promise<void>
```

Delete dialing number information on SIM card.

**Since:** 8

**Required permissions:** ohos.permission.WRITE_CONTACTS

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| type | [ContactType](arkts-telephony-sim-contacttype-e-sys.md) | Yes |
| diallingNumbers | [DiallingNumbersInfo](arkts-telephony-sim-diallingnumbersinfo-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8301002](../errorcode-telephony.md#8301002-failed-to-read-or-update-sim-card-data) |
