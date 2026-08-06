# getRectangleById

## getRectangleById

```TypeScript
function getRectangleById(id: string): ComponentInfo
```

Obtains a **ComponentInfo** object based on the component ID and synchronously returns the geometric properties of the component.
    **NOTE**  
    
    - Since API version 10, you can use the  
    [getComponentUtils]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ API in  
    [UIContext]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to obtain the [ComponentUtils]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ object  
    associated with the current UI context. This API provides access to component coordinates and size information  
    after the target component completes layout. It is recommended that you invoke this API within  
    [layout completion callbacks]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_. Note that dynamically created components  
    must be mounted to the component tree before this API can obtain their information, as unmounted components are  
    not measured or laid out by the UI framework. Always ensure that component mounting precedes information  
    retrieval attempts.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 18

**Substitutes:** ohos.arkui.UIContext.ComponentUtils#getRectangleById

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-componentUtils-function getRectangleById(id: string): ComponentInfo--><!--Device-componentUtils-function getRectangleById(id: string): ComponentInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | Component ID. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | ComponentInfo** object, which provides the size, position, translation, scaling, rotation, and affine matrix information of the component. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../errorcode-internal.md#100001-internal-error) | UI execution context not found. |

**Example**

```TypeScript
import { componentUtils } from '@kit.ArkUI';
let modePosition:componentUtils.ComponentInfo = componentUtils.getRectangleById("onClick");
```

