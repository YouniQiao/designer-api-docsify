# updateIccDiallingNumbers (System API)

## Modules to Import

```TypeScript
import { sim } from '@kit.TelephonyKit';
```

## updateIccDiallingNumbers

```TypeScript
function updateIccDiallingNumbers(slotId: number, type: ContactType, diallingNumbers: DiallingNumbersInfo, callback: AsyncCallback<void>): void
```

Update dialing number information on SIM card.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.WRITE_CONTACTS

<!--Device-sim-function updateIccDiallingNumbers(slotId: int, type: ContactType, diallingNumbers: DiallingNumbersInfo, callback: AsyncCallback<void>): void--><!--Device-sim-function updateIccDiallingNumbers(slotId: int, type: ContactType, diallingNumbers: DiallingNumbersInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| type | [ContactType](arkts-telephony-sim-contacttype-e-sys.md) | Yes |
| diallingNumbers | [DiallingNumbersInfo](arkts-telephony-sim-diallingnumbersinfo-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8301002](../errorcode-telephony.md#8301002-failed-to-read-or-update-sim-card-data) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

let diallingNumbersInfo: sim.DiallingNumbersInfo = {
    alphaTag: "alpha",
    number: "138xxxxxxxx",
    recordNumber: 123,
    pin2: "1234"
};
sim.updateIccDiallingNumbers(0, sim.ContactType.GENERAL_CONTACT, diallingNumbersInfo, (err: BusinessError) => {
    console.info(`callback: err->${JSON.stringify(err)}`);
});
```


## updateIccDiallingNumbers

```TypeScript
function updateIccDiallingNumbers(slotId: number, type: ContactType, diallingNumbers: DiallingNumbersInfo): Promise<void>
```

Update dialing number information on SIM card.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.WRITE_CONTACTS

<!--Device-sim-function updateIccDiallingNumbers(slotId: int, type: ContactType, diallingNumbers: DiallingNumbersInfo): Promise<void>--><!--Device-sim-function updateIccDiallingNumbers(slotId: int, type: ContactType, diallingNumbers: DiallingNumbersInfo): Promise<void>-End-->

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8301002](../errorcode-telephony.md#8301002-failed-to-read-or-update-sim-card-data) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

let diallingNumbersInfo: sim.DiallingNumbersInfo = {
    alphaTag: "alpha",
    number: "138xxxxxxxx",
    recordNumber: 123
};
sim.updateIccDiallingNumbers(0, sim.ContactType.GENERAL_CONTACT, diallingNumbersInfo).then(() => {
    console.info(`updateIccDiallingNumbers success.`);
}).catch((err: BusinessError) => {
    console.error(`updateIccDiallingNumbers failed, promise: err->${JSON.stringify(err)}`);
});
```
