# ControlPanelActionEventCallback

```TypeScript
type ControlPanelActionEventCallback = (event: PiPActionEventType, status?: number) => void
```

Describes the action event callback of the PiP controller.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPWindow-type ControlPanelActionEventCallback = (event: PiPActionEventType, status?: int) => void--><!--Device-PiPWindow-type ControlPanelActionEventCallback = (event: PiPActionEventType, status?: int) => void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [PiPActionEventType](arkts-arkui-pipwindow-pipactioneventtype-t.md) | Yes |
| status | number | No |
