# disableAlertBeforeBackPage

## Modules to Import

```TypeScript
import { router } from 'kits/@kit.ArkUI';
```

## disableAlertBeforeBackPage

```TypeScript
function disableAlertBeforeBackPage(): void
```

禁用页面返回询问对话框。适用于用户已完成保存操作可以安全返回、页面状态切换后不再需要返回确认、需要动态控制返回行为等场景。与showAlertBeforeBackPage()方法成对使用：调用showAlertBeforeBackPage()开启对话框后，可在适当时机调用本方法关闭对话框。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [hideAlertBeforeBackPage](arkts-arkui-arkui-uicontext-router-c.md#hidealertbeforebackpage)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.arkui.UIContext:Router#hideAlertBeforeBackPage](arkts-arkui-arkui-uicontext-router-c.md#hidealertbeforebackpage)

<!--Device-router-function disableAlertBeforeBackPage(): void--><!--Device-router-function disableAlertBeforeBackPage(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Examples

```TypeScript
import { router } from '@kit.ArkUI';

router.disableAlertBeforeBackPage();
```

```TypeScript
import { router } from '@kit.ArkUI';

router.disableAlertBeforeBackPage();
```

