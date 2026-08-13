# @ohos.web.WebNativeMessagingExtensionContext

## Modules to Import

```TypeScript
import { WebNativeMessagingExtensionContext } from '@kit.ArkWeb';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [WebNativeMessagingExtensionContext](arkts-arkweb-web-webnativemessagingextensioncontext-webnativemessagingextensioncontext-c.md) | WebNativeMessagingExtensionContext is the runtime context of the native web message extension ( [WebNativeMessagingExtensionAbility](../../apis-na/arkts-apis/arkts-na-web-webnativemessagingextensionability-webnativemessagingextensionability-c.md#WebNativeMessagingExtensionAbility)). It inherits from ExtensionContext and provides lifecycle management, ability startup, and native message connection control capabilities for the extension ability. In an extension that inherits from WebNativeMessagingExtensionAbility, developers can obtain this context through `this.context` and then call [startAbility](../../apis-na/arkts-apis/arkts-na-web-webnativemessagingextensioncontext-webnativemessagingextensioncontext-c.md#startAbility) to start another ability, call [startAbilityForResult](../../apis-na/arkts-apis/arkts-na-web-webnativemessagingextensioncontext-webnativemessagingextensioncontext-c.md#startAbilityForResult) to start a UIAbility and receive the return result, call [terminateSelf](../../apis-na/arkts-apis/arkts-na-web-webnativemessagingextensioncontext-webnativemessagingextensioncontext-c.md#terminateSelf) to terminate the current extension, or call [stopNativeConnection](../../apis-na/arkts-apis/arkts-na-web-webnativemessagingextensioncontext-webnativemessagingextensioncontext-c.md#stopNativeConnection) to stop a specified native web message connection. |

