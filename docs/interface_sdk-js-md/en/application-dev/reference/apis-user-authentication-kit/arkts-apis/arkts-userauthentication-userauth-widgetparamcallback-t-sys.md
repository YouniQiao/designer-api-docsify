# WidgetParamCallback (System API)

```TypeScript
type WidgetParamCallback = (challenge: Uint8Array) => WidgetParam
```

Triggered to obtain remote authentication page parameters. This callback type is used in remote authentication scenarios. When the system needs to obtain the configuration parameters of the remote authentication page, it calls this callback function.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| challenge | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WidgetParam](arkts-userauthentication-userauth-widgetparam-i.md) |
