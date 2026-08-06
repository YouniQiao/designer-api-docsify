# getState

## getState

```TypeScript
function getState(): RouterState
```

Obtains state information about the page at the top of the navigation stack.
    **NOTE**  
    
    - Since API version 10, you can use the  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ API in  
    [UIContext]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to obtain the [Router]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ object associated  
    with the current UI context.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#getState](arkts-arkui-arkui-uicontext-router-c.md#getstate)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function getState(): RouterState--><!--Device-router-function getState(): RouterState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Page routing state. |

**Example**

```TypeScript
let page = this.getUIContext().getRouter().getState();
console.info('current index = ' + page.index);
console.info('current name = ' + page.name);
console.info('current path = ' + page.path);
```

