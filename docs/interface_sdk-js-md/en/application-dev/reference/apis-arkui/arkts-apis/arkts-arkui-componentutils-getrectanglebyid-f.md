# getRectangleById

## Modules to Import

```TypeScript
import { componentUtils } from 'kits/@kit.ArkUI';
```

## getRectangleById

```TypeScript
function getRectangleById(id: string): ComponentInfo
```

Obtains a **ComponentInfo** object based on the component ID and synchronously returns the geometric properties of the component.

> **NOTE：**&gt;
> - Since API version 10, you can use the
> [getComponentUtils](arkts-arkui-arkui-uicontext-uicontext-c.md#getcomponentutils) API in
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [ComponentUtils](arkts-arkui-arkui-uicontext-uicontext-c.md) object
> associated with the current UI context. This API provides access to component coordinates and size information
> after the target component completes layout. It is recommended that you invoke this API within
> [layout completion callbacks](arkts-arkui-inspector.md). Note that dynamically created components
> must be mounted to the component tree before this API can obtain their information, as unmounted components are
> not measured or laid out by the UI framework. Always ensure that component mounting precedes information
> retrieval attempts.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** getRectangleById

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ComponentInfo](arkts-arkui-componentutils-componentinfo-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../errorcode-internal.md#100001-internal-error) |
