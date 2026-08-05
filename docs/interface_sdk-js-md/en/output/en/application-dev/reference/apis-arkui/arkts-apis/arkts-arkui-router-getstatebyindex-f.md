# getStateByIndex

## getStateByIndex

```TypeScript
function getStateByIndex(index: number): RouterState | undefined
```

Obtains the status information about a page by its index. > **NOTE** > > - Since API version 12, you can use the > \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ API in > [UIContext]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to obtain the [Router]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ object associated > with the current UI context.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#getStateByIndex](arkts-arkui-arkui-uicontext-router-c.md#getstatebyindex)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-router-function getStateByIndex(index: number): RouterState | undefined--><!--Device-router-function getStateByIndex(index: number): RouterState | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | Index of the target page. The index starts from 1 from the bottom to the top of the stack. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | State information about the target page; **undefined** if the specified index |

**Example**

```TypeScript
let options: router.RouterState | undefined = router.getStateByIndex(1);
if (options != undefined) {
  console.info('index = ' + options.index);
  console.info('name = ' + options.name);
  console.info('path = ' + options.path);
  console.info(`params = ${JSON.stringify(options.params)}`);
}
```

