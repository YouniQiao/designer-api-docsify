# AccessibilityElement

Defines the **AccessibilityElement**. Before calling APIs of **AccessibilityElement**, you must call   
[AccessibilityExtensionContext.getFocusElement()](arkts-accessibility-accessibilityextensioncontext-c.md#getFocusElement-1)or   
[AccessibilityExtensionContext.getWindowRootElement()](arkts-accessibility-accessibilityextensioncontext-c.md#getWindowRootElement-1)to obtain an **AccessibilityElement** instance.

**Since:** 9

<!--Device-unnamed-export declare interface AccessibilityElement--><!--Device-unnamed-export declare interface AccessibilityElement-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## enableScreenCurtain

```TypeScript
enableScreenCurtain(isEnable: boolean): void
```

Enables or disables the screen curtain.

**Since:** 12

<!--Device-AccessibilityElement-enableScreenCurtain(isEnable: boolean): void--><!--Device-AccessibilityElement-enableScreenCurtain(isEnable: boolean): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isEnable](#isenable) | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-accessibility-kit/errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

## Examples

```TypeScript
import {
  AccessibilityElement,
  AccessibilityEvent, 
  AccessibilityExtensionContext
} from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class AccessibilityManager {
  private static instance: AccessibilityManager;
  context?: AccessibilityExtensionContext;

  static getInstance(): AccessibilityManager {
    if (!AccessibilityManager.instance) {
      AccessibilityManager.instance = new AccessibilityManager();
    }
    return AccessibilityManager.instance;
  }

  onStart(context: AccessibilityExtensionContext) {
    this.context = context;
  }

  onStop() {
    this.context = undefined;
  }

  onEvent(accessibilityEvent: AccessibilityEvent): void {
    if (!this.context) {
      console.error('context is not available!');
      return;
    }
    this.context.getRootInActiveWindow().then((rootElement: AccessibilityElement) => {
      console.info(`succeeded in getting root element of the window, ${JSON.stringify(rootElement)}`);
      rootElement.enableScreenCurtain(true);
      console.info(`Succeeded in enabling screen curtain`);
    }).catch((err: BusinessError) => {
      console.error(`failed to enable screen curtain, Code is ${err.code}, message is ${err.message}`);
    });
  }
}
```

## executeAction

```TypeScript
executeAction(action: AccessibilityAction, parameters?: Parameter): Promise<void>
```

Executes a specific action based on the specified action type and input parameters. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityElement-executeAction(action: AccessibilityAction, parameters?: Parameter): Promise<void>--><!--Device-AccessibilityElement-executeAction(action: AccessibilityAction, parameters?: Parameter): Promise<void>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| action | [AccessibilityAction](arkts-accessibility-accessibility-accessibilityaction-e-sys.md) | Yes |
| parameters | [Parameter](arkts-accessibility-accessibilityextensioncontext-parameter-c-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [9300005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-accessibility-kit/errorcode-accessibility.md#9300005-operation-not-supported) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
// Example of an action without parameters:
import { AccessibilityAction } from '@kit.AccessibilityKit';

// rootElement is an instance of AccessibilityElement.
// An action that does not require any parameter setting is an action without parameters, as specified in the action description.
try {
  await rootElement.executeAction(AccessibilityAction.CLICK);
  console.info(`succeeded in performing action CLICK`);
}catch (error){
  console.error(`failed to perform action CLICK, Code is ${error?.code}, message is ${error?.message}`);
}
```

```TypeScript
// Example of an action with parameters:
import { AccessibilityAction, Parameter } from '@kit.AccessibilityKit';

try {
  // selectTextBegin: start position of the selected text
  // selectTextEnd: end position of the selected text
  // selectTextInForWard: true indicates to select text forward, and false indicates to select text backward.
  let p : Parameter = { selectTextBegin: '0', selectTextEnd: '8', selectTextInForWard: true }
  // rootElement is an instance of AccessibilityElement.
  // Sample code of setSelection
  rootElement.executeAction(AccessibilityAction.SET_SELECTION, p);
  console.info(`succeeded in performing action SET_SELECTION`);
}catch (error){
  console.error(`failed to perform action SET_SELECTION, Code is ${error?.code}, message is ${error?.message}`);
}
```

```TypeScript
// Example of an action with parameters:
import { AccessibilityAction, Parameter } from '@kit.AccessibilityKit';

try {
  // offset: cursor position
  let p : Parameter = { offset: '1' }
  // rootElement is an instance of AccessibilityElement.
  // Sample code of setCursorPosition
  rootElement.executeAction(AccessibilityAction.SET_CURSOR_POSITION, p);
  console.info(`succeeded in performing action SET_CURSOR_POSITION`);
}catch (error){
  console.error(`failed to perform action SET_CURSOR_POSITION, Code is ${error?.code}, message is ${error?.message}`);
}
```

## findElement

```TypeScript
findElement(type: 'textType', condition: string): Promise<Array<AccessibilityElement>>
```

Finds all node elements based on the **accessibilityTextHint** text type configured for a node. This API uses a promise to return the result.

**Since:** 12

<!--Device-AccessibilityElement-findElement(type: 'textType', condition: string): Promise<Array<AccessibilityElement>>--><!--Device-AccessibilityElement-findElement(type: 'textType', condition: string): Promise<Array<AccessibilityElement>>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [type](#type) | 'textType' | Yes |
| condition | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// The content of condition must be the same as the type value in the accessibilityTextHint attribute of the target component.
let condition = 'location'; 

// rootElement is an instance of AccessibilityElement.
rootElement.findElement('textType', condition).then((data: AccessibilityElement[]) => {
  console.info(`succeeded in finding element, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to find element, Code is ${err.code}, message is ${err.message}`);
});
```

## findElement

```TypeScript
findElement(type: 'elementId', condition: number): Promise<AccessibilityElement>
```

Finds the node element of the current active window based on the element ID. This API uses a promise to return the result.

**Since:** 12

<!--Device-AccessibilityElement-findElement(type: 'elementId', condition: long): Promise<AccessibilityElement>--><!--Device-AccessibilityElement-findElement(type: 'elementId', condition: long): Promise<AccessibilityElement>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [type](#type) | 'elementId' | Yes |
| condition | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// elementId is 10.
let condition = 10;

// rootElement is an instance of AccessibilityElement.
rootElement.findElement('elementId', condition).then((data: AccessibilityElement) => {
  console.info(`succeeded in finding element, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to find element, Code is ${err.code}, message is ${err.message}`);
});
```

## findElementByContent

```TypeScript
findElementByContent(condition: string): Promise<Array<AccessibilityElement>>
```

Finds elements based on the content. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityElement-findElementByContent(condition: string): Promise<Array<AccessibilityElement>>--><!--Device-AccessibilityElement-findElementByContent(condition: string): Promise<Array<AccessibilityElement>>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| condition | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-accessibility-kit/errorcode-accessibility.md#9300006-failed-to-connect-the-target-app-and-accessibility-service) |

## Examples

```TypeScript
// Page.ets
  build() {
    Text('Connect')
        .id('connect')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
// ...

// AccessibilityExtAbility.ets
import { AccessibilityElement } from '@kit.AccessibilityKit';

let windowId: number = 10;

axContext.getRootInActiveWindow(windowId).then((root: AccessibilityElement) => {
    root.findElementByContent('connect').then((elements: AccessibilityElement[]) => {
        console.info("findElementByContent size=" + elements.length)
    }).catch((err: BusinessError) => {
        console.error(`findElementByContent failed, code: ${err.code}, message: ${err.message}`);
    })
}).catch((err: BusinessError) => {
  console.error(`getRootInActiveWindow failed, code: ${err.code}, message: ${err.message}`);
})
```

## findElementByFocusDirection

```TypeScript
findElementByFocusDirection(condition: FocusDirection): Promise<AccessibilityElement>
```

Finds elements based on the focus direction. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityElement-findElementByFocusDirection(condition: FocusDirection): Promise<AccessibilityElement>--><!--Device-AccessibilityElement-findElementByFocusDirection(condition: FocusDirection): Promise<AccessibilityElement>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| condition | [FocusDirection](arkts-accessibility-focusdirection-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-accessibility-kit/errorcode-accessibility.md#9300006-failed-to-connect-the-target-app-and-accessibility-service) |

## Examples

```TypeScript
// Page.ets
// Click TextInput and then it is the accessibility focus element, up direction element is Text#connect
  build() {
    Text('Connect')
        .id('connect')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)

    TextInput({ placeholder: 'please input...' })
        .id('text_input')
        .fontSize($r('app.float.page_text_font_size'))
// ...

// AccessibilityExtAbility.ets
import { AccessibilityElement } from '@kit.AccessibilityKit';

axContext.getAccessibilityFocusedElement().then((focus: AccessibilityElement) => {
    focus.findElementByFocusDirection('up').then((element: AccessibilityElement) => {
        console.info("findElementByFocusDirection UP componentId: " + element.componentId);
    }).catch((err: BusinessError) => {
        console.error(`findElementByFocusDirection UP failed, code: ${err.code}, message: ${err.message}`);
    })
}).catch((err: BusinessError) => {
  console.error(`getAccessibilityFocusedElement failed, code: ${err.code}, message: ${err.message}`);
})
```

## findElementByFocusDirection

```TypeScript
findElementByFocusDirection(condition: FocusDirection, type: FocusRuleType): Promise<AccessibilityElement>
```

Finds elements based on the focus direction. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccessibilityElement-findElementByFocusDirection(condition: FocusDirection, type: FocusRuleType): Promise<AccessibilityElement>--><!--Device-AccessibilityElement-findElementByFocusDirection(condition: FocusDirection, type: FocusRuleType): Promise<AccessibilityElement>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| condition | [FocusDirection](arkts-accessibility-focusdirection-t.md) | Yes |
| [type](#type) | [FocusRuleType](arkts-accessibility-accessibility-focusruletype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-accessibility-kit/errorcode-accessibility.md#9300006-failed-to-connect-the-target-app-and-accessibility-service) |

## findElementById

```TypeScript
findElementById(condition: number): Promise<AccessibilityElement>
```

Finds elements based on element ID. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityElement-findElementById(condition: long): Promise<AccessibilityElement>--><!--Device-AccessibilityElement-findElementById(condition: long): Promise<AccessibilityElement>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| condition | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-accessibility-kit/errorcode-accessibility.md#9300006-failed-to-connect-the-target-app-and-accessibility-service) |

## Examples

```TypeScript
// Page.ets
// Click TextInput and then it is the accessibility focus element
  build() {
    Text('Connect')
        .id('connect')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)

    TextInput({ placeholder: 'please input...' })
        .id('text_input')
        .fontSize($r('app.float.page_text_font_size'))
// ...

// AccessibilityExtAbility.ets
import { AccessibilityElement } from '@kit.AccessibilityKit';

axContext.getAccessibilityFocusedElement().then((focus: AccessibilityElement) => {
    focus.findElementById(0).then((element: AccessibilityElement) => {
        console.info("findElementById componentId: " + element.componentId);
    }).catch((err: BusinessError) => {
        console.error(`findElementById failed, code: ${err.code}, message: ${err.message}`);
    })
}).catch((err: BusinessError) => {
  console.error(`getAccessibilityFocusedElement failed, code: ${err.code}, message: ${err.message}`);
})
```

## findElementsByAccessibilityHintText

```TypeScript
findElementsByAccessibilityHintText(condition: string): Promise<Array<AccessibilityElement>>
```

Finds elements based on the hint text. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityElement-findElementsByAccessibilityHintText(condition: string): Promise<Array<AccessibilityElement>>--><!--Device-AccessibilityElement-findElementsByAccessibilityHintText(condition: string): Promise<Array<AccessibilityElement>>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| condition | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-accessibility-kit/errorcode-accessibility.md#9300006-failed-to-connect-the-target-app-and-accessibility-service) |

## Examples

```TypeScript
// Page.ets
  build() {
    Text('Connect')
        .id('connect')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)

    TextInput({ placeholder: 'please input...' })
        .id('text_input')
        .fontSize($r('app.float.page_text_font_size'))
        .accessibilityTextHint('location')
// ...

// AccessibilityExtAbility.ets
import { AccessibilityElement } from '@kit.AccessibilityKit';

let windowId: number = 10;

axContext.getRootInActiveWindow(windowId).then((root: AccessibilityElement) => {
    root.findElementsByAccessibilityHintText('location').then((elements: AccessibilityElement[]) => {
        console.info("findElementsByAccessibilityHintText size=" + elements.length)
    }).catch((err: BusinessError) => {
        console.error(`findElementsByAccessibilityHintText failed, code: ${err.code}, message: ${err.message}`);
    })
}).catch((err: BusinessError) => {
  console.error(`getRootInActiveWindow failed, code: ${err.code}, message: ${err.message}`);
})
```

## findElementsByCondition

```TypeScript
findElementsByCondition(rule: FocusRule, condition: FocusCondition): Promise<FocusMoveResult>
```

Finds a focusable node by conditions. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityElement-findElementsByCondition(rule: FocusRule, condition: FocusCondition): Promise<FocusMoveResult>--><!--Device-AccessibilityElement-findElementsByCondition(rule: FocusRule, condition: FocusCondition): Promise<FocusMoveResult>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rule | [FocusRule](arkts-accessibility-focusrule-t-sys.md) | Yes |
| condition | [FocusCondition](arkts-accessibility-focuscondition-t-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[FocusMoveResult](arkts-accessibility-accessibilityextensioncontext-focusmoveresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { AccessibilityElement } from '@kit.AccessibilityKit';

axContext.getAccessibilityFocusedElement().then((focus: AccessibilityElement) => {
    focus.findElementsByCondition("bypassSelf", "forward").then((res: FocusMoveResult) => {
        console.info("findElementsByCondition result: " + res.result);
    }).catch((err: BusinessError) => {
        console.error(`findElementsByCondition failed, code: ${err.code}, message: ${err.message}`);
    })
}).catch((err: BusinessError) => {
  console.error(`getAccessibilityFocusedElement failed, code: ${err.code}, message: ${err.message}`);
})
```

## findElementsByCondition

```TypeScript
findElementsByCondition(rule: FocusRule, condition: FocusCondition, type: FocusRuleType): Promise<FocusMoveResult>
```

Finds a focusable node by conditions. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccessibilityElement-findElementsByCondition(rule: FocusRule, condition: FocusCondition, type: FocusRuleType): Promise<FocusMoveResult>--><!--Device-AccessibilityElement-findElementsByCondition(rule: FocusRule, condition: FocusCondition, type: FocusRuleType): Promise<FocusMoveResult>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rule | [FocusRule](arkts-accessibility-focusrule-t-sys.md) | Yes |
| condition | [FocusCondition](arkts-accessibility-focuscondition-t-sys.md) | Yes |
| [type](#type) | [FocusRuleType](arkts-accessibility-accessibility-focusruletype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[FocusMoveResult](arkts-accessibility-accessibilityextensioncontext-focusmoveresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getChildren

```TypeScript
getChildren(): Promise<Array<AccessibilityElement>>
```

Obtains the child elements of an element. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityElement-getChildren(): Promise<Array<AccessibilityElement>>--><!--Device-AccessibilityElement-getChildren(): Promise<Array<AccessibilityElement>>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { AccessibilityElement } from '@kit.AccessibilityKit';

axContext.getAccessibilityFocusedElement().then((element: AccessibilityElement) => {
  console.info(`element childrenIds: ${element.childrenIds}`);
  element.getChildren().then((children: AccessibilityElement[]) => {
    console.info(`children element's size: ${children.length}`);
  }).catch((err: BusinessError) => {
    console.error(`getChildren failed, code: ${err.code}, message: ${err.message}`);
  })
}).catch((err: BusinessError) => {
  console.error(`getAccessibilityFocusedElement failed, code: ${err.code}, message: ${err.message}`);
})
```

## getCursorPosition

```TypeScript
getCursorPosition(callback: AsyncCallback<number>): void
```

Obtains the cursor position in the **Text** component. This API uses an asynchronous callback to return the result.

**Since:** 12

<!--Device-AccessibilityElement-getCursorPosition(callback: AsyncCallback<int>): void--><!--Device-AccessibilityElement-getCursorPosition(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement is an instance of AccessibilityElement.
rootElement.getCursorPosition((err: BusinessError, data: number) => {
  if (err && err.code) {
    console.error(`failed to get cursor position, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`succeeded in getting cursor position, ${data}`);
});
```

## getCursorPosition

```TypeScript
getCursorPosition(): Promise<number>
```

Obtains the cursor position in the **Text** component. This API uses a promise to return the result.

**Since:** 12

<!--Device-AccessibilityElement-getCursorPosition(): Promise<int>--><!--Device-AccessibilityElement-getCursorPosition(): Promise<int>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement is an instance of AccessibilityElement.
rootElement.getCursorPosition().then((data: number) => {
  console.info(`succeeded in getting cursor position, ${data}`);
}).catch((err: BusinessError) => {
  console.error(`failed to get cursor position, Code is ${err.code}, message is ${err.message}`);
});
```

## getParent

```TypeScript
getParent(): Promise<AccessibilityElement>
```

Obtains the parent element of an accessibility node. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityElement-getParent(): Promise<AccessibilityElement>--><!--Device-AccessibilityElement-getParent(): Promise<AccessibilityElement>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { AccessibilityElement } from '@kit.AccessibilityKit';

axContext.getAccessibilityFocusedElement().then((element: AccessibilityElement) => {
  console.info(`element parent id: ${element.parentId}`);
  element.getParent().then((parent: AccessibilityElement) => {
    console.info(`parent element's parent id: ${parent.parentId}`);
  }).catch((err: BusinessError) => {
    console.error(`getParent failed, code: ${err.code}, message: ${err.message}`);
  })
}).catch((err: BusinessError) => {
  console.error(`getAccessibilityFocusedElement failed, code: ${err.code}, message: ${err.message}`);
})
```

## getRoot

```TypeScript
getRoot(): Promise<AccessibilityElement>
```

Obtains the root element of an active window. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityElement-getRoot(): Promise<AccessibilityElement>--><!--Device-AccessibilityElement-getRoot(): Promise<AccessibilityElement>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { AccessibilityElement } from '@kit.AccessibilityKit';

let windows: AccessibilityWindow[] = axContext.getAccessibilityWindowsSync()
for (let window of windows) {
  console.info(`window id: ${window.windowId}`);
  window.getRoot().then((root: AccessibilityElement) => {
    console.info(`root element's componentId: ${root.componentId}`);
  }).catch((err: BusinessError) => {
    console.error(`getRoot failed, code: ${err.code}, message: ${err.message}`);
  })
}
```

## accessibilityFocused

```TypeScript
accessibilityFocused?: boolean
```

Whether the element is focused for accessibility purposes. The value **true** indicates that the element is focused, and **false** indicates the opposite.

Default value: **false**.

**Type:** boolean

**Since:** 20

<!--Device-AccessibilityElement-accessibilityFocused?: boolean--><!--Device-AccessibilityElement-accessibilityFocused?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## accessibilityGroup

```TypeScript
accessibilityGroup?: boolean
```

Whether the element is an accessibility group. The value **true** indicates that the element is an accessibility group, and **false** indicates the opposite.

Default value: **false**.

**Type:** boolean

**Since:** 20

<!--Device-AccessibilityElement-accessibilityGroup?: boolean--><!--Device-AccessibilityElement-accessibilityGroup?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## accessibilityLevel

```TypeScript
accessibilityLevel?: string
```

Accessibility level of a component.

**auto**: The accessibility grouping service and ArkUI jointly determine whether the current component can be identified by accessibility services.

**yes**: The component can be identified by accessibility services.

**no**: The component cannot be identified by accessibility services.

**no-hide-descendants**: The current component and all its child components cannot be identified by accessibility services.

**Type:** string

**Since:** 20

<!--Device-AccessibilityElement-accessibilityLevel?: string--><!--Device-AccessibilityElement-accessibilityLevel?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## accessibilityNextFocusId

```TypeScript
accessibilityNextFocusId?: number
```

ID of the next component to obtain the focus.

Default value: **-1**.

**Type:** number

**Since:** 20

<!--Device-AccessibilityElement-accessibilityNextFocusId?: long--><!--Device-AccessibilityElement-accessibilityNextFocusId?: long-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## accessibilityPreviousFocusId

```TypeScript
accessibilityPreviousFocusId?: number
```

ID of the previous component to obtain the focus.

Default value: **-1**.

**Type:** number

**Since:** 20

<!--Device-AccessibilityElement-accessibilityPreviousFocusId?: long--><!--Device-AccessibilityElement-accessibilityPreviousFocusId?: long-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## accessibilityScrollable

```TypeScript
accessibilityScrollable?: boolean
```

Whether the element can be scrolled for accessibility purposes. This attribute has a higher priority than   
**scrollable**.

The value **true** indicates that the element is scrollable, and **false** indicates the opposite.

Default value: **true**.

**Type:** boolean

**Since:** 20

<!--Device-AccessibilityElement-accessibilityScrollable?: boolean--><!--Device-AccessibilityElement-accessibilityScrollable?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## accessibilityStateDescription

```TypeScript
accessibilityStateDescription?: string
```

Custom accessibility state broadcast text of an element.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccessibilityElement-accessibilityStateDescription?: string--><!--Device-AccessibilityElement-accessibilityStateDescription?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## accessibilityText

```TypeScript
accessibilityText?: string
```

Accessibility text information of an element.

**Type:** string

**Since:** 20

<!--Device-AccessibilityElement-accessibilityText?: string--><!--Device-AccessibilityElement-accessibilityText?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## accessibilityVisible

```TypeScript
accessibilityVisible?: boolean
```

Whether the component is visible for accessibility purposes. The value **true** indicates that the component is visible, and **false** indicates the opposite.

**Type:** boolean

**Since:** 20

<!--Device-AccessibilityElement-accessibilityVisible?: boolean--><!--Device-AccessibilityElement-accessibilityVisible?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## belongTreeId

```TypeScript
belongTreeId?: number
```

Component tree ID that the element belongs to. The default value is **-1**.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccessibilityElement-belongTreeId?: int--><!--Device-AccessibilityElement-belongTreeId?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName?: string
```

Bundle name.

**Type:** string

**Since:** 20

<!--Device-AccessibilityElement-bundleName?: string--><!--Device-AccessibilityElement-bundleName?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## checkable

```TypeScript
checkable?: boolean
```

Whether the element is checkable. The value **true** indicates that the element is checkable, and **false** indicates the opposite.

Default value: **false**.

**Type:** boolean

**Since:** 20

<!--Device-AccessibilityElement-checkable?: boolean--><!--Device-AccessibilityElement-checkable?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## checked

```TypeScript
checked?: boolean
```

Whether the element is checked. The value **true** indicates that the element is checked, and **false** indicates the opposite.

Default value: **false**.

**Type:** boolean

**Since:** 20

<!--Device-AccessibilityElement-checked?: boolean--><!--Device-AccessibilityElement-checked?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## childrenIds

```TypeScript
childrenIds?: Array<number>
```

List of child element IDs of a component.

**Type:** Array&lt;number&gt;

**Since:** 20

<!--Device-AccessibilityElement-childrenIds?: Array<long>--><!--Device-AccessibilityElement-childrenIds?: Array<long>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## childrenTreeId

```TypeScript
childrenTreeId?: number
```

Child component tree ID of the element. The default value is **-1**.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccessibilityElement-childrenTreeId?: int--><!--Device-AccessibilityElement-childrenTreeId?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## clickable

```TypeScript
clickable?: boolean
```

Whether the element is clickable. The value **true** indicates that the element is clickable, and **false** indicates the opposite.

Default value: **false**.

**Type:** boolean

**Since:** 20

<!--Device-AccessibilityElement-clickable?: boolean--><!--Device-AccessibilityElement-clickable?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## clip

```TypeScript
clip?: boolean
```

Whether the component needs to be clipped. The value **true** indicates that the component needs to be clipped, and  
**false** indicates the opposite.

**Type:** boolean

**Since:** 20

<!--Device-AccessibilityElement-clip?: boolean--><!--Device-AccessibilityElement-clip?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## componentId

```TypeScript
componentId?: number
```

ID of the component to which the element belongs.

Default value: **-1**.

**Type:** number

**Since:** 20

<!--Device-AccessibilityElement-componentId?: long--><!--Device-AccessibilityElement-componentId?: long-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## componentType

```TypeScript
componentType?: string
```

Type of the component to which the element belongs.

**Type:** string

**Since:** 20

<!--Device-AccessibilityElement-componentType?: string--><!--Device-AccessibilityElement-componentType?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## contents

```TypeScript
contents?: Array<string>
```

Content displayed in the element.

**Type:** Array&lt;string&gt;

**Since:** 20

<!--Device-AccessibilityElement-contents?: Array<string>--><!--Device-AccessibilityElement-contents?: Array<string>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## currentIndex

```TypeScript
currentIndex?: number
```

Index of the current item.

Default value: **0**.

**Type:** number

**Since:** 20

<!--Device-AccessibilityElement-currentIndex?: int--><!--Device-AccessibilityElement-currentIndex?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## currentItem

```TypeScript
currentItem?: AccessibilityGrid
```

Current item in the component grid.

**Type:** [AccessibilityGrid](arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md)

**Since:** 20

<!--Device-AccessibilityElement-currentItem?: AccessibilityGrid--><!--Device-AccessibilityElement-currentItem?: AccessibilityGrid-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## customActions

```TypeScript
customActions?: Array<string>
```

Indicates the custom actions supported by the component.

**Type:** Array&lt;string&gt;

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccessibilityElement-customActions?: Array<string>--><!--Device-AccessibilityElement-customActions?: Array<string>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## customComponentType

```TypeScript
customComponentType?: string
```

Custom component type.

**Type:** string

**Since:** 20

<!--Device-AccessibilityElement-customComponentType?: string--><!--Device-AccessibilityElement-customComponentType?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## description

```TypeScript
description?: string
```

Description of the element.

**Type:** string

**Since:** 20

<!--Device-AccessibilityElement-description?: string--><!--Device-AccessibilityElement-description?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## editable

```TypeScript
editable?: boolean
```

Whether the element is editable. The value **true** indicates that the element is editable, and **false** indicates the opposite.

Default value: **false**.

**Type:** boolean

**Since:** 20

<!--Device-AccessibilityElement-editable?: boolean--><!--Device-AccessibilityElement-editable?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## endIndex

```TypeScript
endIndex?: number
```

Index of the last list item displayed on the screen.

Default value: **0**.

**Type:** number

**Since:** 20

<!--Device-AccessibilityElement-endIndex?: int--><!--Device-AccessibilityElement-endIndex?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## error

```TypeScript
error?: string
```

Error status of the element.

**Type:** string

**Since:** 20

<!--Device-AccessibilityElement-error?: string--><!--Device-AccessibilityElement-error?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## extraInfo

```TypeScript
extraInfo?: string
```

Additional information about an element. The value is a JSON string.

**Type:** string

**Since:** 20

<!--Device-AccessibilityElement-extraInfo?: string--><!--Device-AccessibilityElement-extraInfo?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## focusable

```TypeScript
focusable?: boolean
```

Whether the element is focusable. The value **true** indicates that the element is focusable, and **false** indicates the opposite.

Default value: **false**.

**Type:** boolean

**Since:** 20

<!--Device-AccessibilityElement-focusable?: boolean--><!--Device-AccessibilityElement-focusable?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## hintText

```TypeScript
hintText?: string
```

Hint text.

**Type:** string

**Since:** 20

<!--Device-AccessibilityElement-hintText?: string--><!--Device-AccessibilityElement-hintText?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## hotArea

```TypeScript
hotArea?: Rect
```

Hot area of an element.

**Type:** [Rect](arkts-accessibility-accessibilityextensioncontext-rect-i.md)

**Since:** 20

<!--Device-AccessibilityElement-hotArea?: Rect--><!--Device-AccessibilityElement-hotArea?: Rect-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## inputType

```TypeScript
inputType?: number
```

Type of the input text.

Default value: **0**.

**Type:** number

**Since:** 20

<!--Device-AccessibilityElement-inputType?: int--><!--Device-AccessibilityElement-inputType?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## inspectorKey

```TypeScript
inspectorKey?: string
```

Inspector key.

**Type:** string

**Since:** 20

<!--Device-AccessibilityElement-inspectorKey?: string--><!--Device-AccessibilityElement-inspectorKey?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## isActive

```TypeScript
isActive?: boolean
```

Whether the element is active. The value **true** indicates that the element is active, and **false** indicates the opposite.

Default value: **true**.

**Type:** boolean

**Since:** 20

<!--Device-AccessibilityElement-isActive?: boolean--><!--Device-AccessibilityElement-isActive?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## isEnable

```TypeScript
isEnable?: boolean
```

Whether the element is enabled. The value **true** indicates that the element is enabled, and **false** indicates the opposite.

Default value: **false**.

**Type:** boolean

**Since:** 20

<!--Device-AccessibilityElement-isEnable?: boolean--><!--Device-AccessibilityElement-isEnable?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## isEssential

```TypeScript
isEssential?: boolean
```

Whether the element is mandatory for the user. The value **true** indicates that the element is mandatory, and the value **false** indicates that the element is not mandatory. The default value is **false**.

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccessibilityElement-isEssential?: boolean--><!--Device-AccessibilityElement-isEssential?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## isFocused

```TypeScript
isFocused?: boolean
```

Whether the element is focused. The value **true** indicates that the element is focused, and **false** indicates the opposite.

Default value: **false**.

**Type:** boolean

**Since:** 20

<!--Device-AccessibilityElement-isFocused?: boolean--><!--Device-AccessibilityElement-isFocused?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## isHint

```TypeScript
isHint?: boolean
```

Whether the element is a hint. The value **true** indicates that the element is a hint, and **false** indicates the opposite.

Default value: **false**.

**Type:** boolean

**Since:** 20

<!--Device-AccessibilityElement-isHint?: boolean--><!--Device-AccessibilityElement-isHint?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## isPassword

```TypeScript
isPassword?: boolean
```

Whether the element is a password. The value **true** indicates that the element is a password, and **false** indicates the opposite.

Default value: **false**.

**Type:** boolean

**Since:** 20

<!--Device-AccessibilityElement-isPassword?: boolean--><!--Device-AccessibilityElement-isPassword?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## isVisible

```TypeScript
isVisible?: boolean
```

Whether the element is visible. The value **true** indicates that the element is visible, and **false** indicates the opposite.

Default value: **false**.

**Type:** boolean

**Since:** 20

<!--Device-AccessibilityElement-isVisible?: boolean--><!--Device-AccessibilityElement-isVisible?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## itemCount

```TypeScript
itemCount?: number
```

Total number of items.

Default value: **0**.

**Type:** number

**Since:** 20

<!--Device-AccessibilityElement-itemCount?: int--><!--Device-AccessibilityElement-itemCount?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## lastContent

```TypeScript
lastContent?: string
```

Last item.

**Type:** string

**Since:** 20

<!--Device-AccessibilityElement-lastContent?: string--><!--Device-AccessibilityElement-lastContent?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## layer

```TypeScript
layer?: number
```

Display layer of the element.

**Type:** number

**Since:** 20

<!--Device-AccessibilityElement-layer?: int--><!--Device-AccessibilityElement-layer?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## longClickable

```TypeScript
longClickable?: boolean
```

Whether the element can be long-pressed. The value **true** indicates that the element can be long-pressed, and   
**false** indicates the opposite.

Default value: **false**.

**Type:** boolean

**Since:** 20

<!--Device-AccessibilityElement-longClickable?: boolean--><!--Device-AccessibilityElement-longClickable?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## mainWindowId

```TypeScript
mainWindowId?: number
```

Main window ID of a component.

**Type:** number

**Since:** 20

<!--Device-AccessibilityElement-mainWindowId?: int--><!--Device-AccessibilityElement-mainWindowId?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## navDestinationId

```TypeScript
navDestinationId?: number
```

Destination ID of a component for navigation.

**Type:** number

**Since:** 20

<!--Device-AccessibilityElement-navDestinationId?: long--><!--Device-AccessibilityElement-navDestinationId?: long-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## offset

```TypeScript
offset?: number
```

Pixel offset of the content area relative to the top coordinate of a scrollable component (such as List and Grid). The unit is pixel (px).

Default value: **0**.

**Type:** number

**Since:** 20

<!--Device-AccessibilityElement-offset?: double--><!--Device-AccessibilityElement-offset?: double-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## pageId

```TypeScript
pageId?: number
```

Page ID.

Default value: **-1**.

**Type:** number

**Since:** 20

<!--Device-AccessibilityElement-pageId?: int--><!--Device-AccessibilityElement-pageId?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## parentId

```TypeScript
parentId?: number
```

Parent element ID of a component.

**Type:** number

**Since:** 20

<!--Device-AccessibilityElement-parentId?: long--><!--Device-AccessibilityElement-parentId?: long-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## pluralLineSupported

```TypeScript
pluralLineSupported?: boolean
```

Whether the element supports multiple lines of text. The value **true** indicates that the element supports multiple lines of text, and **false** indicates the opposite.

Default value: **false**.

**Type:** boolean

**Since:** 20

<!--Device-AccessibilityElement-pluralLineSupported?: boolean--><!--Device-AccessibilityElement-pluralLineSupported?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## rect

```TypeScript
rect?: Rect
```

Rectangular area for the element.

**Type:** [Rect](arkts-accessibility-accessibilityextensioncontext-rect-i.md)

**Since:** 20

<!--Device-AccessibilityElement-rect?: Rect--><!--Device-AccessibilityElement-rect?: Rect-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## resourceName

```TypeScript
resourceName?: string
```

Resource name of the element.

**Type:** string

**Since:** 20

<!--Device-AccessibilityElement-resourceName?: string--><!--Device-AccessibilityElement-resourceName?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## screenRect

```TypeScript
screenRect?: Rect
```

Rectangular area for the element to display.

**Type:** [Rect](arkts-accessibility-accessibilityextensioncontext-rect-i.md)

**Since:** 20

<!--Device-AccessibilityElement-screenRect?: Rect--><!--Device-AccessibilityElement-screenRect?: Rect-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## scrollable

```TypeScript
scrollable?: boolean
```

Whether the element is scrollable. The value **true** indicates that the element is scrollable, and **false** indicates the opposite.

Default value: **false**.

**Type:** boolean

**Since:** 20

<!--Device-AccessibilityElement-scrollable?: boolean--><!--Device-AccessibilityElement-scrollable?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## selected

```TypeScript
selected?: boolean
```

Whether the element is selected. The value **true** indicates that the element is selected, and **false** indicates the opposite.

Default value: **false**.

**Type:** boolean

**Since:** 20

<!--Device-AccessibilityElement-selected?: boolean--><!--Device-AccessibilityElement-selected?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## sourceType

```TypeScript
sourceType?: AccessibilitySourceType
```

Indicates the source of this element.

**Type:** [AccessibilitySourceType](arkts-accessibility-accessibility-accessibilitysourcetype-e-sys.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccessibilityElement-sourceType?: AccessibilitySourceType--><!--Device-AccessibilityElement-sourceType?: AccessibilitySourceType-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## spans

```TypeScript
spans?: AccessibilitySpan[]
```

Span array of a component.

**Type:** [AccessibilitySpan](arkts-accessibility-accessibilityextensioncontext-accessibilityspan-i-sys.md)[]

**Since:** 20

<!--Device-AccessibilityElement-spans?: AccessibilitySpan[]--><!--Device-AccessibilityElement-spans?: AccessibilitySpan[]-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## startIndex

```TypeScript
startIndex?: number
```

Index of the first item on the screen.

Default value: **0**.

**Type:** number

**Since:** 20

<!--Device-AccessibilityElement-startIndex?: int--><!--Device-AccessibilityElement-startIndex?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## supportedActionNames

```TypeScript
supportedActionNames?: Array<string>
```

Supported action names.

**Type:** Array&lt;string&gt;

**Since:** 20

<!--Device-AccessibilityElement-supportedActionNames?: Array<string>--><!--Device-AccessibilityElement-supportedActionNames?: Array<string>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## text

```TypeScript
text?: string
```

Text content of an element.

**Type:** string

**Since:** 20

<!--Device-AccessibilityElement-text?: string--><!--Device-AccessibilityElement-text?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## textLengthLimit

```TypeScript
textLengthLimit?: number
```

Maximum text length of an element.

**Type:** number

**Since:** 20

<!--Device-AccessibilityElement-textLengthLimit?: int--><!--Device-AccessibilityElement-textLengthLimit?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## textMoveUnit

```TypeScript
textMoveUnit?: accessibility.TextMoveUnit
```

Movement unit for traversing and reading text.

Default value: **char**.

**Type:** accessibility.TextMoveUnit

**Since:** 20

<!--Device-AccessibilityElement-textMoveUnit?: accessibility.TextMoveUnit--><!--Device-AccessibilityElement-textMoveUnit?: accessibility.TextMoveUnit-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## textType

```TypeScript
textType?: string
```

Accessibility text type of an element, which is configured by the **accessibilityTextHint** attribute of the component.

**Type:** string

**Since:** 20

<!--Device-AccessibilityElement-textType?: string--><!--Device-AccessibilityElement-textType?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## triggerAction

```TypeScript
triggerAction?: AccessibilityAction
```

Action that triggers the element event.

**Type:** [AccessibilityAction](arkts-accessibility-accessibility-accessibilityaction-e-sys.md)

**Since:** 20

<!--Device-AccessibilityElement-triggerAction?: AccessibilityAction--><!--Device-AccessibilityElement-triggerAction?: AccessibilityAction-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## type

```TypeScript
type?: WindowType
```

Window type of an element.

**Type:** [WindowType](arkts-accessibility-windowtype-t.md)

**Since:** 20

<!--Device-AccessibilityElement-type?: WindowType--><!--Device-AccessibilityElement-type?: WindowType-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## valueMax

```TypeScript
valueMax?: number
```

Maximum value.

Default value: **0**.

**Type:** number

**Since:** 20

<!--Device-AccessibilityElement-valueMax?: double--><!--Device-AccessibilityElement-valueMax?: double-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## valueMin

```TypeScript
valueMin?: number
```

Minimum value.

Default value: **0**.

**Type:** number

**Since:** 20

<!--Device-AccessibilityElement-valueMin?: double--><!--Device-AccessibilityElement-valueMin?: double-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## valueNow

```TypeScript
valueNow?: number
```

Current value.

Default value: **0**.

**Type:** number

**Since:** 20

<!--Device-AccessibilityElement-valueNow?: double--><!--Device-AccessibilityElement-valueNow?: double-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## windowId

```TypeScript
windowId?: number
```

Window ID.

Default value: **-1**.

**Type:** number

**Since:** 20

<!--Device-AccessibilityElement-windowId?: int--><!--Device-AccessibilityElement-windowId?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.
