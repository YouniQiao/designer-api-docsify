# ComponentUtils

class ComponentUtils

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class ComponentUtils--><!--Device-unnamed-export declare class ComponentUtils-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## getRectangleById

```TypeScript
getRectangleById(id: string): componentUtils.ComponentInfo
```

Provide the ability to obtain the coordinates and size of component drawing areas.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentUtils-getRectangleById(id: string): componentUtils.ComponentInfo--><!--Device-ComponentUtils-getRectangleById(id: string): componentUtils.ComponentInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | ID of the component whose attributes are to be obtained. |

**Return value:**

| Type | Description |
| --- | --- |
| componentUtils.ComponentInfo | the object of ComponentInfo. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | UI execution context not found. |

