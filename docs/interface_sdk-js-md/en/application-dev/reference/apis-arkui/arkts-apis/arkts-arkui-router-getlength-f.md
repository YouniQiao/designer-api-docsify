# getLength

## getLength

```TypeScript
function getLength(): string
```

Obtains the number of pages in the current stack.
    **NOTE**  
    
    - Since API version 10, you can use the  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ API in  
    [UIContext]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to obtain the [Router]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ object associated  
    with the current UI context.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#getLength](arkts-arkui-arkui-uicontext-router-c.md#getlength)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function getLength(): string--><!--Device-router-function getLength(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string | Number of pages in the stack. The maximum value is **32**. |

**Example**

```TypeScript
let size = this.getUIContext().getRouter().getLength();
console.info('pages stack size = ' + size);
```

