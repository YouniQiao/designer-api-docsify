# PasteButtonCallback

```TypeScript
type PasteButtonCallback = (event: ClickEvent, result: PasteButtonOnClickResult, error?: BusinessError<void>) => void
```

Triggered when the **PasteButton** component is clicked.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-type PasteButtonCallback = (event: ClickEvent, result: PasteButtonOnClickResult, error?: BusinessError<void>) => void--><!--Device-unnamed-type PasteButtonCallback = (event: ClickEvent, result: PasteButtonOnClickResult, error?: BusinessError<void>) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Click event object, which includes information such as click position, timestamp and input device.  |
| result | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Authorization result for clipboard access permission. \_\_\_HTML\_TAG\_USD\_0\_\_\_A return value of **SUCCESS** means temporary read permission for current clipboard content is granted, and clipboard reading operations can proceed. A return value of **TEMPORARY\_AUTHORIZATION\_FAILED** means the authorization failed, and you must not attempt to read clipboard content.  |
| error | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | No | Error code and message when the component is clicked. \_\_\_HTML\_TAG\_USD\_0\_\_\_Default value:undefined. \_\_\_HTML\_TAG\_USD\_1\_\_\_Use the **result** parameter to determine the authorization status.\_\_\_HTML\_TAG\_USD\_2\_\_\_Error code 1 indicates an internal system error. Check the system status and try again.\_\_\_HTML\_TAG\_USD\_3\_\_\_Error code 2 indicates property configuration errors, including but not limited to:\_\_\_HTML\_TAG\_USD\_4\_\_\_1. The font or icon size is too small.\_\_\_HTML\_TAG\_USD\_5\_\_\_2. The font or icon color is similar to the component background color.\_\_\_HTML\_TAG\_USD\_6\_\_\_3. The font or icon color is too transparent.\_\_\_HTML\_TAG\_USD\_7\_\_\_4. The padding is negative.\_\_\_HTML\_TAG\_USD\_8\_\_\_5. The component is obscured by other components or windows. \_\_\_HTML\_TAG\_USD\_9\_\_\_6. Text extends beyond the component background area.\_\_\_HTML\_TAG\_USD\_10\_\_\_7. The component exceeds the window or screen bounds.\_\_\_HTML\_TAG\_USD\_11\_\_\_8. The component size is too large.\_\_\_HTML\_TAG\_USD\_12\_\_\_9. The component text is truncated and not fully displayed. \_\_\_HTML\_TAG\_USD\_13\_\_\_10. Improper settings of some security component properties prevent the component from displaying correctly.  |

