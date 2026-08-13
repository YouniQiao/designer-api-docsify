# CdsmClient

Manages a CDSM client instance. Before invoking any CDSM client method, you must use [createCdsmClient](arkts-connectivity-cdsm-createcdsmclient-f.md#createCdsmClient) to create a CDSM client instance.

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-cdsm-interface CdsmClient--><!--Device-cdsm-interface CdsmClient-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { cdsm } from '@kit.ConnectivityKit';
```

## getCdsmInfo

```TypeScript
getCdsmInfo(): CdsmInfo
```

Gets the coordinated devices set information.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-CdsmClient-getCdsmInfo(): CdsmInfo--><!--Device-CdsmClient-getCdsmInfo(): CdsmInfo-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CdsmInfo](arkts-connectivity-cdsm-cdsminfo-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |

## offCdsmInfoChange

```TypeScript
offCdsmInfoChange(callback?: Callback<CdsmInfo>): void
```

Unsubscribes from coordinated devices set information change event.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CdsmClient-offCdsmInfoChange(callback?: Callback<CdsmInfo>): void--><!--Device-CdsmClient-offCdsmInfoChange(callback?: Callback<CdsmInfo>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CdsmInfo](arkts-connectivity-cdsm-cdsminfo-i.md)&gt; | No |

## onCdsmInfoChange

```TypeScript
onCdsmInfoChange(callback: Callback<CdsmInfo>): void
```

Subscribes to coordinated devices set information change event. This event is accessible only to applications that granted the ohos.permission.NEARLINK_ACCESS permission. If the application is granted the ohos.permission.GET_NEARLINK_PEER_MAC permission, the callback returns the real device address; otherwise, a random device address is returned.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CdsmClient-onCdsmInfoChange(callback: Callback<CdsmInfo>): void--><!--Device-CdsmClient-onCdsmInfoChange(callback: Callback<CdsmInfo>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CdsmInfo](arkts-connectivity-cdsm-cdsminfo-i.md)&gt; | Yes |
