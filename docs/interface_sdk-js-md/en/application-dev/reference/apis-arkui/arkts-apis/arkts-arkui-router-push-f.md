# push

## Modules to Import

```TypeScript
import { router } from 'kits/@kit.ArkUI';
```

## push

```TypeScript
function push(options: RouterOptions): void
```

跳转到应用内的指定页面。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [pushUrl](arkts-arkui-arkui-uicontext-router-c.md#pushurl)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.arkui.UIContext:Router#pushUrl](arkts-arkui-arkui-uicontext-router-c.md#pushurl)(options:

<!--Device-router-function push(options: RouterOptions): void--><!--Device-router-function push(options: RouterOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | Yes | 跳转页面描述信息。 |

## Examples

```TypeScript
import { router } from '@kit.ArkUI';

class InnerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: InnerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new InnerParams(tuple);
  }
}

router.push({
  url: 'pages/routerpage2',
  params: new RouterParams('message', [123, 456, 789])
});
```

```TypeScript
import { router } from '@kit.ArkUI';

class InnerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: InnerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new InnerParams(tuple);
  }
}

router.push({
  url: 'pages/routerpage2',
  params: new RouterParams('message', [123, 456, 789])
});
```

