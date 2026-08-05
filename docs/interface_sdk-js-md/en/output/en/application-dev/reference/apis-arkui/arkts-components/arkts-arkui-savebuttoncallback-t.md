# SaveButtonCallback

```TypeScript
type SaveButtonCallback = (event: ClickEvent, result: SaveButtonOnClickResult, error?: BusinessError<void>) => void
```

Triggered when the **SaveButton** component is clicked.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-type SaveButtonCallback = (event: ClickEvent, result: SaveButtonOnClickResult, error?: BusinessError<void>) => void--><!--Device-unnamed-type SaveButtonCallback = (event: ClickEvent, result: SaveButtonOnClickResult, error?: BusinessError<void>) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Click event object, which includes information such as click position, timestamp, and input device.  |
| result | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Authorization result. \_\_\_HTML\_TAG\_USD\_1\_\_\_Returns **SUCCESS** if temporary authorization is granted for the save operation, and media library APIs can be accessed. Returns **TEMPORARY\_AUTHORIZATION\_FAILED** if temporary authorization fails and users cannot proceed with subsequent save actions. Returns **CANCELED\_BY\_USER** if users manually cancel authorization in the dialog box. This result is returned only when [userCancelEvent]\_\_\_JSDOC\_LINK\_USD\_0\_\_\_ is called with its parameter set to **true**. If **userCancelEvent** is not set to **true**, **TEMPORARY\_AUTHORIZATION\_FAILED** is returned when users cancel authorization instead.  |
| error | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | No | Error code and message when the component is clicked. If this parameter is not specified, the value is **undefined**. Use the **result** parameter to determine the authorization status. \_\_\_HTML\_TAG\_USD\_0\_\_\_ Error code 1 indicates an internal system error. Possible causes and solutions are as follows: \_\_\_HTML\_TAG\_USD\_1\_\_\_1. Inter-Process Communication (IPC) failure. Check the system status and try again. \_\_\_HTML\_TAG\_USD\_2\_\_\_2. Failed to display the security component dialog box. Check whether the save button is blocked or complies with style constraints for security components. Correct the issues and retry. \_\_\_HTML\_TAG\_USD\_3\_\_\_Error code 2 indicates invalid property settings. Possible causes are as follows: \_\_\_HTML\_TAG\_USD\_4\_\_\_1. The font or icon size is too small. \_\_\_HTML\_TAG\_USD\_5\_\_\_2. The font or icon color is too similar to the background color. \_\_\_HTML\_TAG\_USD\_6\_\_\_3. The font or icon color is too transparent. \_\_\_HTML\_TAG\_USD\_7\_\_\_4. The padding is negative. \_\_\_HTML\_TAG\_USD\_8\_\_\_5. The component is obscured by other components or windows. \_\_\_HTML\_TAG\_USD\_9\_\_\_6. Text extends beyond the component background area. \_\_\_HTML\_TAG\_USD\_10\_\_\_7. The component exceeds the window or screen bounds. \_\_\_HTML\_TAG\_USD\_11\_\_\_8. The component size is too large. \_\_\_HTML\_TAG\_USD\_12\_\_\_9. The component text is truncated and not fully displayed. \_\_\_HTML\_TAG\_USD\_13\_\_\_10. Other improper property settings affect the display of the security component.  |

