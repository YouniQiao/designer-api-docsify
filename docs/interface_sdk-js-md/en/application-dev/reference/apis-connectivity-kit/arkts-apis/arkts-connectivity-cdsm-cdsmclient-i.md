# CdsmClient

Defines a CDSM client class, which provides APIs for obtaining the CDSM information of a remote device.  
- Before using the methods of this class, call [cdsm.createCdsmClient](arkts-connectivity-cdsm-createcdsmclient-f.md) to construct an instance of this class.  
This class is applicable to scenarios where you need to obtain the member devices and connection status changes of a group of NearLink devices (CDSM) and perform service coordination accordingly. For example, after a phone is paired with earphones, the phone can use the CDSM to query the left and right earphones and detect their connection status changes.An app only needs to create one [CdsmClient](#cdsmclient) instance for a remote device. Repeated creation will increase unnecessary resource overhead.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { cdsm } from '@kit.ConnectivityKit';
```

## getCdsmInfo

```TypeScript
getCdsmInfo(): CdsmInfo
```

Queries information about the coordinated devices set of a remote device.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CdsmInfo](arkts-connectivity-cdsm-cdsminfo-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 36100003 |
| 36100099 |

## offCdsmInfoChange

```TypeScript
offCdsmInfoChange(callback?: Callback<CdsmInfo>): void
```

Unsubscribes from the CDSM information change event. This API uses an asynchronous callback to return the result.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CdsmInfo](arkts-connectivity-cdsm-cdsminfo-i.md)&gt; | No |

## onCdsmInfoChange

```TypeScript
onCdsmInfoChange(callback: Callback<CdsmInfo>): void
```

Subscribes to the CDSM information change event. This API uses an asynchronous callback to return the result.The app must have the **ohos.permission.ACCESS_NEARLINK** permission to receive this event.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CdsmInfo](arkts-connectivity-cdsm-cdsminfo-i.md)&gt; | Yes |
