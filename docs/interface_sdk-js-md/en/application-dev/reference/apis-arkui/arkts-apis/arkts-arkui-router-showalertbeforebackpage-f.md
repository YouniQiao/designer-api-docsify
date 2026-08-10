# showAlertBeforeBackPage

## Modules to Import

```TypeScript
import { router } from 'kits/@kit.ArkUI';
```

## showAlertBeforeBackPage

```TypeScript
function showAlertBeforeBackPage(options: EnableAlertOptions): void
```

开启页面返回询问对话框。调用此方法后，执行[back](#routerbackdeprecated)返回页面时将弹出确认对话框，用户确认后才执行页面返回操作。适用于需要防止用户误操作返回导致数据丢失的场景，例如用户正在填写表单、编辑文档或进行支付操作时，弹出确认对话框以避免意外退出。

> **说明：**
> 
> - 从API version 9开始支持，从API version 18开始废弃，建议使用
> [showAlertBeforeBackPage](arkts-arkui-arkui-uicontext-router-c.md#showalertbeforebackpage)替代。showAlertBeforeBackPage需先
> 通过[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)获取
> [Router](arkts-arkui-uicontext.md)实例，然后通过该实例进行调用。
> 
> - 从API version 10开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的
> [Router](arkts-arkui-uicontext.md)对象。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#showAlertBeforeBackPage](arkts-arkui-arkui-uicontext-router-c.md#showalertbeforebackpage)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function showAlertBeforeBackPage(options: EnableAlertOptions): void--><!--Device-router-function showAlertBeforeBackPage(options: EnableAlertOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EnableAlertOptions](arkts-arkui-router-enablealertoptions-i.md) | Yes | 文本弹窗信息描述。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100001 | Internal error. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  this.getUIContext().getRouter().showAlertBeforeBackPage({
    message: 'Message Info'
  });
} catch (err) {
  console.error(`showAlertBeforeBackPage failed. Code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}`);
}
```

