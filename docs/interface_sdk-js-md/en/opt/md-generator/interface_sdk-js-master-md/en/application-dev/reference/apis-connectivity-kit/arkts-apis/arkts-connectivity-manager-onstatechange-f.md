# onStateChange

## Modules to Import

```TypeScript
import { manager } from 'kits/@kit.ConnectivityKit';
```

## onStateChange

```TypeScript
function onStateChange(callback: Callback<NearlinkState>): void
```

Subscribes to state change events.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-manager-function onStateChange(callback: Callback<NearlinkState>): void--><!--Device-manager-function onStateChange(callback: Callback<NearlinkState>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NearlinkState&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 36100099 |
