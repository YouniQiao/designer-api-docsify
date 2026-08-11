# WidgetParamCallback (System API)

```TypeScript
type WidgetParamCallback = (challenge: Uint8Array) => WidgetParam
```

Defines the callback for obtaining remote authentication widget parameters. This type is used in remote authentication scenarios. When the configuration parameters of the remote authentication widget need to be obtained, the system invokes this callback.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-userAuth-type WidgetParamCallback = (challenge: Uint8Array) => WidgetParam--><!--Device-userAuth-type WidgetParamCallback = (challenge: Uint8Array) => WidgetParam-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| challenge | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WidgetParam](arkts-userauthentication-userauth-widgetparam-i-sys.md) |
