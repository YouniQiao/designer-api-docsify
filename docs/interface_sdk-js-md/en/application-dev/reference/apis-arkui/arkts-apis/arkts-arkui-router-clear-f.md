# clear

## clear

```TypeScript
function clear(): void
```

Clears all historical pages in the stack and retains only the current page at the top of the stack.
    **NOTE**  
    
    - Since API version 10, you can use the  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ API in  
    [UIContext]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to obtain the [Router]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ object associated  
    with the current UI context.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#clear](arkts-arkui-arkui-uicontext-router-c.md#clear)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function clear(): void--><!--Device-router-function clear(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Example**

```TypeScript
this.getUIContext().getRouter().clear();
```

