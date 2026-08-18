# getLength

## Modules to Import

```TypeScript
```

## getLength

```TypeScript
function getLength(): string
```

Obtains the number of pages in the current stack. > **NOTE：**> > - Since API version 10, you can use the > [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in > [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#uicontext) to obtain the [Router](arkts-arkui-arkui-uicontext-uicontext-c.md#uicontext) object associated > with the current UI context.

**Since:** 8

**Deprecated since:** 18

**Substitutes:** [getLength](arkts-arkui-arkui-uicontext-router-c.md#getlength)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function getLength(): string--><!--Device-router-function getLength(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Examples**

```TypeScript
let size = this.getUIContext().getRouter().getLength();
console.info('pages stack size = ' + size);
```
