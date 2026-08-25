# unregisterConversationListener (System API)

## Modules to Import

```TypeScript
import { conversation } from '@kit.DistributedServiceKit';
```

## unregisterConversationListener

```TypeScript
function unregisterConversationListener(bundleName: string, abilityName: string): void
```

Unregisters the listener with the specified bundle name and ability name. This API must be used in pairs with [registerConversationListener](arkts-distributedservice-conversation-registerconversationlistener-f-sys.md) to unregister a registered listener. When the listener is no longer needed, call this API to unregister the listener to release resources. If the listener is not unregistered, resources will be continuously occupied. Only one listener can be registered for the same bundle name and ability name. Duplicate registration will overwrite the previously registered listener. After the listener is unregistered, the listener that is currently in effect will be removed. After this API is called, the app will no longer receive session data of the specified bundle name and ability name. If no listener has been registered for the specified bundle name and ability name, this API returns a success message.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC and ohos.permission.sec.ACCESS_UDID

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.SoftBus.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| abilityName | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [2000001](../errorcode-conversation.md#2000001-internal-error) |
