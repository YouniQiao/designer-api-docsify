# ViewModel

View model

**Since:** 4

**Deprecated since:** -1

<!--Device-unnamed-export interface ViewModel--><!--Device-unnamed-export interface ViewModel-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

## $t

```TypeScript
$t(path: string, param?: object | Array<any>): string
```

Displays content based on the current system language and a path of the language resource key specified through \$t.

**Since:** 4

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-ViewModel-$t(path: string, param?: object | Array<any>): string--><!--Device-ViewModel-$t(path: string, param?: object | Array<any>): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| param | object \| Array & lt;any & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## $refs

```TypeScript
$refs: ElementReferences
```

An object that holds all DOM elements and component instances that have been registered with the refs attribute

**Type:** [ElementReferences](arkts-arkui-viewmodel-elementreferences-i.md)

**Since:** 4

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-ViewModel-$refs: ElementReferences--><!--Device-ViewModel-$refs: ElementReferences-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite
