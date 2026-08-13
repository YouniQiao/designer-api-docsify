# AccessibilityElement

Defines the **AccessibilityElement**. Before calling APIs of **AccessibilityElement**, you must call [AccessibilityExtensionContext.getFocusElement()](arkts-accessibility-accessibilityextensioncontext-c.md#getFocusElement) or [AccessibilityExtensionContext.getWindowRootElement()](arkts-accessibility-accessibilityextensioncontext-c.md#getWindowRootElement) to obtain an **AccessibilityElement** instance.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface AccessibilityElement--><!--Device-unnamed-export declare interface AccessibilityElement-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## actionNames

```TypeScript
actionNames(callback: AsyncCallback<Array<string>>): void
```

Obtains the names of all actions supported by this element. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-AccessibilityElement-actionNames(callback: AsyncCallback<Array<string>>): void--><!--Device-AccessibilityElement-actionNames(callback: AsyncCallback<Array<string>>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes | Callback used to return the names of all actions supported by the element. |

## Examples

```TypeScript
// rootElement is an instance of AccessibilityElement.
rootElement.actionNames((err: BusinessError, data: string[]) => {
  if (err && err.code) {
    console.error(`failed to get action names, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in get action names, ${JSON.stringify(data)}`);
})
```

## actionNames

```TypeScript
actionNames(): Promise<Array<string>>
```

Obtains the names of all actions supported by this element. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-AccessibilityElement-actionNames(): Promise<Array<string>>--><!--Device-AccessibilityElement-actionNames(): Promise<Array<string>>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | Promise used to return the names of all actions supported by the element. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement is an instance of AccessibilityElement.
rootElement.actionNames().then((data: string[]) => {
  console.info(`Succeeded in get action names, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to get action names, Code is ${err.code}, message is ${err.message}`);
})
```

## attributeNames

```TypeScript
attributeNames<T extends keyof ElementAttributeValues>(callback: AsyncCallback<Array<T>>): void
```

Obtains all attribute names of this element. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-AccessibilityElement-attributeNames<T extends keyof ElementAttributeValues>(callback: AsyncCallback<Array<T>>): void--><!--Device-AccessibilityElement-attributeNames<T extends keyof ElementAttributeValues>(callback: AsyncCallback<Array<T>>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;T&gt;&gt; | Yes | Callback used to return all attribute names of the element. |

## Examples

```TypeScript
import { ElementAttributeKeys } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement is an instance of AccessibilityElement.
rootElement.attributeNames((err: BusinessError, data: ElementAttributeKeys[]) => {
  if (err && err.code) {
    console.error(`failed to get attribute names, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in get attribute names, ${JSON.stringify(data)}`);
});
```

## attributeNames

```TypeScript
attributeNames<T extends keyof ElementAttributeValues>(): Promise<Array<T>>
```

Obtains all attribute names of this element. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-AccessibilityElement-attributeNames<T extends keyof ElementAttributeValues>(): Promise<Array<T>>--><!--Device-AccessibilityElement-attributeNames<T extends keyof ElementAttributeValues>(): Promise<Array<T>>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;T&gt;&gt; | Promise used to return all attribute names of the element. |

## Examples

```TypeScript
import { ElementAttributeKeys } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement is an instance of AccessibilityElement.
rootElement.attributeNames().then((data: ElementAttributeKeys[]) => {
  console.info(`Succeeded in get attribute names, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to get attribute names, Code is ${err.code}, message is ${err.message}`);
});
```

## attributeValue

```TypeScript
attributeValue<T extends keyof ElementAttributeValues>(
    attributeName: T,
    callback: AsyncCallback<ElementAttributeValues[T]>
  ): void
```

Obtains the attribute value based on an attribute name. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-AccessibilityElement-attributeValue<T extends keyof ElementAttributeValues>(    attributeName: T,    callback: AsyncCallback<ElementAttributeValues[T]>  ): void--><!--Device-AccessibilityElement-attributeValue<T extends keyof ElementAttributeValues>(    attributeName: T,    callback: AsyncCallback<ElementAttributeValues[T]>  ): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| attributeName | T | Yes | Attribute name. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ElementAttributeValues[T]&gt; | Yes | Callback used to return the attribute value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [9300004](../errorcode-accessibility.md#9300004-attribute-does-not-exist) | This property does not exist. |

## Examples

```TypeScript
import { ElementAttributeKeys } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let attributeName: ElementAttributeKeys = 'bundleName';

// rootElement is an instance of AccessibilityElement.
rootElement.attributeValue(attributeName, (err: BusinessError, data: string) => {
  if (err && err.code) {
    console.error(`failed to get attribute value, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in get attribute value, ${JSON.stringify(data)}`);
});
```

## attributeValue

```TypeScript
attributeValue<T extends keyof ElementAttributeValues>(attributeName: T): Promise<ElementAttributeValues[T]>
```

Obtains the attribute value based on an attribute name. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-AccessibilityElement-attributeValue<T extends keyof ElementAttributeValues>(attributeName: T): Promise<ElementAttributeValues[T]>--><!--Device-AccessibilityElement-attributeValue<T extends keyof ElementAttributeValues>(attributeName: T): Promise<ElementAttributeValues[T]>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| attributeName | T | Yes | Attribute name. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ElementAttributeValues[T]&gt; | Promise used to return the attribute value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [9300004](../errorcode-accessibility.md#9300004-attribute-does-not-exist) | This property does not exist. |

## Examples

```TypeScript
import { ElementAttributeKeys } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let attributeName: ElementAttributeKeys = 'bundleName';

// rootElement is an instance of AccessibilityElement.
rootElement.attributeValue(attributeName).then((data: string) => {
  console.info(`Succeeded in get attribute value by name, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to get attribute value, Code is ${err.code}, message is ${err.message}`);
});
```

## findElement

```TypeScript
findElement(type: 'content', condition: string, callback: AsyncCallback<Array<AccessibilityElement>>): void
```

Finds an element based on the content type. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-AccessibilityElement-findElement(type: 'content', condition: string, callback: AsyncCallback<Array<AccessibilityElement>>): void--><!--Device-AccessibilityElement-findElement(type: 'content', condition: string, callback: AsyncCallback<Array<AccessibilityElement>>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'content' | Yes | Type of element finding. The value is fixed at **'content'**. |
| condition | string | Yes | Search criteria. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt;&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let condition = 'keyword';

// rootElement is an instance of AccessibilityElement.
rootElement.findElement('content', condition, (err: BusinessError, data: AccessibilityElement[])=>{
  if (err && err.code) {
    console.error(`failed to find element, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in find element, ${JSON.stringify(data)}`);
});
```

## findElement

```TypeScript
findElement(type: 'content', condition: string): Promise<Array<AccessibilityElement>>
```

Finds an element based on the content type. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-AccessibilityElement-findElement(type: 'content', condition: string): Promise<Array<AccessibilityElement>>--><!--Device-AccessibilityElement-findElement(type: 'content', condition: string): Promise<Array<AccessibilityElement>>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'content' | Yes | Type of element finding. The value is fixed at **'content'**. |
| condition | string | Yes | Search criteria. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt;&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let condition = 'keyword';

// rootElement is an instance of AccessibilityElement.
rootElement.findElement('content', condition).then((data: AccessibilityElement[]) => {
  console.info(`Succeeded in find element, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to find element, Code is ${err.code}, message is ${err.message}`);
});
```

## findElement

```TypeScript
findElement(type: 'focusType', condition: FocusType, callback: AsyncCallback<AccessibilityElement>): void
```

Finds an element based on the focus type. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-AccessibilityElement-findElement(type: 'focusType', condition: FocusType, callback: AsyncCallback<AccessibilityElement>): void--><!--Device-AccessibilityElement-findElement(type: 'focusType', condition: FocusType, callback: AsyncCallback<AccessibilityElement>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'focusType' | Yes | Type of element finding. The value is fixed at **'focusType'**. |
| condition | [FocusType](arkts-accessibility-focustype-t.md) | Yes | Focus type. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
import { FocusType } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let condition: FocusType = 'normal';

// rootElement is an instance of AccessibilityElement.
rootElement.findElement('focusType', condition, (err: BusinessError, data: AccessibilityElement)=>{
  if (err && err.code) {
    console.error(`failed to find element, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in find element, ${JSON.stringify(data)}`);
});
```

## findElement

```TypeScript
findElement(type: 'focusType', condition: FocusType): Promise<AccessibilityElement>
```

Finds an element based on the focus type. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-AccessibilityElement-findElement(type: 'focusType', condition: FocusType): Promise<AccessibilityElement>--><!--Device-AccessibilityElement-findElement(type: 'focusType', condition: FocusType): Promise<AccessibilityElement>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'focusType' | Yes | Type of element finding. The value is fixed at **'focusType'**. |
| condition | [FocusType](arkts-accessibility-focustype-t.md) | Yes | Focus type. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
import { FocusType } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let condition: FocusType = 'normal';

// rootElement is an instance of AccessibilityElement.
rootElement.findElement('focusType', condition).then((data: AccessibilityElement) => {
  console.info(`Succeeded in find element,${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to find element, Code is ${err.code}, message is ${err.message}`);
});
```

## findElement

```TypeScript
findElement(type: 'focusDirection', condition: FocusDirection, callback: AsyncCallback<AccessibilityElement>): void
```

Finds an element based on the focus direction. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-AccessibilityElement-findElement(type: 'focusDirection', condition: FocusDirection, callback: AsyncCallback<AccessibilityElement>): void--><!--Device-AccessibilityElement-findElement(type: 'focusDirection', condition: FocusDirection, callback: AsyncCallback<AccessibilityElement>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'focusDirection' | Yes | Type of element finding. The value is fixed at **'focusDirection'**. |
| condition | [FocusDirection](arkts-accessibility-focusdirection-t.md) | Yes | Direction of the next focus element. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
import { FocusDirection } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let condition: FocusDirection = 'up';

// rootElement is an instance of AccessibilityElement.
rootElement.findElement('focusDirection', condition, (err: BusinessError, data: AccessibilityElement) =>{
  if (err && err.code) {
    console.error(`failed to find element, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in find element, ${JSON.stringify(data)}`);
});
```

## findElement

```TypeScript
findElement(type: 'focusDirection', condition: FocusDirection): Promise<AccessibilityElement>
```

Finds an element based on the focus direction. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-AccessibilityElement-findElement(type: 'focusDirection', condition: FocusDirection): Promise<AccessibilityElement>--><!--Device-AccessibilityElement-findElement(type: 'focusDirection', condition: FocusDirection): Promise<AccessibilityElement>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'focusDirection' | Yes | Type of element finding. The value is fixed at **'focusDirection'**. |
| condition | [FocusDirection](arkts-accessibility-focusdirection-t.md) | Yes | Focus direction. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
import { FocusDirection } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let condition: FocusDirection = 'up';

// rootElement is an instance of AccessibilityElement.
rootElement.findElement('focusDirection', condition).then((data: AccessibilityElement) => {
  console.info(`Succeeded in find element, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to find element, Code is ${err.code}, message is ${err.message}`);
});
```

## performAction

```TypeScript
performAction(actionName: string, parameters: object, callback: AsyncCallback<void>): void
```

Performs an action based on the specified action name. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-AccessibilityElement-performAction(actionName: string, parameters: object, callback: AsyncCallback<void>): void--><!--Device-AccessibilityElement-performAction(actionName: string, parameters: object, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| actionName | string | Yes | Action name. For details, see [Action](arkts-accessibility-accessibility-action-t.md#Action). |
| parameters | object | Yes | Parameters required for performing the target action. Empty by default. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [9300005](../errorcode-accessibility.md#9300005-operation-not-supported) | This action is not supported. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let actionName = 'action';
let parameters: object = [];

// rootElement is an instance of AccessibilityElement.
rootElement.performAction(actionName, parameters, (err: BusinessError) => {
  if (err && err.code) {
    console.error(`failed to perform action, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in perform action,actionName is ${actionName}, parameters is ${parameters}`);
});
```

## performAction

```TypeScript
performAction(actionName: string, parameters?: object): Promise<void>
```

Performs an action based on the specified action name. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-AccessibilityElement-performAction(actionName: string, parameters?: object): Promise<void>--><!--Device-AccessibilityElement-performAction(actionName: string, parameters?: object): Promise<void>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| actionName | string | Yes | Action name. For details, see [Action](arkts-accessibility-accessibility-action-t.md#Action). |
| parameters | object | No | Parameters required for performing the target action. Empty by default. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [9300005](../errorcode-accessibility.md#9300005-operation-not-supported) | This action is not supported. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let actionName = 'action';

// rootElement is an instance of AccessibilityElement.
rootElement.performAction(actionName).then(() => {
  console.info(`Succeeded in perform action,actionName is ${actionName}`);
}).catch((err: BusinessError) => {
  console.error(`failed to perform action, Code is ${err.code}, message is ${err.message}`);
});
```

Example of an action without parameters:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement is an instance of AccessibilityElement.
// An action that does not require any parameter setting is an action without parameters, as specified in the action description.
rootElement.performAction('click').then(() => {
  console.info(`Succeeded in perform action.`);
}).catch((err: BusinessError) => {
  console.error(`failed to perform action, Code is ${err.code}, message is ${err.message}`);
});
```

Example of an action with parameters:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement is an instance of AccessibilityElement.
// Sample code of setSelection
rootElement.performAction('setSelection', {
  selectTextBegin: '0', // Start position of the selection.
  selectTextEnd: '8',   // End position of the selection.
  selectTextInForWard: true   // true indicates the insertion point, and false indicates the selection range.
}).then(() => {
  console.info(`Succeeded in perform action`);
}).catch((err: BusinessError) => {
  console.error(`failed to perform action, Code is ${err.code}, message is ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement is an instance of AccessibilityElement.
// Sample code of setCursorPosition
rootElement.performAction('setCursorPosition', {
  offset: '1'   // Position of the cursor.
}).then(() => {
  console.info(`Succeeded in perform action`);
}).catch((err: BusinessError) => {
  console.error(`failed to perform action, Code is ${err.code}, message is ${err.message}`);
});
```

## performAction

```TypeScript
performAction(actionName: string, callback: AsyncCallback<void>): void
```

Performs an action based on the specified action name. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-AccessibilityElement-performAction(actionName: string, callback: AsyncCallback<void>): void--><!--Device-AccessibilityElement-performAction(actionName: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| actionName | string | Yes | Action name. For details, see [Action](arkts-accessibility-accessibility-action-t.md#Action). |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [9300005](../errorcode-accessibility.md#9300005-operation-not-supported) | This action is not supported. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let actionName = 'action';

// rootElement is an instance of AccessibilityElement.
rootElement.performAction(actionName, (err: BusinessError) => {
  if (err && err.code) {
    console.error(`failed to perform action, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in perform action, actionName is ${actionName}`);
});
```

