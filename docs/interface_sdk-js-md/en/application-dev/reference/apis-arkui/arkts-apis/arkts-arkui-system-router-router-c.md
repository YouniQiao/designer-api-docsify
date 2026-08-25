# Router

The **Router** module provides APIs to access pages through URIs.

**Since:** 3

**ArkTS mode:** Supports only ArkTS-Dyn, since version 3.

**Deprecated since:** 8

**Substitutes:** [router](arkts-router.md)

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

## Modules to Import

```TypeScript
import { SystemRouter, BackRouterOptions, DisableAlertBeforeBackPageOptions, EnableAlertBeforeBackPageOptions, RouterOptions, RouterState } from '@kit.ArkUI';
```

## back

```TypeScript
static back(options?: BackRouterOptions): void
```

Returns to the previous or a specified page.

> **NOTE：**&gt;
> In the example, the **uri** field indicates the page route, which is specified by the **pages** list in the
> configuration file.

**Since:** 3

**ArkTS mode:** Supports only ArkTS-Dyn, since version 3.

**Deprecated since:** 8

**Substitutes:** back

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [BackRouterOptions](arkts-arkui-system-router-backrouteroptions-i.md) | No |

**Examples**

```TypeScript
// index page
import router from '@system.router';
class D{
  indexPushPage() {
    router.push({
      uri: 'pages/detail/detail'
    });
  }
}
export default new D()
```

```TypeScript
// detail page
import router from '@system.router';
class E{
  detailPushPage() {
    router.push({
      uri: 'pages/mall/mall'
    });
  }
}
export default new E()
```

```TypeScript
// Navigate from the mall page to the detail page through router.back().
import router from '@system.router';
class F{
  mallBackPage() {
    router.back();
  }
}
export default new F()
```

```TypeScript
// Navigate from the detail page to the index page through router.back().
import router from '@system.router';
class G{
  defaultBack() {
    router.back();
  }
}
export default new G()
```

```TypeScript
// Return to the detail page through router.back().
import router from '@system.router';
class H{
  backToDetail() {
    router.back({uri:'pages/detail/detail'});
  }
}
export default new H()
```

## clear

```TypeScript
static clear(): void
```

Clears all historical pages in the stack and retains only the current page at the top of the stack.

**Since:** 3

**ArkTS mode:** Supports only ArkTS-Dyn, since version 3.

**Deprecated since:** 8

**Substitutes:** clear

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

```TypeScript
import router from '@system.router';
class I{
  clearPage() {
    router.clear();
  }
}
export default new I()
```

## disableAlertBeforeBackPage

```TypeScript
static disableAlertBeforeBackPage(options?: DisableAlertBeforeBackPageOptions): void
```

Disables the display of a confirm dialog box before returning to the previous page.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 8

**Substitutes:** hideAlertBeforeBackPage

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [DisableAlertBeforeBackPageOptions](arkts-arkui-system-router-disablealertbeforebackpageoptions-i.md) | No |

**Examples**

```TypeScript
import router from '@system.router';
class Z{
  disableAlertBeforeBackPage() {
    router.disableAlertBeforeBackPage({
      success: ()=> {
        console.info('success');
      },
      cancel: ()=> {
        console.info('cancel');
      }
    });
  }
}
export default new Z()
```

## enableAlertBeforeBackPage

```TypeScript
static enableAlertBeforeBackPage(options: EnableAlertBeforeBackPageOptions): void
```

Enables the display of a confirm dialog box before returning to the previous page.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 8

**Substitutes:** showAlertBeforeBackPage

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [EnableAlertBeforeBackPageOptions](arkts-arkui-system-router-enablealertbeforebackpageoptions-i.md) | Yes |

**Examples**

```TypeScript
import router from '@system.router';
class L{
  enableAlertBeforeBackPage() {
    router.enableAlertBeforeBackPage({
      message: 'Message Info',
      success: ()=> {
        console.info('success');
      },
      cancel: ()=> {
        console.info('cancel');
      }
    });
  }
}
export default new L()
```

## getLength

```TypeScript
static getLength(): string
```

Obtains the number of pages in the current stack.

**Since:** 3

**ArkTS mode:** Supports only ArkTS-Dyn, since version 3.

**Deprecated since:** 8

**Substitutes:** getLength

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Examples**

```TypeScript
import router from '@system.router';
class J{
  getLength() {
    let size = router.getLength();
    console.info('pages stack size = ' + size);
  }
}
export default new J()
```

## getParams

```TypeScript
static getParams(): ParamsInterface
```

Obtains parameter information about the current page.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 8

**Substitutes:** getParams

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ParamsInterface](arkts-arkui-paramsinterface-t.md) |

## getState

```TypeScript
static getState(): RouterState
```

Obtains state information about the current page.

**Since:** 3

**ArkTS mode:** Supports only ArkTS-Dyn, since version 3.

**Deprecated since:** 8

**Substitutes:** getState

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RouterState](arkts-arkui-system-router-routerstate-i.md) |

**Examples**

```TypeScript
import router from '@system.router';
class K{
  getState() {
    let page = router.getState();
    console.info('current index = ' + page.index);
    console.info('current name = ' + page.name);
    console.info('current path = ' + page.path);
  }
}
export default new K()
```

## push

```TypeScript
static push(options: RouterOptions): void
```

Navigates to a specified page in the application.

> **NOTE：**&gt;
> The page routing stack supports a maximum of 32 pages.

**Since:** 3

**ArkTS mode:** Supports only ArkTS-Dyn, since version 3.

**Deprecated since:** 8

**Substitutes:** push

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | Yes |

**Examples**

```TypeScript
// Current page
import router from '@system.router';
class A{
  pushPage() {
    router.push({
      uri: 'pages/routerpage2/routerpage2',
      params: {
        data1: 'message',
        data2: {
          data3: [123, 456, 789]
        }
      }
    });
  }
}
export default new A()
```

```TypeScript
// routerpage2 page
class B{
  data:Record<string,string> = {'data1': 'default'}
  data2:Record<string,number[]> = {'data3': [1, 2, 3]}
  onInit() {
    console.info('showData1:' + this.data.data1);
    console.info('showData3:' + this.data2.data3);
  }
}
export default new B()
```

## replace

```TypeScript
static replace(options: RouterOptions): void
```

Replaces the current page with another one in the application and destroys the current page.

**Since:** 3

**ArkTS mode:** Supports only ArkTS-Dyn, since version 3.

**Deprecated since:** 8

**Substitutes:** replace

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | Yes |

**Examples**

```TypeScript
// Current page
import router from '@system.router';
class C{
  replacePage() {
    router.replace({
      uri: 'pages/detail/detail',
      params: {
        data1: 'message'
      }
    });
  }
}
export default new C()
```

```TypeScript
// detail page
class Area {
  data:Record<string,string> = {'data1': 'default'}
  onInit() {
    console.info(`showData1: ${JSON.stringify(this.data)}`);
  }
}
export default new Area()
```
