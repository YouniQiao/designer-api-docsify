# offPairingRequest (System API)

## Modules to Import

```TypeScript
import { remoteDevice } from '@kit.ConnectivityKit';
```

## offPairingRequest

```TypeScript
function offPairingRequest(callback?: Callback<PairingRequestParam>): void
```

Unsubscribes from pairing request events from remote NearLink devices.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-remoteDevice-function offPairingRequest(callback?: Callback<PairingRequestParam>): void--><!--Device-remoteDevice-function offPairingRequest(callback?: Callback<PairingRequestParam>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PairingRequestParam](arkts-connectivity-remotedevice-pairingrequestparam-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 36100099 |
