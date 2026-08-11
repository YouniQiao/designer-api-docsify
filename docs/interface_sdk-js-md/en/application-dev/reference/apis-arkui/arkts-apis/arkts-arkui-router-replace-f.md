# replace

## Modules to Import

```TypeScript
import { router } from 'kits/@kit.ArkUI';
```

## replace

```TypeScript
function replace(options: RouterOptions): void
```

Replaces the current page with another one in the application and destroys the current page.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.arkui.UIContext:Router#replaceUrl](arkts-arkui-arkui-uicontext-router-c.md#replaceurl)(options:

<!--Device-router-function replace(options: RouterOptions): void--><!--Device-router-function replace(options: RouterOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | Yes | Description of the new page. |

## Examples

```TypeScript
class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replace({
  url: 'pages/detail',
  params: new RouterParams('message')
});
```

```TypeScript
class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replace({
  url: 'pages/detail',
  params: new RouterParams('message')
});
```

