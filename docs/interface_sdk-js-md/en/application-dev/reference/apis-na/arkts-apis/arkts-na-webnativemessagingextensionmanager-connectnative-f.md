# connectNative

## connectNative

```TypeScript
function connectNative(context: UIAbilityContext, want: Want, callback: WebExtensionConnectionCallback): int
```

Connects the current ability to the specified web native message extension ability.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.WEB_NATIVE_MESSAGING

**Model restriction:** This API can be used only in the stage model.

<!--Device-webNativeMessagingExtensionManager-function connectNative(context: UIAbilityContext, want: Want, callback: WebExtensionConnectionCallback): int--><!--Device-webNativeMessagingExtensionManager-function connectNative(context: UIAbilityContext, want: Want, callback: WebExtensionConnectionCallback): int-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIAbilityContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md) | Yes | Context of the web native message extension. |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | The element name of the web native messaging ability |
| callback | [WebExtensionConnectionCallback](arkts-na-webnativemessagingextensionmanager-webextensionconnectioncallback-i.md) | Yes | The remote object instance |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the number code of the ability connected |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

