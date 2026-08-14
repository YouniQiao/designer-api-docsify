# AddFormMenuItem

## Modules to Import

```TypeScript
import { AddFormMenuItem } from 'AddFormMenuItem';
import { FormMenuItemStyle } from 'FormMenuItemStyle';
import { AddFormOptions } from 'AddFormOptions';
```

## AddFormMenuItem

```TypeScript
@Builder
export declare function AddFormMenuItem(
  want: Want,
  componentId: string,
  options?: AddFormOptions
): void
```

Build function of AddFormMenuItem.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-@Builderexport declare function AddFormMenuItem(  want: Want,  componentId: string,  options?: AddFormOptions): void--><!--Device-unnamed-@Builderexport declare function AddFormMenuItem(  want: Want,  componentId: string,  options?: AddFormOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | The want of the form to publish. |
| componentId | string | Yes | The id of the component used to get form snapshot. |
| options | AddFormOptions | No | Add form options. |

