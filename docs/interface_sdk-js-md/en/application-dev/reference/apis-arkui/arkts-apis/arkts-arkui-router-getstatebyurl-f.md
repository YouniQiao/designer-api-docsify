# getStateByUrl

## getStateByUrl

```TypeScript
function getStateByUrl(url: string): Array<RouterState>
```

Obtains the status information about a page by its URL.
    **NOTE**  
    
    - Since API version 12, you can use the  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ API in  
    [UIContext]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to obtain the [Router]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ object associated  
    with the current UI context.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#getStateByUrl](arkts-arkui-arkui-uicontext-router-c.md#getstatebyurl)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-router-function getStateByUrl(url: string): Array<RouterState>--><!--Device-router-function getStateByUrl(url: string): Array<RouterState>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | URL of the target page. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;RouterState&gt; | Page routing state. |

**Example**

```TypeScript
let options: Array<router.RouterState> = router.getStateByUrl('pages/index');
for (let i: number = 0; i < options.length; i++) {
  console.info('index = ' + options[i].index);
  console.info('name = ' + options[i].name);
  console.info('path = ' + options[i].path);
  console.info('params = ' + options[i].params);
}
```

