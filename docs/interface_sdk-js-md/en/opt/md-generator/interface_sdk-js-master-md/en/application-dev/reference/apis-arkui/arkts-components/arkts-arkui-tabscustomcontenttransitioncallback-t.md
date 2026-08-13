# TabsCustomContentTransitionCallback

```TypeScript
declare type TabsCustomContentTransitionCallback = (from: number, to: number) => TabContentAnimatedTransition | undefined
```

Defines the callback invoked when the custom tab transition animation starts.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type TabsCustomContentTransitionCallback = (from: number, to: number) => TabContentAnimatedTransition | undefined--><!--Device-unnamed-declare type TabsCustomContentTransitionCallback = (from: number, to: number) => TabContentAnimatedTransition | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| from | number | Yes |
| to | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabContentAnimatedTransition](arkts-arkui-tabcontentanimatedtransition-i.md) \| undefined |
