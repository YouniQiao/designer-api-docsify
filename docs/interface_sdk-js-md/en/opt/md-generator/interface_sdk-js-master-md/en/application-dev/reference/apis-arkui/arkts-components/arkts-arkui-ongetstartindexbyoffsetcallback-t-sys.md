# OnGetStartIndexByOffsetCallback (System API)

```TypeScript
declare type OnGetStartIndexByOffsetCallback = (totalOffset: number) => StartLineInfo
```

Defines the callback type used in onGetStartIndexByOffset of GridLayoutOptions.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare type OnGetStartIndexByOffsetCallback = (totalOffset: double) => StartLineInfo--><!--Device-unnamed-declare type OnGetStartIndexByOffsetCallback = (totalOffset: double) => StartLineInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| totalOffset | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [StartLineInfo](arkts-arkui-startlineinfo-i-sys.md) |
