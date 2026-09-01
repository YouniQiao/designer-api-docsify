# PasteButtonCallback

```TypeScript
type PasteButtonCallback = (event: ClickEvent, result: PasteButtonOnClickResult, error?: BusinessError<void>) => void
```

Triggered when the **PasteButton** component is clicked.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [ClickEvent](arkts-arkui-clickevent-i.md) | Yes | Click event object, which includes information such as click position, timestamp and input device. |
| result | [PasteButtonOnClickResult](arkts-arkui-pastebuttononclickresult-e.md) | Yes | Authorization result for clipboard access permission. A return value of **SUCCESS** means temporary read permission for current clipboard content is granted, and clipboard reading operations can proceed. A return value of **TEMPORARY_AUTHORIZATION_FAILED** means the authorization failed, and you must not attempt to read clipboard content. |
| error | BusinessError&lt;void&gt; | No | Error code and message when the component is clicked. Default value:undefined. Use the **result** parameter to determine the authorization status.Error code 1 indicates an internal system error. Check the system status and try again.Error code 2 indicates property configuration errors, including but not limited to: 1. The font or icon size is too small. 2. The font or icon color is similar to the component background color. 3. The font or icon color is too transparent. 4. The padding is negative. 5. The component is obscured by other components or windows.  6. Text extends beyond the component background area. 7. The component exceeds the window or screen bounds. 8. The component size is too large. 9. The component text is truncated and not fully displayed.  10. Improper settings of some security component properties prevent the component from displaying correctly. |
